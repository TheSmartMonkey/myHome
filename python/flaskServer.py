from flask import Flask, send_from_directory, jsonify
from smbus import SMBus
from lcd import LCD
import struct
import socket
from dataHistory import BackgroundHistory


# Address of the 2 Arduino - Adresse des 2 Arduino
ARDUINO1_I2C_ADDRESS = 18
ARDUINO2_I2C_ADDRESS = 19

last_door_status = False

app = Flask(__name__)
lcd = LCD()
history = BackgroundHistory()

@app.route('/')
def index():
    return send_from_directory('/home/pi/webapp/myHome','index.html')


# Sensors - Capteurs
@app.route('/message/<msg1>/<msg2>')
def display_message(msg1,msg2):
    lcd.displayText(msg1,msg2)
    return msg1 + " " + msg2 + " message displayed"

@app.route('/getIp')
def display_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]

    lcd.displayText("My IP", ipaddress)
    s.close()

    print(ipaddress)
    return ipaddress

@app.route('/setLight/<led>/<onoff>')
def set_light(led,onoff):
    bus = SMBus(1)
    bus.write_i2c_block_data(ARDUINO1_I2C_ADDRESS, ord('L'), [ord(led), ord('O' if onoff == "on" else 'F')])
    bus.close()
    return "light %s is set to %s" % (led, onoff)

@app.route('/setGarageDoor/<closeopen>')
def set_garage_door(closeopen):
    bus = SMBus(1)
    bus.write_i2c_block_data(ARDUINO2_I2C_ADDRESS, ord('D'), [ord('O' if closeopen == "open" else 'C')])
    bus.close()
    return "Garage Door : %s" % (closeopen)

@app.route('/getStatus')
def get_status():
    """
    Get the humidity, tempetature, led and garage door status by calling the arduino by I2C
    Obtenez l'humidité, la température, l'état des leds et de la porte de garage en appelant l'arduino par I2C
    """

    bus = SMBus(1)

    i2c_data1 = bus.read_i2c_block_data(ARDUINO1_I2C_ADDRESS,0)
    humidity, temperature = struct.unpack("ff", struct.pack("B"*8,*i2c_data1[0:8]))
    leds = i2c_data1[8:13]

    i2c_data2 = bus.read_i2c_block_data(ARDUINO2_I2C_ADDRESS,0)
    garage_door = i2c_data2[0]

    bus.close()

    global last_door_status

    # Display door status on LCD - Affiche le status de la porte sur le LCD
    if garage_door == 1 and last_door_status == False:
        display_message("Garage","Open")
        last_door_status = True
    elif garage_door == 0 and last_door_status == True:
        display_message("Garage","Closed")
        last_door_status = False

    response = {"humidity" : humidity,
                "temperature" : temperature,
                "leds" : leds,
                "garageDoor" : garage_door}
    return jsonify(response)

@app.route('/getHistory')
def get_history():
    return jsonify(history.get_elements())


# Web App - Application Web
@app.route('/bootstrap4/<path:filepath>')
def bootstrap(filepath):
    return send_from_directory('/home/pi/webapp/myHome/bootstrap4', filepath)

@app.route('/Chart-lib/<path:filepath>')
def chartLib(filepath):
    return send_from_directory('/home/pi/webapp/myHome/Chart-lib', filepath)

@app.route('/css/<path:filepath>')
def style_css(filepath):
    return send_from_directory('/home/pi/webapp/myHome/css', filepath)

@app.route('/js/<path:filepath>')
def script_js(filepath):
    return send_from_directory('/home/pi/webapp/myHome/js', filepath)

if __name__ == '__main__':
    display_ip()
    app.run(host = '0.0.0.0', port = 8989)