# CPU Temp Import
from gpiozero import CPUTemperature

# Read preferences from files
import preferences as preferences
preferences.read_preferences()

# Gets the list of all possible information values to see on the webpage
# Format: DisplayName, Value, DisplayType, Parameters
# DisplayType Parameters:
#   loadingBar:     minValue, maxValue, displayUnits
#   text:           none
def getInfo():
    params = []

    # Add CPU Temperature
    params.append(['CPU Temperature', get_CPU_temp(), 'loadingBar', 0, 87, '°C'])

    # Add preferences from Setup File
    for key, value in preferences.get_debug_preferences().items():
        params.append([key, value, 'text'])

    return params

# Gets the Pi's CPU temp to send to the client
def get_CPU_temp():
    cpu = CPUTemperature()
    return cpu.temperature
