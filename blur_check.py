import cv2

def check_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    value = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    if(value<100):
        return True
    else:
        return False

