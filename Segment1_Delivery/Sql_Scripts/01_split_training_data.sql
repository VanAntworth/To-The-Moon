DROP PROCEDURE IF EXISTS PyTrainTestSplit;
GO

CREATE PROCEDURE [dbo].[PyTrainTestSplit] (@pct int)
AS

	DROP TABLE IF EXISTS Temp_Credit_risk_data_Training
SELECT * into Temp_Credit_risk_data_Training FROM Credit_risk_data WHERE (ABS(CAST(BINARY_CHECKSUM(loan_amnt,int_rate)  as int)) % 100) < @pct

DROP TABLE IF EXISTS Temp_Credit_risk_data_testing
SELECT * into Temp_Credit_risk_data_testing FROM Credit_risk_data
WHERE (ABS(CAST(BINARY_CHECKSUM(loan_amnt,int_rate)  as int)) % 100) > @pct
GO

EXEC PyTrainTestSplit 70
GO