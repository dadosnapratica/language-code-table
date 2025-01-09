import base64
import sys
import requests
import pandas as pd
import json
import validators
import logging

log_message_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# Configure the logging format
logging.basicConfig(
    level=logging.INFO,
    format=log_message_format,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("get_base64_country_flag")
default_image_data=None
default_image_url='https://raw.githubusercontent.com/dadosnapratica/language-code-table/refs/heads/main/data/generic_flag.png'

# Lista de colunas válidas
valid_columns = [
    'language_country_name',
    'english_name',
    'portuguese_br_name',
    'native_name',
    'subtag',
    'country_flag_url',
    'country_flag_base64'
]

def get_default_image_data():
    global default_image_data
    if default_image_data is None:
        with open('./data/generic_flag.png', 'rb') as file:
            default_image_data = file.read()
            logger.info('First load Default Image')

    return default_image_data    

def remove_invalid_columns(data):
    """
    Remove columns from the DataFrame that are not in the list of valid columns.

    Args:
        data (pandas.DataFrame): The DataFrame to be filtered.
        valid_columns (list): A list of strings representing the valid column names.

    Returns:
        pandas.DataFrame: The filtered DataFrame with only valid columns.
    """
    global valid_columns

    # Filtrar o DataFrame para manter apenas as colunas válidas
    filtered_data = data[valid_columns]
    return filtered_data

# Função para verificar se uma URL é válida
def validate_url(url):
    return url if validators.url(url) else None

def fetch_and_convert_image(url):
    """
    Fetches an image from a URL and converts it to a Base64 string. If the fetch fails,
    it uses a default image from a specified path.
    
    Args:
        url (str): The URL of the image.
    
    Returns:
        str: The Base64 encoded string of the image.
    """
    try:
        # Attempt to fetch the image from the URL
        response = requests.get(url)        
        if response.status_code==200:
            image_data = response.content
        elif response.status_code==404:
            logger.error(f'Url {url} not found.')
            image_data=get_default_image_data()
        else:
            response.raise_for_status()  # Raise an error for bad HTTP responses             

    except Exception as e:
        logger.exception(f"Error fetching or converting image from {url}", e)
        #print(f"Error fetching or converting image from {url}: {e}")
        # If an error occurs, use the default image        
        image_data = get_default_image_data()
    
    # Encode the image data to Base64
    base64_image = base64.b64encode(image_data).decode('utf-8')
    return base64_image

def process_country_flags(data):
    """
    Processes a list of country flag URLs and converts them to Base64.
    Invalid URLs are replaced with None.
    
    Args:
        data (pandas.DataFrame): A DataFrame where each row contains 'language_country_name' and 'country_flag_url'.
    
    Returns:
        dict: A dictionary mapping countries to their Base64-encoded flags or None for invalid URLs.
    """
    global default_image_url

    base64_flags = {}
    for index, row in data.iterrows():
        country = row['language_country_name']
        url = row['country_flag_url']
        logger.debug(f"Processing flag for {country}...")

        # Validate the URL
        if validate_url(url)!=None:
            base64_flags[country] = fetch_and_convert_image(url)
        else:
            logger.error(f"Invalid URL for {country}: {url}")
            base64_flags[country] = base64.b64encode(get_default_image_data()).decode('utf-8')
            # Update the DataFrame directly using .loc method for it to affect the original DataFrame.
            data.loc[index, 'country_flag_url'] = default_image_url

    data['country_flag_base64'] = data['language_country_name'].map(base64_flags)
    return base64_flags


def save_json(data, csv_file_name):
    """
    Saves the given DataFrame to a JSON file and unescapes certain characters.

    Args:
        data (DataFrame): The pandas DataFrame to be saved.
        csv_file_name (str): The name of the CSV file, which will be converted to a JSON filename.
    """
    # Define the path for the JSON file
    json_path = csv_file_name.replace('.csv', '.json')

    # Save the DataFrame to JSON
    data.to_json(json_path, orient='records', force_ascii=False)

    # Read the JSON back in and unescape characters
    with open(json_path, 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    # Correcting the URLs by replacing escaped characters
    for item in data_json:
        if 'country_flag_url' in item and item['country_flag_url'] != None:
            item['country_flag_url'] = item['country_flag_url'].replace('\\/', '/')

    # Write the updated JSON back to the file
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)

def print_invalid_urls(flag_data):
    # Applying URL validation and marking invalid ones
    flag_data['is_url_valid'] = flag_data['country_flag_url'].apply(lambda url: validate_url(url) is not None)

    # Filter rows where the URL is invalid
    invalid_urls = flag_data[~flag_data['is_url_valid']]

    # Logging the result
    if not invalid_urls.empty:
        logger.info('Invalid URLs found:')
        logger.info(invalid_urls[['language_country_name', 'country_flag_url']])
    else:
        logger.info('No invalid URLs found.')

    # Clean up by dropping the temporary validation column
    flag_data.drop(columns=['is_url_valid'], inplace=True)

def clean_data(flag_data):
    # Aplicar a função para remover colunas inválidas
    flag_data = remove_invalid_columns(flag_data)

    # Verifica as Urls invalidas
    print_invalid_urls(flag_data)    

    # Aplica a validação em todas as URLs da coluna 'country_flag_url'
    flag_data['country_flag_url'] = flag_data['country_flag_url'].apply(lambda x: validate_url(x))
   
    return flag_data

# Example usage
if __name__ == "__main__":
    csv_file_name='./data/dadosnapratica_language_code.csv'
    # Example data (replace with your actual data)
    flag_data = pd.read_csv(csv_file_name, encoding='utf-8')
    flag_data.reset_index(drop=True, inplace=True)
    #flag_data.index.name='language_country_name'
    logger.info('Original Table')    
    logger.info(flag_data.head())

    # Clean Original Data
    flag_data=clean_data(flag_data)

    # Process the flags
    base64_flag_data = process_country_flags(flag_data)

    # Logar as linhas onde a coluna 'country_flag_url' é None
    # Check if 'country_flag_url' column contains the default_image_url
    logger.info("Rows with default image URL:")
    if 'country_flag_url' in flag_data.columns and default_image_url in flag_data['country_flag_url'].values:
        count_invalid = len(flag_data[flag_data['country_flag_url'] == default_image_url])
        logger.info(f'# Rows Invalid is {count_invalid}')
        logger.info(flag_data[flag_data['country_flag_url'] == default_image_url].head())
    else:
        logger.info("No rows found with the default image URL.")

    # Output the results
    #for country, base64_flag in base64_flag_data.items():
    #    if base64_flag:
    #        print(f"Base64 flag for {country}:\n{base64_flag}...")  # Truncated for readability
    
    logger.info('Transformed Table')
    flag_data.reset_index(drop=True, inplace=True)
    logger.info(flag_data.head())    
    flag_data.to_csv(csv_file_name, encoding='utf-8', index=False)
    
    
    #flag_data.to_json(csv_file_name.replace('.csv','.json'), orient='records', force_ascii=False)
    save_json(flag_data, csv_file_name)