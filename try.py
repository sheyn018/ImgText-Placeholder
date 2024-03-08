import requests

url = "https://imgtext-placeholder.onrender.com/?font=merriweather"

try:
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        print("Content loaded successfully:")
        print(content)
    else:
        print(f"Failed to load URL. Status code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
