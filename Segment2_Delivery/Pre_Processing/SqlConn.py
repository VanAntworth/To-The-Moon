
import pandas as pd
import psycopg2
from pytest import deprecated_call
from sqlalchemy import create_engine, Table, select
import sqlalchemy
import pyodbc
from config import db_Server 

conn = object
engine = object 

def connectionString():
    db_string = 'mssql+pyodbc:///?odbc_connect=DRIVER={SQL Server};SERVER=' + db_Server + ';DATABASE=ElonMuskTwitterImpact;Trusted_Connection=yes'
   
    return db_string

def insertTweets(df_tweet_tostore):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    df_tweet_tostore.to_sql(name='TwitterData', con=engine, if_exists='append',index=False,index_label="ID")

def insertSentiment(df_sentiment_tostore):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    df_sentiment_tostore.to_sql(name='SentimentScoring',con=engine, index=False, if_exists='append',index_label="ID")

def insertFinanceData(df_finance_tostore):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    df_finance_tostore.to_sql(name='FinanceUsdData',con=engine, index=False, if_exists='append',index_label="ID")  

def fetchFinanceData():
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    return pd.read_sql_query(name='FinanceUsdData',con=engine)

def fetchTweetSentiment():
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    return pd.read_sql_query('exec sp_FetchTweetSentiment', con=engine)

def fetchTweetSentimentForModelling(financeType):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    sql_query = 'exec sp_fetchTweetSentimentForModelling'
    if financeType == 'doge':
        sql_query = sql_query + ' "doge"'
    elif  financeType == 'tesla':
            sql_query = sql_query + ' "tesla"'
    elif financeType == 'twitter':
            sql_query = sql_query + ' "twitter"'
            
    return pd.read_sql_query(sql_query, engine)

def fetchFinanceData(financeType):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    sql_query = 'exec sp_fetchFinanceData'
    if financeType == 'doge':
        sql_query = sql_query + ' "doge"'
    elif  financeType == 'tesla':
            sql_query = sql_query + ' "tesla"'
    elif financeType == 'twitter':
            sql_query = sql_query + ' "twitter"'
            
    return pd.read_sql_query(sql_query, engine)

def fetchTweetSentimentForStandardizing(financeType):
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    sql_query = 'exec sp_fetchTweetSentimentForStandardizing'
    if financeType == 'doge':
        sql_query = sql_query + ' "doge"'
    elif  financeType == 'tesla':
            sql_query = sql_query + ' "tesla"'
    elif financeType == 'twitter':
            sql_query = sql_query + ' "twitter"'
            
    return pd.read_sql_query(sql_query, engine)
