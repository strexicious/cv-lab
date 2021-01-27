import numpy as np
import cv2 as cv

ORIG_IMG = "images/home.jpg"
OTHE_IMG = "images/home_dist.jpg"

img = cv.imread(ORIG_IMG)
imgo = cv.imread(OTHE_IMG)

rows, cols = img.shape[:2]

def mouse_cb(ev, x, y, flags, udata):
	if ev == cv.EVENT_LBUTTONDOWN:
		udata.append((x, y))

# read coordinates of pixels in original image
pts1 = []
cv.imshow(ORIG_IMG, img)
cv.setMouseCallback(ORIG_IMG, mouse_cb, pts1)
cv.waitKey()
cv.destroyWindow(ORIG_IMG)

# read corresponding pixels coordinates in other image in same order
pts2 = []
cv.imshow(OTHE_IMG, imgo)
cv.setMouseCallback(OTHE_IMG, mouse_cb, pts2)
cv.waitKey()
cv.destroyWindow(OTHE_IMG)

# we want to transform other image to original
M = cv.getAffineTransform(np.float32(pts2), np.float32(pts1))
dst = cv.warpAffine(imgo, M, (cols,rows))
cv.imshow("transformed", dst)
cv.waitKey()
cv.destroyAllWindows()
