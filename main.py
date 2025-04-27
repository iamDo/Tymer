import argparse
import json
from pathlib import PosixPath
import re


CONFIG_FILE = PosixPath('~/.config/tymer.json').expanduser()


def load_config():
    configuration = {}
    with open(CONFIG_FILE, encoding='utf-8') as config_file:
        configuration = config_file.read()

    configuration = json.loads(configuration)
    return configuration


def write_config(configuration):
    configuration = json.dumps(configuration, sort_keys=True, indent=4)

    with open(CONFIG_FILE, 'w', encoding='utf-8') as config_file:
        config_file.write(configuration)


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
    configuration = load_config()
    timer = parse_name_and_duration(timer)
    configuration[timer[0]] = timer[1]
    write_config(configuration)


def remove(key_to_remove):
    configuration = load_config()

    configuration.pop(key_to_remove)

    write_config(configuration)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', nargs=2)
    parser.add_argument('--remove', nargs=1)
    args = parser.parse_args()

    if args.add:
        add(args.add)
    elif args.remove:
        remove(args.remove[0])




if __name__ == '__main__':
    main()
