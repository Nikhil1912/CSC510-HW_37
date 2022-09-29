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
    arg_arr = args.split(" ")

    run_tests = False
    if '-e' in arg_arr:
        run_tests = True
        arg_arr.remove("-e")

    for x in range(0, len(arg_arr), 2):
        if arg_arr[x] == "-d":
            if arg_arr[x + 1] == 'True' or arg_arr[x + 1] == 'true':
                configs['the']['dump'] = True
            else:
                configs['the']['dump'] = False
            continue
        elif arg_arr[x] == "-f":
            configs['the']['file'] = str(arg_arr[x + 1])
            continue
        elif arg_arr[x] == "-h":
            if arg_arr[x + 1] == 'True' or arg_arr[x + 1] == 'true':
                configs['the']['help'] = True
            else:
                configs['the']['help'] = False
            continue
        elif arg_arr[x] == "-n":
            configs['the']['nums'] = int(arg_arr[x + 1])
            continue
        elif arg_arr[x] == "-s":
            configs['the']['seed'] = int(arg_arr[x + 1])
            continue
        elif arg_arr[x] == "-S":
            configs['the']['separator'] = str(arg_arr[x + 1])
            continue
        elif arg_arr[x] == "-q":
            print("Exiting.")
            exit()
        else:
            print(args[x], " is not a valid option. Exiting.")
            exit()

    if run_tests:
        call(["python", "Tests.py"])

    return configs



