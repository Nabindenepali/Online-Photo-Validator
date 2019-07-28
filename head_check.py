import numpy as np
import cv2

def head_percentage(image):
	gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Load cascade classifier training file for haarcascade
	haar_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

	# Detect multiscale (some images may be closer to camera than others) images
	faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5);

	# Return false if there are more than one faces in the picture
	if len(faces) > 1:
		return False

	# Get the only face data	
	face = faces[0]
	width = face[2]
	height = face[3]

	# Calculate head percentage based on face percentage, multiplied by 1.25 to assume 80% of head is face
	head_percentage = (width*height)/(image.shape[0]*image.shape[1]) * 1.25 * 100

	# Image is valid if head percentage is between 30% and 50%
	if 30 <= head_percentage <= 50:
		return True
	return False

def check_image(image):
    if not head_percentage(image):
    	return False
    return True

