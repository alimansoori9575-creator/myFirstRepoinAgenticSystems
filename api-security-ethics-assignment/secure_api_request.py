import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("SECRET_API")
url = "https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}
responce = requests.get(url, headers=headers)

if responce.status_code == 200:
    print(responce.json())

elif responce.status_code == 429:
    print("Rate limit reached. Try again later.")

else:
    print("Request failed", responce.status_code)
    