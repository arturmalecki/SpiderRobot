import time

from adafruit_servokit import ServoKit
from pprint import pprint
kit = ServoKit(channels=16)

LEG1 = 0
LEG2 = 180
LEG3 = 180

LEG11 = 180
LEG22 = 0
LEG33 = 0

# FRONT
# [FL][FR]
# --controler--
# --PI--
# [BL][BR]
# BACK

# Initail sequence
FRONT_LEFT_LEG_MOTOR_INDEXES = [0, 1, 2]
FRONT_RIGHT_LEG_MOTOR_INDEXES = [3, 4, 5]
BACK_LEFT_LEG_MOTOR_INDEXES = [6, 7, 8]
BACK_RIGHT_LEG_MOTOR_INDEXES = [9, 10, 11]

INIT_FRONT_LEFT_ANGLES = [180, 0, 0]
INIT_FRONT_RIGHT_ANGLES = [0, 180, 180]
INIT_BACK_LEFT_ANGLES = [180, 0, 180]
INIT_BACK_RIGHT_ANGLES = [0, 180, 0]

READY_FRONT_LEFT_ANGLES = [90, 90, 45]
READY_FRONT_RIGHT_ANGLES = [90, 90, 135]
READY_BACK_LEFT_ANGLES = [90, 90, 135]
READY_BACK_RIGHT_ANGLES = [90, 90, 45]

INIT = [
  [FRONT_LEFT_LEG_MOTOR_INDEXES, INIT_FRONT_LEFT_ANGLES],
  [FRONT_RIGHT_LEG_MOTOR_INDEXES, INIT_FRONT_RIGHT_ANGLES],
  [BACK_LEFT_LEG_MOTOR_INDEXES, INIT_BACK_LEFT_ANGLES],
  [BACK_RIGHT_LEG_MOTOR_INDEXES, INIT_BACK_RIGHT_ANGLES]
]

STAND = [
  [FRONT_LEFT_LEG_MOTOR_INDEXES, READY_FRONT_LEFT_ANGLES],
  [FRONT_RIGHT_LEG_MOTOR_INDEXES, READY_FRONT_RIGHT_ANGLES],
  [BACK_LEFT_LEG_MOTOR_INDEXES, READY_BACK_LEFT_ANGLES],
  [BACK_RIGHT_LEG_MOTOR_INDEXES, READY_BACK_RIGHT_ANGLES]
]

def init():
  for motor_indexes, motor_angles in INIT:
    for index, motor in enumerate(motor_indexes, start = 0):
      print('Motor: ' + str(motor) + ':' + str(motor_angles[index]))
      kit.servo[motor].angle = motor_angles[index]
  print('===========================')

def stand():
  for motor_indexes, motor_angles in STAND:
    for index, motor in enumerate(motor_indexes, start = 0):
      print('Motor: ' + str(motor) + ':' + str(motor_angles[index]))
      kit.servo[motor].angle = motor_angles[index]
  print('===========================')

print('Start')
# while(True):
# init()
# time.sleep(5)
stand()
# time.sleep(1)
# time.sleep(2)
# init()
print('Stop')

# kit.servo[1].angle = 170
# kit.servo[4].angle = 10
# kit.servo[7].angle = 170
# kit.servo[10].angle = 10
# x = 0;
# while(x < 10):
#   x += 1
#   kit.servo[0].angle = 0
#   kit.servo[3].angle = 180
#   kit.servo[6].angle = 0
#   kit.servo[9].angle = 180
#   time.sleep(0.1)
#   kit.servo[0].angle = 90
#   kit.servo[3].angle = 90
#   kit.servo[6].angle = 90
#   kit.servo[9].angle = 90
#   time.sleep(0.2)
stand()
