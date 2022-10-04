import yaml

with open("config.yml", "r") as config_file:
    cfg = yaml.safe_load(config_file)

eg = {}
fails = 0
