# Flask Library Imports
from flask import Flask, render_template, redirect, url_for

# Simple function to get the current IP Address
import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


'''
'   Flask Route
'   Services:   '/'
'   Returns:    Redirect to '/home'
'''
@app.route('/')
def redirecttohome():
    return redirect(url_for('home'))


'''
'   Flask Route
'   Services:   '/home'
'   Returns:    Homepage HTML and CSS
'''
@app.route('/home')
def home():
    return render_template('Home.html', ipaddress=get_ip_address())


'''
'   Flask Route
'   Services:   '/manualinput'
'   Returns:    Manual Input Page HTML and CSS
'''
@app.route('/manualinput')
def manualinput():
    return render_template('ManualInputInterface.html', ipaddress=get_ip_address())

'''
'   Flask Route
'   Services:   '/codeinput'
'   Returns:    Code Input Page HTML and CSS
'''
@app.route('/codeinput')
def codeinput():
    return render_template('CodeInputInterface.html', ipaddress=get_ip_address())

'''
'   Flask Route
'   Services:   '/hardwareinformation'
'   Returns:    Hardware Information Page HTML and CSS
'''
@app.route('/hardwareinformation')
def hardwareinformation():
    return render_template('HardwareInformationInterface.html', ipaddress=get_ip_address())

'''
'   Flask Configuration
'   Services:   All Website
'   Returns:    Disables browser caching
'''
@app.after_request
def addHeader(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
