DROP TABLE IF EXISTS "SentimentScoring" ;
CREATE TABLE "SentimentScoring" (
    "id" BIGINT  IDENTITY(1,1),
    "tweetID" BIGINT   NOT NULL,
    "date" DATE   NOT NULL,
    "adjustedClose" FLOAT   NOT NULL,
    "volume" BIGINT   NOT NULL,
    "sentimentScore" FLOAT   NOT NULL,
    "sentiment" VARCHAR(50)   NOT NULL,
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

