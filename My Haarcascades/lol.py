import cv2
import os
#import matplotlib.pyplot as plt

file =  os.listdir('guitars')
print(file[0])
guit = 'guitars'+file[0]
img = cv2.imread('guit',guit) #access from different directory :P
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()