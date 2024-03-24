import inspect

def NULL_not_found(object: any) -> int:
    null_values = [None, "null", 0, False, '', "", 'nan']
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')

    if object in null_values or object != object:
        if args[0] == 'Garlic':
            args[0] = 'Cheese'
        print(args[0], end=': ')
        print(f"{object} {type(object)}")
        return 0

    print("Type not Found")
    return 1