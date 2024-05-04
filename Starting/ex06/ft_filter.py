def filter_function(iterable, predicate):
    """Filters elements from an iterable based on a predicate function.

    Args:
        iterable: The iterable to filter (list, tuple, string, etc.).
        predicate: A function that takes an element from the iterable and
            returns True if the element should be included, False otherwise.

    Returns:
        A list containing the filtered elements from the iterable.

    Raises:
        TypeError: If either iterable or predicate is not a callable type.
    """
    try:
        if not callable(predicate):
            raise TypeError("predicate must be a callable object")

        return [element for element in iterable if predicate(element)]
    except TypeError as e:
        print(f"Error: {e}")
    return []
