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
    buildTweet7Day();

}


init();

/*Events*/
function optionChanged(value){
    console.log(value)
    const label = document.getElementById("financeType");
    financeType = label.value

    console.log(financeType)
    
}

function selectorChanged(value1){
    financeType1 = value1
    console.log(financeType1)

    const label = document.getElementById("dateSelected");
    dateLogged1 = label.value
    console.log(dateLogged1)

    // fetch('/JSON_files/financeData7Days.json').then(response1 => {
    //     return response1.json();
    //     }).then(data1 => {
    
    //     data1 = data1[financeType1]
    //     filteredbyDate = data1.filter(index => index.tweetDate == dateLogged1)
    //     console.log(filteredbyDate)
    // })

    fetch('/JSON_files/financedeltapercent.json').then(response2 => {
        return response2.json();
        }).then(data2 => {
        
        data2 = data2.filter(index => index.financeType == financeType1 )
        // filteredDate2 = data2.filter(index => index.tweetDate ==dateLogged1)
        console.log(data2)
    })

    fetch('/JSON_files/tweetsperDate.json').then(response3 => {
        return response3.json();
        }).then(data3 => {
    
        data3 = data3[financeType1]

        filteredDate3 = data3.filter(index => index.date==dateLogged1)
        
        // tweetIDsperDate = filteredDate3.tweetIDs

        console.log(filteredDate3)
    })


}
