import requests
import time
import json

def load_config_file():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def load_generation_request(url,frequency):
    try:
        
        response = requests.head(target_url)
        print(f"Request sent. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":

    config = load_config()
    target_url = config.get("target_url", "https://google.com")
    request_frequency = config.get("request_frequency",10)

    interval = 1 / request_frequency  

    while request_frequency > 0:
        load_generation_request(target_url)
        time.sleep(interval)
        request_frequency = request_frequency - 1
