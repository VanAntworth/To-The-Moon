{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f09ec911",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c88e1618",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import datetime\n",
    "import pandas as pd\n",
    "import psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39f8ba85",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_price(stock):\n",
    "    period1 = int(time.mktime(datetime.datetime(2010,1,1,23,59).timetuple()))\n",
    "    period2 = int(time.mktime(datetime.datetime(2022,7,12,23,59).timetuple()))\n",
    "    interval = '1d'\n",
    "    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'\n",
    "    return query_string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8000df29",
   "metadata": {},
   "outputs": [],
   "source": [
    "stock = \"DOGE-USD\"\n",
    "doge_price = pd.read_csv(get_price(stock))\n",
    "doge_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d38ee63",
   "metadata": {},
   "outputs": [],
   "source": [
    "stock = \"TSLA-USD\"\n",
    "tslaUsd_price = pd.read_csv(get_price(stock))\n",
    "tslaUsd_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0991f59b",
   "metadata": {},
   "outputs": [],
   "source": [
    "stock = \"TSLA\"\n",
    "tesla_price = pd.read_csv(get_price(stock))\n",
    "tesla_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "333ca614",
   "metadata": {},
   "outputs": [],
   "source": [
    "stock = \"TWTR\"\n",
    "twitter_price = pd.read_csv(get_price(stock))\n",
    "twitter_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6273e12",
   "metadata": {},
   "outputs": [],
   "source": [
    "#stock = \"spaceX\"\n",
    "#spaceX_price = pd.read_csv(get_price(stock))\n",
    "#spaceX_price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbd77233",
   "metadata": {},
   "outputs": [],
   "source": [
    "doge_price.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "06e92e2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "doge_price.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c44d1632",
   "metadata": {},
   "outputs": [],
   "source": [
    "doge_price['Date'] = pd.to_datetime(doge_price['Date'], format='%Y-%m-%d')\n",
    "twitter_price['Date'] = pd.to_datetime(twitter_price['Date'], format='%Y-%m-%d')\n",
    "tesla_price['Date'] = pd.to_datetime(tesla_price['Date'], format='%Y-%m-%d')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b500487",
   "metadata": {},
   "outputs": [],
   "source": [
    "doge_price.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d01c9a40",
   "metadata": {},
   "outputs": [],
   "source": [
    "twitter_price.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e26f6947",
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_price.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69c29baa",
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_price['financeType']='tesla'\n",
    "twitter_price['financeType']='twitter'\n",
    "doge_price['financeType']='doge'\n",
    "\n",
    "df_finance_tostore = pd.concat([tesla_price, twitter_price, doge_price],axis=0,ignore_index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d74ee6bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_finance_tostore.rename(columns = {'Date':'date','Open':'open','High':'high','Low':'low','Close':'close','Adj Close':'adjustedClose','Volume':'volume'}, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dc6a9e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_finance_tostore = df_finance_tostore[['financeType','date','open','high','low','close','adjustedClose','volume']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1429e641",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Database related all the code is moved to this file\n",
    "%run -i \"SqlConn.py\"\n",
    "#importing local py file\n",
    "import SqlConn \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e073e4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Insert Finance Data \n",
    "try:\n",
    "    SqlConn.insertFinanceData(df_finance_tostore)\n",
    "    print(\"Data transfer Done\")\n",
    "except BaseException as err:\n",
    "    print(err)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f7640c4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
