import sys
from ft_filter import filter_function


def main():
    '''
    Main entry point for the script.
    '''
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    try:
        iterable = sys.argv[1].split()
        print(filter_function(iterable, lambda x: len(x) > int(sys.argv[2])))
    except ValueError:
        print('AssertionError: the arguments are bad')


if __name__ == '__main__':
    main()
