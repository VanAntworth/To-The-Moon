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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_FetchTweetSentiment
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	if (@financeType = '') 
	Begin
		SELECT t.[tweetID]
			  ,t.[financeType]
			  ,t.[date]
			  ,t.[fullText]
			  ,t.[replyCount]
			  ,t.[likesCount]
			  ,t.[retweetCount],
			  f.[adjustedClose], 
			  f.[volume] FROM TwitterData t  INNER JOIN FinanceUsdData f ON f.[date] = t.[date]
	End
	else
	Begin
		SELECT t.[tweetID]
			  ,t.[financeType]
			  ,t.[date]
			  ,t.[fullText]
			  ,t.[replyCount]
			  ,t.[likesCount]
			  ,t.[retweetCount],
			  f.[adjustedClose], 
			  f.[volume] FROM TwitterData t  INNER JOIN FinanceUsdData f ON f.[date] = t.[date]
		where t.financeType = @financeType
	End

END
GO
