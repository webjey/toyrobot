from toyrobot.grid import Grid
from toyrobot.orientation import Orientation
from toyrobot.robot import Robot


class Controller(object):
    
    def __init__(self, grid):
        self.grid = grid
        self.commands = ('PLACE', 'MOVE', 'RIGHT', 'LEFT', 'REPORT')

    def process_command(self, user_input):
        cmd, *args = user_input.strip().upper().split(' ', 1)
        if args:
            args = args[0]

        if not cmd in self.commands:
            print('\nERROR: Invalid command\n')


        if cmd == 'PLACE':
            error_invalid_args = (f'\nERROR:'
                                  f'\nShould be in the format "PLACE X,Y,Direction"'
                                  f'\nDirection should either: {list(Orientation.__members__)}'
                                  f'\neg. PLACE 0,1,NORTH\n')
            
            if not args:
                print(error_invalid_args)
                return

            args = args.split(',', 3) 
            if len(args) != 3:
                print(error_invalid_args)
                return

            x, y, direction = args

            if not (x.isnumeric() and y.isnumeric()):
                print(error_invalid_args)
                return
                
            if direction not in Orientation.__members__:
                print(error_invalid_args)
                return
                
            if self.grid.is_valid(int(x), int(y)):
                robot = Robot(x, y, direction)
                self.grid.add_robot(robot)

        else:
            robot = self.grid.get_robot()

            if not robot:
                return

            if cmd == 'MOVE': 
                x, y = robot.get_next_position()
                if self.grid.is_valid(x, y):
                    robot.move()

            elif cmd == 'LEFT': 
                robot.left()

            elif cmd == 'RIGHT': 
                robot.right()

            elif cmd == 'REPORT': 
                robot.report()

            else:
                pass
