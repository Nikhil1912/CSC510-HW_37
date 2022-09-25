from Utils import ProcessCsv, rnd
import numbers


# Holds rows and their summaries in Cols.
class Data:
    def __init__(self, src):
        self.cols = None  # Summaries of data
        self.rows = {}  # Kept data

        if src:
            ProcessCsv.csv(src, self.add)  # If string name do IO on csv file and send pass the add row func
        else:
            for _, row in src:  # Else given rows so no processing just add
                self.add(row)

    def add(self, xs):
        # Filler code this is TODO
        self.cols = xs

    # Rounding numbers to 'places' (default=2)
    # For showCols, default = self.cols.y
    # No defaults for fun
    def stats(self, places, showCols, fun):
        if not showCols:
            showCols = self.cols.y
        t = {}
        for _, col in showCols:
            v = fun(col)
            if isinstance(v, numbers.Number):
                t[col.name] = rnd(v, places)
            else:
                t[col.name] = v
        return t
