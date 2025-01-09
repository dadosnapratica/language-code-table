import base64
import sys
#from sys import _ExitCode
import requests
import pandas as pd
import json

def fetch_and_convert_image(url):
    """
    Fetches an image from a URL and converts it to a Base64 string.
    
    Args:
        url (str): The URL of the image.
    
    Returns:
        str: The Base64 encoded string of the image.
    """
    try:
        # Fetch the image from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        # Encode the image to Base64
        base64_image = base64.b64encode(response.content).decode('utf-8')
        return base64_image
    except Exception as e:
        print(f"Error fetching or converting image from {url}: {e}. Using default.")

        return None

def process_country_flags(data):
    """
    Processes a list of country flag URLs and converts them to Base64.
    
    Args:
        data (list of dict): A list where each item is a dictionary containing 
                             'country' and 'flag_url' keys.
                             
    Returns:
        dict: A dictionary mapping countries to their Base64-encoded flags.
    """
    base64_flags = {}
    for index, row in data.iterrows():
        country = row['language_country_name']
        url = row['country_flag_url']
        print(f"Processing flag for {country}...")
        base64_flags[country] = fetch_and_convert_image(url)

    data['country_flag_base64']=data['language_country_name'].map(base64_flags)#pd.Series(base64_flags)
    #print(data[['language_country_name','country_flag_base64']].head(10))
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
        if 'country_flag_url' in item:
            item['country_flag_url'] = item['country_flag_url'].replace('\\/', '/')

    # Write the updated JSON back to the file
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)

# Example usage
if __name__ == "__main__":
    csv_file_name='./data/dadosnapratica_language_code.csv'
    # Example data (replace with your actual data)
    flag_data = pd.read_csv(csv_file_name, encoding='utf-8')
    #flag_data.index.name='language_country_name'
    print(flag_data.head())
    #exit(0)
    
    # Process the flags
    base64_flag_data = process_country_flags(flag_data)

    # Output the results
    #for country, base64_flag in base64_flag_data.items():
    #    if base64_flag:
    #        print(f"Base64 flag for {country}:\n{base64_flag}...")  # Truncated for readability
    
    print(flag_data.head(10))
    flag_data.to_csv(csv_file_name, encoding='utf-8')
    
    #flag_data.to_json(csv_file_name.replace('.csv','.json'), orient='records', force_ascii=False)
    save_json(flag_data, csv_file_name)