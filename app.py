from flask import Flask, render_template, request, jsonify
import requests

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
    return render_template('index.html', text=default_text, font_type=default_font, fonts=fonts)

if __name__ == '__main__':
    app.run(debug=True)