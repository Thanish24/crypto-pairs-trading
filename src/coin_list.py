import json

class coins:

    def getData():
        with open('./coins.txt', 'r') as file:
            data = json.load(file)
            return data