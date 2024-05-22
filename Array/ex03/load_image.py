import numpy as np
import cv2


def ft_load(path: str) -> np.array:
    """
    This function takes a string and returns a numpy array.
    """
    try:
        open(path, 'r')
        a = np.array(cv2.imread(path))
        print(f"Shape of the image is {a.shape}")
        print(a)
        return a
    except FileNotFoundError as e:
        print(f"Error: File '{path}' does not exist.")
        exit(e.errno)
    except Exception as e:
        print(f"Error: {e}.")
        exit(e.errno)
