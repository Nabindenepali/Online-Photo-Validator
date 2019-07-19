import argparse
import cv2

def main():
	ap = argparse.ArgumentParser()
	ap.add_argument('-i', '--image', required=True, help='Path to image file')

	# Read the image path from the argument
	args = vars(ap.parse_args())
	imgPath = args['image']

	# Load the image in color
	img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

	# Display the imported image
	cv2.imshow('Application Photo', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()