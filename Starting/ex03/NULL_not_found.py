def NULL_not_found(object: any) -> int:
    null_values = [None, "null", 0, False, '', "", 'nan']

    if object in null_values or object != object:
        if object == None:
            print("Nothing : ",end="")
        elif isinstance(object, float):
            print("Cheese : ",end="")
        elif isinstance(object, bool):
            print("Fake: ",end="")
        elif isinstance(object, int):
            print("Zero : ",end="")
        elif isinstance(object, str):
            print("Empty : ",end="")
        print(f"{object} {type(object)}")
        return 0

    print("Type not Found")
    return 1