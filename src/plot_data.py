from get_historical_data import get_data

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def plot_data(coinId):

    data = get_data(coinId)

    x = pd.Series(data)

    x.plot()

    plt.title('price of ' + coinId + ' over last 365 days (btc)')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    plot_data('cardano')

