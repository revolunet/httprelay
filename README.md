# httprelay

Gpio relays over http

 - `/gpio/7` : get pin 7 current status
 - `/gpio/7/output/0` : set pin 7 output to GPIO.LOW
 - `/gpio/7/output/1` : set pin 7 output to GPIO.HIGH

## setup

 - defines the GPIOs to control in server.py
 - add the sample rc.local to your /etc/rc.local