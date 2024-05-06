class Deque:
    """
    Deque class
    write a class that implements a deque (double-ended queue) in Python. 
        It should have the following methods:
    - add_first(item): Add an item to the front of the deque.
    - add_last(item): Add an item to the end of the deque.
    - remove_first(): Remove the first item in the deque and return it.
    - remove_last(): Remove the last item in the deque and return it.
    - is_empty(): Return True if the deque is empty, and False otherwise.
    - size(): Return the number of items in the deque.
    - peek_first(): Return the first item in the deque without removing it.
    - peek_last(): Return the last item in the deque without removing it.
    - display_deque(): Print the items in the deque from first to last,
        all on one line.
    """
    def __init__(self):
        self.elements = []

    def __add__(self, item):
        if isinstance(item, Deque):
            for i in item.elements:
                self.add_first(i)
            return self

    def add_first(self, item):
        if isinstance(item, Deque):
            self.elements.extend(reversed(item.elements))
        else:
            self.elements.append(item)

    def add_last(self, item):
        self.elements.insert(0, item)

    def remove_first(self):
        return self.elements.pop()

    def remove_last(self):
        return self.elements.pop(0)

    def is_empty(self):
        return (len(self.elements) == 0)

    def size(self):
        return len(self.elements)

    def peek_first(self):
        return self.elements[-1]

    def peek_last(self):
        return self.elements[0]

    def display_deque(self):
        print('\t | \t'.join(str(item) for item in self.elements))
