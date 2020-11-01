# Import Flask
from flask import Flask

# Import SocketIO
from flask_socketio import SocketIO

# Flask Callbacks
__FlaskIOCallbacks__ = 'FlaskCallbacks.py'

# SocketIO Callbacks
__SocketIOCallbacks__ = 'SocketIOCallbacks.py'

# Inform the module of global variables
global preferences

class Website():
    def __init__(self):
        # Configure website variables
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'myspecialsecret'
        self.socketio = SocketIO(self.app)

        # Start the website
        self.socketio.run(self.app, host='0.0.0.0', port='80', debug=preferences.get_debug_preferences('flask-debug'))
