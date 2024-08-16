#---------------------------------------------------------
# Program NAG4.py by Joel Gray, N9LQ  8/13/2024
 
# This program listens to the UDP broadcasts from N1MM, parses the radio
# number and antenna number, and sends it via TCP to the Antenna Genius
# antenna switch.

# This version is designed to work with the new API for the Antenna Genius
# version 4.

# It requires you to configure the antennas in N1MM to reflect the antennas
# you wish to toggle between.  The setup in the Antenna Genius application
# needs to allow the choices that N1MM is making.  The AG can also allow other
# choices which can be accessed from the AG aplication.

# It also reqires the Antenna Genius Windows application to be running.

# To switch antennas from within N1MM, use Alt-F9.

# Maintain the IP address of your antenna switch in the file titled "NAG.TXT"
# You can find the IP address by looking in "Device Information" in the
# Antenna Genius app under the Network Information section.

# This has only been tested on a local network.
# This has only been tested under Python 3.9.7

#-----------------------------------------------------------
