import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a list and two indices, start and end.
    It returns a new list containing the elements of
    the original list from start to end.
    """
    try:
        assert start < len(family) and end <= len(family), \
            "Indices out of range"
        assert isinstance(family, list), \
            "Input must be a list"
        assert isinstance(start, int) and isinstance(end, int), \
            "Indices must be integers"
    except AssertionError as e:
        print(e)
        exit(1)
    arr = np.array(family)
    print(f"My shape is {arr.shape}")
    arr = arr[start:end]
    print(f"My new shape is {arr.shape}")
    return arr.tolist()
