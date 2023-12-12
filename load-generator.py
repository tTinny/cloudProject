import requests
import time
import json
import threading

def load_config_file():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


def load_generation_request(url):
    try:
        start_time = time.time()
        response = requests.head(url,timeout=10)
        end_time = time.time()
        print(f"Time taken for processing request: {end_time-start_time}")
    except requests.Timeout:
        print("Request failed.")
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":

    config = load_config()
    target_url = config.get("target_url", "https://google.com")
    request_frequency = config.get("request_frequency",20)

    # Create a thread for each request
    threads = [threading.Thread(target=load_generation_request(target_url)) for _ in range(request_frequency)]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish before exiting
    for thread in threads:
        thread.join()
