import math


# Num summarizes a stream of numbers
class Num:
    def __init__(self, col_position=0, col_name=""):
        self.num_items = 0                                  # items seen
        self.col_position = col_position                    # column position
        self.col_name = col_name                            # column name
        self.has = {}                                       # kept data
        self.lo = math.inf                                  # lowest seen
        self.hi = -math.inf                                 # highest seen
        self.is_sorted = True                               # no updates since last sort of data
        self.w = 1 if col_name and col_name[-1] == '+' else -1      # maximize or minimize column
