from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/manualinput/')
def manualInput():
    return render_template('ManualInputInterface.html')

@app.route('/codeinput/')
def codeInput():
    return render_template('CodeInputInterface.html')

@app.route('/hardwareinformation/')
def hardwareInformation():
    return render_template('HardwareInformationInterface.html')

# Prevent browsers from caching anything
@app.after_request
def addHeader(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
