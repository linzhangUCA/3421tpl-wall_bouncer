# Project - Wall Bouncing Robot

This is the first project in Robotics 1 class. In this project, we will:
- Build a mobile robot with processors, actuators and sensors that are introduced in the class.
- Write Python code to realize the wall bouncing robot.
- Use a `.sh` file to automatically run a program after booting up the RaspberryPi.
- Complete a project report using this file (`README.md`).
- Upload a short video for demonstration.

## Workflow
1. Enable the motors. Confirm the motors are enabled (check GPIO pins voltage level). 
2. Robot entering **Pausing** mode. Set the GREEN LED to be a dimmer (PWM). Make sure robot's motion is stopped in this mode.
3. Press the button to enable the **Playing** mode. Robot should be able to move forward. Light up GREEN LED and keep the brightness a constant. Use the distance sensor (Feel free to use more than one) to monitor walls in front of the robot. Turn the robot away from the approaching wall within a certain distance.
4. Press the button again will be able to switch the mode back to **Pausing**. Pressing the button later on can switch the mode back and forth. 

Record time consumption in **Playing** mode, once over 60 seconds, light up YELLOW LED. If over 90 seconds, blink (turn on then turn off) the RED LED 10 times, then shut down.

## Summary
> Write below to complete this report. You may want to read the [Markdown guide](https://guides.github.com/features/mastering-markdown/) to better format this report.

### Material List
> Please list hardware (better with links) used in this project below.  

### Software List
> Please list and briefly describe the Python libraries used and files added/modified in this repository.

### Usage
> Briefly describe how to use this robot. Assuming you are going to hand over your robot to another student who is not in this class.


