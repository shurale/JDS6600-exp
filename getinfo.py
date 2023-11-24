#!/usr/bin/python3
# Import module
import jds6600

# Define arguments
import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
parser.add_argument('--port', help='TTY port', default='USB0')
args = parser.parse_args()

portstr='/dev/tty' + args.port
print("Use port",portstr)

# Create object with port for internal USB<->serial converter
j = jds6600.JDS6600(port=portstr)

# Connect to device
j.connect()

# Get channel info and print it
print("Channels status:",j.get_channels())

# Get waveform and print it
for i in [1, 2]:
    print("Channel:", i,", waveform:", j.get_waveform(channel=i),", frequency:", j.get_frequency(channel=i),
            "Hz, Amp:", j.get_amplitude(channel=i), "V, offset:", j.get_offset(channel=i),
            "V, duty cycle:",j.get_dutycycle(channel=i), "%")
