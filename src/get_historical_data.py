import requests

def get_data(coinId):

    url = "https://api.coingecko.com/api/v3/coins/"+ coinId + "/market_chart"

    headers = {"accept": "application/json"}

    params = {"interval": "daily", "vs_currency": "btc", "days": "100"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        print(coinId)

    price_data = data['prices']

    prices = [p[1] for p in price_data]

    return prices

def get_data_last_week(coinId):
    url = "https://api.coingecko.com/api/v3/coins/"+ coinId + "/market_chart"

    headers = {"accept": "application/json"}

    params = {"vs_currency": "btc", "days": "6"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    price_data = data['prices']

    prices = [p[1] for p in price_data]

    return prices


if __name__ == "__main__":
    get_data("cardano")