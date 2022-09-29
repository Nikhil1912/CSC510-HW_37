import math
import Common
import TestEngine
from TestUtils import canPrint
from Sym import Sym
from Num import Num
import sys
import Common


@TestEngine.test
def the():
    canPrint(Common.cfg['the'], 'Should be able to print the')
    return True


@TestEngine.test
def sym():
    s = Sym()

    test_vals = ["a", "a", "a", "a", "b", "b", "c"]

    for x in test_vals:
        s.add(x)

    mode, entropy = s.mid(), s.div()
    entropy = math.floor(entropy * 1000) / 1000
    results = "mid= {}, div= {}".format(mode, entropy)
    canPrint(results, 'Should be able to print mid and div')

    return mode == "a" and 1.37 <= entropy <= 1.38


@TestEngine.test
def num():
    n = Num()
    for x in range(1, 101):
        n.add(x)

    mid, div = n.mid(), n.div()
    results = "mid= {}, div= {}".format(mid, div)
    canPrint(results, 'Should be able to print mid and div')

    return 50 <= mid <= 52 and 30.5 < div < 32


@TestEngine.test
def bignum():
    num = Num()
    Common.cfg["the"]['nums'] = 32

    for i in range(1000):
        num.add(i)
    canPrint(num.nums(), 'Should be able to print nums')
    return len(num.has) == 32


@TestEngine.test
def ALL():
    for k in Common.eg:
        if k != "ALL":
            print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            if not TestEngine.runs(k):
                Common.fails += 1
    return True


if __name__ == "__main__":
    TestEngine.runs(Common.cfg["the"]["eg"])
    sys.exit(Common.fails)
