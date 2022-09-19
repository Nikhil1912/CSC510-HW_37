import math

from TestEngine import test, runs
from TestUtils import canPrint
from Sym import Sym
from Num import Num
import yaml

with open("../config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)

@test
def the():
    canPrint(cfg['the'], 'Should be able to print the')

@test
def sym():
    s = Sym()

    test_vals = ["a", "a", "a", "a", "b", "b", "c"]

    for x in test_vals:
        s.add(x)

    mode, entropy = s.mid(), s.div()
    entropy = math.floor(entropy)
    results = "mid= {}, div= {}".format(mode, entropy)
    canPrint(results, 'Should be able to print mid and div')

    return mode == "a" and 1.37 <= entropy <= 1.38



if __name__ == "__main__":
    runs('the')
    runs('sym')

@test
def bignum() -> bool:
    num = Num()
    the['num'] = 32

    for i in range(1000):
        num.add(i)
    canPrint(num.nums(), 'Should be able to print nums')
    return len(num._has) == 32