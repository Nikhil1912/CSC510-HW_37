import math
import sys

import Common
import TestEngine
from Data import Data
from Num import Num
from Sym import Sym
from Utils import csv
from TestUtils import canPrint


@TestEngine.test
def eg_the():
    canPrint(Common.cfg['the'], 'Should be able to print the')
    return True


@TestEngine.test
def eg_sym():
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
def eg_num():
    n = Num()
    for x in range(1, 101):
        n.add(x)

    mid, div = n.mid(), n.div()
    results = "mid= {}, div= {}".format(mid, div)
    canPrint(results, 'Should be able to print mid and div')

    return 50 <= mid <= 52 and 30.5 < div < 32


@TestEngine.test
def eg_bignum():
    num = Num()
    Common.cfg["the"]['nums'] = 32

    for i in range(1000):
        num.add(i)
    canPrint(num.nums(), 'Should be able to print nums')
    return len(num.has) == 32


@TestEngine.test
def eg_data():
    d = Data('data/auto93.csv')
    for col in d.cols.y:
        canPrint(col, "Should be able to print columns")
    return True


@TestEngine.test
def eg_csv():
    def fun(row):
        fun.n += 1
        if fun.n > 10:
            return
        canPrint(row, 'Should be able to print rows')

    fun.n = 0
    csv('data/auto93.csv', fun)
    return True


@TestEngine.test
def eg_stats():
    def div(col):
        if type(col) == Num:
            return Num.div(col)
        else:
            return Sym.div(col)

    def mid(col):
        if type(col) == Num:
            return Num.mid(col)
        else:
            return Sym.mid(col)

    data = Data('data/auto93.csv')
    print('xmid', end='\t')
    canPrint(data.stats(2, data.cols.x, mid), 'xmid')
    print('xdiv', end='\t')
    canPrint(data.stats(3, data.cols.x, div), 'xdiv')
    print('ymid', end='\t')
    canPrint(data.stats(2, data.cols.y, mid), 'ymid')
    print('ydiv', end='\t')
    canPrint(data.stats(3, data.cols.x, div), 'ydiv')
    return True


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
