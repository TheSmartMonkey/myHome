from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('/home/pi/webapp/myHome','index.html')

@app.route('/bootstrap4/<path:filepath>')
def bootstrap(filepath):
    return send_from_directory('/home/pi/webapp/myHome/boostrap4',filepath)

@app.route('/css/<path:filepath>')
def style_css(filepath):
    return send_from_directory('/home/pi/webapp/myHome/css',filepath)

if __name__ == '__main__':
    app.run(host='192.168.1.114', port=8989)