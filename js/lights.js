// API call - Appel API
var request = new XMLHttpRequest()

function setLights(checkBox) {

    if (checkBox.checked == true) {
        request.open('GET', '/setLight/' + checkBox.getAttribute("led") + '/on')
    } else {
        request.open('GET', '/setLight/' + checkBox.getAttribute("led") + '/off')
    }

    // Displays the action of the button in the console - Affiche l'action du bouton dans la console
    request.onreadystatechange = function() {
        console.log(request.response)
    }
    
    // Send request - Envoie la requete
    request.send()
}

function setGarageDoor(checkBox) {

    if (checkBox.checked == true) {
        request.open('GET', '/setGarageDoor/open')
    } else {
        request.open('GET', '/setGarageDoor/close')
    }

    // Displays the action of the button in the console - Affiche l'action du bouton dans la console
    request.onreadystatechange = function() {
        console.log(request.response)
    }

    // Send request -  Envoie la requete
    request.send()
}

function getStatus() {

    request.open('GET', '/getStatus')

    request.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var statusInfo = JSON.parse(this.responseText)

            // Set humidity and temperature by decimal - Réglage de l'humidité et de la température par décimales
            document.getElementById("humidity").innerHTML = statusInfo.humidity.toFixed(2)
            document.getElementById("temperature").innerHTML = statusInfo.temperature.toFixed(2)

            // Set light status - Fixe le statut de l'éclairage
            var ledContainer = document.getElementById("ledContainer").getElementsByTagName("div")
            for (var led = 0; led < ledContainer.length; led++) {
                var element = ledContainer[led].getElementsByTagName("label")[0].getElementsByTagName("input")[0]
                if (statusInfo.leds[parseInt(element.getAttribute("led"),10)]) {
                    element.checked = true
                } else {
                    element.checked = false
                }
            }

            // Set garage door close/open - Fermeture/ouverture de la porte de garage
            var garageDoor = document.getElementById("garageDoor")
            if (statusInfo.garageDoor) {
                garageDoor.checked = true
            } else {
                garageDoor.checked = false
            }
        }
    }
    
    // Send request - Envoie la requete
    request.send()
}

// Refresh status every seconds - Actualiser l'état toutes les secondes
function checkStatus() {
    getStatus()
    setInterval(getStatus,1000)
}

