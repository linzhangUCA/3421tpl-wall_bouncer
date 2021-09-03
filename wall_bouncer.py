"""
1. Enable the motors. Confirm the motors are enabled (check GPIO pins voltage level). 
2. Robot entering **Pausing** mode. Set the GREEN LED to be a dimmer (PWM). Make sure robot's motion is stopped in this mode.
3. Press the button to enable the **Playing** mode. Robot should be able to move forward. Light up GREEN LED and keep the brightness a constant. Use the distance sensor (Feel free to use more than one) to monitor walls in front of the robot. Turn the robot away from the approaching wall within a certain distance.
4. Press the button again will be able to switch the mode back to **Pausing**. Pressing the button later on can switch the mode back and forth. 

Record time consumption in **Playing** mode, once over 60 seconds, light up YELLOW LED. If over 90 seconds, blink (turn on then turn off) the RED LED 10 times, then shut down.
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
    
      
