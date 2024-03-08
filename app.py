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

@app.route('/save_image', methods=['POST'])
def save_image():
    if request.method == 'POST':
        image_data = request.form.get('image_data')
        # Process the image_data as needed (e.g., save to a file, database, etc.)
        # For now, let's just print it
        print("Received image data:", image_data)
        return jsonify({'data': image_data})

if __name__ == '__main__':
    app.run(debug=True)