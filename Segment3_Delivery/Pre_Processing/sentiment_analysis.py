#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install TextBlob


# In[ ]:


import json
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2
import pyodbc


# In[ ]:


# Database related all the code is moved to this file
get_ipython().run_line_magic('run', '-i "SqlConn.py"')
#importing local py file
import SqlConn 


# In[ ]:


#Fetch Tweets and Sentiment data - Join from Tweet and Sentiment tables
try:
    df_dbSentimentData = SqlConn.fetchTweetSentiment()
    print("Data transfer Done")
except BaseException as err:
    print(err)


# In[ ]:


df_dbSentimentData


# In[ ]:


# Read the csv files containin the tweets by Eon Musk from 2010 to 2022 for DogeCOin, Tesla, spaceX, twitter.
#df_doge = pd.read_csv('../Data_Resources/scrapped_data/doge_tweets.csv')
#df_spaceX = pd.read_csv('../Data_Resources/scrapped_data/spaceX_tweets.csv')
#df_tesla = pd.read_csv('../Data_Resources/scrapped_data/tesla_tweets.csv')
#df_twitter = pd.read_csv('../Data_Resources/scrapped_data/twitter_tweets.csv')


# In[ ]:


df_doge = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'doge']
df_tesla = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'tesla']
df_twitter = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'twitter']


# In[ ]:


df_doge


# In[ ]:


print(f"shape of doge df: " + str(df_doge.shape))
print(f"shape of tesla df: " + str(df_tesla.shape))
print(f"shape of twitter df: " + str(df_twitter.shape))


# In[ ]:


df_doge.head()


# In[ ]:


df_tesla.head()


# In[ ]:


df_twitter.head()


# In[ ]:





# In[ ]:


nltk.download('vader_lexicon')


# In[ ]:


vader = SentimentIntensityAnalyzer()


# In[ ]:


df_doge_vader = df_doge.copy()
df_tesla_vader = df_tesla.copy()
df_twitter_vader = df_twitter.copy()


# In[ ]:


# df_doge_vader["normalized"] = df_doge_vader["Tweet"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))
df_doge_vader["compound_sc"] = df_doge_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["compound"])
df_doge_vader["negative_sc"] = df_doge_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neg"])
df_doge_vader["neutral_sc"] = df_doge_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neu"])
df_doge_vader["positive_sc"] = df_doge_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["pos"])
df_doge_vader.head()


# In[ ]:


# df_doge_vader["normalized"] = df_doge_vader["Tweet"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))
df_tesla_vader["compound_sc"] = df_tesla_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["compound"])
df_tesla_vader["negative_sc"] = df_tesla_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neg"])
df_tesla_vader["neutral_sc"] = df_tesla_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neu"])
df_tesla_vader["positive_sc"] = df_tesla_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["pos"])
df_tesla_vader.head()


# In[ ]:


# df_doge_vader["normalized"] = df_doge_vader["Tweet"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))
df_twitter_vader["compound_sc"] = df_twitter_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["compound"])
df_twitter_vader["negative_sc"] = df_twitter_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neg"])
df_twitter_vader["neutral_sc"] = df_twitter_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["neu"])
df_twitter_vader["positive_sc"] = df_twitter_vader["fullText"].apply(lambda tweet: vader.polarity_scores(tweet)["pos"])
df_twitter_vader.head()


# ### Sentiment Analysis by TextBlob

# In[ ]:


# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

# Create a function to compute the negative, neutral, and positive analysis
def getAnalysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"


# In[ ]:


#Make a copy of the df_doge df
df_doge_txtblb = df_doge.copy()

# Create 2 new columns
df_doge_txtblb["subjectivity"] = df_doge_txtblb["fullText"].apply(getSubjectivity)
df_doge_txtblb["polarity"] = df_doge_txtblb["fullText"].apply(getPolarity)
df_doge_txtblb['Sentiment'] = df_doge_txtblb['polarity'].apply(getAnalysis)
df_doge_txtblb.head()
df_doge_txtblb.to_csv("filename.csv")


# In[ ]:


df_doge_txtblb["Sentiment"].value_counts()


# In[ ]:


# Plot the polarity and subjectivity 
plt.figure(figsize=(8,6))
plt.scatter(df_doge_txtblb["polarity"],df_doge_txtblb["subjectivity"], color = 'Blue')
plt.title("Sentiment Analysis")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.grid()
plt.show()


# In[ ]:


#Make a copy of the df_tesla df
df_tesla_txtblb = df_tesla.copy()

# Create 2 new columns
df_tesla_txtblb["subjectivity"] = df_tesla_txtblb["fullText"].apply(getSubjectivity)
df_tesla_txtblb["polarity"] = df_tesla_txtblb["fullText"].apply(getPolarity)
df_tesla_txtblb['Sentiment'] = df_tesla_txtblb['polarity'].apply(getAnalysis)
df_tesla_txtblb.head()


# In[ ]:


df_tesla_txtblb["Sentiment"].value_counts()


# In[ ]:


# Plot the polarity and subjectivity 
plt.figure(figsize=(8,6))
plt.scatter(df_tesla_txtblb["polarity"],df_tesla_txtblb["subjectivity"], color = 'Blue')
plt.title("Sentiment Analysis")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.grid()
plt.show()


# In[ ]:


#Make a copy of the df_twitter df
df_twitter_txtblb = df_twitter.copy()

# Create 2 new columns
df_twitter_txtblb["subjectivity"] = df_twitter_txtblb["fullText"].apply(getSubjectivity)
df_twitter_txtblb["polarity"] = df_twitter_txtblb["fullText"].apply(getPolarity)
df_twitter_txtblb['Sentiment'] = df_twitter_txtblb['polarity'].apply(getAnalysis)
df_twitter_txtblb.head()


# In[ ]:


df_twitter_txtblb["Sentiment"].value_counts()


# In[ ]:


# Plot the polarity and subjectivity 
plt.figure(figsize=(8,6))
plt.scatter(df_twitter_txtblb["polarity"],df_twitter_txtblb["subjectivity"], color = 'Blue')
plt.title("Sentiment Analysis")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.grid()
plt.show()


# In[ ]:


df_dbSentimentData_Combine = pd.concat([df_doge_txtblb,df_tesla_txtblb,df_twitter_txtblb],ignore_index=False)
df_dbSentimentData_Combine.rename(columns = {'Sentiment':'sentiment','polarity':'sentimentScore'} ,inplace=True)


# In[ ]:


df_sentiment_tostore = df_dbSentimentData_Combine[["tweetID","date","adjustedClose","volume","sentimentScore","sentiment"]]


# In[ ]:


#Insert Sentiment data
try:
    SqlConn.insertSentiment(df_sentiment_tostore)
    print("Data transfer Done")
except BaseException as err:
    print(err)

