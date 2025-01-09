
import pandas as pd
from sklearn import linear_model
from get_historical_data import get_data
import matplotlib.pyplot as plt
import statsmodels.api as sm

def calculate_spread(series1, series2):
    regr = linear_model.LinearRegression()
    x_constant = pd.concat([series1,pd.Series([1]*len(series1),index = series1.index)], axis=1)
    regr.fit(x_constant, series2)    
    beta = regr.coef_[0]
    alpha = regr.intercept_
    spread = series2 - series1*beta - alpha
    return spread, beta, alpha

def get_spread_from_id(name1, name2, graph):

    data1 = get_data(name1)
    data2 = get_data(name2)

    series1 = pd.Series(data1)
    series2 = pd.Series(data2)

    spread, beta, alpha = calculate_spread(series1, series2)

    print("beta: " + str(beta))

    if graph:
        spread.plot()
        plt.ylabel("spread")
        plt.show()

    adf = sm.tsa.stattools.adfuller(spread, maxlag=1)

    print("p value for stationarity of spread: " + str(adf[1]))

def get_spread_from_series(series1, series2, graph):
    regr = linear_model.LinearRegression()
    x_constant = pd.concat([series1,pd.Series([1]*len(series1),index = series1.index)], axis=1)
    regr.fit(x_constant, series2)    
    beta = regr.coef_[0]
    alpha = regr.intercept_
    spread = series2 - series1*beta - alpha

    if graph:
        spread.plot()
        plt.ylabel("spread")
        plt.show()
    
    adf = sm.tsa.stattools.adfuller(spread, maxlag=1)

    print("p value for stationarity of spread: " + str(adf[1]))
    

    return beta

if __name__ == '__main__':
    get_spread_from_id('uniswap', 'near', True)