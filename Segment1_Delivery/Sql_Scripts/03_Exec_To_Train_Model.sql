DROP TABLE IF EXISTS credit_train_models

DECLARE @model VARBINARY(MAX);
EXEC PyTrainScikit @model OUTPUT;
select  'SciKit_model' as model_name, @model as Model INTO credit_train_models 

select * from credit_train_models