from TestEngine import test, runs
from TestUtils import canPrint
import yaml

with open("../config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)

@test
def the():
    canPrint(cfg['the'], 'Should be able to print the')

if __name__ == "__main__":
    runs('the')