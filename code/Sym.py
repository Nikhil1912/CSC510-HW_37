# Sym's summarize a stream of symbols.
from collections import defaultdict
import math


class Sym:
    def __init__(self, col_position=0, col_name=""):
        self.num_items = 0                                  # items seen
        self.col_position = col_position                    # column position
        self.col_name = col_name                            # column name
        self.has = defaultdict(0)                           # kept data

    # Add symbol value to Sym object
    def add(self, value):
        if value != "?":
            self.num_items += 1
            self.has[value] += 1

    # Calculate diversity, which is entropy in the case of Sym
    def div(self, e=0):
        def fun(p):
            return p*math.log(p,2)
        
        for value in self.has:
            if self.has[value] > 0:
                e = e - fun(self.has[value]/self.num_items) 
        
        return e