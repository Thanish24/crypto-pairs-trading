import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import coint

def test(series1, series2):

    result = coint(series1, series2, maxlag=1)
    score = result[0]
    pvalue = result[1]

    print("score: " + str(score))
    print("p-value: " + str(pvalue))

    return [pvalue < 0.05, score, pvalue]

if __name__ == "__main__":
    print(test(pd.Series([1,2]), pd.Series([2,4])))
    
