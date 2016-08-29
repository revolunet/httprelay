import RPi.GPIO as GPIO

from bottle import route, request, response, run, hook

#
# Minimal http server for GPIO control
#

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

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
    print 'GPIO WRITE: ', pin, gpio_value
    GPIO.output(int(pin), gpio_value)
    return get_pin_value(int(pin))

@route('/gpio/<pin:int>', method='GET')
def gpio_read(pin):
    return get_pin_value(int(pin))


run(host = '0.0.0.0', port = '8080', debug = True)

GPIO.cleanup()