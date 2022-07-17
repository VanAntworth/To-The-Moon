DROP PROCEDURE IF EXISTS sp_fetchTweetSentimentForModelling
-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
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
CREATE PROCEDURE sp_fetchTweetSentimentForModelling
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	If (@financeType = '') 
		BEGIN
			SELECT t.[tweetID]
				,t.[financeType]
				,t.[date]
				,t.[fullText]
				,t.[replyCount]
				,t.[likesCount]
				,t.[retweetCount]
				,s.[sentimentScore]
				,s.[sentiment]
				,f.[adjustedClose]
				,f.[volume]
			FROM "TwitterData" t
			INNER JOIN "SentimentScoring" s 
			ON t."tweetID" = s."tweetID"
			INNER JOIN "FinanceUsdData" f
			ON f."date" = t."date"
		END
	ELSE
		BEGIN
			SELECT t.[tweetID]
					,t.[financeType]
					,t.[date]
					,t.[fullText]
					,t.[replyCount]
					,t.[likesCount]
					,t.[retweetCount],
					s.[sentimentScore], 
					s.[sentiment],
					f.[adjustedClose],
					f.[volume]
				FROM "TwitterData" t
				INNER JOIN "SentimentScoring" s 
				ON t."tweetID" = s."tweetID"
				INNER JOIN "FinanceUsdData" f
				ON f."date" = t."date"
			WHERE t.financeType = @financeType
		END

END
GO
