import os
import cv2
from load_image import ft_load
import sys


def main(image_path: str = "../animal.jpeg"):
    """
    This function loads an image and crops it to a specific region.
    Transpose the image and display it.
    """

    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        return
    img = ft_load(image_path)
    if img is None:
        print("""
Error: Unable to load image. Check the file path and file integrity.""")
        return
    h, w = img.shape[:2]
    ci = img[int(h/4)-50:int(h/4)+350, int(w/4)+170:int(w/4)+570]
    ci = cv2.cvtColor(ci, cv2.COLOR_BGR2GRAY)

    single_column = ci.reshape(400, 400, 1)
    print(f"The shape of image is: {single_column.shape}")
    print(single_column)
    print(f"New shape after Transpose: {ci.T.shape}")
    print(ci.T)

    cv2.imshow("Zoomed", ci.T)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
