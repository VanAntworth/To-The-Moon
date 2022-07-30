USE [ElonMuskTwitterImpact]
GO
DROP PROCEDURE IF EXISTS sp_fetchFinanceTweetForecast
/****** Object:  StoredProcedure [dbo].[sp_FinanceTweetForecast]    Script Date: 7/19/2022 12:44:50 PM ******/
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
CREATE PROCEDURE [dbo].[sp_fetchFinanceTweetForecast]
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT 
       [tweetID]
      ,[tweetDate]
      ,[financeType]
      ,[financeID]
      ,[financeDate]
      ,[datePosition]
      ,[adjustedClose]
      ,[volume]
							
	FROM [dbo].[FinanceTweetForecast]

END
	
