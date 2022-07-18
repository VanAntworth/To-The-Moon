DROP PROCEDURE IF EXISTS sp_fetchFinanceData
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
-- Description:	This Stored Procedure will fetch data from Finance table
--              for using it to run sentiment score on it.
-- =============================================
CREATE PROCEDURE sp_fetchFinanceData
	-- Add the parameters for the stored procedure here
	@financeType varchar(10) =''
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	IF (@financeType = '') 
		BEGIN
			SELECT [financeType]
				  ,[date]
				  ,[open]
				  ,[high]
				  ,[low]
				  ,[close]
				  ,[adjustedClose]
				  ,[volume]
			  FROM [FinanceUsdData]
		END
	ELSE
		BEGIN
			SELECT [financeType]
				  ,[date]
				  ,[open]
				  ,[high]
				  ,[low]
				  ,[close]
				  ,[adjustedClose]
				  ,[volume]
			  FROM [FinanceUsdData]
			  WHERE [financeType]=@financeType
		END
END
GO
