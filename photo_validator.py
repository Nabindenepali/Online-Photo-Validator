import os.path
import argparse
import cv2

import file_format_check
import file_size_check
import blur_check
import background_check
import logging


logging.basicConfig(level=logging.INFO)

def main():
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

	# Check image for blurness
	is_blur = blur_check.check_image(img)
	logging.info("Blurness check: " + ('Passed' if not is_blur else 'Failed'))

	# Check the background of image
	is_background_ok = background_check.background_check(img)
	logging.info("Background check: " + ('Passed' if is_background_ok else 'Failed'))


	# Display the imported image
	cv2.imshow('Application Photo', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()