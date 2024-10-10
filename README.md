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
- (5%) Initialization: blink all the LEDs at the same time with frequency of 5 Hz, last 2 seconds. Then the robot enters **PAUSE MODE**.
- Mode switching: **WORK MODE** and **PAUSE MODE**.
  - (15%) When **PAUSE MODE** is activated:
    1. `GREEN` LED fades in and fades out at frequency of 1 Hz.
    2. Robot is stopped.
    3. Press the button to immediately switch to the **WORK MODE**.
  - (15%) When **WORK MODE** is activated:
    1. `GREEN` LED stays constantly on.
    2. Robot starts to move in the cell and avoid the wall.
    3. Press the button to switch back to the **PAUSE MODE**.
- (15%) Low Battery Simulation.
  - If accumulated **WORK MODE** time exceeds 60 seconds, turn on `YELLOW` LED.
  - If accumulated **WORK MODE** time over 75 seconds, blink RED LED at frequency of 10 Hz. Slow down motor with 75% original duty cycle.
  - > **DO NOT** reset **WORK MODE** timer when switching the mode.
- (10%) Termination
  - Terminate everything (include motors) if `RED` LED blinked 15 seconds
  - Press and hold the button for 3 seconds to terminate (in both **WORK MODE** and **PAUSE MODE**).
    
### (40%) Documentation
Complete the following sections in this [README](/README.md) file, so that other people may use it as a guide to replicate this robot.

1. (5%) Part List Table
   - List the names of all the physical components used for this project.
   - Describe the **functionalities or key specifications** of the corresponding components
   - Specify quantities of the components used.
2. (20%) Mechanical Layout Diagram
   - Illustrate shapes of key components (It is OKAY to use rectangles for circuit boards).
   - Mark dimensions of key components.
   - Specify locations and orientations of key components. 
   - > Remember, people are supposed to follow this layout to assemble an identical robot.
   - > You may need to use 2 illustrations (a top-view and a side-view).
4. (10%) Wiring Diagram: attach a drawing to illustrate components wiring.
5. (5%) TODO List: Describe unmet goals and possible solutions in the future.

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
