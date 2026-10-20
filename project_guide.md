# Project 2: Wall Bouncer
> [!IMPORTANT]
> # Due: Thursday, Nov. 5th @ 5 PM


## 1. Overview
[Roomba](https://www.irobot.com/en_US/roomba.html) is a very popular housekeeping robot. 
Despite the new technologies introduced to recent products, the "navigation" strategy of this robot can be fairly simple.
By travelling in straight lines and turning into different directions, Roomba is able to cover the cleaning job in a descent sized room.  
Inspired by the Roomba, we are going to let our robots exploring a closed cell with the help of a distance sensor and a bouncy navigation strategy. 


## 2. Get Started
Major components required to assemble the robot are listed but not limited to the items in the list below:

| Name  | Qty. | Functionality
| ------------- | ------------- | ------------- |
| Body frame  | 1 |  Hosts physical components of the robot.  |
| 18650 Li-ion Battery  | 2 | Power source. |
| N20 Micro-GearMotor | 2 | Actuators for wheels. |
| Wheel | 2 | Move the robot around. |
| Power Expansion Board | 1 | Converts 6~24V to 5V. Split input power. |
| Solderless breadboard  | 1+ | Hosts electronics components |
| Raspberry Pi Pico (2) | 1 | Processes input signals, makes decisions and outputs commanding signals |
| TB6612FNG Motor Driver Board | 1 | Manipulates speed and direction of up to 2 motors |
| HC-SR04 Sensor | 1 | Senses distance via ultrasound |
| Common Cathode RGB LED  | 1 | Indicates robot's status |
| Tactile switch button  | 1 | Switch robot's working mode. |
| Resistors  | Several | Limit current and/or divide voltage  |
| Jumper wires  | Several | Connect electronics components  |
| (Optional) MG90S servo  | 1 | Sweep the ultrasound scanner. |
| (Optional) Sensor case  | 1 | Houses the distance sensor and attaches to the servo. |

> [!TIP]
> Make sure every component is working by testing them.
> Things you may want to check:
> - Have you double checked circuit and no short circuit anywhere?
> - Have you checked continuity of the electrical connections?
> - Have you charged the batteries?
> - Are electronics (LEDs, button, Pico, HC-SR04, TB6612FNG, etc.) functional?


## 3. Requirements:
> [!CAUTION]
> - Live demo is required to redeem the credits for coding.
> - Hitting a wall once during demonstration will cost 1% off your grade of this project.

### 3.1. (15%) Mechanical Design
- (5%) Assemble your robot and upload a portrait picture (you pick the viewing angle) for your robot.
  Try to reveal as many key components as possible.
- (10%) Use a top-view drawing to illustrate:
  - Width and length of the base body (exclude wheels).
  - Diameter of the wheel
  - Length of the driving axle.
  - Location of the driving wheels and the caster wheel.
- (+4% Bonus) Attach a distance scanner (made by the ultrasonic sensor and the MG90S servo) to the bed.
- (+8% Bonus) Design a unique case for the ultrasonic sensor attaching to the MG90S servo.
  Upload a tech draw of the case to illustrate key dimensions of it. 
- (+1~10% Bonus) Other mechanical designs outstand the [TBot](https://github.com/linzhangUCA/tbot_mechanical).
> [!WARNING]
> Temporary solutions, such as tape and glue, are not allowed for mounting the distance scanner.

### 3.2. (20%) Electrical Design
Wire up all the electrical and electronics components.
- (10%) Upload a wiring diagram to **ONLY** depict the **power** flowing around the circuit.
  Please label out the input voltage for different components.
- (10%) Upload a Wiring diagram to **ONLY** illustrate the **signal** streams of the circuit.
  Please express the direction of the signals.
- (+8% Bonus) Include wiring (power and signal) for the MG90S servo.

### 3.3. (50%) Coding
Code Pico to drive the robot around in a rectangular cell without hitting the walls. 
realize following functions:
1. (7%) Initialization (System Check).
   - (6%) Blink all LEDs with frequency of 5 Hz, lasting 2 seconds if both conditions (below) are satisfied.
     **Do not start wall bouncing if any of the init conditions is not met**.
     - The button's GPIO pin is receiving correct default signal (`0` for `PULL_DOWN`, `1` for `PULL_UP`)
     - Ultrasonic sensor is receiving non-zero distance measuring.
   - (1%) The robot enters `PAUSE` mode after the status check.
   - (+2% Bonus) Center the distance sensor (facing straightly forward) after the status check.
2. (6%) When `PAUSE` mode is activated:
   - (2%) Quick stop both motors.
   - (2%) `GREEN` LED fades in and fades out at frequency of 1 Hz (equally allocate fade-in and fade-out time).
   - (2%) Press the button, the robot switch to the `WORK` mode at the instant the button is **released**.
3. (23%) When `WORK` mode is activated:
   - (1%) `GREEN` LED stays on constantly.
   - (2%) Press the button to switch to the `PAUSE` mode at the instant the button is **released**.
   - (20%) Robot start wandering around without hitting the wall.
     - (5%) Drive straight forward (using **at least 50% of the maximum speed in terms of duty cycle**) if no wall was detected within 0.25 m distance.
     - (15%) Avoid hitting the wall within 0.25 m range by driving backward (half a second) then spinning in place in a random direction (half a second) with appropriate speed.
     - (+16% Bonus) Let the robot's heading direction be the reference $0^{\circ}$.
       Under the forward traverse phase, use the servo-driven distance sensor to scan distance from $-60^{\circ}$ to $60^{\circ}$ then from $60^{\circ}$ to $-60^{\circ}$ in a period of 600 ms.
     - (+16% Bonus) If the wall is detected (0.25 m away from any angle), perform the wall avoidance maneuver by:
       1. Centering the distance sensor.
       2. Backing up while turning away from the wall.
          Please turn the robot based on the servo angle when the (0.25 m) wall was detected (CCW for positive angle, CW for negative angle).
       3. Resume forward traverse. 
4. (10%) Low battery simulation.
   - (7%) If the accumulated `WORK` time exceeds 40 seconds (low-battery simulation):
     - substitute `GREEN` light with **`YELLOW`** light for both modes.
     - Reduce the robot's speed to original's 50% in terms of dutycycle (Make sure the robot is still movable).
   - (3%) If accumulated `WORK` time over 50 seconds, blink `RED` LED (no other light) at frequency of 10 Hz.
5. (4%) Termination.
   Despite the mode, stop the motors and put the Pico 2 board into [Deep Sleep](https://docs.micropython.org/en/v1.16/rp2/quickref.html#deep-sleep-mode) if `RED` LED blinked 10 seconds.

> [!TIP]
> - Reuse the code from project 1.
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy debugging tools.

### 3.5. (15%) Documentation
> [!CAUTION]
> Use [README](README.md) for documentaion.

#### 3.5.1. (4%) Illustrate mechanical designs
- Display the portrait of your robot with resolution of 800 px. by 600 px..
- Display the dimension drawing with resolution of 1200 px. by 900 px..

#### 3.5.2. (4%) Wiring diagrams
- Display the wiring diagram of the **power streams** with a resolution of 800 px. by 600 px..
- Display the wiring diagram of the **signal streams** with a resolution of 800 px. by 600 px..

#### 3.5.3. (7%) Algorithm
Use a [flowchart](https://en.wikipedia.org/wiki/Flowchart) or a [algorithm/pseudocode table](https://www.overleaf.com/learn/latex/Algorithms) or a [itemized list](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#lists) to explain your code.

#### 3.5.4. (1%) Acknowledge AI's contributions 
Please list out all the AI's contributions to this project.

## 4. Resources
- [Distance sensor examples](https://github.com/linzhangUCA/3421example-ultrasonic_sensor).
- [(Dual) Motor driver examples](https://github.com/linzhangUCA/3421example-differential_drive_controller).
- [Reference Mechanical Design: tbot_mechanical](https://github.com/linzhangUCA/tbot_mechanical).

