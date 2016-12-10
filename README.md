# PiZeroBarcode

First, Install Jessie-lite. I used this tutorial:

https://learn.adafruit.com/introducing-the-raspberry-pi-zero/setting-up-your-sd-card

Thouth I used fedora-arm-installer-1.1.1-8.x32 not etcher, can't find the original tutorial.

Now, we need a way to communicate with our new board.  I used a FTDI cable (Console cable), following 

this tutorial:

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview

Next we need to get on the internet, so i followed this tutorial:

https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/overview

You can do the serial gadget part, but you really need the Ethernet Gadget part. Don't bother with 

assigning an IP address, using DHCP is fine. I didn't need to install Bonjour (don't know why) to get 

raspberrypi.local to work. Definalty do the "Sharing Network Access" part.  Sometimes when reconnecting 

the pi after it's been set up, it looks like it should be working, but a ping doesn't return good 

results.  I just Unshare the connection, and then re-share it.  Maybe with a reboot. That seems to fix 

it.

sudo apt-get update
sudo apt-get upgrade

you'll want to solder on a 40 pin male header to the PiZero before continuing if you havn't yet.

https://www.adafruit.com/products/3335
https://www.pi-supply.com/product/papirus-zero-epaper-screen-phat-pi-zero/
https://github.com/PiSupply/PaPiRus

Couldn't find a good tutorial, so I followed the github readme and documentation

curl -sSL https://goo.gl/i1Imel | sudo bash
sudo papirus-set 2.0

Should be ready, try:
papirus-write "Some text to write"
and
sudo wget "url to a 2 color image"
sudo papirus-draw [image name]

Ok, now I had some trouble getting the Image API to work in a python script.

sudo nano test.py

from papirus import PapirusImage

image = PapirusImage()

image.write('/home/pi/[image name]')

ctrl-x, y, enter

python test.py

would give me an error about EPD in a file called image.py
sudo nano [path to file]/image.py
add below imports:

from edp import EPD

try again:

python test.py

should work now!

Ok, not for the barcode maker:

first, we need to install the python package manager

https://www.raspberrypi.org/documentation/linux/software/python.md
sudo apt-get install python-pip

now install pyBarcode

https://pypi.python.org/pypi/pyBarcode/0.7
http://pythonhosted.org/pyBarcode/
https://bitbucket.org/whitie/python-barcode/

pip install pyBarcode

now test:
pybarcode2 create -t png "My Text" outfile
sudo papirus-draw outfile.png

now we need to do it in python:

sudo nano test.py

add to top: 

import barcode
from barcode.writer import ImageWriter

add to end:

ean = barcode.get('ean13', u'5901234123457', writer=ImageWriter())
filename = ean.save('ean_barcode', png, options={'dpi':111,'font_size':3})
image.write('/home/pi/ean_barcode.png')


ctrl-x, y, enter

Had issues getting vertical lines until realized that the imagewriter defaults to 300 dpi and the 

papirus is only 111 dpi

try it out:

python test.py

you should have the new scanable barcode on the pi.  try using a smartphone app to scan it
[insert name of app on both Android and Apple that would work!!!!!]

Ok, now to get the buttons working:

Test out the buttons first:

sudo papirus-buttons

After it says "Ready" press a few of the buttons to get the screen to change.  I noticed that one of 

the buttons doesn't do anything.

Stop it with:

ctrl-c 

Ok, now lets copy the code and use it ourselves:

cp /home/pi/PaPiRus/papirus/bin/papirus-buttons barcode-buttons.py

and now edit it to display barcodes instead of numbers:

sudo nano barcode-button.py

at the top, add:

replace the line:

write_text(papirus, "One", SIZE)

with:

image.write('/home/pi/ean_barcode.png')


>Check to see if this file needs more code
>Make it run on startup
>Make the buttons scroll through all available barcodes
>maybe put all barcode images in a new directory
>Add filename of barcode to image
>maybe instead of cp comand, just wget already made file
>get bluetooth to work
>figure out how to send barcode number and type from phone to pizero
>can i make this all easier?
>eventually integrate redboard
>eventually integrate power booster
>eventually integrate enclosure
>eventually figure out low power mode for pizero
