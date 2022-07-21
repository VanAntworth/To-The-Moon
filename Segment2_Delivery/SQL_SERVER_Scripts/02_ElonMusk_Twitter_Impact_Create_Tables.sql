DROP TABLE IF EXISTS "SentimentScoring" ;
CREATE TABLE "SentimentScoring" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "date" DATE   NOT NULL,
    "adjustedClose" FLOAT   NOT NULL,
    "volume" BIGINT   NOT NULL,
    "sentimentScore" FLOAT   NOT NULL,
    "sentiment" VARCHAR(50)   
    CONSTRAINT "pkSentimentScoring" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "TwitterData" ;
CREATE TABLE "TwitterData" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "financeType" VARCHAR(50)   NOT NULL,
    "date" DATE   NOT NULL,
    "fullText" VARCHAR(max)  NOT NULL,
    "replyCount" INTEGER ,
    "likesCount" INTEGER ,
    "retweetCount" INTEGER  ,
    CONSTRAINT "pkTwitterData" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "FinanceUsdData" ;
CREATE TABLE "FinanceUsdData" (
    "id" BIGINT IDENTITY(1,1),
    "financeType" VARCHAR(50)   NOT NULL,
    "date" DATE   NOT NULL,
    "open" FLOAT   NOT NULL,
    "high" FLOAT   ,
    "low" FLOAT   ,
    "close" FLOAT  ,
    "adjustedClose" FLOAT   NOT NULL,
    "volume" BIGINT ,
    CONSTRAINT "pkFinanceUsdData" PRIMARY KEY (
        "id"
     )
);


DROP TABLE IF EXISTS "PredictedValues" ;
CREATE TABLE "PredictedValues" (
    "id" BIGINT  IDENTITY(1,1),
    "modelName" VARCHAR   NOT NULL,
    "accuracy" FLOAT   NOT NULL,
	"results" VARCHAR,
    "predicatedDogecoinValue" FLOAT   NOT NULL,
    "date" DATE   NOT NULL,
    "actualValue" FLOAT   NOT NULL,
	"model" varbinary(max) ,
    CONSTRAINT "pkPredictedValues" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "FinanceDeltaPercents" ;
CREATE TABLE "FinanceDeltaPercents" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "financeType" VARCHAR(50)   NOT NULL,
    "date" DATE   NOT NULL,
    "fullText" VARCHAR(max)  NOT NULL,
    "likesCount" INTEGER ,
	"retweetCount" INTEGER  ,
	"sentimentScore" FLOAT   NOT NULL,
    "sentiment" VARCHAR(50)   NOT NULL,
	"startDate" DATE   NOT NULL,
	"weekendOrHoliday" VARCHAR NOT NULL,
    "deltaPrice_0" FLOAT   NOT NULL,
    "deltaPrice_1" FLOAT   NOT NULL,
    "deltaPrice_2" FLOAT   NOT NULL,
    "deltaPrice_3" FLOAT   NOT NULL,
    "deltaPrice_4" FLOAT   NOT NULL,
    "percentPrice_0" FLOAT   NOT NULL,
    "percentPrice_1" FLOAT   NOT NULL,
    "percentPrice_2" FLOAT   NOT NULL,
    "percentPrice_3" FLOAT   NOT NULL,
    "percentPrice_4" FLOAT   NOT NULL,
    "deltaVol_0" FLOAT   NOT NULL,
    "deltaVol_1" FLOAT   NOT NULL,
    "deltaVol_2" FLOAT   NOT NULL,
    "deltaVol_3" FLOAT   NOT NULL,
    "deltaVol_4" FLOAT   NOT NULL,
    "percentVol_0" FLOAT   NOT NULL,
    "percentVol_1" FLOAT   NOT NULL,
    "percentVol_2" FLOAT   NOT NULL,
    "percentVol_3" FLOAT   NOT NULL,
    "percentVol_4" FLOAT   NOT NULL,

    CONSTRAINT "pkFinanceDeltaPercents" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "FinanceTweetForecast" ;
CREATE TABLE "FinanceTweetForecast" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
	"tweetDate" DATE   NOT NULL,
    "financeType" VARCHAR(50)   NOT NULL,
	"financeID" BIGINT NOT NULL,
    "financeDate" DATE   NOT NULL,
    "datePosition" DATE   NOT NULL,
    "adjustedClose" FLOAT   NOT NULL,
    "volume" BIGINT ,
    CONSTRAINT "pkFinanceTweetForecast" PRIMARY KEY (
        "id"
     )
);
