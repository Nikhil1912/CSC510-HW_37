import math
import random
from collections import OrderedDict
import yaml

with open("config.yml", "r") as config_file:
    cfg = yaml.load(config_file)


# Num summarizes a stream of numbers
class Num:
    def __init__(self, col_position=0, col_name=""):
        self.num_items = 0  # items seen
        self.col_position = col_position  # column position
        self.col_name = col_name  # column name
        self.has = {}  # kept data
        self.lo = math.inf  # lowest seen
        self.hi = -math.inf  # highest seen
        self.is_sorted = True  # no updates since last sort of data
        self.w = 1 if col_name and col_name[-1] == '+' else -1  # maximize or minimize column

    # Get the stored numbers in a sorted order
    def nums(self):
        if not self.is_sorted:
            self.has = OrderedDict(sorted(self.has.items()))
            self.is_sorted = True

        return self.has

    # Reservoir sampler
    def add(self, v):
        if v != '?':
            value = int(v)
            the_nums = int(cfg['the']['nums'])
            self.num_items += 1
            self.lo = min(self.lo, value)
            self.hi = max(self.hi, value)
            if sum(self.has.values()) < the_nums:
                if value in self.has:
                    self.has[value] += 1
                else:
                    self.has[value] = 1
            elif random.random() < the_nums / self.num_items:
                ele = random.choice(list(self.has.keys()))
                self.is_sorted = False
                self.has[ele] -= 1
                if self.has[ele] == 0:
                    del self.has[ele]
                if value in self.has:
                    self.has[value] += 1
                else:
                    self.has[value] = 1

    # Central tendency; for Nums, this is median
    def mid(self):
        if not self.is_sorted:  # If the dictionary is not already sorted, sort it using nums
            self.nums()
        med_position = math.floor(self.num_items/2)  # To find the median position key, halve the length of the OD and take the floor
        return self.has.items()[med_position]  # Return the median (middle) value of the sorted dictionary
