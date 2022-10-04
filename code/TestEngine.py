# Used this tutorial as reference to build a unit test framework:
# https://dev.to/azure/how-you-can-build-your-own-test-framework-in-python-using-decorators-2b00

import functools
import yaml
import random
from Utils import TestError
import Common


def test(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except TestError as te:
            return False

    Common.eg[wrapper.__name__] = wrapper
    return wrapper


def runs(testName):
    if testName not in Common.eg:
        return
    random.seed(Common.cfg['the']['seed'])
    old = {}
    for k, v in Common.cfg['the'].items():
        old[k] = v

    status = True
    if Common.cfg['the']['dump']:
        out = Common.eg[testName]()
    else:
        try:
            out = Common.eg[testName]()
        except:
            status = False

    for k, v in old.items():
        Common.cfg['the'][k] = v

    msg = ("PASS" if out else "FAIL") if status else "CRASH"
    if testName != 'ALL':
        testName = testName[3:]
    print("!!!!!!\t" + msg + "\t" + testName + "\t" + str(status))
