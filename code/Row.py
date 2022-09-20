# Holds one record
class Row:
    def __init__(self, t):
        self.cells = t              # One record
        self.cooked = t.copy()      # Used if we discretize data
        self.isEvaled = False       # True if y-values evaluated
