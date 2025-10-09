# Project 2: Wall Bouncer

## Background
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. 
Despite the new technologies introduced to recent products, the "navigation" strategy of this robot can be fairly simple. 
Inspired by the Roomba, we are going to develop a robot that navigates/bounces in a closed cell. 
A human robot interface (HRI) from first project will be also integrated. 

## Requirements:
- Assemble the robot.
- Code the Raspberry Pi Pico.
- Document this project.
- Demonstrate to the class. **-0.1 points for each failed wall avoidance**

### 1. Assemble the Robot
Make sure every component is functional as expected. 
> ![TIP]
> Things you may want to check are listed but not limited below:
> - Have you double checked circuit and no short circuit anywhere?
> - Have you crimped connectors to motor wires?
> - Have you charged the batteries?
> - Are [Pico, LEDs and button](https://linzhanguca.github.io/_docs/robotics1-2025/0902/pico.pdf) functional?
> - Is [distance sensor](https://github.com/linzhangUCA/3421example-ultrasonic_sensor) functional?
> - Are [motor driver](https://github.com/linzhangUCA/3421example-motor_control) and motors controllable?
> - Are all the components fit into the bed? If not, print one from [here](https://github.com/linzhangUCA/3421example-robot_assembly/tree/main/prints).

- (5%) Off-the-shelf rubber tires and wheels are banned (use 3D printed wheels and tires).

### 2. (60%) Coding
- Program the Raspberry Pi Pico to: 
    - Encode robot's status into colors (`RED`, `GREEN`, `BLUE`) using LEDs .
    - Switch robot's behavior between `WORK MODE` and `PAUSE MODE` using a button.
- Upload your script to this repository.
- Complete following tasks:
1. Initialization (System Check): blink all the LEDs at the same time if the button's GPIO pin is receiving correct default signal (`0` for `PULL_DOWN`, `1` for `PULL_UP`).
   - (4%) Blink all LEDs with frequency of 5 Hz, lasting 2 seconds.
   - (1%) The robot enters `PAUSE MODE` after this step.
2. When `PAUSE MODE` is activated:
   - (10%) `GREEN` LED fades in and fades out at frequency of 1 Hz (equally allocate fade-in and fade-out time).
   - (10%) Press the button to **immediately** switch to the `WORK MODE`.
3. When `WORK MODE` is activated:
   - (4%) `GREEN` LED stays constantly on.
   - (6%) Press the button to **immediately** switch to the **PAUSE MODE**.
4. Time `WORK MODE`.
   - (15%) If the accumulated `WORK MODE` time exceeds 45 seconds, substitute `GREEN` LED with **`BLUE`** LED in both modes (low-battery simulation).
   - (5%) If accumulated `WORK MODE` time over 55 seconds, blink `RED` LED (`BLUE` LED keep working) at frequency of 10 Hz.
5. (10%) Termination. **Despite the mode**, trigger a [hard reset](https://docs.micropython.org/en/latest/wipy/tutorial/reset.html#reset-and-boot-modes) if:
   - `RED` LED blinked 5 seconds
   - button is **pressed and held** for 3 seconds. 

> [!IMPORTANT]
> - Mode switching is NOT a one-time function.
> - After 55 seconds of `WORK`, the `BLUE` LED and the `RED` LED are suppose to be functional together in both modes.

> [!TIP]
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy tools.
> - [global variables](https://realpython.com/python-use-global-variable-in-function/) are useful for interrup handling functions.

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
