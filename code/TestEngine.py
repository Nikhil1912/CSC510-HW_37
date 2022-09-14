# Used this tutorial as reference to build a unit test framework:
# https://dev.to/azure/how-you-can-build-your-own-test-framework-in-python-using-decorators-2b00

import functools
import yaml
import random
from Utils import TestError

with open("../config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)

eg = {}

def test(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            fn(*args,**kwargs)
            return True
        except TestError as te:
            return False
    eg[wrapper.__name__] = wrapper
    return wrapper

def runs(testName):
    if testName not in eg:
        return
    random.seed(cfg['the']['seed'])
    old = {}
    for k, v in cfg['the'].items():
        old[k] = v

    status = True
    if cfg['the']['dump']:
        out = eg[testName]()
    else:
        try:
            out = eg[testName]()
        except:
            status = False

    for k, v in old.items():
        cfg['the'][k] = v

    msg = ("PASS" if out else "FAIL") if status else "CRASH"
    print("!!!!!!\t" + msg + "\t" + testName + "\t" + str(status))