# Website Imports
from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit

# CPU Temp Import
from gpiozero import CPUTemperature

# IP Address Import
import socket

# LED Light Imports
import scenes as scenes

# Set up website variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myspecialsecret'
socketio = SocketIO(app)

# Flask route for '/' which redirects to '/home'
@app.route('/')
def redirecttohome():
    return redirect(url_for('home'))

# Flask route for '/home' which displays the homepage of the website
@app.route('/home')
def home():
    return render_template('Home.html', ipaddress=getIpAddress())

# Socketio response for Home webpage initial connection
@socketio.on('Home Connection')
def homeConnected():
    print("Home Connected")
    modes = scenes.getAnimationNames()
    emit('Home Mode List', modes)

# Socketio response for Home webpage mode change
@socketio.on('Home Mode Change')
def homeModeChanged(message):
    print("Requested to change Animation Mode to " + message)
    if not scenes.changeMode(message):
        print("Requested animation could not be found")

# Flask route for '/manualinput' which displays the manual color changer
@app.route('/manualinput')
def manualinput():
    return render_template('ManualInputInterface.html', ipaddress=getIpAddress())

# Socketio response for Manual Interface webpage initial connection
@socketio.on('MI Connection')
def manualConnected():
    print("MI Connected")

# Socketio response for Manual Interface webpage color change
@socketio.on('MI Update Client')
def manualColorChange(message):
    print("Colors:" + message)
    scenes.thread.setColor(message)

# Flask route for '/codeinput' which displays the code input interface
@app.route('/codeinput')
def codeinput():
    return render_template('CodeInputInterface.html', ipaddress=getIpAddress())

# Flask route for '/hardwareinformation' which displays the current hardware stats of the device
@app.route('/hardwareinformation')
def hardwareinformation():
    return render_template('HardwareInformationInterface.html', ipaddress=getIpAddress())

# Socketio response for Hardware Interface webpage initial connection
@socketio.on('HI Connection')
def firstHIConnection():
    print("HI Connection. Sending INFO")
    emit('HI Update Server', { 'mode': 'test', 'fanSpeed': '50', 'micValue': '70', 'piTemp': getCPUTemp() })

# Socketio response for Hardware Interface webpage requesting periodic information update
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

# Runs the entire python script
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='5050', debug=True)
