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
        for value in line.strip().split(' '):
            if value == 'true' or value == 'True':
                current_line = current_line + (True,)
            elif value == 'false' or value == 'False':
                current_line = current_line + (False,)
            elif value.isdigit():
                current_line = current_line + (int(value),)
            else:
                try:
                    current_line = current_line + (float(value),)
                except ValueError:
                    current_line = current_line + (value,)
        return current_line

    # Read debug preferences from its respective file
    # Should only be run during __init__
    def read_debug_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/debug.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.debug_preferences[line[0]] = self.try_all_type_cast(line[1])

    # Read animation preferences from its respective file
    # Should only be run during __init__
    def read_animation_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/animation-order.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.animation_preferences[line[0]] = self.try_all_type_cast(line[1])

    # Read color preferences from its respective file
    # Should only be run during __init__
    def read_color_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/custom-colors.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.strip().split(':')
                colors = self.try_all_type_cast(line[1])
                if len(colors) is not 3:
                    if self.get_debug_preferences('preferences-debug'):
                        print("Parameters Debug: Invalid Color, Too Few Numbers")
                elif not all([type(n) == int for n in colors]):
                    if self.get_debug_preferences('preferences-debug'):
                        print("Parameters Debug: Invalid Color, Invalid Number")
                else:
                    self.color_preferences[line[0]] = colors

    # Read hardware setup preferences from its respective file
    # Should only be run during __init__
    def read_setup_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/setup.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.setup_preferences[line[0]] = self.try_all_type_cast(line[1])

    # Read info from its respective file
    # Should only be run during __init__
    def read_info(self):
        with open('/home/pi/LEDWebsite/preferences/info.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.info[line[0]] = self.try_all_type_cast(line[1])

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
                self.debug_preferences[key] = self.try_all_type_cast(value)

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/debug.txt', 'w') as pref_file:
                for key, value in self.debug_preferences.items():
                    if type(value) == tuple or type(value) == list:
                        pref_file.write(str(key) + ':')
                        for val in value:
                            pref_file.write(str(val) + ' ')
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Debug Preferences Dictionary with ' + str(key))


    def change_animation_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.animation_preferences.pop(key)
            else:
                self.animation_preferences[key] = self.try_all_type_cast(value)


            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/animation-order.txt', 'w') as pref_file:
                for key, value in self.animation_preferences.items():
                    if type(value) == tuple or type(value) == list:
                        pref_file.write(str(key) + ':')
                        for val in value:
                            pref_file.write(str(val) + ' ')
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Animation Preferences Dictionary with ' + str(key))

    def change_color_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.color_preferences.pop(key)
            else:
                self.color_preferences[key] = self.try_all_type_cast(value)
            print('Color Preferences')
            print(self.color_preferences)


            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/custom-colors.txt', 'w') as pref_file:
                for key, value in self.color_preferences.items():
                    if type(value) == tuple or type(value) == list:
                        print('Writing multiple values for ' + str(key))
                        pref_file.write(str(key) + ':')
                        for val in value:
                            print('Writing ' + str(val))
                            pref_file.write(str(val) + ' ')
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Color Preferences Dictionary with ' + str(key))


    def change_setup_preference(self, key, value):
        try:
            # Change locally
            if value is None:
                self.setup_preferences.pop(key)
            else:
                self.setup_preferences[key] = self.try_all_type_cast(value)

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/setup.txt', 'w') as pref_file:
                for key, value in self.setup_preferences.items():
                    if type(value) == tuple or type(value) == list:
                        pref_file.write(str(key) + ':')
                        for val in value:
                            pref_file.write(str(val) + ' ')
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Setup Preferences Dictionary with ' + str(key))

    def change_info(self, key, value):
        try:
            # Change locally
            if value is None:
                self.info.pop(key)
            else:
                self.info[key] = self.try_all_type_cast(value)

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/info.txt', 'w') as pref_file:
                for key, value in self.info.items():
                    if type(value) == tuple or type(value) == list:
                        pref_file.write(str(key) + ':')
                        for val in value:
                            pref_file.write(' ' + str(val))
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Info Dictionary with ' + str(key))
