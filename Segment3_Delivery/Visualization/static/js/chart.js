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

function buildDateControl(){

var date = new Date();
var today = new Date(date.getFullYear(), date.getMonth(), date.getDate());
console.log("test")
    $('#datepicker').datepicker({
        format: 'yyyy-mm-dd', 
        autoclose: true, 
        todayHighlight: true,
        forceParse: false,
        setDate: today
    });
}


function init()
{
    buildDateControl();
    // buildTweet7Day();

}


init();

/*Events*/

function optionChanged(value){
    // const display = document.getElementById("displayDateSelected");
    // const ele1 = document.getElementById("tweeter-timeline");
    // const ele = document.getElementById("selected-tweet");
    // const tweeEle = document.getElementById("tweet");
    // if (ele.style.display == "block") {
    //     tweeEle.setAttribute("tweetID","1538406040374595584");

    //     ele.style.display = "none";

    //     ele1.style.display = "block";
    //     display.innerHTML = "show";
    // }
    // else {
    //     tweeEle.setAttribute("tweetID", "1544743525585141760");
    //     ele.style.display = "block";
    //     ele1.style.display = "none";
    //     display.innerHTML = "hide";
    // }
    // tweetInfo();
    // console.log(ele.style.display);
    // console.log(ele1.style.display);
    dateLogged = value
    console.log(dateLogged)

    const label = document.getElementById("financeType");
    financeType = label.value

    console.log(financeType)

    /* Data Fetching */

    try {

        fetch('/JSON_files/financeData7Days.json').then(response1 => {
            return response1.json();
            }).then(data1_oc => {
        
            data1_oc = data1_oc[financeType]
            
            // console.log(data1)

            Object.entries(data1_oc).forEach(([key, value]) => {
                if(value.tweetDate == dateLogged){
                    // console.log(key, value);
                    financeDates_oc = value.financeDates
                    volumes_oc = value.volumes
                    adjustedClosed_oc = value.adjustedClosed
                }
            });
            
            console.log(financeDates_oc)
            console.log(volumes_oc)
            console.log(adjustedClosed_oc)

            ctx = document.getElementById('myChart').getContext('2d');

            buildTweet7Day(ctx,financeDates_oc,volumes_oc,adjustedClosed_oc)
        });

        fetch('/JSON_files/financedeltapercent.json').then(response2 => {
            return response2.json();
            }).then(data2_oc => {
            
            data2_oc = data2_oc.filter(index => index.financeType == financeType )
            
            // console.log(data2)

            for(var i=0; i < data2_oc.length; i++){ 
                if(data2_oc[i].date== dateLogged) {
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

            console.log(percentPrice0_oc)
            console.log(percentVol0_oc)
            
        })

        fetch('/JSON_files/tweetsperDate.json').then(response3 => {
            return response3.json();
            }).then(data3_oc => {
        
            data3_oc = data3_oc[financeType]

            filteredDate3_oc = data3_oc.filter(index => index.date==dateLogged)
            
            tweetIDsperDate_oc = filteredDate3_oc[0].tweetIDs

            console.log(tweetIDsperDate_oc)
    }) }

    catch(err) {console.log('No record exhists')}

}


function selectorChanged(value1){
    financeType1 = value1
    console.log(financeType1)

    const label = document.getElementById("dateSelected");
    dateLogged1 = label.value
    console.log(dateLogged1)

    /* Data Fetching */

    try {

        fetch('/JSON_files/financeData7Days.json').then(response1 => {
            return response1.json();
            }).then(data1 => {
        
            data1 = data1[financeType1]
            
            // console.log(data1)

            Object.entries(data1).forEach(([key, value]) => {
                if(value.tweetDate == dateLogged1){
                    // console.log(key, value);
                    financeDates = value.financeDates
                    volumes = value.volumes
                    adjustedClosed = value.adjustedClosed
                }
            });
            
            console.log(financeDates)
            console.log(volumes)
            console.log(adjustedClosed)

            ctx = document.getElementById('myChart').getContext('2d');

            buildTweet7Day(ctx,financeDates,volumes,adjustedClosed)
        });

        fetch('/JSON_files/financedeltapercent.json').then(response2 => {
            return response2.json();
            }).then(data2 => {
            
            data2 = data2.filter(index => index.financeType == financeType1 )
            
            // console.log(data2)

            for(var i=0; i < data2.length; i++){ 
                if(data2[i].date== dateLogged1) {
                    // console.log(data2[i])
                    
                    percentPrice0 = data2[i].percentPrice_0
                    percentPrice1 = data2[i].percentPrice_1
                    percentPrice2 = data2[i].percentPrice_2
                    percentPrice3 = data2[i].percentPrice_3
                    percentPrice4 = data2[i].percentPrice_4

                    percentVol0 = data2[i].percentVol_0
                    percentVol1 = data2[i].percentVol_1
                    percentVol2 = data2[i].percentVol_2
                    percentVol3 = data2[i].percentVol_3
                    percentVol4 = data2[i].percentVol_4
                }
            }      

            console.log(percentPrice0)
            console.log(percentVol0)
            
        })

        fetch('/JSON_files/tweetsperDate.json').then(response3 => {
            return response3.json();
            }).then(data3 => {
        
            data3 = data3[financeType1]

            filteredDate3 = data3.filter(index => index.date==dateLogged1 )
            
            tweetIDsperDate = filteredDate3[0].tweetIDs

            console.log(tweetIDsperDate)
    }) }

    catch(err) {console.log('No record exhists')}

}
