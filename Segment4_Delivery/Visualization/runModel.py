import pickle
import numpy as np
import pandas as pd
import random
# import json
# from json import JSONEncoder

# class NumpyArrayEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)

def runPredictions():

     x_forecast_sentimentscore = np.array([0.5,-0.1,-0.9,0.8,0.0])
     x_forecast_likecount=np.array([234323,234234,332,34234,50949])
     x_forecast_retweetscore=np.array([434,434322,5334,333,2344])
     x_forecast_date=["2022-07-27","2022-07-28","2022-07-29","2022-07-30","2022-07-31"]
     x_forecast_percentage0 =[0.7350,-6.5400,-1.130,-0.3500,2.21]

     x_forecast =  pd.DataFrame(pd.concat([pd.DataFrame(x_forecast_sentimentscore,pd.to_datetime(x_forecast_date)),pd.DataFrame(x_forecast_likecount,pd.to_datetime(x_forecast_date)),pd.DataFrame(x_forecast_retweetscore,pd.to_datetime(x_forecast_date)),pd.DataFrame(x_forecast_percentage0,pd.to_datetime(x_forecast_date))],axis=1))
     x_forecast.columns=["sentimentScore","likesCount","retweetCount","percentPrice_0"]

     filename = 'finalized_model.sav'
     X_scaler = pickle.load(open('scaler_model.sav', 'rb'))
     X_value = X_scaler.transform(x_forecast)

     loaded_model = pickle.load(open(filename, 'rb'))
     forecast = loaded_model.predict(X_value)

     impactString= []
     strYes =[]
     for i in range(0, len(forecast)):
        if forecast[i] > 0:
            strYes.append('Yes')
            if x_forecast["sentimentScore"][i] > 0:
                impactString.append('Price likely to go up')
            else: 
                impactString.append('Price likely to go down')
        else:
            impactString.append(" ")
            strYes.append('No')

     results = pd.DataFrame({'Predict to have influence':strYes,'Positive/Negative change predicted':impactString})
     results["date"]=x_forecast.index
     results.set_index("date",inplace=True)
     x_forecast.rename(columns={'sentimentScore':'Sentiment Score','likesCount':'Likes Count','retweetCount':'Retweet Count','percentPrice_0':'Previous Day Price'},inplace=True)
     df = pd.concat([x_forecast,results],axis=1)
     indexValue = random.randint(0, len(x_forecast)-1) #find a runtime index

     f_senti=df.iloc[[indexValue]]["Sentiment Score"]
     f_like = df.iloc[[indexValue]]["Likes Count"]
     f_retweet = df.iloc[[indexValue]]["Retweet Count"]
     f_price = df.iloc[[indexValue]]["Previous Day Price"]
     f_msg = df.iloc[[indexValue]]["Positive/Negative change predicted"]

     htmlString=f"<p style='font-size:18px; font-family: Verdana;'> <b> Hola!</b> </br> There is a tweet trending which has Sentiment Score {f_senti.values[0]}. </br> <b>{f_msg.values[0]}</b></p>"
     return htmlString
    #  return df.iloc[[indexValue]].to_html()
        
    #  numpyData = {"Impact": forecast}
    #  encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)

    #  print(encodedNumpyData)
    #  return encodedNumpyData