import json

class coins:

    def getData():
        with open('src/coins.txt', 'r') as file:
            data = json.load(file)
            return data
        
if __name__ == "__main__":
    coins.getData()