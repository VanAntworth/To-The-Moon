function buildTweet7Day(){
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
        });

}

function buildDateControl(){

var date = new Date();
var today = new Date(date.getFullYear(), date.getMonth(), date.getDate());

    $('#datepicker').datepicker({
        format: 'dd/mm/yyyy', 
        autoclose: true, 
        todayHighlight: true,
        forceParse: false,
        setDate: today
    });
}

function buildSentimentChart(){
    fetch('/JSON_files/financetweetsentiment.json').then(response => {

        return response.json();
      }).then(data => {
        data = data.filter(index => index.financeType == 'doge')
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
            console.log(adjustedClose);
            console.log(sentimentScore);
            const ctx1 = document.getElementById('sentimentChart').getContext('2d');
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
                    tension: 0.5
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
                    yAxisID: 'dollar'
                }]
            }
            const sentimentChart = new Chart(ctx1, {
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

       
      }).catch(err => {
        console.log(err);
      });
}
function init()
{
    buildDateControl();
    buildTweet7Day();
    buildSentimentChart();
}


init();