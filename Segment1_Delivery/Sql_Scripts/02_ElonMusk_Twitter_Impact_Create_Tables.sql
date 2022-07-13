DROP TABLE IF EXISTS "SentimentScoring" ;
CREATE TABLE "SentimentScoring" (
    "id" SERIAL   NOT NULL,
    "twitterID" INT   NOT NULL,
    "date" DATE   NOT NULL,
    "closingPrice" FLOAT   NOT NULL,
    "volumn" BIGINT   NOT NULL,
    "sentimentScore" FLOAT   NOT NULL,
    "sentiment" SMALLINT   NOT NULL,
    CONSTRAINT "pkSentimentScoring" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "TwitterData" ;
CREATE TABLE "TwitterData" (
    "id" SERIAL  NOT NULL,
    "tweetID" BIGINT   NOT NULL,
    "financeType" VARCHAR   NOT NULL,
    "date" DATE   NOT NULL,
    "fullText" VARCHAR   NOT NULL,
    "replyCount" INTEGER ,
    "likesCount" INTEGER ,
    "retweetCount" INTEGER  ,
    CONSTRAINT "pkTwitterData" PRIMARY KEY (
        "id"
     )
);

DROP TABLE IF EXISTS "FinanceUsdData" ;
CREATE TABLE "FinanceUsdData" (
    "id" SERIAL   NOT NULL,
    "financeType" VARCHAR   NOT NULL,
    "date" DATE   NOT NULL,
    "openAt" FLOAT   NOT NULL,
    "high" FLOAT   ,
    "low" FLOAT   ,
    "close" FLOAT  ,
    "adjustedClose" FLOAT  ,
    "volumn" BIGINT   NOT NULL,
    CONSTRAINT "pkFinanceUsdData" PRIMARY KEY (
        "id"
     )
);


DROP TABLE IF EXISTS "PredictedValues" ;
CREATE TABLE "PredictedValues" (
    "id" SERIAL   NOT NULL,
    "model" VARCHAR   NOT NULL,
    "runFrom" VARCHAR   NOT NULL,
    "precision" FLOAT   NOT NULL,
    "recall" FLOAT   NOT NULL,
    "f1Score" FLOAT   NOT NULL,
    "accuracy" FLOAT   NOT NULL,
    "predicatedDogecoinValue" FLOAT   NOT NULL,
    "date" DATE   NOT NULL,
    "actualValue" FLOAT   NOT NULL,
    CONSTRAINT "pkPredictedValues" PRIMARY KEY (
        "id"
     )
);


ALTER TABLE "SentimentScoring" ADD CONSTRAINT "fk_SentimentScoringTwitterID" FOREIGN KEY("twitterID")
REFERENCES "twitterData" ("id");

