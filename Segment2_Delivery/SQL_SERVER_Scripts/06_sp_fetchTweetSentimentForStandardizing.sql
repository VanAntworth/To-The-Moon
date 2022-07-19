USE [ElonMuskTwitterImpact]
GO
DROP PROCEDURE IF EXISTS sp_fetchTweetSentimentForStandardizing
/****** Object:  StoredProcedure [dbo].[sp_fetchTweetSentimentForModelling]    Script Date: 7/19/2022 12:44:50 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Deepa Gheewala
-- Create date: 7/17/2022
-- Description:	This Stored Procedure will fetch data from Tweeter and Finance tables 
--              for using it to run sentiment score on it.
-- =============================================
CREATE PROCEDURE [dbo].[sp_fetchTweetSentimentForStandardizing]
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	IF @financeType=''
	BEGIN 
			SELECT DISTINCT t.[tweetID]
				,t.[financeType]
				,t.[date]
				,t.[fullText]
				,t.[replyCount]
				,t.[likesCount]
				,t.[retweetCount]
				,s.[sentimentScore]
				,s.[sentiment]
				
			FROM "TwitterData" t
			INNER JOIN "SentimentScoring" s 
			ON t."tweetID" = s."tweetID"

	END
	ELSE
	BEGIN
		SELECT DISTINCT t.[tweetID]
				,t.[financeType]
				,t.[date]
				,t.[fullText]
				,t.[replyCount]
				,t.[likesCount]
				,t.[retweetCount]
				,s.[sentimentScore]
				,s.[sentiment]
				
			FROM "TwitterData" t
			INNER JOIN "SentimentScoring" s 
			ON t."tweetID" = s."tweetID"
			AND t.[financeType] = @financeType
	END

END
