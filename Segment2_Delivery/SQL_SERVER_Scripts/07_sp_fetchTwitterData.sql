USE [ElonMuskTwitterImpact]
GO
DROP PROCEDURE IF EXISTS sp_fetchTwitterData
/****** Object:  StoredProcedure [dbo].[sp_fetchTwitterData]    Script Date: 7/20/2022 12:29:57 AM ******/
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
CREATE PROCEDURE [dbo].[sp_fetchTwitterData]
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT [tweetID]
      ,[financeType]
      ,[date]
      ,[fullText]
  FROM [dbo].[TwitterData]

END
