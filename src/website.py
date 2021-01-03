# Import Flask
from flask import Flask, Blueprint

# Import SocketIO
from FlaskSocketIO import socketio_callbacks

# Import Flask Callbacks
from FlaskCallbacks import flask_callbacks


class Website():
    def __init__(self, preferences):
        # Save the preferences object
        self.preferences = preferences

        # Configure website variables
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'myspecialsecret'
        self.socketio = SocketIO(self.app)
       
        # Link the FlaskCallbacks Blueprint
        self.app.register_blueprint(flask_callbacks)
        
        self.socketio = SocketIO()

        self.socketio.register_blueprint(socketio_callbacks)

        # Start the website
        self.socketio.run(self.app, host='0.0.0.0', port='80', debug=preferences.get_debug_preferences('flask-debug'))
