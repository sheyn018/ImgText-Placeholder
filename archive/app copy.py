from flask import Flask, render_template, request, jsonify
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64

app = Flask(__name__)

# Replace this with your actual Google Fonts API key
google_fonts_api_key = "AIzaSyA2oLesrP-WPRZOSzQvb9IMQ5NYwytHfbA"
google_fonts_api_url = f"https://www.googleapis.com/webfonts/v1/webfonts?key={google_fonts_api_key}"

def fetch_google_fonts():
    response = requests.get(google_fonts_api_url)
    data = response.json()
    fonts = data.get('items', [])
    return fonts

@app.route('/')
def home():
    user_font = request.args.get('font')
    
    if user_font:
        default_font = user_font
    else:
        default_font = "Playfair Display"

    fonts = fetch_google_fonts()
    default_text = default_font
    url = f'https://imgtext-placeholder.onrender.com/?font=={default_text}'

    # For saving image data
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)

    # Navigate to the URL
    driver.get(url)

    # Take screenshot as binary data
    screenshot_binary = driver.get_screenshot_as_png()

    # Convert the binary data to a base64 encoded string
    screenshot_base64 = base64.b64encode(screenshot_binary).decode('utf-8')

    # Create data URL
    data_url = f"data:image/png;base64,{screenshot_base64}"

    driver.quit()

    if data_url is not None:
        # Safe to proceed with operations that assume data_url is a string
        parts = data_url.split(',')
        if len(parts) > 1:
            # Further processing if needed, for example extracting the base64 part
            image_base64 = f"data:image/png;base64,{parts[1]}"
            print(image_base64)
        else:
            print("Unexpected data URL format.")
    else:
        # Handle the case where data_url is None
        print("No data URL to process.")

    return render_template('index.html', text=default_text, font_type=default_font, fonts=fonts)

if __name__ == '__main__':
    app.run(debug=True)