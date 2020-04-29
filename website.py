from flask import Flask
from flask import render_template



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/hardwareinformation/')
def hardwareInformation():
    return render_template('HardwareInformationInterface.html')


@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    r.headers['Pragma'] = 'no-cache'
    r.headers['Expires'] = '0'
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
