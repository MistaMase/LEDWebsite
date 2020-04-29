from flask import Flask, render_template, redirect, url_for

import socket

app = Flask(__name__)

@app.route('/')
def redirecttohome():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('Home.html', ipaddress=getIpAddress())

@app.route('/manualinput')
def manualinput():
    return render_template('ManualInputInterface.html', ipaddress=getIpAddress())

@app.route('/codeinput')
def codeinput():
    return render_template('CodeInputInterface.html', ipaddress=getIpAddress())

@app.route('/hardwareinformation')
def hardwareinformation():
    return render_template('HardwareInformationInterface.html', ipaddress=getIpAddress())

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
