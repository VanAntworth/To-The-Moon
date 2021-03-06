DROP TABLE IF EXISTS "SentimentScoring" ;
CREATE TABLE "SentimentScoring" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "date" DATE   NOT NULL,
    "adjustedClose" FLOAT   NULL,
    "volume" BIGINT    NULL,
    "sentimentScore" FLOAT   NOT NULL,
    "sentiment" VARCHAR(50)   
    CONSTRAINT "pkSentimentScoring" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "TwitterData" ;
CREATE TABLE "TwitterData" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" VARCHAR(50)   NOT NULL,
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


DROP TABLE IF EXISTS "FinanceDeltaPercents" ;
CREATE TABLE "FinanceDeltaPercents" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "financeType" VARCHAR(50)   NOT NULL,
    "date" DATE   NOT NULL,
    "fullText" VARCHAR(max)  NOT NULL,
    "likesCount" INTEGER ,
	"retweetCount" INTEGER  ,
	"sentiment" VARCHAR  ,
	"sentimentScore" FLOAT   NOT NULL,
	"startDate" DATE   NOT NULL,
	"datesDifference" INTEGER NOT NULL,
	"weekendOrHoliday" VARCHAR NOT NULL,
    "deltaPrice_0" FLOAT   NULL,
    "deltaPrice_1" FLOAT   NULL,
    "deltaPrice_2" FLOAT   NULL,
    "deltaPrice_3" FLOAT   NULL,
    "deltaPrice_4" FLOAT   NULL,
	"deltaPrice_5" FLOAT   NULL,
    "deltaPrice_6" FLOAT   NULL,
    "deltaPrice_7" FLOAT   NULL,
    "percentPrice_0" FLOAT   NULL,
    "percentPrice_1" FLOAT   NULL,
    "percentPrice_2" FLOAT   NULL,
    "percentPrice_3" FLOAT   NULL,
    "percentPrice_4" FLOAT   NULL,
	"percentPrice_5" FLOAT   NULL,
    "percentPrice_6" FLOAT   NULL,
    "percentPrice_7" FLOAT   NULL,
    "deltaVol_0" FLOAT   NULL,
    "deltaVol_1" FLOAT   NULL,
    "deltaVol_2" FLOAT   NULL,
    "deltaVol_3" FLOAT   NULL,
    "deltaVol_4" FLOAT   NULL,
	"deltaVol_5" FLOAT   NULL,
    "deltaVol_6" FLOAT   NULL,
    "deltaVol_7" FLOAT   NULL,
    "percentVol_0" FLOAT   NULL,
    "percentVol_1" FLOAT   NULL,
    "percentVol_2" FLOAT   NULL,
    "percentVol_3" FLOAT   NULL,
    "percentVol_4" FLOAT   NULL,
	"percentVol_5" FLOAT   NULL,
    "percentVol_6" FLOAT   NULL,
    "percentVol_7" FLOAT   NULL,

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
    "datePosition" INTEGER   NOT NULL,
    "adjustedClose" FLOAT   NOT NULL,
    "volume" BIGINT ,
    CONSTRAINT "pkFinanceTweetForecast" PRIMARY KEY (
        "id"
     )
);
