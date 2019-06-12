from flask import Flask, send_from_directory
from smbus import SMBus
from lcd import LCD

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

# Application Web - Web App
@app.route('/bootstrap4/<path:filepath>')
def bootstrap(filepath):
    return send_from_directory('/home/pi/webapp/myHome/bootstrap4', filepath)

@app.route('/css/<path:filepath>')
def style_css(filepath):
    return send_from_directory('/home/pi/webapp/myHome/css', filepath)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8989)