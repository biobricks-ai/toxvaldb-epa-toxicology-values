import requests
import sys

def check_releases():
    url = "https://api.github.com/repos/USEPA/toxvaldbmain/releases"
    try:
        response = requests.get(url)
        response.raise_for_status()
        releases = response.json()
        print(f"Found {len(releases)} releases.")
        for release in releases:
            print(f"Release: {release['tag_name']}")
            if not release['assets']:
                print("  No assets.")
            for asset in release['assets']:
                print(f"  Asset: {asset['name']} - {asset['browser_download_url']}")
    except Exception as e:
        print(f"Error checking releases: {e}")

if __name__ == "__main__":
    check_releases()
