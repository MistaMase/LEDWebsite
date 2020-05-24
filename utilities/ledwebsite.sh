#!/bin/bash
### BEGIN INIT INFO
# Provides:		ledwebsite
# Required-Start:	$remote_fs $syslog ledwebsite_update
# Required-Stop:	$remote_fs $syslog ledwebsite_update
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Starts the LED Controller at boot
# Description:		Starts the LED Controller at boot
### END INIT INFO

python3 home/pi/LEDWebsite/src/website.py

