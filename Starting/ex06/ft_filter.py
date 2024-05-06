def filter_function(iterable, predicate):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    try:
        if not callable(predicate):
            raise TypeError("predicate must be a callable object")

        return [element for element in iterable if predicate(element)]
    except TypeError as e:
        print(f"Error: {e}")
    return []
