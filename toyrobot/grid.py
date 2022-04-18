class Grid(object):
    
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.robot = None

    def add_robot(self, robot):
        self.robot = robot

    def get_robot(self):
        return self.robot

    def has_robot(self):
        return True if self.robot else False

    def is_valid(self, x, y):
        if ((x >= 0 and x < self.cols) and 
            (y >= 0 and y < self.rows)):
            return True

        return False