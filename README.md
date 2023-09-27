# Project 2: Wall Bouncer

## Background
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. Despite the new technologies that are introduced to recent products, the "navigation" strategy of this robot can be fairly simple. Inspired by the Roomba, we are going to develop a robot that bounces in a closed space with motors and a distance sensor. We are going to integrate the human machine interface (HMI) that has been developed in the [first project](https://classroom.github.com/a/Ov8Qve2i) into this roomba replica. 

## Requirements:
- Move the robot in the walled cell for 1 minute without hitting the wall. The "Forward And Turn" policy as described below should be good enough. You can also propose your own control policy and realize it. 
  1. Move forward if the robot is "far" from a wall.
  2. Turn around if the robot is about to hit a wall.
  3. Repeat i and ii.
- The robot has 3 modes: **WORK**, **PAUSE** and **DEV**.
  - **WORK**: Robot carrys out wall-bouncing maneuvering. `GREEN` LED constantly on at full brightness.
  - **PAUSE**: Robot stops moving. `GREEN` LED fade in and fade out at 1 Hz.
  - **DEV**: `BLUE` LED on. Terminate all other tasks.
  - Switch the modes using a `button`.
    - Short clicks: back and forth between **WORK** and **PAUSE**.
    - Hold 3 seconds: into **DEV**.
- Besides mode indication LEDs (`GREEN` and `BLUE`), use `YELLOW` and `RED` LED to indicate **WORK** status
  - `YELLOW` turned on to indicate the robot has worked more than **45 seconds**.
  - `RED` blinks at 10 Hz to indicate the robot has worked more than **55 seconds**. **Robot speed should be reduced to 75% of original speed**.
  - Only time the **WORK** mode. **DO NOT light up `YELLOW` or `RED` no matter how long the robot is under PAUSE mode**.
- Shutdown the robot after 1 minute of accumulated work (stop the motors, turn off all the LEDs).
- Upload a python script that takes care of above robot behaviors. 
- Complete the **Documentation** section in this README file. A newcomer is supposed to use this document to replicate your project.


### (70%) Coding
1. (30%) HMI
   - (10%) Mode switching (`GREEN`, `BLUE`, `button`, motors).
   - (15%) **WORK** status indication (`YELLOW`, `RED`, timer, motors).
   - (5%) Terminal state handling (**DEV**, 1-minute shutdown).
2. (10%) Robot moving strategy (how the robot moves). 
3. (30%) Robot wall bouncing strategy (how the robot handling walls)

### (30%) Documentation
1. (10%) Part List Table: list the names, descriptions and quantities of physical components used in this project.
2. (15%) Wiring Diagram: attach a drawing to illustrate components wiring.
3. (5%) Summary: describe technical details

## Part List Table
| Name | Description | Quantity |
| :--- | :---        |  :---:   |
|      |             |          |
|      |             |          |

## Wiring Diagram
> ![image name](link)

## Summary
> Describe your robot's speed, distance detection threshold, turning strategy, etc.. Place as many technical details as possible in this section. You are welcome to use more tables and images.
