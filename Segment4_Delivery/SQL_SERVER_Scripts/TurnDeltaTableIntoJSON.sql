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
		,isnull([deltaPrice_0],'') as deltaPrice_0
		,isnull([deltaPrice_1],'') as deltaPrice_1
		,isnull([deltaPrice_2],'') as deltaPrice_2
		,isnull([deltaPrice_3],'') as deltaPrice_3
		,isnull([deltaPrice_4],'') as deltaPrice_4
		,isnull([deltaPrice_5],'') as deltaPrice_5
		,isnull([deltaPrice_6],'') as deltaPrice_6
		,isnull([deltaPrice_7],'') as deltaPrice_7
		,isnull([percentPrice_0],'') as percentPrice_0
		,isnull([percentPrice_1],'') as percentPrice_1
		,isnull([percentPrice_2],'') as percentPrice_2
		,isnull([percentPrice_3],'') as percentPrice_3
		,isnull([percentPrice_4],'') as percentPrice_4
		,isnull([percentPrice_5],'') as percentPrice_5
		,isnull([percentPrice_6],'') as percentPrice_6
		,isnull([percentPrice_7],'') as percentPrice_7
		,isnull([deltaVol_0],'') as deltaVol_0
		,isnull([deltaVol_1],'') as deltaVol_1
		,isnull([deltaVol_2],'') as deltaVol_2
    	,isnull([deltaVol_3],'') as deltaVol_3
		,isnull([deltaVol_4],'') as deltaVol_4
		,isnull([deltaVol_5],'') as deltaVol_5
    	,isnull([deltaVol_6],'') as deltaVol_6
		,isnull([deltaVol_7],'') as deltaVol_7
		,isnull([percentVol_0],'') as percentVol_0
		,isnull([percentVol_1],'') as percentVol_1
		,isnull([percentVol_2],'') as percentVol_2
		,isnull([percentVol_3],'') as percentVol_3
		,isnull([percentVol_4],'') as percentVol_4
		,isnull([percentVol_5],'') as percentVol_5
		,isnull([percentVol_6],'') as percentVol_6
		,isnull([percentVol_7],'') as percentVol_7				 	
	FROM [dbo].[FinanceDeltaPercents] FOR JSON PATH