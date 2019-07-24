# import the necessary packages
from imutils import paths
import argparse
import cv2


def variance_of_laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    value = cv2.Laplacian(gray, cv2.CV_64F).var()
    print("value",value)
    if(value<100):
        return "blur"
    else:
        return "not blur"

