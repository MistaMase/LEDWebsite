# Import Regex for checking if parameter is a decimal number
import re
num_pattern = re.compile('\d+(\.\d+)?')

# Define the empty dictionaries
debug_preferences = {}
animation_preferences = {}
color_preferences = {}
setup_preferences = {}
info = {}


# Read debug preferences from its respective file
def read_debug_preferences():
    with open('/home/pi/LEDWebsite/preferences/debug.txt', 'r') as pref_file:
        for line in pref_file.readlines():
            line = line.lower().replace(' ', '').strip().split(':')
            if line[1] == 'true':
                debug_preferences[line[0]] = True
            elif line[1] == 'false':
                debug_preferences[line[0]] = False
            elif line[1].isdigit():
                debug_preferences[line[0]] = int(line[1])
            elif num_pattern.match(line[1]) is not None:
                debug_preferences[line[0]] = float(line[1])
            else:
                debug_preferences[line[0]] = line[1]

# Read animation preferences from its respective file
def read_animation_preferences():
    with open('/home/pi/LEDWebsite/preferences/animation-order.txt', 'r') as pref_file:
        for line in pref_file.readlines():
            line = line.lower().replace(' ', '').strip().split(':')
            if line[1] == 'true':
                animation_preferences[line[0]] = True
            elif line[1] == 'false':
                animation_preferences[line[0]] = False
            elif line[1].isdigit():
                animation_preferences[line[0]] = int(line[1])
            elif num_pattern.match(line[1]) is not None:
                animation_preferences[line[0]] = float(line[1])
            else:
                animation_preferences[line[0]] = line[1]

# Read color preferences from its respective file
def read_color_preferences():
    with open('/home/pi/LEDWebsite/preferences/custom-colors.txt', 'r') as pref_file:
        for line in pref_file.readlines():
            line = line.lower().replace(' ', '').strip().split(':')
            if line[1] == 'true':
                color_preferences[line[0]] = True
            elif line[1] == 'false':
                color_preferences[line[0]] = False
            elif line[1].isdigit():
                color_preferences[line[0]] = int(line[1])
            elif num_pattern.match(line[1]) is not None:
                color_preferences[line[0]] = float(line[1])
            else:
                color_preferences[line[0]] = line[1]

# Read hardware setup preferences from its respective file
def read_setup_preferences():
    with open('/home/pi/LEDWebsite/preferences/setup.txt', 'r') as pref_file:
        for line in pref_file.readlines():
            line = line.lower().replace(' ', '').strip().split(':')
            if line[1] == 'true':
                setup_preferences[line[0]] = True
            elif line[1] == 'false':
                setup_preferences[line[0]] = False
            elif line[1].isdigit():
                setup_preferences[line[0]] = int(line[1])
            elif num_pattern.match(line[1]) is not None:
                setup_preferences[line[0]] = float(line[1])
            else:
                setup_preferences[line[0]] = line[1]

# Read info from its respective file
def read_info():
    with open('/home/pi/LEDWebsite/preferences/info.txt', 'r') as pref_file:
        for line in pref_file.readlines():
            line = line.lower().replace(' ', '').strip().split(':')
            if line[1] == 'true':
                info[line[0]] = True
            elif line[1] == 'false':
                info[line[0]] = False
            elif line[1].isdigit():
                info[line[0]] = int(line[1])
            elif num_pattern.match(line[1]) is not None:
                info[line[0]] = float(line[1])
            else:
                info[line[0]] = line[1]

# Read all preferences in one call
def read_preferences():
    read_debug_preferences()
    read_animation_preferences()
    read_color_preferences()
    read_setup_preferences()
    read_info()
    if get_debug_preferences('preferences-debug'):
        print('Debug Preferences')
        print(debug_preferences)
        print('Animation Preferences')
        print(animation_preferences)
        print('Color Preferences')
        print(color_preferences)
        print('Setup Preferences')
        print(setup_preferences)
        print('Info')
        print(info)

def get_debug_preferences(key='all'):
    if key == 'all':
        return debug_preferences
    else:
        return debug_preferences[key]

def get_animation_preferences(key='all'):
    if key == 'all':
        return animation_preferences
    else:
        return animation_preferences[key]

def get_color_preferences(key='all'):
    if key == 'all':
        return color_preferences
    else:
        return color_preferences[key]

def get_setup_preferences(key='all'):
    if key == 'all':
        return setup_preferences
    else:
        return setup_preferences[key]

def get_info(key='all'):
    if key == 'all':
        return info
    else:
        return info[key]