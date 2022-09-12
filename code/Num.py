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
        med_position = math.floor(len(self.has.keys())/2)  # To find where the median value is, divide the number of keys in the dictionary by 2 and take the floor
        return [key for key in self.has.keys()][med_position]  # Return the median (middle) value of the key in the sorted dictionary
        # The above assumes that the key is what is being returned; if this is not the case, and it should return the values, use the following:
        # return [value for value in self.has.values()][med_position]

    # Diversity; for Nums, this is standard deviation
    def div(self):
        if not self.is_sorted:  # If the OD is not already sorted, sort it using nums
            self.nums()
        a = self.has.keys() # for simplicity in later lines and to better reflect the lua code
        ninetieth_percentile_position = math.floor(len(self.has.keys())*0.9)  # The position of the 90th percentile in the OD
        tenth_percentile_position = math.floor(len(self.has.keys())*0.1)  # The position of the 10th percentile in the OD
        ninetieth_percentile_value = [key for key in a][ninetieth_percentile_position] # The value of the key at the 90th percentile
        tenth_percentile_value = [key for key in a][tenth_percentile_position] # The value of the key at the 10th percentile
        return (ninetieth_percentile_value-tenth_percentile_value)/2.58  # Return the standard deviation, as defined in the original lua code (line 195)

