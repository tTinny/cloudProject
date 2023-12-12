import requests
import time
import json
import threading

def load_config_file():
    with open('/Users/prakritiarora/Documents/cloud_computing/config.json', 'r') as config_file:
        config = json.load(config_file)
    return config


def load_generation_request(url,response_time,count):
    try:
        start_time = time.time()
        response = requests.head(url,timeout=10)
        end_time = time.time()
        time_taken = end_time - start_time
        response_time.append(time_taken)
    except requests.Timeout:
        print("Request failed.")
        count = count+1
    except requests.RequestException as e:
        print(f"Error sending request: {e}")

if __name__ == "__main__":
    
    config = load_config_file()
    target_url = config.get("target_url", "https://google.com")
    request_frequency = config.get("request_frequency",20)
    
    response_time = []
    failure_count = 0

    # Create a thread for each request
    threads = [threading.Thread(target=load_generation_request(target_url,response_time,failure_count)) for _ in range(request_frequency)]
    avg_resp_time = sum(response_time)/len(response_time)
    print(avg_resp_time)
    print(failure_count)
    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish before exiting
    for thread in threads:
        thread.join()




