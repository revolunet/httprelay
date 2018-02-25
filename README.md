# httprelay

Minimal python HTTP server with CORS support to control RaspberryPi GPIOs, for example to control relays.

You can control up to 24 GPIO.

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

API returns:

```json
{
  "pin": 7,
  "value" : true
}
```


## Available GPIOs

Use the physical port to address the API

Physical port | GPIO#
:------------:|:-----:
  7           | 7
  8           | 15
  10          | 16
  11          | 0
  12          | 1
  13          | 2
  15          | 3
  16          | 4
  18          | 5
  19          | 12
  21          | 13
  22          | 6
  23          | 14
  24          | 10
  26          | 11
  29          | 21
  31          | 22
  32          | 26
  33          | 23
  35          | 24
  36          | 27
  37          | 25
  38          | 28
  40          | 29

## Autostart

 - add `/home/pi/httprelay/start.sh &` to your `/etc/rc.local`
 - the sample `start.sh` script shows how to start the process in a [screen](https://www.gnu.org/software/screen) session
