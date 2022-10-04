import math
import re
import yaml
from subprocess import call
import Common

with open("config.yml", "r") as config_file:
    configs = yaml.safe_load(config_file)

passer = ""


class TestError(Exception):
    def __init__(self, mess):
        self.mess = mess


# Call "fun" on each row. Row cells are divided in "the.seperator"
def csv(fname, fun=None):
    if fname is None or len(fname.strip()) == 0:
        raise Exception("File not found")
    else:
        sep = Common.cfg['the']['separator']
        with open(fname, 'r') as s:
            for s1 in s.readlines():
                t = []
                csv_row = s1.split(sep)  # Split a row using the separator, here ','
                csv_row[-1] = csv_row[-1][:-1]  # Removing \n from the end of last element
                for cell in csv_row:
                    t.append(coerce(cell))          # Every cell should be type casted
                if fun:
                    fun(t)


def coerce(s):
    # convert input in the form of a string to appropriate data type int/bool/str
    def fun(s1):
        # returns boolean for the string
        if s == "true":
            return True
        elif s == "false":
            return False
        return s1

    # return integer of the number in the form of string or calls fun to return appropriately
    if is_number(s):
        return float(s)
    else:
        return None or fun(s)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def fun_the():
    # create "the" variable and parse through "help" to get the values needed
    configs['the'] = {}
    extract = re.findall(r"[-][-]([\S]+)[^\n]+= ([\S]+)", passer)
    for k, v in extract:
        configs['the'][k] = coerce(v)
    return configs['the']


configs['the']['separator'] = fun_the()


def rnd(x, places=2):
    mult = 10 ** places
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
