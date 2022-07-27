function buildTweet7Day(ctx1,financeDates,volume,adjustedClosed){
    console.log("test")
    const dataset = {
        labels: financeDates,
        datasets: [{
            label: 'Adjusted Close',
            data: adjustedClosed,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
               
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                
            ],
            tension: 0.5,
            pointHoverBorderColor:'white',
            pointHoverBorderColor:'rgba(255,99,132,1)',
            pointHoverBorderWidth:3,
            pointHoverRadius:10
        },
        {
            label: 'Trading Stock Volume',
            data: volume,
            backgroundColor: [

                'rgba(54, 162, 235, 0.2)',
              
            ],
            borderColor: [

                'rgba(54, 162, 235, 1)',
          
            ],
            tension: 0.5,
            pointHoverBorderColor:'white',
            pointHoverBorderColor:'rgba(54, 162, 235, 1)',
            pointHoverBorderWidth:3,
            pointHoverRadius:10,
            yAxisID: 'dollar'
        }]
    }
    const chart = new Chart(ctx1, {
        type: 'line',
        data: dataset,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title:{
                        display: true,
                        text: 'Adjusted Value'
                    }
                },
                dollar:{
                    beginAtZero: true,
                    position: 'right',
                    title:{
                        display: true,
                        text: 'Trading Stock Volume'
                    }
                }
            }
        }
       
    });
}

/*Update Functions*/

function update7DayChart(dateLogged,financeType){

    fetch('JSON_files/financeData7Days.json').then(response1 => {
        return response1.json();
        }).then(data1_oc => {
    
        data1_oc = data1_oc[financeType]
        
        // console.log(data1)

        financeDates_oc = []
        volumes_oc = []
        adjustedClosed_oc = []

        Object.entries(data1_oc).forEach(([key, value]) => {
            if(value.tweetDate == dateLogged){
                // console.log(key, value);
                financeDates_oc = value.financeDates
                volumes_oc = value.volumes
                adjustedClosed_oc = value.adjustedClosed

            }
        });
            
        if (financeDates_oc.length == 0){
            let chartStatus1 = Chart.getChart("myChart");
            chartStatus1.clear()
            console.log('No Fincancial Records for date')

        } else if (financeDates_oc.length > 0) {
            console.log(financeDates_oc)
            console.log(volumes_oc)
            console.log(adjustedClosed_oc)
    
            // JS - Destroy exiting Chart Instance to reuse <canvas> element
            let chartStatus = Chart.getChart("myChart"); // <canvas> id
            if (chartStatus != undefined) {
            chartStatus.destroy();
            }
            //-- End of chart destroy   

            ctx = document.getElementById('myChart').getContext('2d');

            buildTweet7Day(ctx,financeDates_oc,volumes_oc,adjustedClosed_oc)
            
        } else {
            console.log('Error reading financial records')
        } 
        
    })

}

function update7Tweets(dateLogged,financeType){

    const display = document.getElementById("displayDateSelected");
    const ele1 = document.getElementById("tweeter-timeline");
    const ele = document.getElementById("selected-tweet");
    const tweeEle = document.getElementById("tweet");

    fetch('JSON_files/tweetsperDate.json').then(response3 => {
        return response3.json();
        }).then(data3_oc => {
    
        data3_oc = data3_oc[financeType]

        filteredDate3_oc = data3_oc.filter(index => index.date==dateLogged)
        
        if (filteredDate3_oc.length == 0){

            console.log('No tweetID records for date')

            ele.style.display = "none";

            ele1.style.display = "block";   

        } else if (filteredDate3_oc.length > 0) {

            tweetIDsperDate_oc = filteredDate3_oc[0].tweetIDs
            console.log(tweetIDsperDate_oc)

            ele.style.display = "block";
            ele1.style.display = "none";
            document.getElementById("tweet").innerHTML = " "

            var_tweet = " "
            for (let i = 0; i < tweetIDsperDate_oc.length; i++) {
                var_tweet = tweetIDsperDate_oc[i]
                console.log(var_tweet)
                tweetInfo(var_tweet)
              }
    
        } else {console.log('Error reading tweet IDs')}

    }) 

    // tweetInfo();
    // console.log(ele.style.display);
    // console.log(ele1.style.display);

}

function update7Percentages(dateLogged,financeType){
    
    fetch('JSON_files/financedeltapercent.json').then(response2 => {
        return response2.json();
        }).then(data2_oc => {
        
        data2_oc = data2_oc.filter(index => index.financeType == financeType)
        
        // console.log(data2)

        for(var i=0; i < data2_oc.length; i++){ 
            if(data2_oc[i].date == dateLogged) {
                // console.log(data2[i])
                
                percentPrice0_oc = data2_oc[i].percentPrice_0
                percentPrice1_oc = data2_oc[i].percentPrice_1
                percentPrice2_oc = data2_oc[i].percentPrice_2
                percentPrice3_oc = data2_oc[i].percentPrice_3
                percentPrice4_oc = data2_oc[i].percentPrice_4

                percentVol0_oc = data2_oc[i].percentVol_0
                percentVol1_oc = data2_oc[i].percentVol_1
                percentVol2_oc = data2_oc[i].percentVol_2
                percentVol3_oc = data2_oc[i].percentVol_3
                percentVol4_oc = data2_oc[i].percentVol_4
                
            } 
        }      

        if (percentPrice0_oc === undefined) {

            console.log('No percentage records for date')

        } else if (percentPrice0 !== undefined) {

            console.log(percentPrice0_oc)
            console.log(percentVol0_oc)

        } else {

            console.log('Error reading percentages')
        }

        
    })
}

/* Initiate Finctions*/

function buildDateControl(){

var date = new Date();
var date_init = new Date('2022-05-31');
console.log("test")
    $('#datepicker').datepicker({
        format: 'yyyy-mm-dd', 
        autoclose: true, 
        todayHighlight: true,
        forceParse: false,
        setDate: date_init,
        value:date_init,
        startDate:"2010-01-01",
        endDate: new Date()
    });
    $('#datepicker').datepicker('setDate', date_init);
}


function catchDefaultDateData(){
    date_init = '2022-05-31'
    const label = document.getElementById("financeType");
    financeType_init = label.value

    console.log(financeType_init)

    /* Data Fetching */

    update7DayChart(date_init, financeType_init)
    update7Tweets(date_init, financeType_init)
    update7Percentages(date_init, financeType_init)
}

function init()
{
    buildDateControl();
    catchDefaultDateData();

}


init();


/*Events*/

function optionChanged(value){

    dateLogged = value
    console.log(dateLogged)

    const label = document.getElementById("financeType");
    financeType = label.value

    console.log(financeType)

    /* Data Fetching */

    update7DayChart(dateLogged, financeType)
    update7Tweets(dateLogged,financeType)
    update7Percentages(dateLogged,financeType)

}


function selectorChanged(value1){
    financeType1 = value1
    console.log(financeType1)

    const label = document.getElementById("dateSelected");
    dateLogged1 = label.value
    console.log(dateLogged1)

    /* Data Fetching */

    update7DayChart(dateLogged1, financeType1)
    update7Tweets(dateLogged1,financeType1)
    update7Percentages(dateLogged1,financeType1)

}
