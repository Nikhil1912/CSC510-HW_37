import math
from subprocess import call


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


def cli(args, configs):

    for x in range(0, len(args), 2):
        if args[x] == "-e":
            call(["python", "your_file.py"])
            continue
        elif args[x] == "-d":
            configs['the'][0]['dump'] = args[x + 1]
            continue
        elif args[x] =="-f":
            configs['the'][0]['file'] = args[x + 1]
            continue
        elif args[x] == "-h":
            configs['the'][0]['help'] = args[x + 1]
            continue
        elif args[x] == "-n":
            configs['the'][0]['nums'] = args[x + 1]
            continue
        elif args[x] == "-s":
            configs['the'][0]['seed'] = args[x + 1]
            continue
        elif args[x] == "-S":
            configs['the'][0]['separator'] = args[x + 1]
            continue
        elif args[x] == "-q":
            print("Exiting.")
            exit()
        else:
            print(args[x], " is not a valid option. Exiting.")
            exit()

    return configs



