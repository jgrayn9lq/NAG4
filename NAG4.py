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
# This has only tested under Python 3.9.7

#-----------------------------------------------------------

import socket

# N1NN UDP broadcasts data on port 12066 
UDP_IP = "127.0.0.1"
UDP_PORT = 12066

# Read file with Antenna Genius IP address
myfile = open("NAG.txt","r")
AG_address=myfile.readline()
AG_address=AG_address[:-1]
myfile.close()

# Antenna Genius TCP communicates on port 9007
TCP_IP = AG_address
TCP_PORT = 9007

#Open UDP socket to N1MM
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

#Open TCP socket to Antenna Genius
sss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sss.connect((TCP_IP, TCP_PORT))

rad_1_ant='0'
rad_2_ant='0'
myflag='0'
seq_num=1

while True:

# Get the N1MM broadcast information   
    data, addr = sock.recvfrom(1024)
    print("received data:",data)
    
     
# Parse the UDP data to find the Radio # and the Antenna #
    y=data.decode("utf-8")
    z=y.find('<RadioNr>')
    z=z+9
    radio_nr=(y[z])
    x=y.find('<Antenna>')
    x=x+9
    antenna_nr=(y[x])
#    radio_nr=radio_nr
#    antenna_nr=antenna_nr

# To reduce TCP trafic, only send the information if it has changed    
    flag='0'
    if((radio_nr=='1') and (rad_1_ant!=antenna_nr)):
        rad_1_ant=antenna_nr
        flag='1'
    if((radio_nr=='2') and (rad_2_ant!=antenna_nr)):
        rad_2_ant=antenna_nr
        flag='1'
    if(flag=='1') :
        seqnum=ascii(seq_num)
        qqq='C'+seqnum+'|'+'port set '+radio_nr+' rxant='+antenna_nr+'\n'
        ttt=qqq.encode('utf-8')
        print(ttt)
        seq_num=seq_num+1
        if seq_num>250:
            seq_num=1
#       Send the information to the Antenna Genius   
        try:
            sss.send(ttt)
            tcpdata = sss.recv(1024)
        except:
            pass 
    print("received data:",tcpdata)
    

      
    
    

        

    
    
    
