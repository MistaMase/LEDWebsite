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
        if line[1] == 'true':
            return True
        elif line[1] == 'false':
            return False
        elif line[1].isdigit():
            return int(line[1])
        else:
            try:
                return float(line[1])
            except ValueError:
                return line[1]

    # Read debug preferences from its respective file
    # Should only be run during __init__
    def read_debug_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/debug.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.debug_preferences[line[0]] = self.try_all_type_cast(line)

    # Read animation preferences from its respective file
    # Should only be run during __init__
    def read_animation_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/animation-order.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.animation_preferences[line[0]] = self.try_all_type_cast(line)

    # Read color preferences from its respective file
    # Should only be run during __init__
    def read_color_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/custom-colors.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.strip().split(':')
                color = line[1].strip().split(' ')
                try:
                    colors = (int(color[0]), int(color[1]), int(color[2]))
                    self.color_preferences[line[0]] = colors
                except ValueError:
                    if self.get_debug_preferences('preferences-debug'):
                        print("Parameters Debug: Invalid Color, Invalid Number")
                except IndexError:
                    if self.get_debug_preferences('preferences-debug'):
                        print("Parameters Debug: Invalid Color, Too Few Numbers")

    # Read hardware setup preferences from its respective file
    # Should only be run during __init__
    def read_setup_preferences(self):
        with open('/home/pi/LEDWebsite/preferences/setup.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.setup_preferences[line[0]] = self.try_all_type_cast(line)

    # Read info from its respective file
    # Should only be run during __init__
    def read_info(self):
        with open('/home/pi/LEDWebsite/preferences/info.txt', 'r') as pref_file:
            for line in pref_file.readlines():
                line = line.lower().replace(' ', '').strip().split(':')
                self.info[line[0]] = self.try_all_type_cast(line)

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
                    if len(value) > 1:
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
                self.animation_preferences[key] = self._type_cast(value)


            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/animation-order.txt', 'w') as pref_file:
                for key, value in self.animation_preferences.items():
                    if type(value) == tuple:
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
        print(key + ' ' + str(value))
        try:
            # Change locally
            if value is None:
                self.color_preferences.pop(key)
            else:
                self.color_preferences[key] = self.try_all_type_cast(value)

            # Update the file accordingly
            with open('/home/pi/LEDWebsite/preferences/custom-colors.txt', 'w') as pref_file:
                for key, value in self.color_preferences.items():
                    if type(value) == tuple:
                        pref_file.write(str(key) + ':')
                        for val in value:
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
                    if type(value) == tuple:
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
                    if type(value) == tuple:
                        pref_file.write(str(key) + ':')
                        for val in value:
                            pref_file.write(' ' + str(val))
                        pref_file.write('\n')
                    else:
                        pref_file.write(str(key) + ':' + str(value) + '\n')
        except KeyError:
            if self.get_debug_preferences('preferences-debug'):
                print('Parameters Debug: Error Updating Info Dictionary with ' + str(key))
