//Generate Doge Sentiment Chart
function buildDogeSentimentChart(){
    fetch('/JSON_files/dogeTFS.json').then(response => {

        return response.json();
      }).then(data => {
        // Work with JSON data here
        const dateData = data.map(
            function(index){
                return index.date;
                }
            )
        const adjustedClose = data.map(
            function(index){
                return index.adjustedClose;
                }
            )
        const sentimentScore = data.map(
            function(index){
                return index.sentimentScore;
                }
            )
          //  console.log(adjustedClose);
          //  console.log(sentimentScore);
            const ctx1 = document.getElementById('dogeChart').getContext('2d');
            buildSentimentFinanceChart(ctx1,dateData,adjustedClose,sentimentScore)

       const impactMarker = {
        id:'impactMarker',
        beforeDraw: chart => {
            const ctx = chart.ctx;
            console.log(chart);
        }
       }
      }).catch(err => {
        console.log(err);
      });
}
//Generate Twitter Sentiment Chart
function buildTwitterSentimentChart(){
    fetch('/JSON_files/twitterTFS.json').then(response => {

        return response.json();
      }).then(data => {
        // Work with JSON data here
        const dateData = data.map(
            function(index){
                return index.date;
                }
            )
        const adjustedClose = data.map(
            function(index){
                return index.adjustedClose;
                }
            )
        const sentimentScore = data.map(
            function(index){
                return index.sentimentScore;
                }
            )
          //  console.log(adjustedClose);
          //  console.log(sentimentScore);
            const ctx1 = document.getElementById('twitterChart').getContext('2d');
            buildSentimentFinanceChart(ctx1,dateData,adjustedClose,sentimentScore)

       const impactMarker = {
        id:'impactMarker',
        beforeDraw: chart => {
            const ctx = chart.ctx;
            console.log(chart);
        }
       }
      }).catch(err => {
        console.log(err);
      });
}
//Generate Tesla Sentiment Chart
function buildTeslaSentimentChart(){
    fetch('/JSON_files/teslaTFS.json').then(response => {

        return response.json();
      }).then(data => {
        // Work with JSON data here
        const dateData = data.map(
            function(index){
                return index.date;
                }
            )
        const adjustedClose = data.map(
            function(index){
                return index.adjustedClose;
                }
            )
        const sentimentScore = data.map(
            function(index){
                return index.sentimentScore;
                }
            )
          //  console.log(adjustedClose);
          //  console.log(sentimentScore);
            const ctx1 = document.getElementById('teslaChart').getContext('2d');
            buildSentimentFinanceChart(ctx1,dateData,adjustedClose,sentimentScore)

       const impactMarker = {
        id:'impactMarker',
        beforeDraw: chart => {
            const ctx = chart.ctx;
            console.log(chart);
        }
       }
      }).catch(err => {
        console.log(err);
      });
}
// Common function for plotting chart
function buildSentimentFinanceChart(ctx1,dateData,adjustedClose,sentimentScore){
    console.log("test")
    const dataset = {
        labels: dateData,
        datasets: [{
            label: 'Adjusted Close',
            data: adjustedClose,
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
            label: 'Sentiment Score',
            data: sentimentScore,
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
                        text: 'Sentiment score'
                    }
                }
            }
        }
       
    });
}

function init()
{
    console.log("new file");
    buildDogeSentimentChart();
    buildTeslaSentimentChart();
    buildTwitterSentimentChart();
}

init();