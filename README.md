# httprelay

Minimal python HTTP server with CORS support to control RaspberryPi GPIOs, for example to control relays.

## setup

 - [download](https://github.com/revolunet/httprelay/archive/master.zip) the project
 - run `pip install -r requirements.txt`
 - defines the GPIOs pins to control in server.py

Run with `python server.py`

## HTTP API

 - `/gpio/7` : get pin 7 current status
 - `/gpio/7/output/0` : set pin 7 output to GPIO.LOW
 - `/gpio/7/output/1` : set pin 7 output to GPIO.HIGH

Sample test UI : http://jsbin.com/mahexo

## Autostart

 - add `/home/pi/httprelay/start.sh &` to your `/etc/rc.local`
 - the sample `start.sh` script shows how to start the process in a [screen](https://www.gnu.org/software/screen) session
