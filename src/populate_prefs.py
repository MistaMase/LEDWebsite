import json
import os.path
from os import path

def cleanup_prefs():
    # Read from the mandatory_setup.json
    with open('mandatory_setup.json', 'r') as file:
        mandatory_parameters = json.load(file)

    for file in mandatory_parameters:
        params = {}
        if path.exists('/home/pi/LEDWebsite/preferences/' + str(file) + '.json'):
            # Read the values in that file
            with open('/home/pi/LEDWebsite/preferences/' + str(file) + '.json', 'r') as pref_file:
                params = json.load(pref_file)

        # Brute force check if the file has the mandatory key, and if not add it to the dictionary
        for key in mandatory_parameters[file]:
            print(key)
            if not key in params.keys():
                params[key] = mandatory_parameters[file][key]

        print(params)

        # Write the parameters back to the file
        with open('/home/pi/LEDWebsite/preferences/' + str(file) + '.json', 'w') as write_file:
            json.dump(params, write_file)
