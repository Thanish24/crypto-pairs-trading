from test_cointegration import test
from get_historical_data import get_data

import pandas as pd
import matplotlib.pyplot as plt

def test_pair(name1, name2, graph):

    s1 = pd.Series(get_data(name1))
    s2 = pd.Series(get_data(name2))

    res = test(s1, s2)

    if (graph):
        s1.plot(label=name1)
        s2.plot(label=name2)
        plt.legend()
        plt.show()
    
    print("null rejected?: " + str(res[0]))

    return res[0]

if __name__ == "__main__":
    test_pair('solana', 'uniswap', True)