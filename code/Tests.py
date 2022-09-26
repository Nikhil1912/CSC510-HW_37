import math

from TestEngine import test, runs
from TestUtils import canPrint
from Sym import Sym
from Num import Num
from Utils import ProcessCsv
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

@test
def num():
    n = Num()
    for x in range(1, 1000):
        n.add(x)

    mid, div = n.mid(), n.div()
    results = "mid= {}, div= {}".format(mid, div)
    canPrint(results, 'Should be able to print mid and div')

    return 50 <= mid <= 52 and 30.5 < div < 32

@test
def bignum():
    num = Num()
    cfg["the"]['nums'] = 32

    for i in range(1000):
        num.add(i)
    canPrint(num.nums(), 'Should be able to print nums')
    return len(num.has) == 32

@test
def csv():
    n = 0
    csv("../data/auto93.csv")
    ProcessCsv.csv(src, self.add)
    n = n++
    if n > 0:
        return
    else:
        canPrint(cfg['the'], 'Should be able to print csv')
    return True

if __name__ == "__main__":
    runs('the')
    runs('bignum')
    runs('sym')
    runs('num')


