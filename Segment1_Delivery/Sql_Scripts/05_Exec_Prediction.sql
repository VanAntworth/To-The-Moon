DECLARE @query_string nvarchar(max) -- Specify input query
  SET @query_string='
  select loan_amnt, int_rate,  installment, annual_inc, dti, delinq_2yrs, inq_last_6mths, open_acc, pub_rec, revol_bal, total_acc, loan_status_int
from Temp_Credit_risk_data_testing'
EXEC [dbo].[PredictTipSciKitPy] 'SciKit_model', @query_string;