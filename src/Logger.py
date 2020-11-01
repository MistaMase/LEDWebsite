
# Inform the module of the globals
global preferences


class Logger:
    def __init__(self):
        pass

    def log(self, source, message):
        """ Logs the event if the specific debug variable is True
            Logs in the format {Source}: {Message}

        :param source: The class/segment the message originated from
        :param message: The message to log
        :return: The formatted message
        """
        log_level = 'Unknown'
        if source == 'Website':
            log_level = 'website-debug'
        elif source == 'Flask':
            log_level = 'flask-debug'
        elif source == 'Scenes':
            log_level = 'scenes-debug'
        elif source == 'Preferences':
            log_level = 'preferences-debug'

        # Check if we have a debugging parameter for the given key
        if self.preferences.get_debug_preferences(source) is not None:
            message = f'{source}: {message}'
            print(message, flush=True)
            return message
