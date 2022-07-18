{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43933ecd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install wordcloud"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "be0f6476",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import re\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from wordcloud import WordCloud\n",
    "from wordcloud import STOPWORDS as stopwords_wc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38db485d",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.max_colwidth', 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f345b5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the csv files containin gthe tweets by Eon Musk from 2010 to 2022.\n",
    "df_2010 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2010.csv')\n",
    "df_2011 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2011.csv')\n",
    "df_2012 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2012.csv')\n",
    "df_2013 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2013.csv')\n",
    "df_2014 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2014.csv')\n",
    "df_2015 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2015.csv')\n",
    "df_2016 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2016.csv')\n",
    "df_2017 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2017.csv')\n",
    "df_2018 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2018.csv')\n",
    "df_2019 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2019.csv')\n",
    "df_2020 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2020.csv')\n",
    "df_2021 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2021.csv')\n",
    "df_2022 = pd.read_csv('../Data_Resources/elon_musk_kaggle/2022.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d913207e",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f\"shape of 2010 df: \" + str(df_2010.shape))\n",
    "print(f\"shape of 2011 df: \" + str(df_2012.shape))\n",
    "print(f\"shape of 2012 df: \" + str(df_2012.shape))\n",
    "print(f\"shape of 2013 df: \" + str(df_2013.shape))\n",
    "print(f\"shape of 2014 df: \" + str(df_2014.shape))\n",
    "print(f\"shape of 2015 df: \" + str(df_2015.shape))\n",
    "print(f\"shape of 2016 df: \" + str(df_2016.shape))\n",
    "print(f\"shape of 2017 df: \" + str(df_2017.shape))\n",
    "print(f\"shape of 2018 df: \" + str(df_2018.shape))\n",
    "print(f\"shape of 2019 df: \" + str(df_2019.shape))\n",
    "print(f\"shape of 2020 df: \" + str(df_2020.shape))\n",
    "print(f\"shape of 2021 df: \" + str(df_2021.shape))\n",
    "print(f\"shape of 2022 df: \" + str(df_2022.shape))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "942fef1c",
   "metadata": {},
   "source": [
    "### From the above o/p I see that all the dataframes have the same number of columns (39) except for 2021 and 2022 (36). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1b3a33f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Rename and make all columns with same names\n",
    "\n",
    "df_2010 = df_2010[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2011 = df_2011[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2012 = df_2012[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2013 = df_2013[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2014 = df_2014[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2015 = df_2015[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2016 = df_2016[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2017 = df_2017[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2018 = df_2018[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2019 = df_2019[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2020 = df_2020[['id','date','tweet','nreplies','nlikes','nretweets']]\n",
    "df_2021 = df_2021[['id','date','tweet','replies_count','likes_count','retweets_count']]\n",
    "df_2022 = df_2022[['id','date','tweet','replies_count','likes_count','retweets_count']]\n",
    "\n",
    "df_2021.rename(columns = {'replies_count':'nreplies', 'likes_count':'nlikes','retweets_count':'nretweets'}, inplace = True)\n",
    "df_2022.rename(columns = {'replies_count':'nreplies', 'likes_count':'nlikes','retweets_count':'nretweets'}, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aedf0f37",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_2010.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95feb9a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_2022.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a2fbb51",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets = pd.concat([df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016,df_2017,df_2018,df_2019,df_2020,df_2021,df_2022],axis = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a90dd99d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "190a91a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd069003",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "482c729b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_elon_tweets = pd.read_csv('../../Tamara/elon_tweets_2.csv')\n",
    "df_elon_tweets.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ffcab60",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_elon_tweets = df_elon_tweets.loc[df_elon_tweets['Date']>='2022-03-05']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74998527",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_elon_tweets['Date'] = pd.to_datetime(df_elon_tweets['Date']).dt.date"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "663c3534",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_elon_tweets=df_elon_tweets.drop(df_elon_tweets.columns[0], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3583e9ce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffed73d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_elon_tweets.rename(columns = {'Tweet_ID':'id','Date':'date','Tweet_Text':'tweet','likes_count':'nlikes','retweet_counts':'nretweets'}, inplace = True)\n",
    "df_elon_tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aed19788",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "325f4368",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets_new = pd.concat([df_tweets,df_elon_tweets],axis=0)\n",
    "\n",
    "df_tweets_new.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7761717",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert the date column from string to \"datetime\" column. extracting just the date.\n",
    "df_tweets_new['date'] = pd.to_datetime(df_tweets_new['date']).dt.date\n",
    "df_tweets_new.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f2d55ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweets_new.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c167b571",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let us sort the dates in ascending order.\n",
    "df_tweets_new.sort_values(by=['date'], inplace=True, ascending=True)\n",
    "df_tweets_new.reset_index(drop=True, inplace=True)\n",
    "df_tweets_new.head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3ecdb2d",
   "metadata": {},
   "source": [
    "#### After sorting the records in ascending order, we see a lot of duplicate records. These duplicate records need to be removed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0513c751",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Checking for duplicate records\n",
    "df_tweets_new[df_tweets_new.duplicated(keep='first')][:10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d81912f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Drop duplicate records from the dataframe and reset the index\n",
    "df_tweets_final = df_tweets_new.drop_duplicates(keep='first')\n",
    "df_tweets_final.reset_index(drop=True, inplace=True)\n",
    "df_tweets_final.head(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9c4aff4",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df_tweets_final.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bf9dc7d",
   "metadata": {},
   "source": [
    "#### After dropping the duplicate records we see that only half of the records remain. Let us no clean the tweets, ie remove all the #,@ symbols. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc6d9ff2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Lets clean the tweets (remove @'s' and urls and)\n",
    "TEXT_CLEANING_RE = \"@\\S+|https?:\\S+|http?:\\S|[^A-Za-z0-9]+\"\n",
    "new = []\n",
    "for t in df_tweets_final.tweet:\n",
    "    words = t.split()\n",
    "    t = t.split()\n",
    "    t = ' '.join(word for word in t if not word.startswith('@'))\n",
    "    t = t.split()\n",
    "    t = ' '.join(word for word in t if not word.startswith('http'))\n",
    "    new.append(t)\n",
    "    \n",
    "df_tweets_final['tweet'] = new\n",
    "df_tweets_final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ee06c73",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.DatetimeIndex(df_tweets_final[\"date\"]).year"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d69c0ce",
   "metadata": {},
   "source": [
    "### Visualize the number of tweets from 2010 to 2022 of Elon Musk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7807952d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the number of tweets every year by Elon Musk\n",
    "date_count_df = df_tweets_final.groupby(pd.DatetimeIndex(df_tweets_final[\"date\"]).year)[\"tweet\"].count()\n",
    "date_count_df = date_count_df.to_frame()\n",
    "date_count_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1672b0c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot\n",
    "plt.figure(figsize=(25, 11))\n",
    "ax = sns.lineplot(data=date_count_df, x= \"date\", y= \"tweet\", lw=4)\n",
    "plt.title(\"Tweet Count Evolution\", size=25)\n",
    "plt.xlabel(\"Year\", size=20)\n",
    "plt.ylabel(\"Frequency\", size=20)\n",
    "sns.despine(left=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb09ae4f",
   "metadata": {},
   "source": [
    "### The number of tweets by Elon Musk kept increasing every year from 2010. Maximum number of tweets were generated in year 2018."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd600816",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Filter the dogecoin tweets from the df_tweets_new dataset\n",
    "def filterTweetData(financialType=''):\n",
    "    df = pd.DataFrame(columns = ['Date', 'Tweet'])\n",
    "\n",
    "    for i in range(len(df_tweets_final)):\n",
    "        cur = df_tweets_final.loc[i].tweet\n",
    "        cur = cur.lower()\n",
    "        if financialType in cur:\n",
    "            df = df.append({'id' :df_tweets_final.loc[i].id,\n",
    "                            'Date' : df_tweets_final.loc[i].date, \n",
    "                            'Tweet' : df_tweets_final.loc[i].tweet, \n",
    "                            'nlikes':df_tweets_final.loc[i].nlikes,\n",
    "                            'nreplies':df_tweets_final.loc[i].nreplies,\n",
    "                            'nretweets':df_tweets_final.loc[i].nretweets\n",
    "                                     },\n",
    "                    ignore_index = True)\n",
    "\n",
    "    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')\n",
    "    df\n",
    "    return df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0ddf312",
   "metadata": {},
   "source": [
    "### Filter the tweets containing the word \"doge\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0503517",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge = filterTweetData('doge')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09158116",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e89eef5",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "allWords = ' '.join([twts for twts in df_doge[\"Tweet\"]])\n",
    "wordCloud = WordCloud(width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)\n",
    "plt.imshow(wordCloud, interpolation = \"bilinear\")\n",
    "plt.axis(\"off\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6a44176",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the number of tweets every year by Elon Musk\n",
    "date_doge_df = df_doge.groupby(pd.DatetimeIndex(df_doge[\"Date\"]).year)[\"Tweet\"].count()\n",
    "date_doge_df = date_doge_df.to_frame()\n",
    "date_doge_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0748f83",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the number of tweets for dogecoing by elon musk\n",
    "plt.figure(figsize=(25, 11))\n",
    "ax = sns.lineplot(data=date_doge_df, x= \"Date\", y= \"Tweet\", lw=4)\n",
    "plt.title(\"Dogecoin Tweet Count Evolution\", size=25)\n",
    "plt.xlabel(\"Year\", size=20)\n",
    "plt.ylabel(\"Frequency\", size=20)\n",
    "# sns.despine(left=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a792937",
   "metadata": {},
   "source": [
    "### Filter the tweets containing the word \"tesla\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "853ac1ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tesla = filterTweetData('tesla')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "131998d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tesla"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "557c0e06",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "allWords = ' '.join([twts for twts in df_tesla[\"Tweet\"]])\n",
    "wordCloud = WordCloud(width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)\n",
    "plt.imshow(wordCloud, interpolation = \"bilinear\")\n",
    "plt.axis(\"off\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcdd3d14",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the number of tweets every year by Elon Musk\n",
    "date_tesla_df = df_tesla.groupby(pd.DatetimeIndex(df_tesla[\"Date\"]).year)[\"Tweet\"].count()\n",
    "date_tesla_df = date_tesla_df.to_frame()\n",
    "date_tesla_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24dbb57d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the number of tweets for spaceX by elon musk\n",
    "plt.figure(figsize=(25, 11))\n",
    "ax = sns.lineplot(data=date_tesla_df, x= \"Date\", y= \"Tweet\", lw=4)\n",
    "plt.title(\"Tesla Tweet Count Evolution\", size=25)\n",
    "plt.xlabel(\"Year\", size=20)\n",
    "plt.ylabel(\"Frequency\", size=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8fcdb0ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_twitter = filterTweetData('twitter')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "996e8365",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_twitter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00c91d6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(10,8))\n",
    "stopwords_wc = set(stopwords_wc)\n",
    "allWords = ' '.join([twts for twts in df_twitter[\"Tweet\"]])\n",
    "wordCloud = WordCloud(stopwords=stopwords_wc, width = 1000, height = 600, random_state = 21, max_font_size = 119).generate(allWords)\n",
    "plt.imshow(wordCloud, interpolation = \"bilinear\")\n",
    "plt.axis(\"off\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "702461a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Get the number of tweets every year by Elon Musk\n",
    "date_twitter_df = df_twitter.groupby(pd.DatetimeIndex(df_twitter[\"Date\"]).year)[\"Tweet\"].count()\n",
    "date_twitter_df = date_twitter_df.to_frame()\n",
    "date_twitter_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28cdbe68",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the number of tweets for Twitter by elon musk\n",
    "plt.figure(figsize=(25, 11))\n",
    "ax = sns.lineplot(data=date_twitter_df, x= \"Date\", y= \"Tweet\", lw=4)\n",
    "plt.title(\"Twitter Tweet Count Evolution\", size=25)\n",
    "plt.xlabel(\"Year\", size=20)\n",
    "plt.ylabel(\"Frequency\", size=20)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0dd5e44e",
   "metadata": {},
   "source": [
    "# Database population - Prepare Data for storing in Database and append records"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b082609",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge['financeType']='doge'\n",
    "df_tesla['financeType']='tesla'\n",
    "df_twitter['financeType']='twitter'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b1b9a7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tweet_tostore = pd.concat([df_doge, df_tesla, df_twitter],axis=0,ignore_index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a78bedf4",
   "metadata": {},
   "outputs": [],
   "source": [
    " df_tweet_tostore.rename(columns = {'id':'tweetID','Date':'date','Tweet':'fullText','nlikes':'likesCount','nreplies':'replyCount','nretweets':'retweetCount'}, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "978eaa90",
   "metadata": {},
   "outputs": [],
   "source": [
    " df_tweet_tostore"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5160526",
   "metadata": {},
   "outputs": [],
   "source": [
    "# need to fix this reindexing and dataloss issue\n",
    "df_tweet_tostore= df_tweet_tostore[[\"tweetID\",\"financeType\",\"date\",\"fullText\",\"replyCount\",\"likesCount\",\"retweetCount\"]]\n",
    "df_tweet_tostore"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c52b9d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Database related all the code is moved to this file\n",
    "%run -i \"SqlConn.py\"\n",
    "#importing local py file\n",
    "import SqlConn "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "08c1c595",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save Tweet data\n",
    "\n",
    "try:\n",
    "    SqlConn.insertTweets(df_tweet_tostore)\n",
    "    print(\"Data Transfer Done\")\n",
    "except BaseException as err:\n",
    "    print(err)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0c61453",
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
