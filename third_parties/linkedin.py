import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Shypooper007/6e3825aeb57f0a49ad0d1f07bfd5e096/raw/89f8fa13bd5478eb442357b034d88a020f8ab6ea/gistfile1.txt"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=headers, timeout=10)
    data = clean_json(response.json())
    return data

def clean_json(json_data):
    cleaned_data = {}
    for key, value in json_data.items():
        if value is not None and value != []:
            if isinstance(value, dict):
                cleaned_value = clean_json(value)
                if cleaned_value != {}:
                    cleaned_data[key] = cleaned_value
            else:
                cleaned_data[key] = value
    return cleaned_data


if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/advait-wakulkar-258574221/"))
