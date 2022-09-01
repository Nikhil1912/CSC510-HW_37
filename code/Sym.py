# Sym's summarize a stream of symbols.
from collections import defaultdict


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
