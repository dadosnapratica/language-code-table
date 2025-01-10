# Release Notes - Program Updates

2025-01-10 - Updates - tag v1.0.1
Add Brazilian Portuguese

2025-01-09 - Updates - tag v1.0.0
-----
**1. Correct Handling of Invalid URLs**

*Summary:* Improved the handling of invalid URLs to ensure that all entries with non-valid URLs are updated to use a default image URL. This corrects issues where invalid URLs failed to display an alternative image.

**2. Update to DataFrame Directly in Loop**

*Summary*: Modified the process_country_flags function to directly update the DataFrame's 'country_flag_url' when an invalid URL is detected. Previously, changes to the URL during iteration did not persist post-function execution because the updates were made to a copy of the row rather than the DataFrame itself.

**3. Improved Logging for Invalid URLs**

*Summary*: Enhanced logging capabilities to provide more detailed feedback on processing steps, particularly around the handling of invalid URLs. This includes logging both when invalid URLs are detected and when default data is used as a replacement.

**4. Base64 Encoding of Default Image**

*Summary*: Ensured that the default image used for invalid URLs is correctly converted to Base64 format. This guarantees that the fallback image is properly displayed in all cases where the original URL fails to load.

**5. Efficient URL Validation and Image Fetching**

*Summary*: Streamlined the URL validation and image fetching processes to improve efficiency and reduce potential errors. The validate_url function now robustly checks URL validity and the fetching function handles various HTTP response scenarios gracefully.

**6. Enhanced Error Handling and Default Image Fallback**

*Summary*: Implemented more robust error handling within the fetch_and_convert_image function to manage exceptions more effectively. In cases of fetch failure, the function now reliably falls back to using a predefined default image.

**7. JSON Output Improvements**

*Summary*: Adjustments were made to ensure that JSON outputs are correctly formatted, particularly concerning the unescaping of URLs. This ensures that data saved in JSON format retains accurate and user-friendly URL strings.