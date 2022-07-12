DROP PROCEDURE IF EXISTS PredictTipSciKitPy;
GO

CREATE PROCEDURE [dbo].[PredictTipSciKitPy] (@model varchar(50), @inquery nvarchar(max))
AS
BEGIN
DECLARE @lmodel2 varbinary(max) = (select Model from credit_train_models where model_name = @model);
EXEC sp_execute_external_script
  @language = N'Python',
  @script = N'
import pickle;
import numpy;
from sklearn import metrics

mod = pickle.loads(lmodel2)
X = InputDataSet[["loan_amnt", "int_rate", "installment", "annual_inc", "dti", "delinq_2yrs", "inq_last_6mths", "open_acc", "pub_rec", "revol_bal", "total_acc"]]
y = numpy.ravel(InputDataSet[["loan_status_int"]])

probArray = mod.predict_proba(X) 
print(probArray)
probList = []
for i in range(len(probArray)):
  probList.append((probArray[i])[1])

y_Pred = numpy.asarray(probList)
print(y_Pred)
fpr, tpr, thresholds = metrics.roc_curve(y, y_Pred, pos_label=1)
aucResult = metrics.auc(fpr, tpr)
variance = metrics.explained_variance_score(y, y_Pred)
avg_pre = metrics.average_precision_score(y, y_Pred, pos_label=1)

print("False Positive" + str(fpr))
print("True positive" + str(tpr))
print("threshold" + str(thresholds))
print ("AUC on testing data is: " + str(aucResult))
print ("Explained Variance score :" + str(variance))
print ("avg precision score :" + str(avg_pre))

OutputDataSet = pandas.DataFrame(data = probList, columns = ["predictions"])
',	
  @input_data_1 = @inquery,
  @input_data_1_name = N'InputDataSet',
  @params = N'@lmodel2 varbinary(max)',
  @lmodel2 = @lmodel2
WITH RESULT SETS ((Score float));
END
GO