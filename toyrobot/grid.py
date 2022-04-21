class Grid(object):
    """
    The context of the robot. eg Table top

    Limitation: 
    - Can add a single robot only (as per requirement)
      but can be easily be refactored to supports multiple robots.

    Attributes:
    cols (int): maximum number of columns
    rows (int): maximum number of rows
    """
    
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.robot = None

    def add_robot(self, robot):
        """
        Places a single robot. 
        At this time, 
        the robot's x,y position and orientation 
        against the current grid has been defined.

        Parameters:
        robot (Robot): A Robot instance
        """

        self.robot = robot

    def get_robot(self):
        """
        Get robot instance

        Returns:
        Robot: returns a Robot instance
        """
        return self.robot

    def has_robot(self):
        """
        Checks if a robot is already placed in the grid (or Table top)

        Returns:
        bool: True if a robot already placed in the grid, False otherwise
        """
        return True if self.robot else False

    def is_valid(self, x, y):
        """
        Determines if the x,y position is out of bound

        Returns:
        bool: True if valid, False otherwise
        """

        if ((x >= 0 and x < self.cols) and 
            (y >= 0 and y < self.rows)):
            return True

        return False