import numbers

import yaml

from Cols import Cols
from Row import Row
from Utils import csv, rnd

with open("config.yml", 'r') as config_file:
    cfg = yaml.safe_load(config_file)


# Holds rows and their summaries in Cols.
class Data:
    def __init__(self, src):
        self.cols = None  # Summaries of data
        self.rows = []  # Kept data

        if src:
            csv(src, self.add)  # If string name do IO on csv file and send pass the add row func
        else:
            for _, row in src:  # Else given rows so no processing just add
                self.add(row)

    def add(self, xs: Row):

        if not self.cols:
            self.cols = Cols(xs)
        else:
            row = xs if type(xs) == Row else Row(xs)
            self.rows.append(row)
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.col_position])

    # Rounding numbers to 'places' (default=2)
    # For showCols, default = self.cols.y
    # No defaults for fun
    def stats(self, places, showCols, fun):
        if not showCols:
            showCols = self.cols.y
        t = {}
        for col in showCols:
            v = fun(col)
            if isinstance(v, numbers.Number):
                t[col.col_name] = rnd(v, places)
            else:
                t[col.col_name] = v
        return t

