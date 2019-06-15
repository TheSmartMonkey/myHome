// Temperature Chart  - Graphique de Temperature
var ctx = document.getElementById('temperatureChart').getContext('2d');
var temperatureChart = new Chart(ctx, {
    // Chart type we want to create - Type de graphique que nous voulons créer
    type: 'line',

    // Dataset - Ensemble de données
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "temperature",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45],
        }]
    },

    // Configuration options - Options de configuration
    options: {}
});