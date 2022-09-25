import math


class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess


class ProcessCsv:
    def csv(self, filename, funct):
        seperator = None

        # TODO


def rnd(x, places=2):
    mult = 10**places
    return math.floor(x * mult + 0.5) / mult
