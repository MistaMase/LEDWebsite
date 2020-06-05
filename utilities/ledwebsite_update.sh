#!/bin/bash
### BEGIN INIT INFO
# Provides:		ledwebsite_update
# Required-Start:	$remote_fs $syslog $network
# Required-Stop:	$remote_fs $syslog $network
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Starts the LED Controller update script at boot
# Description:		Starts the LED Controller update script at boot
### END INIT INFO

# Check if we have internet, and if so fetch the newest version of the repository

# Sending the output of the wget in a variable and not what wget fetches
RESULT=`wget --spider http://www.google.com 2>&1`

# Traverse the string considering it as an array of words
for x in $RESULT; do
    if [ "$x" = '200' ]; then
        # Download the possible new version to the update directory
        mkdir /home/pi/LEDWebsite/update/
        cd /home/pi/LEDWebsite/update/
        git clone https://github.com/MistaMase/LEDWebsite.git

        # Move the "new" files to the LEDWebsite directory
        rsync -r LEDWebsite/ /home/pi/LEDWebsite

        # Cleanup the download
        rm -r ../update

        # Correct the permissions
        cd /home/pi/LEDWebsite/
        sudo chown -R "${USER:-$(id -un)}" .

    fi
done
