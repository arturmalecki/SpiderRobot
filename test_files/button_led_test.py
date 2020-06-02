import RPi.GPIO as GPIO
import time

led_pin  = 11
button_pin = 12

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(led_pin, GPIO.OUT)
  GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  GPIO.output(led_pin, GPIO.HIGH)

def loop():
  state = 0
  while True:
    if GPIO.input(button_pin) == GPIO.LOW:
      state = 1
    else:
      if state == 1:
        if GPIO.input(led_pin) == GPIO.LOW:
          GPIO.output(led_pin, GPIO.HIGH)
        else:
          GPIO.output(led_pin, GPIO.LOW)
          destroy()
          return True
      state = 0

def destroy():
  GPIO.output(led_pin, GPIO.LOW)
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()