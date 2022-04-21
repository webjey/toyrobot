# ToyRobot
Sample application for simulating a robot within a table top.

## Requirements:
- Python version 3.2 or above 

## How to setup
```bash
git clone https://github.com/webjey/toyrobot.git
cd toyrobot
```

## How to run application
- In the command prompt (or terminal), type:
  ```
  # In default, the maximum rows and columns is 5
  python -m toyrobot --file tests/data/2.txt
  ```

- You may also specify the maximum rows and columns:
  ```
  python -m toyrobot --file tests/data/2.txt --rows=10 --columns=10 
  ```


## Available Commands
**PLACE** - required argument is a string "X,Y,F". eg PLACE 0,0,NORTH

**MOVE** -  will move the toy robot one unit forward in the direction it is currently facing

**LEFT** /  **RIGHT** - will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

**REPORT** - will announce the X,Y and F of the robot.


## Sample command
- First, you need to position the robot.
  ```bash
  PLACE 0,0,NORTH
  ```
- Move the robot 1 step (facing north)
  ```bash
  MOVE
  ```
- Check the robot position
  ```bash
  REPORT
  
  # Output
  # 0,1,NORTH
  ```

## How to run unit test
```bash
python -m unittest

```


