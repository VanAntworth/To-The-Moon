#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS as stopwords_wc


# In[ ]:


pd.set_option('display.max_colwidth', 100)


# In[ ]:


# Read the csv files containin gthe tweets by Eon Musk from 2010 to 2022.
df_2010 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2010.csv')
df_2011 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2011.csv')
df_2012 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2012.csv')
df_2013 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2013.csv')
df_2014 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2014.csv')
df_2015 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2015.csv')
df_2016 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2016.csv')
df_2017 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2017.csv')
df_2018 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2018.csv')
df_2019 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2019.csv')
df_2020 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2020.csv')
df_2021 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2021.csv')
df_2022 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2022.csv')


# In[ ]:


print(f"shape of 2010 df: " + str(df_2010.shape))
print(f"shape of 2011 df: " + str(df_2012.shape))
print(f"shape of 2012 df: " + str(df_2012.shape))
print(f"shape of 2013 df: " + str(df_2013.shape))
print(f"shape of 2014 df: " + str(df_2014.shape))
print(f"shape of 2015 df: " + str(df_2015.shape))
print(f"shape of 2016 df: " + str(df_2016.shape))
print(f"shape of 2017 df: " + str(df_2017.shape))
print(f"shape of 2018 df: " + str(df_2018.shape))
print(f"shape of 2019 df: " + str(df_2019.shape))
print(f"shape of 2020 df: " + str(df_2020.shape))
print(f"shape of 2021 df: " + str(df_2021.shape))
print(f"shape of 2022 df: " + str(df_2022.shape))


# ### From the above o/p I see that all the dataframes have the same number of columns (39) except for 2021 and 2022 (36). 

# In[ ]:


# Rename and make all columns with same names

df_2010 = df_2010[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2011 = df_2011[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2012 = df_2012[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2013 = df_2013[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2014 = df_2014[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2015 = df_2015[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2016 = df_2016[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2017 = df_2017[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2018 = df_2018[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2019 = df_2019[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2020 = df_2020[['id','date','tweet','nreplies','nlikes','nretweets']]
df_2021 = df_2021[['id','date','tweet','replies_count','likes_count','retweets_count']]
df_2022 = df_2022[['id','date','tweet','replies_count','likes_count','retweets_count']]

df_2021.rename(columns = {'replies_count':'nreplies', 'likes_count':'nlikes','retweets_count':'nretweets'}, inplace = True)
df_2022.rename(columns = {'replies_count':'nreplies', 'likes_count':'nlikes','retweets_count':'nretweets'}, inplace = True)


# In[ ]:


df_2010.columns


# In[ ]:


df_2022.columns


# In[ ]:


df_tweets = pd.concat([df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016,df_2017,df_2018,df_2019,df_2020,df_2021,df_2022],axis = 0)


# In[ ]:


df_tweets.shape


# In[ ]:


df_tweets.head()


# In[ ]:


df_tweets.info()


# In[ ]:


df_elon_tweets = pd.read_csv('../../Tamara/elon_tweets_2.csv')
df_elon_tweets.columns


# In[ ]:


df_elon_tweets = df_elon_tweets.loc[df_elon_tweets['Date']>='2022-03-05']


# In[ ]:


df_elon_tweets['Date'] = pd.to_datetime(df_elon_tweets['Date']).dt.date


# In[ ]:


df_elon_tweets=df_elon_tweets.drop(df_elon_tweets.columns[0], axis=1)


# In[ ]:





# In[ ]:


df_elon_tweets.rename(columns = {'Tweet_ID':'id','Date':'date','Tweet_Text':'tweet','likes_count':'nlikes','retweet_counts':'nretweets'}, inplace = True)
df_elon_tweets


# In[ ]:


df_tweets


# In[ ]:


df_tweets_new = pd.concat([df_tweets,df_elon_tweets],axis=0)

df_tweets_new.shape


# In[ ]:


#Convert the date column from string to "datetime" column. extracting just the date.
df_tweets_new['date'] = pd.to_datetime(df_tweets_new['date']).dt.date
df_tweets_new.head()


# In[ ]:


df_tweets_new.shape


# In[ ]:


# Let us sort the dates in ascending order.
df_tweets_new.sort_values(by=['date'], inplace=True, ascending=True)
df_tweets_new.reset_index(drop=True, inplace=True)
df_tweets_new.head(20)


# #### After sorting the records in ascending order, we see a lot of duplicate records. These duplicate records need to be removed.

# In[ ]:


#Checking for duplicate records
df_tweets_new[df_tweets_new.duplicated(keep='first')][:10]


# In[ ]:


#Drop duplicate records from the dataframe and reset the index
df_tweets_final = df_tweets_new.drop_duplicates(keep='first')
df_tweets_final.reset_index(drop=True, inplace=True)
df_tweets_final.head(15)


# In[ ]:


print(df_tweets_final.shape)


# #### After dropping the duplicate records we see that only half of the records remain. Let us no clean the tweets, ie remove all the #,@ symbols. 

# In[ ]:


#Lets clean the tweets (remove @'s' and urls and)
TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
new = []
for t in df_tweets_final.tweet:
    words = t.split()
    t = t.split()
    t = ' '.join(word for word in t if not word.startswith('@'))
    t = t.split()
    t = ' '.join(word for word in t if not word.startswith('http'))
    new.append(t)
    
df_tweets_final['tweet'] = new
df_tweets_final


# In[ ]:


pd.DatetimeIndex(df_tweets_final["date"]).year


# ### Visualize the number of tweets from 2010 to 2022 of Elon Musk

# In[ ]:


# Get the number of tweets every year by Elon Musk
date_count_df = df_tweets_final.groupby(pd.DatetimeIndex(df_tweets_final["date"]).year)["tweet"].count()
date_count_df = date_count_df.to_frame()
date_count_df


# In[ ]:


# Plot
plt.figure(figsize=(25, 11))
ax = sns.lineplot(data=date_count_df, x= "date", y= "tweet", lw=4)
plt.title("Tweet Count Evolution", size=25)
plt.xlabel("Year", size=20)
plt.ylabel("Frequency", size=20)
sns.despine(left=True)


# ### The number of tweets by Elon Musk kept increasing every year from 2010. Maximum number of tweets were generated in year 2018.

# In[ ]:


#Filter the dogecoin tweets from the df_tweets_new dataset
def filterTweetData(financialType=''):
    df = pd.DataFrame(columns = ['Date', 'Tweet'])

    for i in range(len(df_tweets_final)):
        cur = df_tweets_final.loc[i].tweet
        cur = cur.lower()
        if financialType in cur:
            df = df.append({'id' :df_tweets_final.loc[i].id,
                            'Date' : df_tweets_final.loc[i].date, 
                            'Tweet' : df_tweets_final.loc[i].tweet, 
                            'nlikes':df_tweets_final.loc[i].nlikes,
                            'nreplies':df_tweets_final.loc[i].nreplies,
                            'nretweets':df_tweets_final.loc[i].nretweets
                                     },
                    ignore_index = True)

    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df
    return df


# ### Filter the tweets containing the word "doge"

# In[ ]:


df_doge = filterTweetData('doge')


# In[ ]:


df_doge


# In[ ]:


plt.figure(figsize=(10,8))
allWords = ' '.join([twts for twts in df_doge["Tweet"]])
wordCloud = WordCloud(width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()


# In[ ]:


# Get the number of tweets every year by Elon Musk
date_doge_df = df_doge.groupby(pd.DatetimeIndex(df_doge["Date"]).year)["Tweet"].count()
date_doge_df = date_doge_df.to_frame()
date_doge_df


# In[ ]:


# Plot the number of tweets for dogecoing by elon musk
plt.figure(figsize=(25, 11))
ax = sns.lineplot(data=date_doge_df, x= "Date", y= "Tweet", lw=4)
plt.title("Dogecoin Tweet Count Evolution", size=25)
plt.xlabel("Year", size=20)
plt.ylabel("Frequency", size=20)
# sns.despine(left=True)


# ### Filter the tweets containing the word "tesla"

# In[ ]:


df_tesla = filterTweetData('tesla')


# In[ ]:


df_tesla


# In[ ]:


plt.figure(figsize=(10,8))
allWords = ' '.join([twts for twts in df_tesla["Tweet"]])
wordCloud = WordCloud(width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()


# In[ ]:


# Get the number of tweets every year by Elon Musk
date_tesla_df = df_tesla.groupby(pd.DatetimeIndex(df_tesla["Date"]).year)["Tweet"].count()
date_tesla_df = date_tesla_df.to_frame()
date_tesla_df


# In[ ]:


# Plot the number of tweets for spaceX by elon musk
plt.figure(figsize=(25, 11))
ax = sns.lineplot(data=date_tesla_df, x= "Date", y= "Tweet", lw=4)
plt.title("Tesla Tweet Count Evolution", size=25)
plt.xlabel("Year", size=20)
plt.ylabel("Frequency", size=20)


# In[ ]:


df_twitter = filterTweetData('twitter')


# In[ ]:


df_twitter


# In[ ]:


plt.figure(figsize=(10,8))
stopwords_wc = set(stopwords_wc)
allWords = ' '.join([twts for twts in df_twitter["Tweet"]])
wordCloud = WordCloud(stopwords=stopwords_wc, width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)
plt.imshow(wordCloud, interpolation = "bilinear")
plt.axis("off")
plt.show()


# In[ ]:


# Get the number of tweets every year by Elon Musk
date_twitter_df = df_twitter.groupby(pd.DatetimeIndex(df_twitter["Date"]).year)["Tweet"].count()
date_twitter_df = date_twitter_df.to_frame()
date_twitter_df


# In[ ]:


# Plot the number of tweets for Twitter by elon musk
plt.figure(figsize=(25, 11))
ax = sns.lineplot(data=date_twitter_df, x= "Date", y= "Tweet", lw=4)
plt.title("Twitter Tweet Count Evolution", size=25)
plt.xlabel("Year", size=20)
plt.ylabel("Frequency", size=20)


# In[ ]:


# Get Popularity Information - to be looked by Shreha
popularity = ["likes_count", "retweets_count", "replies_count"]
popularity_df = tweets[tweets["year"]!="2021"].groupby("year").agg({popularity[0] : 'sum',
                                                                    popularity[1] : 'sum',
                                                                    popularity[2] : 'sum',
                                                                    'tweet' : 'count'}).reset_index()
popularity_df["likes_count"] = popularity_df["likes_count"]/popularity_df["tweet"]
popularity_df["retweets_count"] = popularity_df["retweets_count"]/popularity_df["tweet"]
popularity_df["replies_count"] = popularity_df["replies_count"]/popularity_df["tweet"]


# # Database population - Prepare Data for storing in Database and append records

# In[ ]:


df_doge['financeType']='doge'
df_tesla['financeType']='tesla'
df_twitter['financeType']='twitter'


# In[ ]:


df_tweet_tostore = pd.concat([df_doge, df_tesla, df_twitter],axis=0,ignore_index=False)


# In[ ]:


df_tweet_tostore.rename(columns = {'id':'tweetID','Date':'date','Tweet':'fullText','nlikes':'likesCount','nreplies':'replyCount','nretweets':'retweetCount'}, inplace = True)


# In[ ]:


df_tweet_tostore


# In[ ]:


# need to fix this reindexing and dataloss issue
df_tweet_tostore= df_tweet_tostore[["tweetID","financeType","date","fullText","replyCount","likesCount","retweetCount"]]
df_tweet_tostore


# In[ ]:


# Database related all the code is moved to this file
get_ipython().run_line_magic('run', '-i "SqlConn.py"')
#importing local py file
import SqlConn 


# In[ ]:


# Save Tweet data

try:
    SqlConn.insertTweets(df_tweet_tostore)
    print("Data Transfer Done")
except BaseException as err:
    print(err)


# In[ ]:




