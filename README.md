# Project - Wall Bouncing Robot
> Please add/modify required sections to complete this report.

This is the first project in Robotics 1 class. In this project, we will:
- Build a mobile robot with processors, actuators and sensors that are introduced in the class.
- Write Python code to realize the wall bouncing robot.
- Use a `.sh` file to automatically run a program after booting up the RaspberryPi.
- Complete a project report using this file (`README.md`).
- Upload a short video for demonstration.

## Requirment
1. Write Python code in `wall_bouncer.py`. 
### Material List
> Please list hardware (better with links) used in this project below.  


**Workflow:**

1. Light up LEDs one by one in order: RED for 1 second >> YELLOW for 2 seconds >> BLUE for 3 seconds >> GREEN for 4 seconds >> blink ALL in 2Hz for 2 seconds. Button operations shall not interrupt this procedure. (20%)
2. Slowly blink GREEN use PWM (2 seconds gradually on and 2 seconds gradually off). Press B1, GREEN stays on. Press B1 again, GREEN gets back to PWM blinking mode.
3. Count time consumption of GREEN stays on (GO). DO NOT count GREEN blink (GB) time.
4. If GO takes more than 10 seconds, light up YELLOW (other LED will remain their status). 
5. If GO takes more than 20 seconds, blink RED in 2 Hz for 10 seconds. Then, shutdown the system (pull down all involved GPIOs).
6. If press B1 and B2 together over 3 seconds, turn on BLUE and turn off all other LEDs.
