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

logging.basicConfig(level=logging.INFO)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--directory', required=True, help='Path to directory containing images')

    # Read the directory path from the argument
    args = vars(ap.parse_args())

    directory = args['directory']

    fileLists= os.listdir(directory)

    error_message = {}
    for image in fileLists:

        messages = []

        # Check image file format
        is_file_format_valid = file_format_check.check_image(directory+"/"+ image)
        if not is_file_format_valid:
            messages.append("File format check failed")
            error_message[image]= messages

            continue

        is_file_size_valid = file_size_check.check_image(directory+"/"+ image)
        if not is_file_size_valid:
            messages.append("File size check failed")
            error_message[image] = messages
            continue

        # Load the image
        img = cv2.imread(directory+"/"+ image)

        #Check for grey image
        if grey_black_and_white_check.is_grey(img):
            messages.append("GreyScale Check Failed")

        # Check image for blurness
        if blur_check.check_image_blurness(img):
            messages.append("Blurness Check Failed")


        # Check the background of image
        if not background_check.background_check(img):
            messages.append("Background check failed")

        # Check image for head position and coverage

        if not background_check.background_check(img):
            messages.append("Head check Faied")

        if len(messages)>0:
            error_message[image] = messages

        # Display the imported image
        # cv2.imshow('Application Photo', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    if(len(error_message)>0):
        print("Following are invalid images with reasons: \n")
        print(error_message)
    else:
        print("There are no invalid images")

if __name__ == '__main__':
    main()