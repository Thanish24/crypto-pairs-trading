import requests
from credentials import gecko_api_key

url = "https://api.coingecko.com/api/v3/ping"

headers = {"accept": "application/json", "x-cg-api-key": gecko_api_key}

response = requests.get(url, headers=headers)

print(response.text)