import requests
import json

def check_figshare():
    # Attempt to use the ID from the DOI
    article_id = "20394501" 
    url = f"https://api.figshare.com/v2/articles/{article_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"Title: {data['title']}")
        print(f"URL: {data['url']}")
        print("Files:")
        for file in data['files']:
            print(f"  {file['name']} - {file['download_url']}")
            
        print("\nVersions:")
        # Versions endpoint might be needed if this is just the latest
        versions_url = f"https://api.figshare.com/v2/articles/{article_id}/versions"
        v_response = requests.get(versions_url)
        v_response.raise_for_status()
        versions = v_response.json()
        for v in versions:
            print(f"  v{v['version']} - {v['url']}")
            
    except Exception as e:
        print(f"Error checking FigShare: {e}")

if __name__ == "__main__":
    check_figshare()
