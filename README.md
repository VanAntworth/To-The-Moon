
# To-The-Moon <img src="Images/rocket.png" height="50" width="100">
<img src="Images/banner_for_Readme.jpg"  align="center" height="300" width="1200">


## Table of Contents
- [Project Overview](#OverviewProject)   
  * [Background](#Background)
  * [Questions We Hope to Answer with Data](#Questions)
  * [Approach](#Approach)
- [Data Exploration phase](#DataExp)
  * [Data Retrieval](#retrieval)
  * [Database Design](#dbDesign)
  * [Preprocessing of Data](#preprocessing)
- [Analysis Phase](#Analysis)
- [Machine Learning](#ML)
  * [Models used for Stock Prdiction](#stockPred)
  * [Models used for Stock Prdiction with Sentiment Score](#sentiPred)
- [Visualization](#visual)
- [Technologies](#Technologies)
- [Resources](#Resources)

## <a name="OverviewProject"></a> Project Overview

It has been observed that Elon Musk tweets have been impacting the Stocks and Cryptocurrency market. We wanted to analyze the impact of the tweets and how long the impact was holding true.
This project will predict the Stock or Cryptocurrencys (Tesla, Twitter and Dogecoin data) future value, and also show the impact of tweets for respective stock/crypto.


### <a name="Background"></a> Background 

In November of 2020, one of our teammates' family invested $500 into Doge Coin. At the time the coin was worth $0.002, not even one cent. In Feb 11th, at a price of $0.07, her family decided to sell having multiplied their monitary investment 35 times. 

**Under the influence of social media Doge Coin would continue to climb in price and reach $0.71 cents at its highest in May 6th of 2021, 355 times the price from November 2020.** The $500 could've have turned into $177,500, something most stocks couldn't do without social media. The value has since dropped close to the $0.07, the price at which her family sold the coin. 

In 2020 and 2021 Twitter, Reddit and Robin Hood changed the dynamics of the stock market and crypto currencies. Social media became a disruptive force in the economy. Yet **Doge could've just been one of many many crypto coins that did not rise in price, if it wasn't for one person that brought notoriety to this currency, Elon Musk.**  

Therefore we are embarking on a quest to find the influence Elon Musk tweet's have had over **Dogecoin, Tesla stock, and Twitter stock**. In the process we are interested in understanding how the use of language by a single individual with a large following, can influence the price of stocks and coins. 

### <a name="Questions"></a> Questions we hope to answer with Data

Does Elon Musk have the ability to sway the market in his favor? With our data analysis and visualizations and after implementing machine learning algorithms we hope to answer the follwing questions:  

 1. Whether the sentiments of elon musks tweets affects the price in the short term of crypto and stocks 

 2. Prediction of DogeCoin/ Tesla/ Twitter for near future after related tweets.
 
 3. Impact of Elon Musk Tweets on DogeCoin/ Tesla/ Twitter.
 
 4. How long the impact (on the value of the stock/coin) stays in effect after the tweet.


### <a name="Approach"></a> Approach:

- Retrieving tweet data as well as stock data.
- Display the trends and also predict the stock prices and crypto price based on yahoo financial data. 
- Preprocessed the data dumps to clean data and store it into postgres database. 
- Used sentiment analysis to analyse the tweets as positive, negative or neutral.
- Used the sentiment analysis imputs to build a model for predicting the impact of the tweets on the near future stock price.
- Pull the data from database to create visualizations.

<p align="center"> <img width ="45%" src ="Images/system.png"> </p>
<p align="center"> <b> <i> Proposed System</i></b></p>

## <a name="DataExp"></a> Data Exploration Phase:
  
  During the data exploration phase the following steps are implemented:

- Retrieving tweet data as well as stock data
- Create a ER design of the database and then implement it
- EDA and Data Preprocessing - using Python
- Finally populate the database with the clean and preprocessed data.

### <a name="retrieval"></a> Data retrieval

For our project we have prepared the data in the following ways:

- [Elon Musk Kaggle Data](Segment4_Delivery/Data_Resources) - Pulled the data from Kaggle, which contains a dump of Elon Musk tweets from 2010 to 2021. 
- [Code for scraping Twitter data](Segment4_Delivery/Data_Scraping/TwitterScrape_UserTimeLine.ipynb) - Used **Twitter API - Tweepy**, to get the latest tweets of Elon Musk in 2022. 
- [Code for scraping Stock price data from Yahoo Finance](Segment4_Delivery/Data_Scraping/Finance_data.ipynb) - Retrieved the stock price data for **Doge,Tesla,Twitter** using **Yahoo Finance API**.

### <a name="dbDesign"></a> Database Design

For our project, we are using a relational database - **Microsoft SQL Server**.
Below is the ER Diagram of the database:

<p align="center"> <img width ="45%" src ="Images/ERD_Diagram.png"> </p>
<p align="center"> <b> <i> Entity–relationship Diagram</i></b></p>

**Stored procedures and SQL scripts** are used to populate, read/write to database. These stored Procedures helped us in reusing the code in every python program , without manually writing each command. 

Click below to see the SQL Scripts :

[SQL Scripts for populating the database](Segment4_Delivery/SQL_SERVER_Scripts)

### <a name="preprocessing"></a> Preprocessing of Data

The scraped data from Twitter and Yahoo Finance, was first stored in CSVs. We read these csvs in our python programs and performed the below preprocessing steps:
1. Merged the twitter scraped data with the Kaggle data.
2. Renamed the columns to keep only matching ones.
3. Checked for null values.
4. Checked for duplicates and removed them.
5. Dropped the unnecessary columns and retrieved only the ones required for our analysis.
6. Formatted the date and changed it to datetime index.
7. Cleaned the tweets to make it more readable using Regex library in Python. We removed any special charactes like @,#. Also removed any URLs in the text.
8. The finance data for the stocks/ crypto was processed using Python program and then stored in the database.

Below is the link to the codes for preprocessing phase:

[Python notebooks for Preprocessing](Segment4_Delivery/Pre_Processing) 


## <a name="Analysis"></a> Analysis Phase

After the preprocessing of the data we performed the following analysis: 
- Performed sentiment analysis on the tweets using the **NLTK Vader** library. VADER not only tells about the Positivity and Negativity score but also tells us about how positive or negative a sentiment is. After performing sentiment analysis on every tweet, we get a 'positive','negative','neutral',compound scores. We classified a tweet as Positive, if the compund score was > 1 and Negative if the compund score was < 1. 
- We analyzed the finance date to see current and past market trends for **Doge, Tesla and Twitter**.  
- We merged the Twitter data and the Finance data to analyze the stock/crypto price for seven days when the Elon Musk tweeted. We calculated a percentage change in price for these 7 days. 
- Now it was the time to choose the machine learning models to predict and stock prices and also to predict an impact on stock price of Elon Musk tweet.

**One of the charts created in tableau to show sentiment scoring as well as the respective tweet(stacked tweets indicate multiple tweets on that particular day).**

<p align="center"><img width ="50%" alt="Screen Shot 2022-07-29 at 2 25 08 PM" src="https://user-images.githubusercontent.com/99001393/181830431-c160ec05-cde4-4994-9e00-40160578de0d.png"></p>

## <a name="ML"></a> Machine Learning

We have implemented machine learning models to do the following:
1.	Prediction of Stock Prices
2.	Predict of impact of Elon’s tweets on stock prices.

### <a name="stockPred"></a> Models used for Stock Prdiction

The first step that was performed before training the models was to fetch the values for **Tesla, Twitter and Doge** using **Yahoo Finance API** and store then in our SQL database. Following information is extracted for every stock - Date, Open, High, Low, adjustedClose, Volume. Before fitting our model, we preprocessed the data tried to visualize the data with the help of graphs.

Following models have been implemented for predicting the stock price:
1. Linear Regression
2. Arima (AutoRegressive Integrated Moving Average)
3. LSTM (Long Short Term Memory)

**Linear Regression:**

Linear regression is a linear model, e.g. a model that assumes a linear relationship between the input variables (x) and the single output variable (y). 
For predicting stock prices, we started with creating a **base model with Linear Regression**. We train a simple linear regression model using a 10-day exponential moving average as a predictor for the closing price. The ‘Date’ column will be converted to a DatetimeIndex and the ‘Adj Close’ will be the only numerical values we keep, while dropping the rest of the columns. 

**ARIMA (AutoRegressive Integrated Moving Average):**

After Linear Regression, we implemented a time series model – Arima. It is a form of regression analysis that gauges the strength of one dependent variable relative to other changing variables.

**LSTM (Long Short Term Memory):**

It is a variety of recurrent neural networks (RNNs) that are capable of learning long-term dependencies, especially in sequence prediction problems. LSTM has feedback connections, i.e., it is capable of processing the entire sequence of data, apart from single data points such as images. LSTMs help solve exploding and vanishing gradient problems.

<p align="center"><img src = "Images/ml_comp.png" width = 50%></p>
<p align="center"><b><i> Model Comparison for Stock Price Prdictions </i></b></p>


**Error Metric Comparison for all the Models:**

<img src = "Images/error_doge.png" width = 33%> <img src = "Images/error_tesla.png" width = 33%> <img src = "Images/error_twitter.png" width = 33%>

<img src = "Images/error_doge1.png" width = 33%> <img src = "Images/error_tesla1.png" width = 33%> <img src = "Images/error_twitter1.png" width = 33%>
<p align="center"><b><i> MAE, MAPE, RMSE values comparison for Doge,Tesla,Twitter</i></b></p>

**Conclusion:**

To summarize, we started with the prediction of the closing price of a stock/cryptocurrency with a univariate model – Linear Regression. Several features were visualized with the help of graphs and the data was preprocessed for the machine learning models. We have implemented 3 different machine learning models – Linear Regression, ARIMA, LSTM. 

The possible ways to improve every model is:

-	Implement a multivariate model for Linear Regression as the stock price is dependent on various other factors.
-	Implement a multivariate LSTM model. Also, understand the learning rate and create a customized function for our model to work better.
-   Implement an ensemble model by integrating Arima and LSTM.

Below is the link to all the Machine Learning notebooks:

[Machine Learning Jupyter Notebooks](Segment4_Delivery/Machine_Learning)


## <a name="sentiPred"></a> Models used for Stock Prdiction with Sentiment Score


## <a name="visual"></a> Visualization

We have chosen the below technologies to showcase our project:

- Tableau
- Website 

We have deployed our website on Heroku and Github.

## <a name="communication"></a> Communication Protocols



 ## <a name="Technologies"></a> Technologies
 
 <img width="745" alt="Screen Shot 2022-07-27 at 2 32 14 PM" src="https://user-images.githubusercontent.com/99001393/181356685-026f4361-dc5b-4ec6-a7e9-216ba3e09f22.png">


## <a name="Resources"></a> Resources

### Information Resources

Elon Musk Tweets

Yahoo Finance data

### <ins>Deliverable 1</ins>

#### Code Used

<a name="1">[1]</a> [Finance Scrapping Code](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Data_Scraping/Finance_data.ipynb)

<a name="2">[2]</a> [Twitter Scrapping Code](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Data_Scraping/TwitterScrape_UserTimeLine.ipynb)

<a name="3">[3]</a> [Data Pre-Processing Code](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Pre_Processing/Elon_tweets_preprocessing.ipynb)

<a name="4">[4]</a> [Sentiment Analysis Code](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Pre_Processing/sentiment_analysis.ipynb)

<a name="5">[5]</a> [Data Base - SQL Queries](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment1_Delivery/Sql_Scripts)

#### Data Resources

<a name="6">[6]</a> [Elon Tweets from Kaggle](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment1_Delivery/Data_Resources/elon_musk_kaggle)

<a name="7">[7]</a> [Elon Tweets Scrapped](https://github.com/VanAntworth/To-The-Moon/blob/main/Segment1_Delivery/Data_Resources/elon_musk_kaggle/elon_tweets_2.csv)

<a name="8">[8]</a> [Finance Data Scrapped](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment1_Delivery/Data_Resources/scrapped_data)

### <ins>Deliverable 2</ins>

#### Machine Learning

<a name="9">[1]</a> [Machine Learning Code](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment2_Delivery/Machine_Learning)

#### Data Base

<a name="10">[2]</a> [Data Base Script](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment2_Delivery/SQL_SERVER_Scripts)

#### Visualization




<a name="10">[3]</a> [Visualization Discussion](https://github.com/VanAntworth/To-The-Moon/blob/main/Resources/Visualizations.docx)  
<a name="10">[4]</a> [Visualization Dashboard](https://github.com/VanAntworth/To-The-Moon/tree/main/Segment2_Delivery/Visualization)




