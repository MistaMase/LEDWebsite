# Website Imports
from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit

# IP Address Import
import socket

# LED Light Imports
import scenes as scenes

# Hardware Information
import hardwareInfo as hwInfo

# User Preferences
import preferences as preferences

# Update Shell Script
import os

# Set up website variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myspecialsecret'
socketio = SocketIO(app)

# Set up user settings
preferences.read_preferences()

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
    if preferences.get_debug_preferences('website-debug'):
        print("Home Connected")
    modes = scenes.getAnimationNames()
    emit('Home Mode List', modes)
    emit('Home Parameters', scenes.getAnimationOptions())

# Socketio response for Home webpage mode change
@socketio.on('Home Mode Change')
def homeModeChanged(message):
    if preferences.get_debug_preferences('website-debug'):
        print("Requested to change Animation Mode to " + message)
    if not scenes.changeMode(message):
        if preferences.get_debug_preferences('website-debug'):
            print("Requested animation could not be found")
    emit('Home Parameters', scenes.getAnimationOptions())

# Socketio response to Home webpage color change
@socketio.on('Home Color Change')
def homeColorChange(message):
    if preferences.get_debug_preferences('website-debug'):
        print("Requested to change Color Mode")
        print(message)
    scenes.changeMode('Manual')
    rvalue = ['RValue', message[0]]
    gvalue = ['GValue', message[1]]
    bvalue = ['BValue', message[2]]
    scenes.thread.setParameter(rvalue)
    scenes.thread.setParameter(gvalue)
    scenes.thread.setParameter(bvalue)
    emit('Home Parameters', scenes.getAnimationOptions())

# Flask route for '/manualinput' which displays the manual color changer
@app.route('/manualinput')
def manualinput():
    return render_template('ManualInputInterface.html', ipaddress=getIpAddress())

# Socketio response for Manual Interface webpage initial connection
@socketio.on('MI Connection')
def manualConnected():
    if preferences.get_debug_preferences('website-debug'):
        print("MI Connected")
    emit('MI Parameters', scenes.getAnimationOptions())

# Socketio response for Manual Interface webpage color change
@socketio.on('MI Update Client')
def manualColorChange(message):
    if preferences.get_debug_preferences('website-debug'):
        print("Parameter Change")
        print(message)
    scenes.thread.setParameter(message)

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
    if preferences.get_debug_preferences('website-debug'):
        print("HI Connection. Sending INFO")
    emit('HI Update Server', hwInfo.getInfo())

# Socketio response for Hardware Interface webpage requesting periodic information update
@socketio.on("HI Update Client")
def sendHardwareInfo():
    if preferences.get_debug_preferences('website-debug'):
        print("HI Requesting Periodic Update")
    emit('HI Update Server', hwInfo.getInfo())

# Client requested update
@socketio.on('HI Software Update')
def softwareUpdate():
    if preferences.get_debug_preferences('website-debug'):
        print('Updating Software')
    os.system('./update')

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

# Runs the entire python script
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='5050', debug=preferences.get_debug_preferences('flask-debug'))
