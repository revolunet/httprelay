import RPi.GPIO as GPIO

from bottle import route, response, run, hook

#
# Minimal http server for GPIO control
#

# physical board pin number
GPIO.setmode(GPIO.BOARD)

GPIOS = [
  7,
  11,
  13,
  15,
  19,
  21,
  23,
  29,
  31,
  33,
  35,
  37,
  8,
  10,
  12,
  16,
  18,
  22,
  24,
  26,
  32,
  36,
  38,
  40
];

for pin in GPIOS:
  print "setup GPIO", pin
  GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def get_pin_value(pin):
  value = GPIO.input(pin)
  return {
    'pin'   : pin,
    'value' : value
  }

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

# ex:
# /gpio/4/output/0
# /gpio/4/output/1
@route('/gpio/<pin:int>/output/<value:int>', method='GET')
def gpio_write(pin, value):
    gpio_value = GPIO.LOW if (value == 0) else GPIO.HIGH
    print 'GPIO WRITE', pin, gpio_value
    GPIO.output(int(pin), gpio_value)
    return get_pin_value(int(pin))

@route('/gpio/<pin:int>', method='GET')
def gpio_read(pin):
    return get_pin_value(int(pin))


run(host = '0.0.0.0', port = '8080', debug = True, server='cherrypy')

GPIO.cleanup()