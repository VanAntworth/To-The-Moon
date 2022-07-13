
DROP TABLE IF EXISTS "Twitter_data" ;
CREATE TABLE "Twitter_data" (
    "ID" INT   NOT NULL,
    "tweet_id" BIGINT   NOT NULL,
    "Finance_Type" VARCHAR   NOT NULL,
    "date" DATE   NOT NULL,
    "full_text" VARCHAR   NOT NULL,
    "reply_count" INTEGER   NOT NULL,
    "likes_count" INTEGER   NOT NULL,
    "retweet_count" INTEGER   NOT NULL,
    CONSTRAINT "pk_Twitter_data" PRIMARY KEY (
        "ID"
     ),
    CONSTRAINT "uc_Twitter_data_tweet_id" UNIQUE (
        "tweet_id"
    )
);

DROP TABLE IF EXISTS "Finance_USD_Data" ;
CREATE TABLE "Finance_USD_Data" (
    "ID" INTEGER   NOT NULL,
    "Finance_Type" VARCHAR   NOT NULL,
    "Date" DATE   NOT NULL,
    "OPEN_AT" FLOAT   NOT NULL,
    "HIGH" FLOAT   NOT NULL,
    "LOW" FLOAT   NOT NULL,
    "CLOSE" FLOAT   NOT NULL,
    "ADJUSTED_CLOSE" FLOAT   NOT NULL,
    "Volumn" BIGINT   NOT NULL,
    CONSTRAINT "pk_Finance_USD_Data" PRIMARY KEY (
        "ID"
     )
);

DROP TABLE IF EXISTS "Sentiment_Scoring" ;
CREATE TABLE "Sentiment_Scoring" (
    "ID" INTEGER   NOT NULL,
    "Twitter_ID" INT   NOT NULL,
    "Date" DATE   NOT NULL,
    "Closing_Price" FLOAT   NOT NULL,
    "Volumn" BIGINT   NOT NULL,
    "Sentiment_Score" FLOAT   NOT NULL,
    "Sentiment" SMALLINT   NOT NULL,
    CONSTRAINT "pk_Sentiment_Scoring" PRIMARY KEY (
        "ID"
     )
);

DROP TABLE IF EXISTS "Predicted_Values" ;
CREATE TABLE "Predicted_Values" (
    "ID" INTEGER   NOT NULL,
    "Model" VARCHAR   NOT NULL,
    "runFrom" VARCHAR   NOT NULL,
    "Precision" FLOAT   NOT NULL,
    "Recall" FLOAT   NOT NULL,
    "F1_score" FLOAT   NOT NULL,
    "Accuracy" FLOAT   NOT NULL,
    "Predicated_Dogecoin_Value" FLOAT   NOT NULL,
    "Date" DATE   NOT NULL,
    "Actual_value" FLOAT   NOT NULL,
    CONSTRAINT "pk_Predicted_Values" PRIMARY KEY (
        "ID"
     )
);

--CREATE TABLE "twitter_data_Extension" (
--    "tweet_id" BIGINT   NOT NULL,
--    "reply_to" VARCHAR   NOT NULL,
--    "language" VARCHAR   NOT NULL,
--    "timezone" VARCHAR   NOT NULL,
--    "mentions" VARCHAR   NOT NULL,
--    "hashtag" VARCHAR   NOT NULL,
--    "CASHTAG" VARCHAR   NOT NULL,
--    "type" VARCHAR   NOT NULL,
--    "username" VARCHAR   NOT NULL,
--    CONSTRAINT "pk_twitter_data_Extension" PRIMARY KEY (
--        "tweet_id"
--     )
--);

ALTER TABLE "Sentiment_Scoring" ADD CONSTRAINT "fk_Sentiment_Scoring_Twitter_ID" FOREIGN KEY("Twitter_ID")
REFERENCES "Twitter_data" ("ID");

