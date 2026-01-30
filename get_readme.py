import requests
import base64

def get_readme():
    url = "https://api.github.com/repos/USEPA/toxvaldbmain/readme"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        content = base64.b64decode(data['content']).decode('utf-8')
        print(content)
    except Exception as e:
        print(f"Error getting readme: {e}")

if __name__ == "__main__":
    get_readme()
