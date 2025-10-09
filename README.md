# Project 2: Wall Bouncer

## Background
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. 
Despite the new technologies introduced to recent products, the "navigation" strategy of this robot can be fairly simple. 
Inspired by the Roomba, we are going to develop a robot that navigates/bounces in a closed cell. 
A human robot interface (HRI) from first project will be also integrated. 

## Requirements:

### 1. Assemble the Robot
Make sure every component is functional as expected.
Major required components are listed below:

| Name  | Qty. | Functionality
| ------------- | ------------- | ------------- |
| Mobile Base  | 1 | To host other physical components of the robot |
| 18650 Battery  | 2 | Power all the electrical and electronic components |
| Power Expansion Board | 1 | Converts 6~24V to 5V. Split input power. |
| Micro-GearMotor | 2 | Robot's actuator |
| Wheels | 2 | Attach to the motors and maneuver the robot |
| Ultrasonic Sensor | 1 | Sense distance to wall |
| Common Cathode LED  | 1 | Indicate robot's status |
| Tactile switch button  | 1 | Switch robot's working mode |

- (5%) Off-the-shelf rubber tires and wheels are banned (use 3D printed wheels and tires).

> [!TIP]
> Things you may want to check are listed but not limited below:
> - Have you double checked circuit and no short circuit anywhere?
> - Have you crimped connectors to motor wires?
> - Have you charged the batteries?
> - Are [Pico, LEDs and button](https://linzhanguca.github.io/_docs/robotics1-2025/0902/pico.pdf) functional?
> - Is [distance sensor](https://github.com/linzhangUCA/3421example-ultrasonic_sensor) functional?
> - Are [motor driver](https://github.com/linzhangUCA/3421example-motor_control) and motors controllable?
> - Are all the components fit into the bed? If not, print one from [here](https://github.com/linzhangUCA/3421example-robot_assembly/tree/main/prints).


### 2. (65%) Coding
- Program the Raspberry Pi Pico to: 
    - Encode robot's status into colors (`RED`, `GREEN`, `BLUE`) using LEDs .
    - Switch robot's behavior between `WORK MODE` and `PAUSE MODE` using a button.
    - **Read distance from ultrasonic sensor**.
    - **Send signals to motor driver board and move the robot according to the distance sensing**.
- Upload your script to this repository.
- Complete following tasks:
1. (3%) Initialization (System Check): blink all the LEDs at the same time if the button's GPIO pin is receiving correct default signal (`0` for `PULL_DOWN`, `1` for `PULL_UP`).
   - (2%) Blink all LEDs with frequency of 5 Hz, lasting 2 seconds.
   - (1%) The robot enters `PAUSE MODE` after this step.
2. (16%) When `PAUSE MODE` is activated:
   - (3%) `GREEN` LED fades in and fades out at frequency of 1 Hz (equally allocate fade-in and fade-out time).
   - (3%) Press the button to **immediately** switch to the `WORK MODE`.
   - (10%) Robot stop moving
3. (24%) When `WORK MODE` is activated:
   - (1%) `GREEN` LED stays constantly on.
   - (3%) Press the button to **immediately** switch to the **PAUSE MODE**.
   - (20%) Robot start moving without hitting the wall.
4. (20%) Low battery simulation.
   - (5%) If the accumulated `WORK MODE` time exceeds 45 seconds, substitute `GREEN` LED with **`BLUE`** LED for both modes (low-battery simulation).
   - (5%) If accumulated `WORK MODE` time over 55 seconds, blink `RED` LED at frequency of 10 Hz (`BLUE` and `GREEN` LED off).
   - (10%) If the accumulated `WORK MODE` time exceeds 45 seconds, Use 50% dutycycle of the original to be the robot's speed (Make sure the robot is still movable). 
5. (2%) Termination. Shutdown the system after the `RED` LED blinked 5 seconds.

> [!IMPORTANT]
> - It doesn't matter how your robot moves, but hitting a wall once during demonstration will cost 1% off your grade.
> - Plan a good strategy of wall avoidance.

> [!TIP]
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy tools.

### (35%) Documentation
Complete the following sections in this [README](/README.md) file, so that other people may use it as a guide to replicate this robot.

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
