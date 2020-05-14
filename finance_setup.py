# This program takes arguments from the command line and looks up their stock data
# 
# run this program in the command line: python finance_setup.py stockname1 stockname2 ... 
# 
# Known bugs: stops working after 5th stock is added to arguments list

import sys
import pandas_datareader as pdr
import datetime 

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

stock_array = sys.argv[1:]

for i in range (0 , len(stock_array)):
    stock_name = stock_array[i]
    # print (stock_name)
    stock_data = pdr.get_data_yahoo(stock_array[i], start=datetime.datetime(2006, 10, 1), end=datetime.datetime(2012, 1, 1))
    # print (stock_data)