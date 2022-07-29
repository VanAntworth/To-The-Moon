//Generate Doge Sentiment Chart
function buildDogeSentimentChart() {
    fetch('JSON_files/dogeTFS.json').then(response => {

        return response.json();
    }).then(data => {
        // Work with JSON data here
        const mark1 = 45
        const mark2 = 34
        const mark3 = 62
        const dateData = data.map(
            function (index) {
                return index.date;
            }
        )
        const adjustedClose = data.map(
            function (index) {
                return index.adjustedClose;
            }
        )
        const sentimentScore = data.map(
            function (index) {
                return index.sentimentScore;
            }
        )
        //  console.log(adjustedClose);
        //  console.log(sentimentScore);
        const ctx1 = document.getElementById('dogeChart').getContext('2d');
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3)

     
    }).catch(err => {
        console.log(err);
    });
}
//Generate Twitter Sentiment Chart
function buildTwitterSentimentChart() {
    fetch('JSON_files/twitterTFS.json').then(response => {

        return response.json();
    }).then(data => {
        // Work with JSON data here
        const mark1 = 35
        const mark2 = 56
        const mark3 = 100
        const dateData = data.map(
            function (index) {
                return index.date;
            }
        )
        const adjustedClose = data.map(
            function (index) {
                return index.adjustedClose;
            }
        )
        const sentimentScore = data.map(
            function (index) {
                return index.sentimentScore;
            }
        )
        //  console.log(adjustedClose);
        //  console.log(sentimentScore);
        const ctx1 = document.getElementById('twitterChart').getContext('2d');
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3)

    }).catch(err => {
        console.log(err);
    });
}
//Generate Tesla Sentiment Chart
function buildTeslaSentimentChart() {
    fetch('JSON_files/teslaTFS.json').then(response => {

        return response.json();
    }).then(data => {
        data = data.filter(index => new Date(index.date) > new Date('2021/01/01'))
        const mark1 = 50
        const mark2 = 125
        const mark3 = 100
        // Work with JSON data here
        const dateData = data.map(
            function (index) {
                return index.date;
            }
        )
        const adjustedClose = data.map(
            function (index) {
                return index.adjustedClose;
            }
        )
        const sentimentScore = data.map(
            function (index) {
                return index.sentimentScore;
            }
        )
        const tweetText = data.map(
            function (index) {
                return index.fullText;
            }
        )
        //  console.log(adjustedClose);
        //  console.log(sentimentScore);
        const ctx1 = document.getElementById('teslaChart').getContext('2d');
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, tweetText, mark1, mark2, mark3)

    }).catch(err => {
        console.log(err);
    });
}
// Common function for plotting chart
function buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, tweetText, mark1, mark2, mark3) {
   
    const dataset = {
        labels: dateData,
        datasets: [
        {
            label: 'Sentiment Score',
            data: sentimentScore,
            backgroundColor: [

                'rgba(54, 162, 235, 0.5)',

            ],
            borderColor: [

                'rgba(54, 162, 235, 1)',

            ],
            tension: 0.5,
            width:0.5,
            pointHoverBorderColor: 'white',
            pointHoverBorderColor: 'rgba(54, 162, 235, 1)',
            pointHoverBorderWidth: 3,
            pointHoverRadius: 10,
            
            type:'line',
            yAxisID: 'dollar'
        },{
            label: 'Adjusted Close',
            data: adjustedClose,
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1.5)',

            ],
            tension: 0.5,
            width:0.5,
            pointHoverBorderColor: 'white',
            pointHoverBorderColor: 'rgba(255,99,132,1)',
            pointHoverBorderWidth: 3,
            pointHoverRadius: 10
        }]
    }

    const chart = new Chart(ctx1, {
        type: 'bar',
        data: dataset,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Adjusted Value'
                    }
                },
                dollar: {
                    beginAtZero: true,
                    position: 'right',
                    title: {
                        display: true,
                        text: 'Sentiment score'
                    }
                }
            },
            plugins: {
                autocolors:false,
                annotation:{
                    annotations:[{
                        type: 'line', 
                        scaleID: 'x', 
                        value: mark2,
                        borderWidth: 2, 
                        borderColor: 'black'
                    },
                    {
                        type: 'line', 
                        scaleID: 'x', 
                        value: mark1,
                        borderWidth: 2, 
                        borderColor: 'black' 
                    },
                    {
                        type: 'line', 
                        scaleID: 'x', 
                        value: mark3,
                        borderWidth: 2, 
                        borderColor: 'black' 
                    },
                ]
                }
            }
        }

    });

}

function init() {
    buildDogeSentimentChart();
    buildTeslaSentimentChart();
    buildTwitterSentimentChart();
}

init();