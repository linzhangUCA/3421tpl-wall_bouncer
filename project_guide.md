# Project 2: Wall Bouncer
> [!IMPORTANT]
> # Due: Thursday, Nov. 5th @ 5 PM


## 1. Overview
[Roomba](https://www.irobot.com/en_US/roomba.html) is a widely popular autonomous housekeeping robot. 
Despite the advanced technologies in recent models, its fundamental navigation strategy remains remarkably straightforward: traveling in straight lines and changing directions upon encountering obstacles allows it to effectively clean a decent-sized room. 

Inspired by this concept, you will design, assemble, and program an autonomous robot to explore a bounded arena using an ultrasonic distance sensor and a reactive "wall-bouncing" navigation algorithm.

## 2. Get Started
The primary hardware components required to build the robot are listed below:

| Name  | Qty. | Functionality
| ------------- | ------------- | ------------- |
| Body frame  | 1 |  Chassis that hosts all mechanical and electronic components.  |
| 18650 Li-ion Battery  | 2 | Main power source. |
| N20 Micro-GearMotor | 2 | Actuators for wheel drive. |
| Wheel | 2 | Primary propulsion. |
| Power Expansion Board | 1 | Regulates input power ($6 V - 24 V) and splits power rails. |
| Solderless breadboard  | 1+ | Prototype circuit connections for electronic components. |
| Raspberry Pi Pico (2) | 1 | Microcontroller for sensor input processing, state logic, and motor control output. |
| TB6612FNG Motor Driver Board | 1 | Controls speed and directional rotation for up to 2 DC motors. |
| HC-SR04 Sensor | 1 | Distance measurement via ultrasonic pinging. |
| Common Cathode RGB LED  | 1 | Multi-color visual status indicator. |
| Tactile switch button  | 1 | User interface button to toggle operating modes. |
| Resistors  | Set | Current limiting for LEDs and voltage division for signals.  |
| Jumper wires  | Set | Electrical interconnections between components.  |
| (Optional) MG90S servo  | 1 | Actuator for panning the ultrasonic distance scanner. |
| (Optional) Sensor case  | 1 | Custom housing attaching the HC-SR04 sensor to the servo shaft. |

> [!TIP]
> Verify every component's operational status prior to final assembly:
> - Double-check circuit topology to ensure no power-to-ground short circuits exist.
> - Verify electrical continuity across all jumper cables and breadboard rows.
> - Ensure batteries are fully charged before conducting motor drive tests.
> - Individually test peripheral functionality (RGB LED output, button state reading, Pico GPIOs, HC-SR04 distance readings, and TB6612FNG logic pins).


## 3. Requirements:
> [!CAUTION]
> - A live demonstration is required to receive code implementation credits.
> - Penalty: Each instance of hitting a wall during the live demonstration will result in a 1% deduction from the total project grade.

### 3.1. Mechanical Design (15% Base + Bonus)
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
- (+0~8% Bonus) Other mechanical designs outstand the [TBot](https://github.com/linzhangUCA/tbot_mechanical).
> [!WARNING]
> Temporary solutions, such as tape and glue, are not allowed for mounting the distance scanner.

### 3.2. Electrical Design (20% Base + Bonus)
Wire up all the electrical and electronics components.
- (10%) Upload a schematic depicting **ONLY the power** distribution paths.
  Clearly label nominal operating voltage levels for all connected modules.
- (10%) Upload a schematic depicting **ONLY signal lines**.
  Use directional arrows to represent signal flow.
- (+8% Bonus) Include wiring (power and signal) for the MG90S servo in both schematics.

### 3.3. Coding (50% Base + Bonus)
> [!IMPORTANT]
> Upload all your code to the project repository, including the imported ones.

Code Pico to drive the robot around in a rectangular cell without hitting the walls. 
realize following functions:
1. (7%) Initialization (System Check).
   - (6%) On power-up, verify system hardware conditions before enabling motor movement.
     If all of the following conditions are met, blink all status LEDs simultaneously at 5 Hz for 2 seconds.
     **If any initialization check fails, the robot must not proceed to active navigation.**.
     - Button GPIO pin reads its configured default resting logic level (`0` for `PULL_DOWN`, `1` for `PULL_UP`)
     - Ultrasonic sensor returns a non-zero, valid distance reading.
   - (1%) Automatically transition into `PAUSE` mode upon successful self-test completion.
   - (+2% Bonus) Automatically position the distance sensor facing directly forward ($0^\circ$) upon successful self-test completion.
2. (6%) When `PAUSE` mode is activated:
   - (2%) Execute a quick stop/brake command on both drive motors.
   - (2%) Modulate the `GREEN` LED with a breathing/fading effect at 1 Hz (allocating equal duration to fade-in and fade-out cycles).
   - (2%) Switch to `WORK` mode at the exact moment the tactile button is **released**.
3. (23%) When `WORK` mode is activated:
   - (1%) Solid `GREEN` LED continuously lit.
   - (2%) Switch to `PAUSE` mode at the exact moment the tactile button is released.
   - (20%) Robot start wandering around without hitting the wall.
     - (5%) Drive straight forward at a minimum of 50% PWM duty cycle whenever no obstacle is detected within a 0.25 m range.
     - (15%) Upon detecting a wall within 0.25 m, reverse drive for 0.5 seconds, then spin in place in a random direction (clockwise or counter-clockwise) for 0.5 seconds to turn away from the detected wall at an appropriate turn speed before resuming forward travel.
     - (+16% Bonus) Define forward heading as $0^\circ$ and couner-clockwise rotation to be positive.
       During forward travel, sweep the servo-mounted sensor back and forth continuously from $-60^\circ$ to $+60^\circ$ over a full cycle period of $600\text{ ms}$.
     - (+16% Bonus) When an obstacle within 0.25 m is detected at any scan angle:
       1. Immediately re-center the servo sensor to $0^\circ$.
       2. Reverse while steering away from the wall based on the sensor angle at detection (steer CCW for positive angles, CW for negative angles).
       3. Resume forward navigation. 
4. (10%) Low battery simulation.
   - (7%) If the accumulated `WORK` time exceeds 40 seconds (low-battery simulation):
     - Replace the `GREEN` status illumination with `YELLOW` across all operating modes (Note: there is no native `YELLOW` in the RGB LED).
     - Reduce drive motor speed by 50% relative to its initial configuration (ensuring sufficient torque remains for robot movement).
   - (3%) If accumulated `WORK` time over 50 seconds, blink `RED` LED **exclusively** at frequency of 10 Hz.
5. (4%) Termination.
   Despite the mode, stop the motors and put the Pico 2 board into [Deep Sleep](https://docs.micropython.org/en/v1.16/rp2/quickref.html#deep-sleep-mode) if `RED` LED blinked 10 seconds.

> [!TIP]
> - Reuse the code from project 1.
> - Break tasks down into small pieces (the smaller the better). You may need write a handful of unit test scripts.
> - `print()` function and Python Shell are handy debugging tools.

### 3.5. Documentation (15% Base)
> [!CAUTION]
> All project documentation must be committed directly to your repository's root [README.md](README.md) file.

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

