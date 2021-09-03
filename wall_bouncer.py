"""

"""

#### Write your code below ####
import time
from gpiozero import LED, PWMLED, Button, DistanceSensor, PhaseEnableRobot

# Instantiate pins, LEDs, button, distance sensor and the robot

# Initiate variables such as mode, duty cycles, run time

# Enable the motors and confirm it.

# Main
while True:
  # if button pressed, switch mode
  
  # if in Playing mode:
    # light up GREEN
    # robot move forward
    # if distance < d:
      # turn away
    # update run_time
    # if run_time >= 60:
      # light up YELLOW
    # if run_time >= 90:
      # blink RED
      # break
    # time.sleep(.02)
    
  # elif in Pausing mode:
    # change GREEN's duty cycle
    # robot stop
    # time.sleep(.02)
    
      
