# CPU Temp Import
from gpiozero import CPUTemperature


# Globals
version = '1.0.1'

# Gets the list of all possible information values to see on the webpage
# Format: DisplayName, Value, VersionType, Parameters
# VersionType Parameters:
#   loadingBar:     minValue, maxValue, displayUnits
#   text:           none
def getInfo():
    params = []

    # Add Version Number
    params.append(['Version', version, 'text'])

    # Add CPU Temperature
    params.append(['CPU Temperature', getCPUTemp(), 'loadingBar', 0, 87, '°C'])

    return params


# Gets the Pi's CPU temp to send to the client
def getCPUTemp():
    cpu = CPUTemperature()
    return cpu.temperature