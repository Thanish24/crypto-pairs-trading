from test_cointegration import test
from get_historical_data import get_data
from test_returns import test_returns
from calculate_spread import get_spread_from_series

import pandas as pd
import matplotlib.pyplot as plt
import csv

def test_pair(name1, name2, graph):

    data1 = get_data(name1)
    data2 = get_data(name2)

    s1 = pd.Series(data1)
    s2 = pd.Series(data2)

    if (len(data1) != len(data2)):
        print("data length different!")
        print(len(data1))
        print(len(data2))

    res = test(s1, s2)

    if (graph):
        s1.plot(label=name1)
        s2.plot(label=name2)
        plt.legend()
        plt.show()
    
    print("null rejected?: " + str(res[0]))

    test_returns(data1, data2, True)

    beta = get_spread_from_series(s1, s2, True)

    if res[0]:

        with open("src/cointegrated_pairs.csv", mode='a', newline='', encoding='utf-8') as csv_file:
        
            writer = csv.writer(csv_file)

            # Write each row from the JSON data
            writer.writerow([name1, name2, res[1], res[2], beta])

    return res[0]

if __name__ == "__main__":
    test_pair('solana', 'stellar', True)