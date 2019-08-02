from PIL import Image

def check_image(path):
	try:
		img = Image.open(path)
		format = img.format
		return format == 'JPEG' or format == 'PNG'
	except IOError:
		return False



def is_corrupted_image(img):
	try:
		w, h, channel = img.shape
		return False
	except:
		return True
