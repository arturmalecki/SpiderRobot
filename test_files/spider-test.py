import time

from adafruit_servokit import ServoKit
from pprint import pprint
kit = ServoKit(channels=16)

# FRONT
# [FL][FR]
# --controler--
# --PI--
# [BL][BR]
# BACK

# Initail sequence
FRONT_LEFT_LEG_MOTOR_INDEXES = [0, 1, 2]
FRONT_RIGHT_LEG_MOTOR_INDEXES = [4, 5, 6]
BACK_LEFT_LEG_MOTOR_INDEXES = [8, 9, 10]
BACK_RIGHT_LEG_MOTOR_INDEXES = [12, 13, 14]

INIT_FRONT_LEFT_ANGLES = [0, 0, 180]
INIT_FRONT_RIGHT_ANGLES = [180, 180, 0]
INIT_BACK_LEFT_ANGLES = [180, 0, 180]
INIT_BACK_RIGHT_ANGLES = [0, 180, 0]

READY_FRONT_LEFT_ANGLES = [45, 90, 90]
READY_FRONT_RIGHT_ANGLES = [145, 90, 90]
READY_BACK_LEFT_ANGLES = [135, 90, 90]
READY_BACK_RIGHT_ANGLES = [45, 90, 90]

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
# stand()
# time.sleep(1)
# kit.servo[4].angle = 180
# kit.servo[5].angle = 140
# kit.servo[6].angle = 120
# time.sleep(0.1)
# kit.servo[8].angle = 45
# kit.servo[9].angle = 40
# kit.servo[10].angle = 60
# time.sleep(0.5)
# kit.servo[1].angle = 180



n = 0
kit.servo[0].angle = 0
kit.servo[1].angle = 180
kit.servo[2].angle = 180

kit.servo[4].angle = 180
kit.servo[5].angle = 0
kit.servo[6].angle = 0

kit.servo[8].angle = 180
kit.servo[9].angle = 180
kit.servo[10].angle = 180

kit.servo[12].angle = 0
kit.servo[13].angle = 0
kit.servo[14].angle = 0
# kit.servo[5].angle = 0
# kit.servo[6].angle = 0
# while(n < 180):
#   time.sleep(0.01)
#   kit.servo[6].angle = n
#   print(n)
#   n += 1
# print('Stop')

# kit.servo[0].angle = 0
# kit.servo[1].angle = 90
# kit.servo[4].angle = 180
# kit.servo[5].angle = 90
# while(True):
#   n = 0
#   y = 180
#   while(n < 180):
#     time.sleep(0.01)
#     kit.servo[2].angle = n
#     kit.servo[6].angle = n
#     print(n)
#     n += 1
#     y -= 1
#   kit.servo[1].angle = 90
#   kit.servo[2].angle = 0
#   kit.servo[4].angle = 180
#   kit.servo[5].angle = 180

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
# stand()
