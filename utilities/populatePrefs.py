import json
import os.path
from os import path

mandatory_parameters = {}

# Read from the mandatory_setup.json
with open('mandatory_setup.json', 'r') as file:
    mandatory_parameters = json.load(file)

for file in mandatory_parameters:
    print(str(file))
    print('/home/pi/LEDWebsite/preferences/' + str(file) + '.json')
    if path.exists('/home/pi/LEDWebsite/preferences/' + str(file) + '.json'):
        # Read the values in that file
        with open('/home/pi/LEDWebsite/preferences/' + str(file) + '.json', 'r') as pref_file:
            params = json.load(pref_file)

        # Brute force check if the file has the key
        for key in mandatory_parameters[file]:
            if mandatory_parameters[file][key] in params.keys():
                print(params[key])


   #for file in x:
   #     for value in x[file]:
   #         print(value)