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
    - Check distance sensor's health.
    - Blink `GREEN` LED at frequency of 4 Hz for 2 seconds to indicate the distance sensor is working correctly. 
    - Robot enters **PAUSE** mode if passed self-check.
2. (5%) **PAUSE** mode: 
    - `GREEN` LED endlessly fades in and fades out with frequency of 1 Hz. 
    - Robot stops.
    - Press and release the button to switch mode to **WORK**.
3. (30%) **WORK** mode: 
    - `GREEN` LED is constantly turned on. 
    - Robot moves forward, turn a certain angle before getting too close to a wall. 
    - Press and release the button to switch mode to **PAUSE**.
4. (25%) Time **WORK** mode:
    - If the accumulated **WORK** time exceeds 30 seconds, turn on `YELLOW` LED to indicate "low battery". Set robot speed to 75% as in **WORK** mode. 
    - If accumulated **WORK** time over 40 seconds, turn off `YELLOW` LED. Blink `RED` LED at frequency of 10 Hz for 2 seconds to indicate "out of energy".
    - After `RED` LED blinks over, turn all the LEDs off, stop the robot and shutdown the system. 

### (30%) Documentation
1. (5%) Part List Table: list the names, descriptions and quantities of physical components used in this project.
2. (10%) Wiring Diagram: attach a drawing to illustrate components wiring.
3. (15%) Summary: describe technical details

## Part List Table
> Name, Description, Quantity

## Wiring Diagram
> ![image name](link)

## Summary
> Describe your robot's speed, distance detection threshold, turning strategy, etc.. Place as many technical details as possible in this section.
