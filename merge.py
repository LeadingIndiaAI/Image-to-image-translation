import cv2
import numpy as np
img1 = cv2.imread('C:/Users/Shanmukha Yenneti/Desktop/sp (2).jpg')
img2 = cv2.imread('C:/Users/Shanmukha Yenneti/Desktop/sketchesshr.png')
vis = np.concatenate((img1, img2), axis=1)
cv2.imwrite('out.jpg', vis)
