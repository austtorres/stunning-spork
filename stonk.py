import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import re

# summary data: 

from pandas_datareader import data as pdr

'''yf.pdr_override() # ensures data will be returned in format compatible with pandas

pd.set_option('display.max_rows', 10) # expand command line output
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)'''

startyear = 2010
startmonth = 2
startday = 20

start = dt.datetime(startyear, startmonth, startday)    # .datetime() is a class in the dt module with attributes year, month, day, ...
now = dt.datetime.now()

'''ticker = input('Enter a ticker: ')

stock_data = round(pdr.get_data_yahoo(ticker, start, now),2) 
market_data = round(pdr.get_data_yahoo('SPY', start, now),2) # S&P 500 index

ma = 50 # 50 day moving average
smaString = 'SMA_'+str(ma)

stock_data[smaString] = round(stock_data.iloc[:,4].rolling(window = ma).mean(),2) # add 50 day moving average column rounded to 2 decimals
# .iloc[] is how you index the data frame in pandas

summary_data = stock_data.iloc[ma:]   # starts after 50 days
'''

import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

ticker1, ticker2 = input('Enter 2 tickers you want to compare: ').split()
company1 = yf.Ticker(ticker1)
company2 = yf.Ticker(ticker2)
print('Comparing '+ company1.info['shortName']+' to '+company2.info['shortName']+':')

'''hist1 = company1.history(period = "max")
op1 = company1.option_chain('2020-05-14')

print(hist1, op1, end='\n')'''

'''fig, axs = plt.subplots(2) 
fig.suptitle(choice1+'  vs. '+choice2)
axs[0].plot(choice1)
axs[1].plot(choice2)
plt.ylabel('Stock price')
plt.legend()
plt.show()'''