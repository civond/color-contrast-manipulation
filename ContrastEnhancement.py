import numpy as np
import cv2
import matplotlib.pyplot as plt

#Question 2a
Image_Path = 'C:/Users/doria/OneDrive/Desktop/Storage/School/ECE 6123 Image Processing/hw/color-contrast-manipulation/sample2.jpg'
img = cv2.imread(Image_Path);

cv2.imshow('low contrast image',img)
cv2.waitKey(0)

#Question 2b
def histogram():
    ax1 = plt.subplot(1,2,1)
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)
    ax1.title.set_text('Low Contrast Image')
    plt.imshow(img,cmap=plt.cm.gray)
    ax2 = plt.subplot(1,2,2)
    plt.hist(img.ravel(),256,[0,256])
    ax2.title.set_text('Histogram')
    plt.savefig('images/sample_histogram.jpg')
    #plt.show()
#histogram()

#Question 2c
def cdf2():
    # Calculate the histogram and corresponding bins
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    # Calculate the cdf and normalize the values to 0-255
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    plt.hist(cdf_normalized)
    plt.show()
cdf2()
#Question 2d
def cdf():
    # Calculate the histogram and corresponding bins
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    # Calculate the cdf and normalize the values to 0-255
    cdf = hist.cumsum()
    cdf_normalized = cdf * 255 / cdf[-1]
    # Replace the vales with normalized cdf values
    img_histeq = cdf_normalized[img]

    ax1 = plt.subplot(1, 2, 1)
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)
    plt.imshow(img_histeq.astype('uint8'),cmap=plt.cm.gray)
    ax1.title.set_text('Normalized Image')
    ax2 = plt.subplot(1, 2, 2)
    ax2.title.set_text('Histogram')
    plt.hist(img_histeq.ravel(), 256, [0, 256])
    plt.savefig('images/cdf_transformation_histogram.jpg')
    #plt.show()
#cdf()