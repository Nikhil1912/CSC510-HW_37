import re
from Sym import Sym
from Num import Num
import Common


# Holds summaries of columns
class Cols:
    def __init__(self, names):
        self.names = names  # All column names
        self.all = []  # All columns including the skipped ones
        self.klass = None  # The single dependent klass column (if it exists)
        self.x = []  # Independent columns
        self.y = []  # Dependent columns
        for c, s in enumerate(names):
            if re.match('^[A-Z]+', s):
                col = Num(c, s)  # Numerics start with uppercase
            else:
                col = Sym(c, s)
            self.all.append(col)
            if s[-1] != ':':  # Some columns are skipped
                if s[-1] in ['+', '-']:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if s[-1] == '!':
                    self.klass = col
