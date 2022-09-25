import math


class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess


class ProcessCsv:
    def csv(self, filename, funct):
        seperator = None

        # TODO


def rnd(x, places):
    mult = 10**places if places else 10**2
    return math.floor(x * mult + 0.5) / mult
