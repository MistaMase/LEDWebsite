import json

class Preferences:
    # Only allow the class to be created once
    _shared_state = {}
    def __init__(self):
        # 'Singleton' for this class
        self.__dict__ = self._shared_state

        # Define the empty dictionaries
        self.debug_preferences = {}
        self.animation_preferences = {}
        self.color_preferences = {}
        self.setup_preferences = {}
        self.info = {}

        # Read all the preferences in
        self.read_debug_preferences()
        self.read_animation_preferences()
        self.read_color_preferences()
        self.read_setup_preferences()
        self.read_info()
        if self.get_debug_preferences('preferences-debug'):
            print('Parameters Debug: Debug Preferences ' + str(self.debug_preferences))
            print('Parameters Debug: Animation Preferences ' + str(self.animation_preferences))
            print('Parameters Debug: Color Preferences ' + str(self.color_preferences))
            print('Parameters Debug: Setup Preferences ' + str(self.setup_preferences))
            print('Parameters Debug: Info ' + str(self.info))


    def try_all_type_cast(self, line):
        current_line = ()
        parsed_line = line.strip().split(' ')
        for value in parsed_line:
            if value == 'true' or value == 'True':
                if len(parsed_line) > 1:
                    current_line = current_line + (True,)
                else:
                    return True
            elif value == 'false' or value == 'False':
                if len(parsed_line) > 1:
                    current_line = current_line + (False,)
                else:
                    return False
            elif value.isdigit():
                if len(parsed_line) > 1:
                    current_line = current_line + (int(value),)
                else:
                    return int(value)
            else:
                try:
                    if len(parsed_line) > 1:
                        current_line = current_line + (float(value),)
                    else:
                        return float(value)
                except ValueError:
                    if len(parsed_line) > 1:
                        current_line = current_line + (value,)
                    else:
                        return value
        return current_line


    # Read debug preferences from its respective file
    # Should only be run during __init__
    def read_debug_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/debug.json', 'r') as pref_file:
            self.debug_preferences = json.load(pref_file)


    # Read animation preferences from its respective file
    # Should only be run during __init__
    def read_animation_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/animation-order.json', 'r') as pref_file:
            self.animation_preferences = json.load(pref_file)


    # Read color preferences from its respective file
    # Should only be run during __init__
    def read_color_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/custom-colors.json', 'r') as pref_file:
            self.color_preferences = json.load(pref_file)


    # Read hardware setup preferences from its respective file
    # Should only be run during __init__
    def read_setup_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/setup.json', 'r') as pref_file:
            self.setup_preferences = json.load(pref_file)


    # Read info from its respective file
    # Should only be run during __init__
    def read_info(self):
        with open('/home/pi/LEDWebsite/preferences/info.json', 'r') as pref_file:
            self.info = json.load(pref_file)


    def get_debug_preferences(self, key='all'):
        if key == 'all':
            return self.debug_preferences
        else:
            return self.debug_preferences[key]


    def get_animation_preferences(self, key='all'):
        if key == 'all':
            return self.animation_preferences
        else:
            return self.animation_preferences[key]


    def get_color_preferences(self, key='all'):
        if key == 'all':
            return self.color_preferences
        else:
            return self.color_preferences[key]


    def get_setup_preferences(self, key='all'):
        if key == 'all':
            return self.setup_preferences
        else:
            return self.setup_preferences[key]


    def get_info(self, key='all'):
        if key == 'all':
            return self.info
        else:
            return self.info[key]


    def change_debug_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.debug_preferences.pop(key)
            else:
                self.debug_preferences[key] = value

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/debug.json', 'w') as pref_file:
                json.dump(self.debug_preferences, pref_file)
                # for key, value in self.debug_preferences.items():
                #     if type(value) == tuple or type(value) == list:
                #         pref_file.write(str(key) + ':')
                #         for val in value:
                #             pref_file.write(str(val) + ' ')
                #         pref_file.write('\n')
                #     else:
                #         pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Debug Preferences Dictionary with ' + str(key))


    def change_animation_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.animation_preferences.pop(key)
            else:
                self.animation_preferences[key] = value

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/animation-order.json', 'w') as pref_file:
                json.dump(self.animation_preferences, pref_file)
                # for key, value in self.animation_preferences.items():
                #     if type(value) == tuple or type(value) == list:
                #         pref_file.write(str(key) + ':')
                #         for val in value:
                #             pref_file.write(str(val) + ' ')
                #         pref_file.write('\n')
                #     else:
                #         pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Animation Preferences Dictionary with ' + str(key))

    def change_color_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.color_preferences.pop(key)
            else:
                self.color_preferences[key] = value

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/custom-colors.json', 'w') as pref_file:
                json.dump(self.color_preferences, pref_file)
                # for key, value in self.color_preferences.items():
                #     if type(value) == tuple or type(value) == list:
                #         pref_file.write(str(key) + ':')
                #         for val in value:
                #             pref_file.write(str(val) + ' ')
                #         pref_file.write('\n')
                #     else:
                #         pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Color Preferences Dictionary with ' + str(key))


    def change_setup_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.setup_preferences.pop(key)
            else:
                self.setup_preferences[key] = value

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/setup.json', 'w') as pref_file:
                json.dump(self.setup_preferences, pref_file)
                # for key, value in self.setup_preferences.items():
                #     if type(value) == tuple or type(value) == list:
                #         pref_file.write(str(key) + ':')
                #         for val in value:
                #             pref_file.write(str(val) + ' ')
                #         pref_file.write('\n')
                #     else:
                #         pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Setup Preferences Dictionary with ' + str(key))

    def change_info(self, key, value):
        try:
            # Change locally
            if value is None:
                self.info.pop(key)
            else:
                self.info[key] = value

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/info.json', 'w') as pref_file:
                json.dump(self.info, pref_file)
                # for key, value in self.info.items():
                #     if type(value) == tuple or type(value) == list:
                #         pref_file.write(str(key) + ':')
                #         for val in value:
                #             pref_file.write(' ' + str(val))
                #         pref_file.write('\n')
                #     else:
                #         pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Info Dictionary with ' + str(key))
