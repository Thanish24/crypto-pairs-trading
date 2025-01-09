import numpy as np
import pandas as pd
from test_cointegration import test

from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

def test_returns(series1, series2, graph): # testing log returns for cointegration, 

    returns1 = np.diff(series1)
    returns2 = np.diff(series2)

    if graph:
        pd.Series(returns1).plot()
        pd.Series(returns2).plot()
        plt.show()

    res = test(returns1, returns2)

    print("returns cointegrated?: " + str(res[0]))

    return res