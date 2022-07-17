
import pandas as pd
import psycopg2
from pytest import deprecated_call
from sqlalchemy import create_engine, Table, select
import sqlalchemy
import pyodbc

conn = object
engine = object 

def connectionString():
    db_string = 'mssql+pyodbc:///?odbc_connect=DRIVER={SQL Server};SERVER=LAPTOP-BOGKDVQK\SQLEXPRESS;DATABASE=ElonMuskTwitterImpact;Trusted_Connection=yes'
   
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

def fetchTweetSentiment():
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    return pd.read_sql_query('exec sp_FetchTweetSentiment', con=engine)


def fetchTweetSentimentForModelling():
    engine = sqlalchemy.create_engine(connectionString()) 
    engine.connect()
    return pd.read_sql_query('exec sp_FetchTweetSentiment', engine)
