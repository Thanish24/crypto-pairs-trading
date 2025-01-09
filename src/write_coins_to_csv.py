from coin_list import coins
import csv

def write():

    data = coins.getData()

    with open("src/coin_csv.csv", mode='w', newline='', encoding='utf-8') as csv_file:
        
        writer = csv.writer(csv_file)

        writer.writerow(['id', 'symbol', 'name'])

        # Write each row from the JSON data
        for item in data:
            writer.writerow([item['id'], item['symbol'], item['name']])

if __name__ == "__main__":
    write()