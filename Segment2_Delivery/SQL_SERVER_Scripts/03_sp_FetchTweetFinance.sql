USE [ElonMuskTwitterImpact]
GO
DROP PROCEDURE IF EXISTS sp_fetchTweetSentiment
DROP PROCEDURE IF EXISTS sp_fetchTweetFinance
/****** Object:  StoredProcedure [dbo].[sp_fetchTweetFinance]    Script Date: 7/20/2022 12:26:27 AM ******/
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
CREATE PROCEDURE [dbo].[sp_fetchTweetFinance]
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	IF (@financeType = '') 
	BEGIN
		SELECT DISTINCT t.[tweetID]
			  ,t.[financeType]
			  ,t.[date]
			  ,t.[fullText]
			  ,Max(t.[replyCount]) as replyCount
			  ,Max(t.[likesCount]) as likesCount
			  ,Max(t.[retweetCount]) as retweetCount,
			  f.[adjustedClose], 
			  f.[volume] FROM TwitterData t  INNER JOIN FinanceUsdData f 
			  ON f.[date] = t.[date]
			  AND t.[financeType] = f.[financeType]
			  GROUP BY t.[tweetID],t.[financeType],t.[date],t.[fullText], f.[adjustedClose], f.[volume] 
	END
	ELSE
	BEGIN
		SELECT DISTINCT t.[tweetID]
			  ,t.[financeType]
			  ,t.[date]
			  ,t.[fullText]
			  ,Max(t.[replyCount]) as replyCount
			  ,Max(t.[likesCount]) as likesCount
			  ,Max(t.[retweetCount]) as retweetCount,
			  f.[adjustedClose], 
			  f.[volume] FROM TwitterData t  INNER JOIN FinanceUsdData f 
		ON f.[date] = t.[date]
		AND t.[financeType] = f.[financeType]
		WHERE t.financeType = @financeType
		GROUP BY t.[tweetID],t.[financeType],t.[date],t.[fullText], f.[adjustedClose], f.[volume] 
	END

END
