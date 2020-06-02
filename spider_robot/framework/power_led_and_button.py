try :
  import RPi.GPIO as GPIO
except ModuleNotFoundError:
  import mock_RPi.GPIO as GPIO

import time

class PowerLedAndButton:
  def __init__(self):
    self.led_pin = 11
    self.button_pin = 12
    self.prev_button_state = 0
    self.turn_on = False
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(self.led_pin, GPIO.OUT)
    GPIO.setup(self.button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.output(self.led_pin, GPIO.HIGH)

  def update(self):
    if GPIO.input(self.button_pin) == GPIO.LOW:
      self.prev_button_state = 1
    else:
      if self.prev_button_state == 1:
        if self.turn_on == False:
          self.turn_on = True
        else:
          self.turn_on = False
      self.prev_button_state = 0

  def process(self):
    if self.turn_on == False:
      GPIO.output(self.led_pin, GPIO.LOW)
    else:
      GPIO.output(self.led_pin, GPIO.HIGH)

  def __destroy(self):
    GPIO.output(self.led_pin, GPIO.LOW)
    GPIO.cleanup()