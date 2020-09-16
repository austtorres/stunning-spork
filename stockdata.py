# This program takes a stock, e.g. AAPL, 
# 
# and writes its 5 yr stock data to a file called 
# 
# aapl_data.csv which can be exported to Excel 

import pandas_datareader as pdr
import pandas as pd
import datetime as dt

aapl = pdr.get_data_yahoo('AAPL', start=dt.datetime(2006, 10, 1), 
                          end=dt.datetime(2020, 5, 15))

# print(aapl.head())
# print(aapl.tail())
# print(aapl.describe())

# to_csv allows you to write the data to a file
# read_csv reads the data in your file back into Python
# aapl.to_csv('aapl_data.csv')
# df = pd.read_csv('aapl_data.csv', header = 0, index_col='Date', parse_dates=True)
# print(df) 

# Inspect the data in the aapl dataframe:
# print(aapl.index)   #rows
# print(aapl.columns) #columns
ts = aapl['Close'][-10:]
# print(type(ts))

# pandas has loc and iloc
# loc() is for label-based indexing e.g. 01-01-2020
# iloc() is for positional indexing e.g. a cell in the df

# Inspect the first rows of November-December 2006
# print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())

# Inspect the first rows of 2007
# print(aapl.loc['2007'].head())

# Inspect November 2006
# print(aapl.iloc[22:43])

# Inspect the 'Open' and 'Close' values at 2006-11-01 and 2006-12-01 using .iloc[row range, columns]
# print(aapl.iloc[[22,43], [2, 3]])

# Sample 20 rows
sample = aapl.sample(20)

# Resample to monthly level
monthly_aapl = aapl.resample('M').mean()

# Add a column `diff` to `aapl` 
aapl['diff'] = aapl.Close - aapl.Open

# Delete the new `diff` column
# del aapl['diff']

import matplotlib.pyplot as plt
# Plot the closing prices for `aapl`
# aapl['Close'].plot(grid=True)
# Show the plot
# plt.show()

import numpy as np
# Assign `Adj Close` to `daily_close`
daily_close = aapl[['Adj Close']]

# Daily returns
daily_pct_change = daily_close.pct_change()
# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)
daily_log_returns.fillna(0, inplace=True)
# Replace NA values with 0
daily_pct_change.fillna(0, inplace=True)
# print(daily_pct_change)
# print(daily_log_returns)

# Resample `aapl` to business months, take last observation as value 
monthly = aapl.resample('BM').apply(lambda x: x[-1])
# Calculate the monthly percentage change
# print(monthly.pct_change())

# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()
# Calculate the quarterly percentage change
# print(quarter.pct_change())

# Daily returns
daily_pct_change = daily_close / daily_close.shift(1) - 1

daily_log_returns_shift = np.log(daily_close / daily_close.shift(1))

# Print `daily_pct_change`
# print(daily_pct_change)

# Import matplotlib
import matplotlib.pyplot as plt

# Plot the distribution of `daily_pct_c`
# daily_pct_change.hist(bins=50)

# Show the plot
# plt.show()

# Pull up summary statistics
print(daily_pct_change.describe())

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_change).cumprod()

# Print `cum_daily_return`
print(cum_daily_return)

# Import matplotlib
import matplotlib.pyplot as plt 

# Plot the cumulative daily returns
cum_daily_return.plot(figsize=(12,8))

# Show the plot
plt.show()

# Resample the cumulative daily return to cumulative monthly return 
cum_monthly_return = cum_daily_return.resample("M").mean()

# Print the `cum_monthly_return`
print(cum_monthly_return)
