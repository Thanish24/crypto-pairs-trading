import requests

def load_category(category="none"): # empty category gives list of categories

    if category == "none":
        url = "https://api.coingecko.com/api/v3/coins/categories/list"
    else:
        url = "https://api.coingecko.com/api/v3/coins/categories/" + category

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")

    print(response.text)

if __name__ == "__main__":
    load_category("aave-tokens")