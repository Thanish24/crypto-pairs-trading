## crypto pairs trading

These are a set of python scripts I wrote to explore pairs trading opportunities for cryptcurrencies.

step 1. Use the coingecko API to get a list of coins from a similar category (TODO)
    step 1.5. pre screen the data so you arent running into multiple comparisons bias
    andreesen horowitz, exchange based tokens, smart contract platform
step 2. Get time series data for the past year for both coins
    dont use all data- reserve for backtesting
step 3. test for cointegration on all the pairs (engle granger two step)
    look into kalman filters or use moving averages
    check if returns are correlated
        why are they always cointegrated with really low p-values?
        trying log returns
step 4. start logging trades and testing effectiveness (TODO)

Further research:
    use genetic programming to find mean reverting groups of assets