import sys

def isaplhanumeric(context):
    """
    Check if the context is alphanumeric digit or space ? true : false
    """
    for i in context:
        if i.isalpha() or i.isalnum() or i.isspace():
            continue
        else:
            return False
    return True

def main():
    """
    Main function
    translate alphanumeric characters to morse code (argv[1])
    else return AssertionError
    """
    if len(sys.argv) < 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    context = sys.argv[1]
    if not isaplhanumeric(context):
        print("AssertionError: the arguments are bad")
        sys.exit(1)
        
    NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    }
    
    print("".join([' ' + NESTED_MORSE[i.upper()] for i in context])[1:])

if __name__ == '__main__':
    main()
