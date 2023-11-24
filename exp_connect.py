#!/usr/bin/python3
# Import module
import jds6600

# Create object with port for internal USB<->serial converter
j = jds6600.JDS6600(port="/dev/ttyUSB0")

# Connect to device
j.connect()

# Get channel info and print it
print("Channels status:",j.get_channels())
