USE [ElonMuskTwitterImpact]
GO
DROP PROCEDURE IF EXISTS sp_fetchFinanceDeltaPercents
/****** Object:  StoredProcedure [dbo].[sp_FinanceDeltaPercents]    Script Date: 7/19/2022 12:44:50 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Tamara Espinosa with Deepa Gheewala
-- Create date: 7/21/2022
-- Description:	This Stored Procedure will fetch data from FinanceDeltaPercents table 
--              for using it for modeling stock percents.
-- =============================================
CREATE PROCEDURE [dbo].[sp_fetchFinanceDeltaPercents]
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT [id]
		,[tweetID]
		,[financeType]
 	    ,[date]
		,[fullText]
		,[likesCount]
		,[retweetCount]
		,isnull([sentiment],'') as sentiment
		,[sentimentScore]
		,[startDate]
		,[datesDifference]
		,[weekendOrHoliday]
		,[deltaPrice_0]
		,[deltaPrice_1]
		,[deltaPrice_2]
		,[deltaPrice_3]
		,[deltaPrice_4]
		,[percentPrice_0]
		,[percentPrice_1]
		,[percentPrice_2]
		,[percentPrice_3]
		,[percentPrice_4]
		,[deltaVol_0]
		,[deltaVol_1]
		,[deltaVol_2]
    	,[deltaVol_3]
		,[deltaVol_4]
		,[percentVol_0]
		,[percentVol_1]
		,[percentVol_2]
		,[percentVol_3]
		,[percentVol_4]
							
	FROM [dbo].[FinanceDeltaPercents]

END
	
