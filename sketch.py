import imageio
img="C:/Users/Shanmukha Yenneti/Desktop/rr.jpeg"
start_img = imageio.imread(img)

#Y= 0.299 * R + 0.587 * G + 0.114 * B
import numpy as np
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
gray_img = grayscale(start_img)
inverted_img = 255-gray_img
import scipy.ndimage
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=30)
def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')
final_img= dodge(blur_img,gray_img)
import matplotlib.pyplot as plt
plt.imshow(final_img, cmap="gray")
plt.imsave('C:/Users/Shanmukha Yenneti/Desktop/finalr.jpg', final_img, cmap='gray', vmin=0, vmax=255)
