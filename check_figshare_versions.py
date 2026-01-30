import requests
import json

def check_figshare_versions():
    article_id = "20394501" 
    versions_url = f"https://api.figshare.com/v2/articles/{article_id}/versions"
    try:
        v_response = requests.get(versions_url)
        v_response.raise_for_status()
        versions = v_response.json()
        for v in versions:
            # Get details for this version
            detail_url = v['url']
            d_response = requests.get(detail_url)
            d_data = d_response.json()
            print(f"Version {v['version']}: {d_data['title']}")
            for file in d_data['files']:
                 print(f"  File: {file['name']} - {file['download_url']}")
            
    except Exception as e:
        print(f"Error checking FigShare: {e}")

if __name__ == "__main__":
    check_figshare_versions()
