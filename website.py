from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit

from gpiozero import CPUTemperature

import socket

import scenes as scenes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myspecialsecret'
socketio = SocketIO(app)

scenes.thread = scenes.ManualColor()
scenes.thread.start()

@app.route('/')
def redirecttohome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('Home.html', ipaddress=getIpAddress())

@app.route('/manualinput')
def manualinput():
    return render_template('ManualInputInterface.html', ipaddress=getIpAddress())

@socketio.on('MI Connection')
def manualConnected():
    print("MI Connected")

@socketio.on('MI Update Client')
def manualColorChange(message):
    print("Colors:" + message)
    scenes.thread.setColor(message)

@app.route('/codeinput')
def codeinput():
    return render_template('CodeInputInterface.html', ipaddress=getIpAddress())

@app.route('/hardwareinformation')
def hardwareinformation():
    return render_template('HardwareInformationInterface.html', ipaddress=getIpAddress())

@socketio.on('HI Connection')
def firstHIConnection():
    print("HI Connection. Sending INFO")
    emit('HI Update Server', { 'mode': 'test', 'fanSpeed': '50', 'micValue': '70', 'piTemp': getCPUTemp() })

@socketio.on("HI Update Client")
def sendHardwareInfo():
    print("HI Requesting Periodic Update")
    emit('HI Update Server', { 'mode': 'test', 'fanSpeed': '50', 'micValue': '70', 'piTemp': getCPUTemp() })


# Prevent browsers from caching anything
@app.after_request
def addHeader(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Gets the current IP Address
def getIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Gets the Pi's CPU temp to send to the client
def getCPUTemp():
    cpu = CPUTemperature()
    return cpu.temperature


if __name__ == '__main__':
    print(getCPUTemp())
    socketio.run(app, host='0.0.0.0', port='5050', debug=True)
