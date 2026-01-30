import requests
import json

def search_repo():
    url = "https://api.github.com/search/repositories?q=ToxValDB+user:USEPA"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Found {data['total_count']} repositories.")
        for item in data['items']:
            print(f"Repo: {item['full_name']}")
            print(f"URL: {item['html_url']}")
    except Exception as e:
        print(f"Error searching repo: {e}")

if __name__ == "__main__":
    search_repo()
