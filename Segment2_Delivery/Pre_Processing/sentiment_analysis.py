{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d95eef9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17b90156",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import re\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "from textblob import TextBlob\n",
    "import nltk\n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer\n",
    "import unicodedata\n",
    "from sqlalchemy import create_engine\n",
    "from sqlalchemy.orm import scoped_session, sessionmaker\n",
    "import psycopg2\n",
    "import pyodbc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a45c91f",
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
   "id": "7e793efd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Fetch Tweets and Sentiment data - Join from Tweet and Sentiment tables\n",
    "try:\n",
    "    df_dbSentimentData = SqlConn.fetchTweetSentiment()\n",
    "    print(\"Data transfer Done\")\n",
    "except BaseException as err:\n",
    "    print(err)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1eb4195c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_dbSentimentData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2aa14490",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the csv files containin the tweets by Eon Musk from 2010 to 2022 for DogeCOin, Tesla, spaceX, twitter.\n",
    "#df_doge = pd.read_csv('../Data_Resources/scrapped_data/doge_tweets.csv')\n",
    "#df_spaceX = pd.read_csv('../Data_Resources/scrapped_data/spaceX_tweets.csv')\n",
    "#df_tesla = pd.read_csv('../Data_Resources/scrapped_data/tesla_tweets.csv')\n",
    "#df_twitter = pd.read_csv('../Data_Resources/scrapped_data/twitter_tweets.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6f3baf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'doge']\n",
    "df_tesla = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'tesla']\n",
    "df_twitter = df_dbSentimentData.loc[df_dbSentimentData.financeType == 'twitter']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd32863d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21add833",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(f\"shape of doge df: \" + str(df_doge.shape))\n",
    "print(f\"shape of tesla df: \" + str(df_tesla.shape))\n",
    "print(f\"shape of twitter df: \" + str(df_twitter.shape))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94455c4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cba280fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tesla.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b545d7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_twitter.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1e634c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "nltk.download('vader_lexicon')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c44fa83",
   "metadata": {},
   "outputs": [],
   "source": [
    "vader = SentimentIntensityAnalyzer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c7aa9f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge_vader = df_doge.copy()\n",
    "df_tesla_vader = df_tesla.copy()\n",
    "df_twitter_vader = df_twitter.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5cd5806c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_doge_vader[\"normalized\"] = df_doge_vader[\"Tweet\"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))\n",
    "df_doge_vader[\"compound_sc\"] = df_doge_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"compound\"])\n",
    "df_doge_vader[\"negative_sc\"] = df_doge_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neg\"])\n",
    "df_doge_vader[\"neutral_sc\"] = df_doge_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neu\"])\n",
    "df_doge_vader[\"positive_sc\"] = df_doge_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"pos\"])\n",
    "df_doge_vader.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "467ac979",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_doge_vader[\"normalized\"] = df_doge_vader[\"Tweet\"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))\n",
    "df_tesla_vader[\"compound_sc\"] = df_tesla_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"compound\"])\n",
    "df_tesla_vader[\"negative_sc\"] = df_tesla_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neg\"])\n",
    "df_tesla_vader[\"neutral_sc\"] = df_tesla_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neu\"])\n",
    "df_tesla_vader[\"positive_sc\"] = df_tesla_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"pos\"])\n",
    "df_tesla_vader.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a438233",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df_doge_vader[\"normalized\"] = df_doge_vader[\"Tweet\"].apply(lambda tweet:unicodedata.normalize('NFKD', tweet))\n",
    "df_twitter_vader[\"compound_sc\"] = df_twitter_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"compound\"])\n",
    "df_twitter_vader[\"negative_sc\"] = df_twitter_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neg\"])\n",
    "df_twitter_vader[\"neutral_sc\"] = df_twitter_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"neu\"])\n",
    "df_twitter_vader[\"positive_sc\"] = df_twitter_vader[\"fullText\"].apply(lambda tweet: vader.polarity_scores(tweet)[\"pos\"])\n",
    "df_twitter_vader.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00b47293",
   "metadata": {},
   "source": [
    "### Sentiment Analysis by TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbee5101",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to get the subjectivity\n",
    "def getSubjectivity(text):\n",
    "    return TextBlob(text).sentiment.subjectivity\n",
    "\n",
    "# Create a function to get the polarity\n",
    "def getPolarity(text):\n",
    "    return TextBlob(text).sentiment.polarity\n",
    "\n",
    "# Create a function to compute the negative, neutral, and positive analysis\n",
    "def getAnalysis(score):\n",
    "    if score < 0:\n",
    "        return \"Negative\"\n",
    "    elif score == 0:\n",
    "        return \"Neutral\"\n",
    "    else:\n",
    "        return \"Positive\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63d021f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Make a copy of the df_doge df\n",
    "df_doge_txtblb = df_doge.copy()\n",
    "\n",
    "# Create 2 new columns\n",
    "df_doge_txtblb[\"subjectivity\"] = df_doge_txtblb[\"fullText\"].apply(getSubjectivity)\n",
    "df_doge_txtblb[\"polarity\"] = df_doge_txtblb[\"fullText\"].apply(getPolarity)\n",
    "df_doge_txtblb['Sentiment'] = df_doge_txtblb['polarity'].apply(getAnalysis)\n",
    "df_doge_txtblb.head()\n",
    "df_doge_txtblb.to_csv(\"filename.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "122dd7f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_doge_txtblb[\"Sentiment\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f96e082",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the polarity and subjectivity \n",
    "plt.figure(figsize=(8,6))\n",
    "plt.scatter(df_doge_txtblb[\"polarity\"],df_doge_txtblb[\"subjectivity\"], color = 'Blue')\n",
    "plt.title(\"Sentiment Analysis\")\n",
    "plt.xlabel(\"Polarity\")\n",
    "plt.ylabel(\"Subjectivity\")\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "09c5333a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Make a copy of the df_tesla df\n",
    "df_tesla_txtblb = df_tesla.copy()\n",
    "\n",
    "# Create 2 new columns\n",
    "df_tesla_txtblb[\"subjectivity\"] = df_tesla_txtblb[\"fullText\"].apply(getSubjectivity)\n",
    "df_tesla_txtblb[\"polarity\"] = df_tesla_txtblb[\"fullText\"].apply(getPolarity)\n",
    "df_tesla_txtblb['Sentiment'] = df_tesla_txtblb['polarity'].apply(getAnalysis)\n",
    "df_tesla_txtblb.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad2bf529",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_tesla_txtblb[\"Sentiment\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b189269e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the polarity and subjectivity \n",
    "plt.figure(figsize=(8,6))\n",
    "plt.scatter(df_tesla_txtblb[\"polarity\"],df_tesla_txtblb[\"subjectivity\"], color = 'Blue')\n",
    "plt.title(\"Sentiment Analysis\")\n",
    "plt.xlabel(\"Polarity\")\n",
    "plt.ylabel(\"Subjectivity\")\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62ebf3b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Make a copy of the df_twitter df\n",
    "df_twitter_txtblb = df_twitter.copy()\n",
    "\n",
    "# Create 2 new columns\n",
    "df_twitter_txtblb[\"subjectivity\"] = df_twitter_txtblb[\"fullText\"].apply(getSubjectivity)\n",
    "df_twitter_txtblb[\"polarity\"] = df_twitter_txtblb[\"fullText\"].apply(getPolarity)\n",
    "df_twitter_txtblb['Sentiment'] = df_twitter_txtblb['polarity'].apply(getAnalysis)\n",
    "df_twitter_txtblb.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "213a9998",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_twitter_txtblb[\"Sentiment\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eed4feee",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot the polarity and subjectivity \n",
    "plt.figure(figsize=(8,6))\n",
    "plt.scatter(df_twitter_txtblb[\"polarity\"],df_twitter_txtblb[\"subjectivity\"], color = 'Blue')\n",
    "plt.title(\"Sentiment Analysis\")\n",
    "plt.xlabel(\"Polarity\")\n",
    "plt.ylabel(\"Subjectivity\")\n",
    "plt.grid()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5266797",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_dbSentimentData_Combine = pd.concat([df_doge_txtblb,df_tesla_txtblb,df_twitter_txtblb],ignore_index=False)\n",
    "df_dbSentimentData_Combine.rename(columns = {'Sentiment':'sentiment','polarity':'sentimentScore'} ,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3044c111",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sentiment_tostore = df_dbSentimentData_Combine[[\"tweetID\",\"date\",\"adjustedClose\",\"volume\",\"sentimentScore\",\"sentiment\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d739489f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Insert Sentiment data\n",
    "try:\n",
    "    SqlConn.insertSentiment(df_sentiment_tostore)\n",
    "    print(\"Data transfer Done\")\n",
    "except BaseException as err:\n",
    "    print(err)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "514824d0",
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
