from flask_socketio import SocketIO, emit

# Informs this module of the global variables
global logger, scenes, preferences, hardware

'''
'   SocketIO Callback
'   Services:   Home initial connection
'   Returns:    Animation list, Home Parameters, Power Button Status
'''
@socketio.on('Home Connection')
def homeConnected():
    logger.log('Website', 'Home Connected')
    modes = scenes.getAnimationNames()
    emit('Home Mode List', modes)
    emit('Home Parameters', scenes.getAnimationOptions())
    emit('Home Power Status', 'Off' if (scenes.thread.name == 'Off') else 'On')


'''
'   SocketIO Callback
'   Services:   Home Animation Change
'   Returns:    New Animation Options
'''
@socketio.on('Home Mode Change')
def homeModeChanged(message):
    logger.log('Website', f'Changing Animation Mode to {message}')
    if not scenes.changeMode(message):
        logger.log('Website', 'Requested animation could not be found')
    emit('Home Parameters', scenes.getAnimationOptions())


'''
'   SocketIO Callback
'   Services:   Home Color Change
'   Returns:    New Animation Options
'''
@socketio.on('Home Color Change')
def homeColorChange(message):
    logger.log('Website', f'Requested to change Color Mode {message}')
    scenes.changeMode('Manual')
    colors = (['RValue', message[0]], ['GValue', message[1]], ['BValue', message[2]])
    scenes.thread.setParameter(colors[0])
    scenes.thread.setParameter(colors[1])
    scenes.thread.setParameter(colors[2])
    emit('Home Parameters', scenes.getAnimationOptions())


'''
'   SocketIO Callback
'   Services:   Manual Interface Initial Connection
'   Returns:    Current Animation Options, Power Button Status
'''
@socketio.on('MI Connection')
def manualConnected():
    logger.log('Website', 'Manual Interface Connected')
    emit('MI Parameters', scenes.getAnimationOptions())
    if scenes.thread.name == 'Manual':
        emit('MI Color Profiles', preferences.get_color_preferences())
    emit('MI Power Status', 'Off' if (scenes.thread.name == 'Off') else 'On')

'''
'   SocketIO Callback
'   Services:   Manual Interface Update
'   Returns:    None
'''
@socketio.on('MI Update Client')
def manualColorChange(message):
    logger.log('Website', f'Parameter Change {message}')
    scenes.thread.setParameter(message)

'''
'   SocketIO Callback
'   Services:   Manual Interface Remove Custom Color Profile
'   Returns:    New Custom Color Profile List
'''
@socketio.on('MI Remove Color Profile')
def manualRemoveColorProfile(message):
    if message is not '':
        logger.log('Website', f'Removing Color Profile {message}')
        preferences.change_color_preference(message, None)
        emit('MI Color Profiles', preferences.get_color_preferences())

'''
'   SocketIO Callback
'   Services:   Manual Interface Add Custom Color Profile
'   Returns:    New Custom Color Profile List
'''
@socketio.on('MI Add Color Profile')
def manualAddColorProfile(message):
    if message is not '':
        logger.log('Website', f'Adding Color Profile {message}')
        preferences.change_color_preference(message[0], message[1])
    emit('MI Color Profiles', preferences.get_color_preferences())


'''
'   SocketIO Callback
'   Services:   Hardware Interface Initial Connection
'   Returns:    Hardware Status, Power Button Status
'''
# Socketio response for Hardware Interface webpage initial connection
@socketio.on('HI Connection')
def firstHIConnection():
    logger.log('Website', 'Hardware Interface Connection, Sending INFO')
    emit('HI Update Server', hardware.get_info())
    emit('HI Power Status', 'Off' if (scenes.thread.name == 'Off') else 'On')

'''
'   SocketIO Callback
'   Services:   Hardware Interface Periodic Client Update
'   Returns:    Hardware Status
'''
@socketio.on("HI Update Client")
def sendHardwareInfo():
    logger.log('Website', 'HI Requesting Periodic Update')
    emit('HI Update Server', hardware.get_info())
