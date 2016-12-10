# startup file
# sudo nano /etc/rc.local
# add sudo python /home/pi/startup.py &

import os
from papirus import PapirusText

text = PapirusText()

# Write text to the screen
# text.write(text) 

text.write("Ronald's RPi0")

#ips = os.system("hostname -I")
#print str(ips)
#ip = str(ips).split(" ")[0]
#print(ip)
#text.write(ip)

