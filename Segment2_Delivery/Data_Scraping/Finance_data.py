#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import datetime
import pandas as pd


# In[ ]:


def get_price(stock):
    period1 = int(time.mktime(datetime.datetime(2010,1,1,23,59).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2022,7,12,23,59).timetuple()))
    interval = '1d'
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    return query_string


# In[ ]:


stock = "DOGE-USD"
doge_price = pd.read_csv(get_price(stock))
doge_price


# In[ ]:


stock = "TSLA-USD"
tslaUsd_price = pd.read_csv(get_price(stock))
tslaUsd_price


# In[ ]:


stock = "TSLA"
tesla_price = pd.read_csv(get_price(stock))
tesla_price


# In[ ]:


stock = "TWTR"
twitter_price = pd.read_csv(get_price(stock))
twitter_price


# In[ ]:


#stock = "spaceX"
#spaceX_price = pd.read_csv(get_price(stock))
#spaceX_price


# In[ ]:


doge_price.info()


# In[ ]:


doge_price.dtypes


# In[ ]:


doge_price['Date'] = pd.to_datetime(doge_price['Date'], format='%Y-%m-%d')
twitter_price['Date'] = pd.to_datetime(twitter_price['Date'], format='%Y-%m-%d')
tesla_price['Date'] = pd.to_datetime(tesla_price['Date'], format='%Y-%m-%d')


# In[ ]:


doge_price.dtypes


# In[ ]:


twitter_price.dtypes


# In[ ]:


tesla_price.dtypes


# In[ ]:


tesla_price['financeType']='tesla'
twitter_price['financeType']='twitter'
doge_price['financeType']='doge'

df_finance_tostore = pd.concat([tesla_price, twitter_price, doge_price],axis=0,ignore_index=False)


# In[ ]:


df_finance_tostore.rename(columns = {'Date':'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adjustedClose','Volume':'volume'}, inplace = True)


# In[ ]:


df_finance_tostore = df_finance_tostore[['financeType','date','open','high','low','close','adjustedClose','volume']]


# In[ ]:


# Database related all the code is moved to this file
get_ipython().run_line_magic('run', '-i "SqlConn.py"')
#importing local py file
import SqlConn 


# In[ ]:


#Insert Finance Data 
try:
    SqlConn.insertFinanceData(df_finance_tostore)
    print("Data transfer Done")
except BaseException as err:
    print(err)


# In[ ]:




