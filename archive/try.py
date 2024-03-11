from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64

def screenshot_to_data_url(url):
    print("START...")
    # Set up Chrome to run in headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    print("Options set...")

    # Set up ChromeDriver
    # service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(options=options)
    print("Service set...")
    print("Capturing screenshot...")

    try:
        # Navigate to the URL
        driver.get(url)

        # Take screenshot as binary data
        screenshot_binary = driver.get_screenshot_as_png()

        # Convert the binary data to a base64 encoded string
        screenshot_base64 = base64.b64encode(screenshot_binary).decode('utf-8')

        # Create data URL
        data_url = f"data:image/png;base64,{screenshot_base64}"
        print(data_url)
        print("Screenshot captured successfully.")
        
        return data_url
    finally:
        # Clean up: close the browser window
        driver.quit()

def process_data_url(data_url):
    if data_url is not None:
        # Safe to proceed with operations that assume data_url is a string
        parts = data_url.split(',')
        if len(parts) > 1:
            # Further processing if needed, for example extracting the base64 part
            image_base64 = parts[1]
            print("Base64 part of the data URL:", image_base64)
        else:
            print("Unexpected data URL format.")
    else:
        # Handle the case where data_url is None
        print("No data URL to process.")

# Example usage, ensuring data_url is checked for None
url = 'https://imgtext-placeholder.onrender.com/?font=merriweather'
data_url = screenshot_to_data_url(url)
# process_data_url(data_url)
