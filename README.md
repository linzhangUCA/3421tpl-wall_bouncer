# Project 2: Wall Bouncer

## Background
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. Despite the new technologies that are introduced to recent products, the navigation strategy of this robot can be fairly simple. In this project, we are going to turn our robots into Roomba replications. We will implement "FORWARD -> TURN" strategy to maneuver our robots in a closed space without running into the the walls.

You are expected to
- Indicate robot's status using LEDs.
- Change robot's working mode using a switch button.
- Move robot around without hitting the walls.

## Requirements:
- The robot has 2 modes: **WORK** and **PAUSE**. 
- Three LEDs (`GREEN`, `YELLOW`, `RED`) will be used to indicate the robot's status.
- A button will be used to switch modes bewteen **WORK** and **PAUSE**.
- A ultrasonic distance sensor will be used to detect walls.
- A motor driver board will be used to drive the DC motors.

### (70%) Programming
1. (10%) Check sensor's health: 
    - Check distance sensorsblink all the LEDs at the same time with frequency of 4 Hz, last 2 seconds. Then the robot enters **PAUSE** mode.
2. (20%) When in **PAUSE** mode: `GREEN` LED endlessly fades in and fades out with frequency of 1 Hz. Press and release the button to switch mode to **WORK**.
3. (20%) When in **WORK** mode: `GREEN` LED is constantly turned on. Press and release the button to switch mode to **PAUSE**.
4. (20%) When in **WORK** or **PAUSE** mode, press and hold the button for 3 seconds to enter **DEV** mode. When in **DEV** mode, `BLUE` LED is constantly turned on and other LED should be turned off. 
5. (15%) Time **WORK** mode. If the accumulated **WORK** time exceeds 15 seconds, turn on `YELLOW` LED (in **WORK** or **PAUSE** mode). If accumulated **WORK** time over 20 seconds, blink `RED` LED with frequency of 10 Hz for 2 seconds, then turn all the LEDs off and shutdown the system. 
> If `RED` is blinking, you cannot enter **DEV** mode.

### (15%) Documentation
Complete the following sections in this README. Please refer to [Github formatting guide](https://docs.github.com/en/get-started/writing-on-github) to get familiar with Markdown formatting.
1. (5%) Hardware Table: list the names, descriptions and quantities of physical components used in this project.
2. (5%) Wiring Diagram: attach a drawing to illustrate components wiring.
3. (5%) Summary: a few words to close this project.

## Hardware Table
> Name, Description, Quantity

## Wiring Diagram
> ![image name](link)

## Summary
> What has been done? What are learned? Any thoughts? Any discussions?
