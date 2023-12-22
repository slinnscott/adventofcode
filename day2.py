import argparse
import re


def day_2(values):
    # possible_games = []
    power_set = []

    for string in values:
        min_values = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        # game_number = re.findall(r'Game (\d+)*', string)
        # print(game_number)
        pulls = re.findall(r'(\d+) (\w+)', string)
        # print(pulls)
        # valid = True
        for pull in pulls:
            if int(pull[0]) > min_values[pull[1]]:
                min_values[pull[1]] = int(pull[0])
        power_set.append(min_values['red'] * min_values['blue'] * min_values['green'])

    total = sum(power_set)
    print('total: ', total)


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Advent of code!')

    # Add a positional argument for the filename
    parser.add_argument('--filename', '-f', help='Name of the input file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print the name of the file
    print(f'input file is: {args.filename}')
    values = []
    with open(args.filename, 'r', encoding='utf-8') as f:
        values = f.readlines()
    day_2(values)


if __name__ == '__main__':

    main()
