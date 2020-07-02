import requests
import os

google_api_key = os.getenv("google_api_key")

def google_civics_api(address):
    request_url = 'https://www.googleapis.com/civicinfo/v2/representatives?' + f'key={google_api_key}' + f'&address={address}'
    response = requests.get(request_url).json()
    return response