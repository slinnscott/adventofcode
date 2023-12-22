import argparse


def day_n(values):
    pass


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
    day_n(values)


if __name__ == '__main__':

    main()
