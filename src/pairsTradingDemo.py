import time
import numpy as np
import pandas as pd

np.random.seed(107)

import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

import matplotlib.pyplot as plt

# generate returns which are normally distributed
X_returns = np.random.normal(0, 1, 100)

price = pd.Series(np.cumsum(X_returns)) + 50

price.plot()
plt.title('price plot')
plt.show()