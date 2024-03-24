import sys


if __name__ == '__main__':
    # print(sys.argv, len(sys.argv))
    if len(sys.argv) > 2:
        print('AssertionError: more than one argument is provided')
        exit()
    if len(sys.argv) == 1:
        exit()
    try:
        int_value = int(sys.argv[1])
        if int_value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print('AssertionError: argument is not an integer')
        exit()
