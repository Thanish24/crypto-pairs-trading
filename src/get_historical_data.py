import requests

def get_data(coinId):

    url = "https://api.coingecko.com/api/v3/coins/"+ coinId + "/market_chart"

    headers = {"accept": "application/json"}

    params = {"interval": "daily", "vs_currency": "btc", "days": "365"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")

    price_data = data['prices']

    prices = [p[1] for p in price_data]

    return prices

if __name__ == "__main__":
    get_data("ethereum")