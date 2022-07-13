
# To-The-Moon


## Table of Contents
- [Project Overview](#OverviewProject)
- [Background](#Background)
- [Approach](#Approach)
- [Description of Data Exploration](#DataExp)
- [Project Design](#ProjectDesign)
- [Questions We Hope to Answer with Data](#Questions)
- [Resources](#Resources)

## <a name="OverviewProject"></a> Project Overview


It has been observed that Elon Musk tweets have been impacting the Stocks and Cryptocurrency market. We wanted to analyze the impact of the tweets and how long the impact was holding true.
This project will predict the Stock or Cryptocurrencys (Tesla, SpaceX, Twitter and Dogecoin data) future value, and also show the impact of tweets for respective stock/crypto.



## <a name="Backgroud"></a> Backgroud 

In November of 2020, Tamara's husband invested $500 into Doge Coin. At the time the coin was worth $0.002, not even one cent. In Feb 11th, at a price of %0.07, Tamara's husband decided to sell having multiplied his monitary investment 35 times. 

Under the influence of social media Doge Coin would continue to climb in price and reach $0.71 cents at its highest in May 6th of 2021, 355 times the price from November 2020.  The $500 could've have turned into $177,500, something most stocks couldn't do without social media. The value has since dropped close to the $0.07, the price at which Tamara's family sold the coin. 

In 2020 and 2021 Twitter, Reddit and Robin Hood changed the dynamic of the stock market and crypto currencies. Social media became a disruptive force in the economy. Yet Doge could've just been one of many many crypto coins that did not rise in price, if it wasn't for one person that brought notoriety to this currency, Elon Musk.  

Therefore we are embarking on a quest to find the influence Elon Musk tweet's have had over Doge Coin. In the process we are interested in understanding how the use of language by a single individual with a large following, can influence the price of stocks and coins. 

## <a name="Approach"></a> Approach:

- Retrieving tweet data as well as stock data.

- Display the trends and also predict the stock prices and crypto price based on yahoo financial data. 

- Preprocessed the data dumps to clean data and store it into postgres database. 

- Used sentiment analysis to analyse the tweets as positive, negative or neutral.

- Used the sentiment analysis imputs to build a model for predicting the impact of the tweets on the near future stock price.

- Pull the data from database to create visualizations.


## <a name="DataExp"></a> Description of the Data Exploration:
  
Troubleshooting with different web scraping libraries while using python code in jupyter notebook to acces twitter/twitter API

Worked with creating different environments in terminal 
  
? (Question for Tammy and Shreha) Forced to make version adjustments due to different libraries and web scraping tools requiring different versions of python.

## <a name="ProjectDesign"></a> Project Design

ER Diagram

![ERD_Diagram](https://user-images.githubusercontent.com/99001393/178597346-950f6185-d9a7-4ead-bb12-8c7a80fbe2df.jpg)

  
## <a name="Questions"></a> Questions we hope to answer with Data

Whether the sentiments of elon musks tweets affects the price in the short term of crypto and stocks 

How long does an Elon Musk tweet affect the price of the coin.

 1.) Prediction of DogeCoin/ Tesla/ SpaceX/ Twitter for near future after related tweets.
 
 2.) Impact of Elon Musk Tweets on DogeCoin/ Tesla/ SpaceX/ Twitter.
 
 3.) How long the impact (on the value of the stock/coin) stays in effect after the tweet.

## Resources

### Information Resources

Elon Musk Tweets

Yahoo Finance data

### Code Used

<a name="1">[1]</a> [School Distric Analysis without Thomas High School 9th Grade](https://github.com/tamiespinosa/School_District_Analysis/blob/d230e051353b12aff7ec079be477609ec4f7bb8c/PyCitySchools_Challenge.ipynb)


### Data Resources

<a name="1">[1]</a> [Elon Tweets from Kaggle](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment1_Delivery/Data_Resources/elon_musk_kaggle)

<a name="1">[1]</a> [Elon Tweets Scrapped](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Data_Resources/elon_musk_kaggle/elon_tweets_2.csv)

<a name="1">[1]</a> [Finance Data Scrapped](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment1_Delivery/Data_Resources/scrapped_data)


