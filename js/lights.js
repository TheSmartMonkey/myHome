// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

function setLights(checkBox) {

    if (checkBox.checked == true) {
        request.open('GET', '/setLight/' + checkBox.getAttribute("led") + '/on')
    } else {
        request.open('GET', '/setLight/' + checkBox.getAttribute("led") + '/off')
    }

    // Send request
    request.send()
}

function getTemperature() {

    request.open('GET', '/getTemperature')

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var temperatureInfo = JSON.parse(this.responseText)
            document.getElementById("humidity").innerHTML = temperatureInfo.humidity.toFixed(2)
            document.getElementById("temperature").innerHTML = temperatureInfo.temperature.toFixed(2)
        }
    }
    
    // Send request
    request.send()
}

function checkTemperature() {
    getTemperature()
    setInterval(getTemperature,10000)
}

