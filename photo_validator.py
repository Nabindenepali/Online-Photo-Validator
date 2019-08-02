import os.path
import argparse
import cv2

import file_format_check
import file_size_check
import blur_check
import head_check
import background_check
import grey_black_and_white_check
import logging
import time

logging.basicConfig(level=logging.INFO)

def main():
    initial = time.time()
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, help='Path to image file')

    # Read the image path from the argument
    args = vars(ap.parse_args())
    imgPath = args['image']

    # Check if the file exists
    if not os.path.isfile(imgPath):
        logging.info("The specified file does not exist")
        exit()

    # Check image file format
    is_file_format_valid = file_format_check.check_image(imgPath)
    logging.info("File format check: " + ('Passed' if is_file_format_valid else 'Failed'))

    if not is_file_format_valid:
        exit()

    # Check image file size
    is_file_size_valid = file_size_check.check_image(imgPath)
    logging.info("File size check: " + ('Passed' if is_file_format_valid else 'Failed'))

    if not is_file_size_valid:
        exit()

    # Load the image
    img = cv2.imread(imgPath)

    is_corrupted = file_format_check.is_corrupted_image(img)
    logging.info("File Open Test: " + ('Passed' if not is_corrupted else 'Failed'))
    if file_format_check.is_corrupted_image(img):
        exit()

    logging.info("Greyscale check: " + ('Passed' if not grey_black_and_white_check.is_grey(img) else 'Failed'))

    # Check image for blurness
    is_blur = blur_check.check_image_blurness(img)
    logging.info("Blurness check: " + ('Passed' if not is_blur else 'Failed'))

    # Check the background of image
    is_background_ok = background_check.background_check(img)
    logging.info("Background check: " + ('Passed' if is_background_ok else 'Failed'))

    # Check image for head position and coverage
    is_head_valid = head_check.valid_head_size(img)
    logging.info("Head check: " + ('Passed' if is_head_valid else 'Failed'))

    #Check Eye Covered
    is_eye_covered = head_check.is_eye_covered(img)
    logging.info("Eye check: " + ('Passed' if not is_eye_covered else 'Failed'))

    # Display the imported image
    # cv2.imshow('Application Photo', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    final = time.time()
    logging.info("Total time in second = "+ str(final-initial))

if __name__ == '__main__':
    main()