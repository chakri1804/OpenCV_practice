import numpy as numpy
import cv2

img1 = cv2.imread('spongegar.jpg')
img2 = cv2.imread('spongebob.jpg')

# add = img1+img2 #overlap images
# add = cv2.add(img1,img2) # add pixel values

rows, cols, channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #converting the image to grayscale
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) # making the mask by setting the threshold and inverting them colors

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
# dst = cv2.add(img1_bg,img2_fg) # add pixel values
dst = img1_bg + img2_fg
weighted = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
#cv2.imshow('weighted',weighted)
#cv2.imshow('mask',mask_inv)
cv2.imshow('lol',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()