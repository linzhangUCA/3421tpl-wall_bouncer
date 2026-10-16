# Project 2: Wall Bouncer
> [!IMPORTANT]
> # Due: Thursday, Nov. 5th @ 5 PM


## 1. Overview
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. 
Despite the new technologies introduced to recent products, the "navigation" strategy of this robot can be fairly simple. 
Inspired by the Roomba, we are going to develop a robot that navigates/bounces in a closed cell. 
The human robot interface (HRI) from first project will also be integrated. 


## 2. Get Started
Major components required to assemble the robot are listed below:

| Name  | Qty. | Functionality
| ------------- | ------------- | ------------- |
| Body frame  | 1 |  Hosts physical components of the robot.  |
| 18650 Li-ion Battery  | 2 | Power all the electrical components. |
| N20 Micro-GearMotor | 2 | Actuators. |
| Wheel | 2 | Move the robot around. |
| Power Expansion Board | 1 | Converts 6~24V to 5V. Split input power. |
| Solderless breadboard  | 1+ | Host electronics components |
| Raspberry Pi Pico (2) | 1 | Process input signals, make decisions and output commanding signals |
| TB6612FNG Motor Driver Board | 1 | Control motor speed |
| HC-SR04 Sensor | 1 | Sense distance via ultrasound |
| Common Cathode LED  | 1 | Indicate robot's status |
| Tactile switch button  | 1 | Switch robot's working mode. |

> [!TIP]
> Make sure every component is working by testing them.
> Things you may want to check are listed but not limited below:
> - Have you double checked circuit and no short circuit anywhere?
> - Have you crimped connectors to motor wires?
> - Have you charged the batteries?
> - Are [Pico, LEDs and button](https://linzhanguca.github.io/_docs/robotics1-2025/0902/pico.pdf) functional?
> - Is [distance sensor](https://github.com/linzhangUCA/3421example-ultrasonic_sensor) functional?
> - Are [motor driver](https://github.com/linzhangUCA/3421example-motor_control) and motors controllable?
> - Are all the components fit into the bed? If not, print one from [here](https://github.com/linzhangUCA/3421example-robot_assembly/tree/main/prints).


## 3. Requirements:
> [!IMPORTANT]
> Demonstrate your robot to Dr. Zhang to redeem your credits.

### 3.1. Mechanical Design
Please feel free to adapt to the [TBot](https://github.com/linzhangUCA/tbot_mechanical)'s mechanical design.
You are encouraged to bring in unique designs made by yourselves.
- (?%) Assemble your robot and upload a portrait picture (you pick the viewing angle) for your robot.
- (?%) Use a top view diagram to illustrate:
  - Width and length of the base body (exclude wheels).
  - Diameter of the wheel
  - Length of the driving axle.
  - Location of the driving wheels and the caster wheel.
- (+?% Bonus) Attach a distance scanner (made by the ultrasonic sensor and the MG90S servo) to the bed.
- (+?% Bonus) Design a unique case for the ultrasonic sensor attaching to the MG90S servo.
  Upload a tech draw of the case to illustrate key dimensions of it. 
> [!WARNING]
> Tape is not allowed for the distance scanner.

### 3.2. Electrical Design
Wire up all the electrical and electronics components.
- (?%) Deliver a wiring diagram to **ONLY** depict the power flowing around the circuit.
  Please label out the input voltage for different components.
- (?%) Deliver a Wiring diagram to **ONLY** illustrate the signal streams of the circuit.
  Please express the direction of the signals.
- (+?% Bonus) Include wiring (power and signal) for the MG90S servo.

### 3.3. (40%) Coding
Code Pico to drive the robot around in a rectangular cell without hitting the walls. 
- realize following functions:
    - Encode robot's status into LED colors (`RED`, `GREEN`, `BLUE`).
    - Switch robot's behavioral modes between `WORK` and `PAUSE` using a tactile button.
    - **Read distance from ultrasonic sensor**.
    - **Control differential drive mobile base's motion through the motor driver board**.
1. (?%) Initialization (System Check).
   - (?%) Blink all LEDs with frequency of 5 Hz, lasting 2 seconds if both conditions (below) are satisfied.
     **Do not start wall bouncing if any of the init conditions is not met**.
     - The button's GPIO pin is receiving correct default signal (`0` for `PULL_DOWN`, `1` for `PULL_UP`)
     - Ultrasonic sensor is receiving non-zero distance measuring.
   - (?%) The robot enters `PAUSE` mode after this step.
2. (?%) When `PAUSE` mode is activated:
   - (?%) Stop both motors.
   - (?%) `GREEN` LED fades in and fades out at frequency of 1 Hz (equally allocate fade-in and fade-out time).
   - (?%) Press the button, the robot switch to the `WORK` mode at the instant the button is **released**.
3. (?%) When `WORK` mode is activated:
   - (?%) `GREEN` LED stays on constantly.
   - (?%) Press the button to switch to the `PAUSE` mode at the instant the button is **released**.
   - (?%) Robot start wandering around without hitting the wall.
     - Drive straight forward (using **at least 50% of the maximum duty cycle**) if no wall was detected within 0.25 m distance.
     - Avoid hitting the wall within 0.25 m range by driving backward (half a second) then spinning in place in a random direction (half a second) with appropriate speed.
     - (+?% Bonus) 
4. (?%) Low battery simulation.
   - (?%) If the accumulated `WORK MODE` time exceeds 45 seconds, substitute `GREEN` LED with **`BLUE`** LED for both modes (low-battery simulation).
   - (?%) If accumulated `WORK MODE` time over 55 seconds, blink `RED` LED at frequency of 10 Hz (`BLUE` and `GREEN` LED off).
   - (?%) If the accumulated `WORK MODE` time exceeds 45 seconds, Use 50% dutycycle of the original to be the robot's speed (Make sure the robot is still movable). 
5. (?%) Termination.
   Despite the mode, stop the motors and put the Pico 2 board into [Deep Sleep](https://docs.micropython.org/en/v1.16/rp2/quickref.html#deep-sleep-mode) if `RED` LED blinked 5 seconds.

> [!IMPORTANT]
> - It doesn't matter how your robot moves, but hitting a wall once during demonstration will cost 1% off your grade.
> - Plan a good strategy of wall avoidance.

> [!TIP]
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy tools.

### 3.5. (?%) Documentation

#### 3.1. (15%) Mechanical Design: attach (multiple) technical drawings to illustrate dimensions and locations of the key components of the mobile base. 
- Denote dimensions of the bed.
- Denote dimensions and locations of the wheel assembly and the caster wheel.
- Denote locations of the mounting holes.
- Denote dimensions of the mounting holes.

> [!TIP]
> - You may want to checkout TechDraw of FreeCAD. Other CAD software should have the similar tools.  
> - Hand drawings are acceptable.

#### 3.2 (10%) Wiring Diagram: attach a drawing to illustrate electrical components' wiring.
- Specify power wires using red and black wires.
- Mark out employed signal pins' names.
- Electronic components' values have to match your actual circuit.

#### 3.3 (6%) Software Design
Use a [flowchart](https://en.wikipedia.org/wiki/Flowchart) or a [algorithm/pseudocode table](https://www.overleaf.com/learn/latex/Algorithms) or a [itemized list](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) to explain your wall avoidance strategy.

#### 3.4 (4%) Energy Efficient Path Planning 
> The goal is using this robot to cover a rectangle-shape area.
> Do your research, make reasonable assumptions and propose a path pattern for the robot to follow.
> Please state why this pattern is energy efficient.  
