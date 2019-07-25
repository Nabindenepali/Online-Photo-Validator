import os.path

def check_image(path):
	size = os.path.getsize(path)
	
	# Check if the size of the file is greater than 1MB or not
	if size < 1024*1024:
		return True
	return False