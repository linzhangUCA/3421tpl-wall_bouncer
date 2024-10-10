# Project 2: Wall Bouncer

## Background
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. Despite the new technologies that are introduced to recent products, the "navigation" strategy of this robot can be fairly simple. Inspired by the Roomba, we are going to develop a robot that bounces in a closed space with motors and a distance sensor. We are going to integrate the human machine interface (HMI) that has been developed in the [first project](https://classroom.github.com/a/jYniyPtg) into this roomba replica. 

## Requirements:
- Assemble the robot.
- Code the Raspberry Pi Pico.
- Document this project.
- Demonstrate to the class. **-0.1 points for each failed wall avoidance**

### (60%) Coding
> **Upload your Python script to this repository.** 

#### Main Objective
Move the robot in a walled cell for 1 minute without hitting the wall.

#### Reference Maneuver Strategy
You can use the "Forward And Turn" strategy as described below as your robot's maneuvering strategy. You can also propose your own strategy and realize it. 
  1. Move forward if the robot is "far" from a wall (distance to wall > 0.4 m).
  2. Turn to a different direction if the robot is about to hit a wall (distance to wall <= 0.4 m).
  3. Repeat i and ii.
     
#### Functionalities 
- (2%) Initialization: blink all the LEDs at the same time with frequency of 5 Hz, last 2 seconds. Then the robot enters **PAUSE MODE**.
- Mode switching: **WORK MODE** and **PAUSE MODE**.
  - When **PAUSE MODE** is activated:
    1. `GREEN` LED fades in and fades out at frequency of 1 Hz.
    2. Robot is stopped.
    3. Press the button to immediately switch to the **WORK MODE**.
  - When **WORK MODE** is activated:
    1. `GREEN` LED stays constantly on.
    2. Robot starts to move in the cell and avoid the wall.
    3. Press the button to switch back to the PAUSE MODE.
  - **PAUSE**: Robot stops moving. `GREEN` LED fade in and fade out at 1 Hz.
  - Switch the modes using a `button`.
    - Short clicks: back and forth between **WORK** and **PAUSE**.
    - Hold 3 seconds: into **DEV**.
- Besides mode indication LEDs (`GREEN` and `BLUE`), use `YELLOW` and `RED` LED to indicate **WORK** status
  - `YELLOW` turned on to indicate the robot has worked more than **45 seconds**.
  - `RED` blinks at 10 Hz to indicate the robot has worked more than **55 seconds**. **Robot speed should be reduced to 75% of original speed**.
  - Only time the **WORK** mode. **DO NOT light up `YELLOW` or `RED` no matter how long the robot is under PAUSE mode**.
- Shutdown the robot after 1 minute of accumulated work (stop the motors, turn off all the LEDs).
1. (30%) HMI
   - (10%) Mode switching (`GREEN`, `BLUE`, `button`, motors).
   - (15%) **WORK** status indication (`YELLOW`, `RED`, timer, motors).
   - (5%) Terminal state handling (**DEV**, 1-minute shutdown).
2. (10%) Robot moving strategy (how the robot moves). 
3. (30%) Robot wall bouncing strategy (how the robot handles the walls)

### (30%) Documentation
Complete the following sections in this [README](/README.md) file, so that other people may use it as a guide to replicate this robot.

1. (10%) Part List Table: list the names, descriptions and quantities of physical components used in this project.
2. (15%) Mechanical Layout Diagram: attach a drawing to illustrate how your robot is assembled.
3. (15%) Wiring Diagram: attach a drawing to illustrate components wiring.
4. (5%) Summary: describe technical details

#### Part List Table
> Please refer to the [table formatting guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)

| Name | Description | Quantity |
| :--- | :---        |  :---:   |
|      |             |          |
|      |             |          |

#### Mechanical Layout Diagram
> Please refer to the [image insertion guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images)

![layout](link)

#### Wiring Diagram
> Please refer to the [image insertion guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images)

![wiring](link)

#### TODO List
> Describe your robot's speed, distance detection threshold, turning strategy, etc.. Place as many technical details as possible in this section. You are welcome to use more tables and images.
