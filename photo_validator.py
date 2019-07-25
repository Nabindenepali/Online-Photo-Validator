import os.path
import argparse
import cv2

import file_format_check
import blur_check

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument('-i', '--image', required=True, help='Path to image file')

	# Read the image path from the argument
	args = vars(ap.parse_args())
	imgPath = args['image']

	# Check if the file exists
	if not os.path.isfile(imgPath):
		print("The specified file does not exist")
		exit()

	# Check image file format
	is_file_format_valid = file_format_check.check_image(imgPath)
	print("File format check: " + ('Passed' if is_file_format_valid else 'Failed'))

	if not is_file_format_valid:
		exit()

	# Load the image in color
	img = cv2.imread(imgPath)

	# Check image for blurness
	is_blur = blur_check.check_image(img)
	print("Blurness check: " + ('Passed' if not is_blur else 'Failed'))

	# Display the imported image
	cv2.imshow('Application Photo', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()