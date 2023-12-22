import argparse


def day_1(values):
    dictionary = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    output = []
    for string in values:
        numbers = []
        current_str = ''
        for char in string:
            if char.isnumeric():
                numbers.append(char)
                current_str = ''
            else:
                current_str += char
                if current_str[-3:] in dictionary.keys():
                    numbers.append(dictionary[current_str[-3:]])
                if current_str[-4:] in dictionary.keys():
                    numbers.append(dictionary[current_str[-4:]])
                if current_str[-5:] in dictionary.keys():
                    numbers.append(dictionary[current_str[-5:]])
        output.append(int(numbers[0] + numbers[-1]))
    print(output)
    total = sum(output)
    print(total)


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
    day_1(values)


if __name__ == '__main__':

    main()
