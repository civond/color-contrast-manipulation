import numpy as np
import cv2
import matplotlib as plt

Image_Path = 'C:/Users/doria/OneDrive/Desktop/Storage/School/ECE 6123 Image Processing/hw/color-contrast-manipulation/sample.jpg'
img = cv2.imread(Image_Path);
imS = cv2.resize(img, (450, 540));
#imS = cv2.resize(img, (400, 540));

#Question 1a
def RGB():
    blue, green, red = cv2.split(imS)

    # define channel having all zeros
    zeros = np.zeros(blue.shape, np.uint8)

    # merge zeros to make BGR image
    blueBGR = cv2.merge([blue,zeros,zeros])
    greenBGR = cv2.merge([zeros,green,zeros])
    redBGR = cv2.merge([zeros,zeros,red])

    #Display RGB image
    cv2.imshow('RGB', imS)
    cv2.waitKey(0)

    RGB_split = np.concatenate((redBGR, blueBGR, greenBGR), axis=1)

    #Display RGB split
    cv2.imshow('RGB Split', RGB_split)
    cv2.imwrite('images/RGBsplit_sample2.jpg', RGB_split)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
RGB()

#Question 1b
def HSV():
    hsv_img = cv2.cvtColor(imS, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    hsv_split = np.concatenate((h, s, v), axis=1)

    #Display HSV
    cv2.imshow('HSV Img', hsv_img)
    cv2.imwrite('images/hsv_sample.jpg',hsv_img)
    cv2.waitKey(0)

    #Display split HSV
    cv2.imshow("Split HSV", hsv_split)
    cv2.imwrite('images/HSVsplit_sample.jpg', hsv_split)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
#HSV()

#Question 1c
def blue_pixels():
    hsv = cv2.cvtColor(imS, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # blue colored objects are stored in res
    res = cv2.bitwise_and(imS, imS, mask=mask)

    #Display blue pixels in white
    cv2.imshow('mask', mask)
    cv2.imwrite('images/maskBlue_sample.jpg', mask)
    cv2.waitKey(0)

    #Display blue pixels in blue
    cv2.imshow('res', res)
    cv2.imwrite('images/resBlue_sample.jpg', res)
    cv2.waitKey(0)
#blue_pixels()