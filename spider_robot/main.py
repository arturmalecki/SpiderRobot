VERSION = "0.0.1"
print("Starting SpiderRobot Version: " + VERSION)

import time
import sys
sys.path.append('./spider_robot/framework')

import power_led_and_button

    
def time_now_in_miliseconds():
  return int(round(time.time() * 1000))

class Main:
  def __init__(self):
    self.power_led_and_button = power_led_and_button.PowerLedAndButton()

    # States:
    # 0 - Non active
    # 1 - Activated
    self.state = 0

  
  def run(self):
    running = True

    previous_frame_time_starts_at = time_now_in_miliseconds()
    second = 0
    fps_count = 0
    frame_time_limit = int(1000 / 240)
    while running:
      fps_count+= 1
      frame_time_starts_at = time_now_in_miliseconds()
      elapsed_time = frame_time_starts_at - previous_frame_time_starts_at
      previous_frame_time_starts_at = frame_time_starts_at

      second += elapsed_time

      if second >= 60000:
        print("FPS:", fps_count/60, flush = True)
        second = 0
        fps_count = 0

      self._update()
      self._process()

      frame_time_ends_at = time_now_in_miliseconds()
      frame_time = frame_time_ends_at - frame_time_starts_at

      if frame_time < frame_time_limit:
        time_to_wait = (frame_time_limit - frame_time) / 1000
        time.sleep(time_to_wait)

  def _update(self):
    self.power_led_and_button.update()

    if self.state == 0:
      pass
    elif self.state == 1: 
      pass

    print("Update state: ", self.state, flush=True)

  def _process(self):
    self.power_led_and_button.process()

    if self.state == 0:
      if self.power_led_and_button.turn_on == True:
        self.state = 1
    elif self.state == 1: 
      if self.power_led_and_button.turn_on == False:
        self.state = 0

    print("Process state: ", self.state, flush=True)
  
  def __turn_off(self):
    print("Buy buy")
    sys.exit(0)

  
if __name__ == '__main__':
  Main().run()