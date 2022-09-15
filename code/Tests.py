from TestEngine import test, runs
from TestUtils import canPrint
from Sym import Sym
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
    entropy = (1000*entropy)/ 1000
    results = "mid= {}, div= {}".format(mode, entropy)
    canPrint(results, 'Should be able to print mid and div')

    return mode == "a" and 1.37 <= entropy <= 1.38



if __name__ == "__main__":
    runs('the')
    runs('sym')