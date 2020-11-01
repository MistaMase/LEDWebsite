# CPU Temp Import
from gpiozero import CPUTemperature

# Inform the module of the globals
global preferences

class Hardware:
    def __init__(self):
        self.cpu = CPUTemperature()

    # Gets the list of all possible information values to see on the webpage
    # Format: DisplayName, Value, DisplayType, Parameters
    # DisplayType Parameters:
    #   loadingBar:     minValue, maxValue, displayUnits
    #   text:           none
    def get_info(self):
        params = []

        # Add CPU Temperature
        params.append(['CPU Temperature', self.get_CPU_temp(), 'loadingBar', 0, 87, '°C'])

        # Add preferences from Setup File
        for key, value in preferences.get_debug_preferences().items():
            params.append([key, value, 'text'])

        return params

    # Gets the Pi's CPU temp to send to the client
    def get_CPU_temp(self):
        return self.cpu.temperature
