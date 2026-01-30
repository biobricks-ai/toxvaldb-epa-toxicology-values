import requests
import json

def search_zenodo():
    url = "https://zenodo.org/api/records"
    params = {'q': 'ToxValDB', 'sort': 'mostrecent'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        for item in data['hits']['hits']:
            print(f"Title: {item['metadata']['title']}")
            print(f"Date: {item['metadata']['publication_date']}")
            print(f"Record URL: {item['links']['self_html']}")
            for file in item['files']:
                 print(f"  File: {file['key']} - {file['links']['self']}")
    except Exception as e:
        print(f"Error searching Zenodo: {e}")

if __name__ == "__main__":
    search_zenodo()
