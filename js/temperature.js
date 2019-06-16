// Temperature Chart  - Graphique de Temperature
var ctxTemperature = document.getElementById('temperatureChart').getContext('2d');
var temperatureChart = new Chart(ctxTemperature, {
    // Chart type we want to create - Type de graphique que nous voulons créer
    type: 'line',

    // Dataset - Ensemble de données
    data: {
        labels: [],
        datasets: [{
            label: "temperature",
            backgroundColor: 'rgb(255,140,0)',
            borderColor: 'rgb(255,140,0)',
            data: [],
        }]
    },

    // Configuration options - Options de configuration
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: false
                }
            }]
        }
    }
});


// Humidity Chart  - Graphique de l'Humidité
var ctxHumidity = document.getElementById('humidityChart').getContext('2d');
var humidityChart = new Chart(ctxHumidity, {
    // Chart type we want to create - Type de graphique que nous voulons créer
    type: 'line',

    // Dataset - Ensemble de données
    data: {
        labels: [],
        datasets: [{
            label: "humidity",
            backgroundColor: 'rgb(30,144,255)',
            borderColor: 'rgb(30,144,255)',
            data: [],
        }]
    },

    // Configuration options - Options de configuration
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: false
                }
            }]
        }
    }
});


function updateChart() {
    request.open('GET', '/getHistory')

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var history = JSON.parse(this.responseText)
            var labels = []
            var dataTemperature = []
            var dataHumidity = []

            for (var i = 0; i < history.length; i++) {
                labels.push(history[i].timestamp.substring(11, 19))
                dataTemperature.push(history[i].temperature.toFixed(2))
                dataHumidity.push(history[i].humidity.toFixed(2))
            }

            temperatureChart.data.labels = labels
            temperatureChart.data.datasets[0].data = dataTemperature
            temperatureChart.update()

            humidityChart.data.labels = labels
            humidityChart.data.datasets[0].data = dataHumidity
            humidityChart.update()
        }
    }

    // Send request - Envoie la requete
    request.send()
}

setInterval(updateChart,10000)