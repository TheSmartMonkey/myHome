from flask import Flask, send_from_directory, jsonify
from smbus import SMBus
from lcd import LCD
import struct


app = Flask(__name__)
display = LCD()

@app.route('/')
def index():
    return send_from_directory('/home/pi/webapp/myHome','index.html')


# Capteur - Sensors
@app.route('/message/<msg1>/<msg2>')
def display_message(msg1,msg2):
    display.displayText(msg1,msg2)
    return msg1 + " " + msg2 + " message displayed"

@app.route('/setLight/<led>/<onoff>')
def set_light(led,onoff):
    bus = SMBus(1)
    bus.write_i2c_block_data(18, ord('L'), [ord(led), ord('O' if onoff == "on" else  'F')])
    bus.close()
    return "light %s is set to %s"%(led, onoff)

@app.route('/getTemperature')
def get_humidity_temperature():
    "get the humidity and the tempetature by calling the arduino by I2C"
    bus = SMBus(1)
    data = bus.read_i2c_block_data(18,0)
    humidity, temperature = struct.unpack("ff", struct.pack("B"*8,*data[0:8]))
    return jsonify({"humidity":humidity,"temperature":temperature})


# Application Web - Web App
@app.route('/bootstrap4/<path:filepath>')
def bootstrap(filepath):
    return send_from_directory('/home/pi/webapp/myHome/bootstrap4', filepath)

@app.route('/css/<path:filepath>')
def style_css(filepath):
    return send_from_directory('/home/pi/webapp/myHome/css', filepath)

@app.route('/js/<path:filepath>')
def script_js(filepath):
    return send_from_directory('/home/pi/webapp/myHome/js', filepath)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8989)