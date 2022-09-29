import yaml
from Utils import cli

with open("../config.yml", "r") as config_file:
    configs = yaml.safe_load(config_file)

print("Welcome to csv summary!")
print("Help \n USAGE EX: -d true -n 5 -e \n OPTIONS:\n"
              " -e start-up example \n -d on test failure, exit with stack dump \n"
              " -f file with csv data \n -h show help \n -n number of nums to keep \n"
              " -s random number seed \n -S field separator \n -q quit")

run_csv = True

while run_csv:
    if configs['the']['help']:
        print("Help \n USAGE EX: -d true -n 5 -e \n OPTIONS:\n"
              " -e start-up example \n -d on test failure, exit with stack dump \n"
              " -f file with csv data \n -h show help \n -n number of nums to keep \n"
              " -s random number seed \n -S field separator \n -q quit")
    csv_args = input("Select an option/s \n")
    new_configs = cli(csv_args, configs)

    with open("../config.yml", "w") as config_file:
        config_file.write(yaml.dump(new_configs))


