function buildTweet7Day(ctx1,date,financeDates,volume,adjustedClosed){
    console.log("test")
    console.log(date)
    var date_tweet =new Date(date+ "T00:00:01")

    // var date_0 = financeDates[0]
    console.log(date_tweet)

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
                x: {
                    display: true,
                    type: 'time',
                    title:{
                        display: true,
                        text: 'Date'
                    },
                    time: {
                      unit: 'day',
                      displayFormats: {
                        'day': 'MM/DD/YYYY'
                      }
                      }
                    }
                ,               
                y: {
                    beginAtZero: false,
                    title:{
                        display: true,
                        text: 'Adjusted Value'
                    }
                },
                dollar:{
                    beginAtZero: false,
                    position: 'right',
                    title:{
                        display: true,
                        text: 'Trading Stock Volume'
                    }
                }
            },
            plugins: {
                annotation:{
                    drawTime: 'afterDatasetsDraw',
                    annotations: [{
                      type: 'line',
                      mode: 'vertical',
                      scaleID: 'x',
                      value: date_tweet,
                      borderColor: 'magenta',
                      borderWidth: 2,
                    //   label: {
                    //     enabled: true,
                    //     position: "bottom",
                    //     content: "Tweet Date"
                    //   }
                    }]
                  }
            }

        }
       
    });
}

/*Update Functions*/

function update7Percentages(dateLogged,financeType, financeDates){
    
    fetch('JSON_files/financedeltapercent.json').then(response2 => {
        return response2.json();
        }).then(data2_oc => {
        
        data2_oc = data2_oc.filter(index => index.financeType == financeType)
        
        // console.log(data2)

        percentPrice0_oc = null
        percentPrice1_oc = null
        percentPrice2_oc = null
        percentPrice3_oc = null
        percentPrice4_oc = null
        percentPrice5_oc = null
        percentPrice6_oc = null
        percentPrice7_oc = null

        percentVol0_oc = null
        percentVol1_oc = null
        percentVol2_oc = null
        percentVol3_oc = null
        percentVol4_oc = null
        percentVol5_oc = null
        percentVol6_oc = null
        percentVol7_oc = null
        
        percentPrices = []
        percentVolumes = []

        for(var i=0; i < data2_oc.length; i++){ 
            if(data2_oc[i].date == dateLogged) {
                // console.log(data2[i])
                
                percentPrice0_oc = data2_oc[i].percentPrice_0
                percentPrice1_oc = data2_oc[i].percentPrice_1
                percentPrice2_oc = data2_oc[i].percentPrice_2
                percentPrice3_oc = data2_oc[i].percentPrice_3
                percentPrice4_oc = data2_oc[i].percentPrice_4
                percentPrice5_oc = data2_oc[i].percentPrice_5
                percentPrice6_oc = data2_oc[i].percentPrice_6
                percentPrice7_oc = data2_oc[i].percentPrice_7

                percentVol0_oc = data2_oc[i].percentVol_0
                percentVol1_oc = data2_oc[i].percentVol_1
                percentVol2_oc = data2_oc[i].percentVol_2
                percentVol3_oc = data2_oc[i].percentVol_3
                percentVol4_oc = data2_oc[i].percentVol_4
                percentVol5_oc = data2_oc[i].percentVol_5
                percentVol6_oc = data2_oc[i].percentVol_6
                percentVol7_oc = data2_oc[i].percentVol_7

                percentPrices = [percentPrice0_oc, percentPrice1_oc,percentPrice2_oc, percentPrice3_oc, percentPrice4_oc, percentPrice5_oc, percentPrice6_oc, percentPrice7_oc]
                percentVolumes = [percentVol0_oc, percentVol1_oc, percentVol2_oc, percentVol3_oc, percentVol4_oc, percentVol5_oc, percentVol6_oc, percentVol7_oc]
            } 
        }      

        if (percentPrice0_oc === null) {

            console.log('No percentage records for date')
            var tbody = d3.select("tbody");
            var thead = d3.select("thead"); 
            thead.html("");
            tbody.html("");

            let head0 = thead.append("tr");
            head_row = head0.append("th").text("No record to display")



        } else if (percentPrice0_oc !== null) {

            console.log(percentPrice0_oc)
            console.log(percentVol0_oc)

            var thead = d3.select("thead");
            thead.html("");
            var tbody = d3.select("tbody");
            tbody.html("");

            let row0 = tbody.append("tr");

            Object.values(financeDates).forEach((val) => {
                let cell = row0.append("td");
                cell.text(val);
                });

            function insertPercentsTable() {
                let row1 = tbody.append("tr");
                let cell1_1 = row1.append("th").text('Price Change %')
                let row2 = tbody.append("tr");
                let cell2_1 = row2.append("th").text('Volume Change %')

                var i = 0;
                while(i < (financeDates.length - 1)) {
                    let cell1 = row1.append("td");
                    cell1.text(percentPrices[i].toFixed(3))
                    let cell2 = row2.append("td");
                    cell2.text(percentVolumes[i].toFixed(3))
                    i++
                }
            }

            if (financeDates.length==8){
                row_head = thead.append('tr')
                head1 = row_head.append("th").text("Start Date")
                head2 = row_head.append("th").text("Day 1")
                head3 = row_head.append("th").text("Day 2")
                head4 = row_head.append("th").text("Day 3")
                head5 = row_head.append("th").text("Day 4")
                head6 = row_head.append("th").text("Day 5")
                head7 = row_head.append("th").text("Day 6")
                head8 = row_head.append("th").text("Day 7")

                insertPercentsTable()
                
            } else if (financeDates.length==7){
                row_head = thead.append('tr')
                head1 = row_head.append("th").text("Start Date")
                head2 = row_head.append("th").text("Day 1")
                head3 = row_head.append("th").text("Day 2")
                head4 = row_head.append("th").text("Day 3")
                head5 = row_head.append("th").text("Day 4")
                head6 = row_head.append("th").text("Day 5")
                head7 = row_head.append("th").text("Day 6")

                insertPercentsTable()

            } else if (financeDates.length==6){
                row_head = thead.append('tr')
                head1 = row_head.append("th").text("Start Date")
                head2 = row_head.append("th").text("Day 1")
                head3 = row_head.append("th").text("Day 2")
                head4 = row_head.append("th").text("Day 3")
                head5 = row_head.append("th").text("Day 4")
                head6 = row_head.append("th").text("Day 5")

                insertPercentsTable()

            } else if (financeDates.length==5){
                row_head = thead.append('tr')
                head1 = row_head.append("th").text("Start Date")
                head2 = row_head.append("th").text("Day 1")
                head3 = row_head.append("th").text("Day 2")
                head4 = row_head.append("th").text("Day 3")
                head5 = row_head.append("th").text("Day 4")

                insertPercentsTable()
           
            } else if (financeDates.length==3){
                row_head = thead.append('tr')
                head1 = row_head.append("th").text("Start Date")
                head2 = row_head.append("th").text("Day 1")
                head3 = row_head.append("th").text("Day 2")
                head4 = row_head.append("th").text("Day 3")

                insertPercentsTable()
                
            } else {
                let head0 = thead.append("tr");
                head_row = head0.append("th").text("Record Message")
    
                let row2 = tbody.append("tr");
                
                let cell1_1 = row2.append("tr").text('Not sufficient stock data to display calculations.')
            }                

        } else {

            console.log('Error reading percentages')
        }

        
    })
}

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

                financeDates = []

                for (let i = 0; i < financeDates_oc.length; i++) {
                    value = financeDates_oc[i]
                    // console.log(value)
                    var parts = value.toString().split('-');
                    // Please pay attention to the month (parts[1]); JavaScript counts months from 0:
                     // January - 0, February - 1, etc.
                    // console.log(parts)
                    var mydate = new Date(parts[0], parts[1] - 1, parts[2],0,0,1)
                    // console.log(mydate)
                    financeDates.push(mydate);
                    
                  }
            }
        });
            
        if (financeDates_oc.length == 0){
            let chartStatus1 = Chart.getChart("myChart");
            chartStatus1.clear()
            console.log('No Fincancial Records for date')

            errorMessage = document.getElementById('errorMessage').innerHTML="<span style='font-size:30px'>Elon did not tweet about this Stock / Coin on this date.</span>";

        } else if (financeDates_oc.length > 0) {
            // console.log(financeDates_oc)
            console.log(financeDates)
            console.log(volumes_oc)
            console.log(adjustedClosed_oc)
            
            
            clearErrorMessage = document.getElementById('errorMessage').innerHTML=""
            
            // JS - Destroy exiting Chart Instance to reuse <canvas> element


            let chartStatus = Chart.getChart("myChart"); // <canvas> id
            if (chartStatus != undefined) {
            chartStatus.destroy();
            }
            //-- End of chart destroy   

            ctx = document.getElementById('myChart').getContext('2d');

            buildTweet7Day(ctx,dateLogged,financeDates,volumes_oc,adjustedClosed_oc)
            
        } else {
            console.log('Error reading financial records')
        } 
        
        update7Percentages(dateLogged,financeType, financeDates_oc)
        
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
    date_init = '2022-05-30'
    const label = document.getElementById("financeType");
    financeType_init = label.value

    console.log(financeType_init)

    /* Data Fetching */

    update7DayChart(date_init, financeType_init)
    update7Tweets(date_init, financeType_init)
    // update7Percentages(date_init, financeType_init)
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
    // update7Percentages(dateLogged,financeType)

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
    // update7Percentages(dateLogged1,financeType1)

}
