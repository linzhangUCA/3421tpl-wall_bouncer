# Project 2: Wall Bouncer
> [!IMPORTANT]
> # Due: Thursday, Nov. 5th @ 5 PM


## 1. Overview
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. 
Despite the new technologies introduced to recent products, the "navigation" strategy of this robot can be fairly simple.
By travelling in straight lines and turning into different directions, Roomba is able to cover the cleaning job in a descent sized room.  
Inspired by the Roomba, we are going to let our robot exploring a closed cell with the help of a distance sensor and a bouncy navigation strategy. 


## 2. Get Started
Major components required to assemble the robot are listed below:

| Name  | Qty. | Functionality
| ------------- | ------------- | ------------- |
| Body frame  | 1 |  Hosts physical components of the robot.  |
| 18650 Li-ion Battery  | 2 | Power source. |
| N20 Micro-GearMotor | 2 | Actuators for wheels. |
| Wheel | 2 | Move the robot around. |
| Power Expansion Board | 1 | Converts 6~24V to 5V. Split input power. |
| Solderless breadboard  | 1+ | Hosts electronics components |
| Raspberry Pi Pico (2) | 1 | Processes input signals, make decisions and output commanding signals |
| TB6612FNG Motor Driver Board | 1 | Manipulates speed and direction of up to 2 motors |
| HC-SR04 Sensor | 1 | Sense distance via ultrasound |
| Common Cathode RGB LED  | 1 | Indicate robot's status |
| Resistors  | ? | limit current and/or divide voltage  |
| Tactile switch button  | 1 | Switch robot's working mode. |
| MG90S servo  | 1 | Sweep the ultrasound scanner. |

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
> [!CAUTION]
> - Live demo is required to redeem the credits for coding.
> - Hitting a wall once during demonstration will cost 1% off your grade.

### 3.1. (15%) Mechanical Design
Please feel free to adapt to the [TBot](https://github.com/linzhangUCA/tbot_mechanical)'s mechanical design.
You are encouraged to bring in unique designs made by yourselves.
- (?%) Assemble your robot and upload a portrait picture (you pick the viewing angle) for your robot.
- (?%) Use a top-view drawing to illustrate:
  - Width and length of the base body (exclude wheels).
  - Diameter of the wheel
  - Length of the driving axle.
  - Location of the driving wheels and the caster wheel.
- (+?% Bonus) Attach a distance scanner (made by the ultrasonic sensor and the MG90S servo) to the bed.
- (+?% Bonus) Design a unique case for the ultrasonic sensor attaching to the MG90S servo.
  Upload a tech draw of the case to illustrate key dimensions of it. 
- (+?% Bonus) Other mechanical designs different from the [TBot](https://github.com/linzhangUCA/tbot_mechanical).
> [!WARNING]
> Temporary solutions, such as tape and glue, are not allowed for mounting the distance scanner.

### 3.2. (20%) Electrical Design
Wire up all the electrical and electronics components.
- (?%) Upload a wiring diagram to **ONLY** depict the **power** flowing around the circuit.
  Please label out the input voltage for different components.
- (?%) Upload a Wiring diagram to **ONLY** illustrate the **signal** streams of the circuit.
  Please express the direction of the signals.
- (+?% Bonus) Include wiring (power and signal) for the MG90S servo.

### 3.3. (45%) Coding
Code Pico to drive the robot around in a rectangular cell without hitting the walls. 
realize following functions:
1. (?%) Initialization (System Check).
   - (?%) Blink all LEDs with frequency of 5 Hz, lasting 2 seconds if both conditions (below) are satisfied.
     **Do not start wall bouncing if any of the init conditions is not met**.
     - The button's GPIO pin is receiving correct default signal (`0` for `PULL_DOWN`, `1` for `PULL_UP`)
     - Ultrasonic sensor is receiving non-zero distance measuring.
   - (?%) The robot enters `PAUSE` mode after this step.
   - (+?% Bonus) Center the distance sensor (facing straightly forward).
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
     - (+?% Bonus) Let the robot's heading direction be the reference $0^{\circ}$.
       Under the forward traverse phase, use the servo-driven distance sensor to scan distance from $-60^{\circ}$ to $60^{\circ}$ then from $60^{\circ}$ to $-60^{\circ}$ in a period of 600 ms.
     - (+?% Bonus) If the wall is detected (0.25 m away from any angle), perform the wall avoidance maneuver by:
       1. Centering the distance sensor.
       2. Backing up while turning away from the wall.
          Please turn the robot based on the servo angle when the (0.25 m) wall was detected (CCW for positive angle, CW for negative angle).
       3. Resume forward traverse. 
4. (?%) Low battery simulation.
   - (?%) If the accumulated `WORK` time exceeds 40 seconds (low-battery simulation):
     - substitute `GREEN` light with **`YELLOW`** light for both modes.
     - Reduce the robot's speed to original's 50% in terms of dutycycle (Make sure the robot is still movable).
   - (?%) If accumulated `WORK` time over 50 seconds, blink `RED` LED (no other light) at frequency of 10 Hz.
5. (?%) Termination.
   Despite the mode, stop the motors and put the Pico 2 board into [Deep Sleep](https://docs.micropython.org/en/v1.16/rp2/quickref.html#deep-sleep-mode) if `RED` LED blinked 10 seconds.

> [!TIP]
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy debugging tools.

### 3.5. (20%) Documentation
> [!CAUTION]
> Use [README](README.md) for documentaion.

#### 3.5.1. (6%) Illustrate mechanical designs
- Display the portrait of your robot with resolution of 800 px. by 600 px..
- Display the dimension drawing with resolution of 1200 px. by 900 px..

#### 3.5.2. (9%) Wiring diagrams
- Display the wiring diagram of the **power streams** with a resolution of 800 px. by 600 px..
- Display the wiring diagram of the **signal streams** with a resolution of 800 px. by 600 px..

#### 3.5.3. (4%) Algorithm
Use a [flowchart](https://en.wikipedia.org/wiki/Flowchart) or a [algorithm/pseudocode table](https://www.overleaf.com/learn/latex/Algorithms) or a [itemized list](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) to explain your robot's navigation strategy.

#### 3.5.4. (1%) Acknowledge AI's contributions 
Please list out all the AI's contributions to this project.

