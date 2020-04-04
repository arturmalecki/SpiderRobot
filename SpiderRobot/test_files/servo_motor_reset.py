import RPi.GPIO as GPIO
import time
OFFSE_DUTY = 0.5
SERVO_MIN_DUTY = 2.5 + OFFSE_DUTY # Min position
SERVO_MAX_DUTY = 12.5 + OFFSE_DUTY # Max position
servoPin = 12

def setup():
  global p
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(servoPin, GPIO.OUT)
  GPIO.output(servoPin, GPIO.LOW)

  p = GPIO.PWM(servoPin, 50)
  p.start(0)

def loop():
  while True:
    for dc in range(180, -1, -1):
      print(dc)
      servoWrite(dc)
      time.sleep(0.001)

    time.sleep(1)
    for dc in range(0, 181, 1):
      print(dc)
      servoWrite(dc)
      time.sleep(0.001)
  time.sleep(0.5)

def servoWrite(angle):
  if(angle < 0):
    angle = 0
  elif(angle > 180):
    angle = 180
  p.ChangeDutyCycle(map(angle))

def map(value):
  # Mapping angle (1-180) to servo motor range
  return ((((SERVO_MAX_DUTY-SERVO_MIN_DUTY) * value) / 180) + SERVO_MIN_DUTY)

def destroy():
  p.stop()
  GPIO.cleanup()

if __name__ == '__main__':
  print('Program is starting...')
  setup()
  try:
    loop()
    destroy()
  except KeyboardInterrupt:
    destroy()