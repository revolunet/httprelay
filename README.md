# httprelay

Minimal python HTTP server with CORS support to control RaspberryPi GPIOs, for example to control relays.

 - `/gpio/7` : get pin 7 current status
 - `/gpio/7/output/0` : set pin 7 output to GPIO.LOW
 - `/gpio/7/output/1` : set pin 7 output to GPIO.HIGH

Sample test UI : http://jsbin.com/mahexo

## setup

 - clone the project
 - defines the GPIOs pins to control in server.py

## Autostart

 - add the sample `rc.local` to your `/etc/rc.local`
 - the sample `start.sh` script shows how to start the process in a [screen](https://www.gnu.org/software/screen) session
