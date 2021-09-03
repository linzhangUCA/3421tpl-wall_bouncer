# Project - Wall Bouncing Robot

This is the first project in Robotics 1 class. In this project, we will make a Roomba-like robot. The robot is expected to maneuver in a closed room without hitting the walls. The outcomes of this project are expected as follows:
- Build a mobile robot with processors, actuators and sensors that are introduced in the class.
- Write Python code to realize the wall bouncing robot (Feel free to write your code from scratch or start from [`wall_bouncer.py`](https://github.com/linzhangUCA/project_template-wall_bouncer/blob/main/wall_bouncer.py)).
- Figure out a way to automatically launch the robot after booting up the RaspberryPi. Briefly describe your automatic startup approach or upload the script you used.  
- Complete a project report using this file (`README.md`).
- Upload a video for demonstration (Unfortunately, you may need to compress your video before uploading).

## Workflow
3 LEDs (GREEN, YELLOW, RED), 1 button, (at least) 1 ultrasonic distance sensor and 2 motor drivers are needed. [gpiozero](https://gpiozero.readthedocs.io/en/stable/) library is highly recommended for your coding.
1. Enable the motors. Confirm the motors are enabled (check GPIO pins voltage level). 
2. Robot entering **Pausing** mode. Set the GREEN LED to be a dimmer (PWM). Make sure robot's motion is stopped in this mode.
3. Press the button to enable the **Playing** mode. Robot should be able to move forward. Light up GREEN LED and keep the brightness a constant. Use the distance sensor (Feel free to use more than one) to monitor walls in front of the robot. Turn the robot away from the approaching wall within a certain distance.
4. Press the button again will be able to switch the mode back to **Pausing**. Pressing the button later on can switch the mode back and forth. 

Record time consumption in **Playing** mode, once over 60 seconds, light up YELLOW LED. If over 90 seconds, turn off the robot and blink (turn on then turn off) the RED LED 10 times, then shut down the whole system.

## Summary
> Write below to complete this report. You may want to read the [Markdown guide](https://guides.github.com/features/mastering-markdown/) to better format this report.

### Material List
> Please list hardware (better with links) used in this project below.  

### Software List
> Please list and briefly describe the Python libraries and any software used to realize the robot.

### Usage
> Briefly describe how to use this robot. Imagine you are teaching a person how to use your robot.


