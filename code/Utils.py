import math


class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess


class ProcessCsv:
    # csv reads each line of a text file,
    # divides on an operator (here, a comma),
    # removes leading/trailing white space,
    # then coerces the cells to ints or floats or booleans or strings
    # def csv(self, filename, funct):
    #     sep = "([^"+","+"]+)"
    #     src = open(filename, "r")
    #     s = src.read()
    #     if not s:
    #         src.close()
    #     else:
    #         t = {}
    #         for s1 in s.gmatch(sep):  # The string.gmatch function will take an input string and a pattern. This pattern describes on what to actually get back. This function will return a function which is actually an iterator. The result of this iterator will match to the pattern.
    #             t[1+len(t)] = coerce(s1)
    #     funct(t)
    # help from https://stackoverflow.com/questions/43447221/removing-all-spaces-in-text-file-with-python-3-x
    def csv(self, filename, funct):
        sep = ","
        t = {}
        with open (filename, 'r') as s:
            lines = s.readlines()
        lines = [line.replace(' ','') for line in lines]
        for s1 in lines:

        else:
            t = {}
            for s1 in s.gmatch(sep):  # The string.gmatch function will take an input string and a pattern. This pattern describes on what to actually get back. This function will return a function which is actually an iterator. The result of this iterator will match to the pattern.
                t[1+len(t)] = coerce(s1)
        funct(t)


def rnd(x, places):
    mult = 10**places if places else 10**2
    return math.floor(x * mult + 0.5) / mult


# helper function for csv
def coerce(s, funct):
    def funct(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1
    return int(s) or funct(s.match("^%s*(.-)%s*$"))

