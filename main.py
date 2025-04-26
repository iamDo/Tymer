import argparse
import json
from pathlib import PosixPath
import re


CONFIG_FILE = PosixPath('~/.config/tymer.json').expanduser()


def parse_name_and_duration(timer):
    duration_regex = r'[0-9]*[sSmMhH]'
    duration = ''
    name = ''
    if re.match(duration_regex, timer[0]):
        duration = timer[0]
        name = timer[1]
    else:
        duration = timer[1]
        name = timer[0]

    return (name, duration)


def add(timer):
    configuration = {}
    with open(CONFIG_FILE, encoding='utf-8') as config_file:
        configuration = config_file.read()

    configuration = json.loads(configuration)
    timer = parse_name_and_duration(timer)
    configuration[timer[0]] = timer[1]
    configuration = json.dumps(configuration, sort_keys=True, indent=4)
    print(configuration)

    with open(CONFIG_FILE, 'w', encoding='utf-8') as config_file:
        config_file.write(configuration)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', nargs=2)
    args = parser.parse_args()
    add(args.add)



if __name__ == '__main__':
    main()
