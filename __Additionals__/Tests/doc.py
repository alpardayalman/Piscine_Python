def greet(name):

    """Greets the person with the provided name

    Args:
        name: The name of the person to greet

    Returns:
        A greeting message
    """
    return f"Hello, {name}!"


class Animal:
    """Represents a general animal"""

    def identify(self):

        """Prints a generic identification message"""
        print("This is an animal")


class Dog(Animal):

    def identify(self):

        """Prints a specific identification message for a dog"""
        print("Woof! I am a dog")


if __name__ == "__main__":
    message = greet("Alice")
    print(greet.__doc__)
    my_dog = Dog()

    print(my_dog.identify.__doc__)
    print(Animal.__doc__)
