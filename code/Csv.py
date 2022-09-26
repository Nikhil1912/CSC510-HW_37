import yaml
from Utils import cli

fname = "config.yaml"

stream = open(fname, 'r')
configs = yaml.load(stream)

print("Welcome to csv summary!")
print("Help \n USAGE EX: -d true -n 5 -e \n OPTIONS:\n"
      " -e start-up example \n -d on test failure, exit with stack dump \n"
      " -h show help \n -n number of nums to keep \n"
      " -s random number seed \n -S field separator")
print("Select an option.")

run_csv = True

while run_csv:
    if configs['the'][0]['help']:
        print("Help \n USAGE EX: -d true -n 5 -e \n OPTIONS:\n"
              " -e start-up example \n -d on test failure, exit with stack dump \n"
              " -h show help \n -n number of nums to keep \n"
              " -s random number seed \n -S field separator \n -q quit")
    csv_args = input("Select an option/s")
    new_configs = cli(csv_args, configs, fname)

    with open(fname, 'w') as yaml_file:
        yaml_file.write(yaml.dump(new_configs, default_flow_style=False))

