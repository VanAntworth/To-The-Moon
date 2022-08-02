//Generate Doge Sentiment Chart
function buildDogeSentimentChart() {
    fetch('JSON_files/dogeTFS.json').then(response => {

        return response.json();
    }).then(data => {
        // Work with JSON data here
        const mark1 = 8
        const mark2 = 32
        const mark3 = 62
        const tweetText1 = "SpaceX launching satellite"
        const tweetText2 = "Doge-1 to the moon next year.."
        const tweetText3 = "I don’t use Binance (tried at one point,"


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
        const annotation1 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: "Dogecoin is the people’s crypto",
            font: {
                size: 13
            },
            position: {
                x: 8,
                y: 'bottom'
            },
            xAdjust: +120,
            xValue: 8,
            yAdjust: +10,
            yValue: 0.2
        }
        const annotation2 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: [tweetText1, tweetText2],
            font: {
                size: 13
            },
            position: {
                x: 32,
                y: 'bottom'
            },
            xAdjust: -140,
            xValue: 32,
            yAdjust: -40,
            yValue: 0.4
        };
       
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3, annotation1, annotation2)


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
        const mark2 = 60
        const mark3 = 88
        const tweetText1 = "Taking Twitter private at $54.20 should"
        const tweetText2 = "be up to shareholders, not the board"
        const tweetText3 = "If Twitter can tell the difference between real and "
        const tweetText4 = "fake users, why does it allow these in our comments?"
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
        const annotation1 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: [tweetText1, tweetText2],
            font: {
                size: 13
            },
            position: {
                x: 35,
                y: 'top'
            },
            xAdjust: -10,
            xValue: 35,
            yAdjust: -40,
            yValue: 20
        };
        const annotation2 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: [tweetText3, tweetText4],
            font: {
                size: 13
            },
            position: {
                x: 88,
                y: 'top'
            },
            xAdjust: -50,
            xValue: 88,
            yAdjust: -40,
            yValue: 20
        }
        const annotation = [annotation1, annotation2]
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3, annotation1, annotation2)

    }).catch(err => {
        console.log(err);
    });
}
//Generate Tesla Sentiment Chart
function buildTeslaSentimentChart() {
    fetch('JSON_files/teslaTFS.json').then(response => {

        return response.json();
    }).then(data => {
        data = data.filter(index => (new Date(index.date) > new Date('2018/07/01')) & (new Date(index.date) < new Date('2020/06/01')))
        const mark1 = 25
        const mark2 = 430
        const mark3 = -1
        const tweetText1 = "Am considering taking Tesla"
        const tweetText2 = "private at $420. Funding secured."
        const tweetText3 = "As always, I am optimistic about Tesla long-term"
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

        //  console.log(adjustedClose);
        //  console.log(sentimentScore);
        const ctx1 = document.getElementById('teslaChart').getContext('2d');
        const annotation1 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: [tweetText1,tweetText2],
            font: {
                size: 13
            },
            position: {
                x: 116,
                y: 'center'
            },
            xAdjust: +140,
            xValue: 25,
            yAdjust: -40,
            yValue: 40
        };
        const annotation2 = {
            type: 'label',
            backgroundColor: 'rgba(245,245,245)',
            callout: {
                enabled: true,
                borderColor: 'rgba(245,0,0)'
            },
            content: tweetText3,
            font: {
                size: 13
            },
            position: {
                x: 55,
                y: 'top'
            },
            xAdjust: -175,
            xValue: 430,
            yAdjust: -60,
            yValue: 40
        }
        const annotation = [annotation1, annotation2]
        buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3, annotation1, annotation2)

    }).catch(err => {
        console.log(err);
    });
}
// Common function for plotting chart
function buildSentimentFinanceChart(ctx1, dateData, adjustedClose, sentimentScore, mark1, mark2, mark3, annotation1, annotation2) {

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
                width: 0.5,
                pointHoverBorderColor: 'white',
                pointHoverBorderColor: 'rgba(54, 162, 235, 1)',
                pointHoverBorderWidth: 3,
                pointHoverRadius: 10,

                type: 'line',
                yAxisID: 'dollar'
            }, {
                label: 'Adjusted Close',
                data: adjustedClose,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',

                ],
                borderColor: [
                    'rgba(255, 99, 132, 1.5)',

                ],
                tension: 0.5,
                width: 0.5,
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
                        text: 'Adjusted Close ($)'
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
                autocolors: false,
                annotation: {
                    annotations: [{
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
                        annotation1,
                        annotation2
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