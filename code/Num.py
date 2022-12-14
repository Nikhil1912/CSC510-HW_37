import math
import random
import Common


# Num summarizes a stream of numbers
class Num:
    def __init__(self, col_position=0, col_name=""):
        self.num_items = 0  # items seen
        self.col_position = col_position  # column position
        self.col_name = col_name  # column name
        self.has = []  # kept data
        self.lo = math.inf  # lowest seen
        self.hi = -math.inf  # highest seen
        self.is_sorted = True  # no updates since last sort of data
        self.w = 1 if col_name and col_name[-1] == '+' else -1  # maximize or minimize column

    #Get the string representation of the object
    def __str__(self):
        toPrintList = []
        toPrintList.append("at: " + str(self.col_position))
        toPrintList.append("hi: " + str(self.hi))
        toPrintList.append("isSorted: " + str(self.is_sorted))
        toPrintList.append("lo: " + str(self.lo))
        toPrintList.append("n: " + str(self.num_items))
        toPrintList.append("name: " + str(self.col_name))
        toPrintList.append("w: " + str(self.w))
        return str(toPrintList)

    # Get the stored numbers in a sorted order
    def nums(self):
        if not self.is_sorted:
            self.has.sort()
            self.is_sorted = True

        return self.has

    # Reservoir sampler
    def add(self, v):
        if v != '?':
            value = int(v)
            the_nums = int(Common.cfg['the']['nums'])
            self.num_items += 1
            self.lo = min(self.lo, value)
            self.hi = max(self.hi, value)
            pos = -1
            if len(self.has) < the_nums:
                pos = len(self.has) + 1               
            elif random.random() < the_nums / self.num_items:
                pos = random.randint(0, len(self.has)-1)
                del self.has[pos]                
            if pos > -1:
                self.is_sorted = False
                self.has.insert(pos, value)

    # Central tendency; for Nums, this is median
    def mid(self):
        if not self.is_sorted:  # If the dictionary is not already sorted, sort it using nums
            self.nums()
        med_position = math.floor(len(self.has)/2)  # To find where the median value is, divide the number of keys in
        # the dictionary by 2 and take the floor
        return self.has[med_position]  # Return the median (middle) value of the key in the sorted dictionary
        # The above assumes that the key is what is being returned; if this is not the case, and it should return the
        # values, use the following: return [value for value in self.has.values()][med_position]

    # Diversity; for Nums, this is standard deviation
    def div(self):
        if not self.is_sorted:  # If the OD is not already sorted, sort it using nums
            self.nums()
        a = self.has # for simplicity in later lines and to better reflect the lua code
        ninetieth_percentile_position = math.floor(len(self.has)*0.9)  # The position of the 90th percentile in the OD
        tenth_percentile_position = math.floor(len(self.has)*0.1)  # The position of the 10th percentile in the OD
        ninetieth_percentile_value = [key for key in a][ninetieth_percentile_position] # The value of the key at the
        # 90th percentile
        tenth_percentile_value = [key for key in a][tenth_percentile_position] # The value of the key at the 10th
        # percentile
        return (ninetieth_percentile_value-tenth_percentile_value)/2.58  # Return the standard deviation, as defined
        # in the original lua code (line 195)

