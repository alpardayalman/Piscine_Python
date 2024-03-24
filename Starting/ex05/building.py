import sys


def printAnalysis(object: str) -> None:

    """
    argument object is a string and this function returns nothing
    Prints upper lower punctuation spaces digits and number of characters
    """
    print(f'The text contains {len(object)} characters:')
    print(f'{len([i for i in object if i.isupper()])} upper letters')
    print(f'{len([i for i in object if i.islower()])} lower letters')
    u = 0
    for i in object:
        if i in "!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~":
            u += 1
    print(f"{u} punctuation marks")
    print(f'{len([i for i in object if i.isspace()])} spaces')
    print(f'{len([i for i in object if i.isdigit()])} digits')


def main():
    """
    Only 1 argv: if more Throw AssertionError.
    argv[1] = single string argument
    print: sum of upper_case lower_case punctuation spaces digits
    1: without argument program does the same thing with an input
    """
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        exit()
    object = None
    try:
        object = sys.argv[1]
    except IndexError:
        object = input("What is the text to count?\n")
    printAnalysis(object)


if __name__ == '__main__':
    main()
