from PIL import Image

def check_image(path):
	try:
		Image.open(path)
	except IOError:
		return False
	return True