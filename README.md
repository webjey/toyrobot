# ToyRobot
Sample application for simulating a robot on a 5x5 unit table.

## Requirements:
- Python version 3.1 or above 

## How to run
```bash
git clone https://github.com/webjey/toyrobot.git
cd toyrobot
python -m toyrobot

# You should see:
# Valid commands are:  PLACE, MOVE, RIGHT, LEFT, REPORT

```

## Available Commands
**PLACE** - required argument is a string "X,Y,F". eg PLACE 0,0,NORTH

**MOVE** -  will move the toy robot one unit forward in the direction it is currently facing

**LEFT** /  **RIGHT** - will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

**REPORT** - will announce the X,Y and F of the robot.


## How to use
- First, you need to position the robot. In the command prompt, type:
  ```bash
  PLACE 0,0,NORTH
  ```
- Move the robot 1 step (facing north), type:
  ```bash
  MOVE
  ```
- Check the robot position, type:
  ```bash
  REPORT
  
  # should show similar to this
  # 0,1,NORTH
  ```

## How to run unit test
```bash
python -m unittest

```


