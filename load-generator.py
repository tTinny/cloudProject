import requests
import time
import json

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def send_web_request(target_url):
    try:
        response = requests.head(target_url)
        print(f"Request sent. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    while True:
        config = load_config()
        target_url = config.get("target_url", "https://example.com")
        request_frequency = config.get("request_frequency", 5)

        send_web_request(target_url)
        time.sleep(request_frequency)
