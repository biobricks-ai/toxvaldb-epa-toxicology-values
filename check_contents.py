import requests
import json

def check_contents():
    url = "https://api.github.com/repos/USEPA/toxvaldbmain/contents"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for item in data:
            print(f"{item['type']}: {item['name']} ({item['size']} bytes)")
    except Exception as e:
        print(f"Error checking contents: {e}")

if __name__ == "__main__":
    check_contents()
