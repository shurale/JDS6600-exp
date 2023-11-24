import jds6600
j = jds6600.JDS6600(port="/dev/ttyUSB0")
j.connect()
print(j.get_channels())
