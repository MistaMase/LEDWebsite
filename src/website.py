# Import Flask
from flask import Flask

# Import SocketIO
from flask_socketio import SocketIO

class Website():
    def __init__(self, preferences):
        # Save the preferences object
        self.preferences = preferences

        # Configure website variables
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'myspecialsecret'
        self.socketio = SocketIO(self.app)

        # Flask Callbacks
        import FlaskCallbacks

        # SocketIO Callbacks
        import SocketIOCallbacks

        # Start the website
        self.socketio.run(self.app, host='0.0.0.0', port='80', debug=preferences.get_debug_preferences('flask-debug'))
