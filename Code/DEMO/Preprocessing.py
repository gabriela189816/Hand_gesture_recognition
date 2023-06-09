"""
Created on Friday Apr 07 00:15:00 2023

@author: Gabriela Hilario Acuapan & Luis Alberto Pineda Gómez
File: Preprocessing.py
Comments: Preprocessing of images.
            ------------------------- Steps --------------------------
            (1) Binarize the loaded image
            (2) Obtain and draw the contours of the image
            (3) Crop of the image
            (4) Resize of the image to the standard 200 x 200 pixels
            (5) Save all the images in the standard size
"""

# --- IMPORT LIBRARIES ---
import os
import numpy
import numpy as np
import cv2 as cv

# PATH TO READ THE IMAGES
# path ="C:/Users/gabri/OneDrive/Documentos/GitHub/Hand_gesture_recognition/Final_DEMO"
# list_dir = os.listdir(path)
# print("Total amount of files in the current directory:", len(list_dir))

def img_prepro(input_image):
    # LOAD THE INPUT IMAGE
    path = "/Users/lapg/Documents/2do Cuatrimestre/Vision/Proyecto-Hand-Recognition/Pruebas/"
    list_dir = os.listdir(path)
    print("Total amount of files in the current directory:", len(list_dir))
    image = cv.imread(str(path)+str(input_image), cv.IMREAD_GRAYSCALE)

    if type(image) is numpy.ndarray:
        original = image.copy()
        threshold_value, threshold = cv.threshold(image, 20, 255, cv.THRESH_BINARY)
        cv.imshow('Binarized Image', threshold)
        cv.waitKey(0)
        cv.destroyAllWindows()
        # --- FIND THE CONTOURS OF THE CURRENT IMAGE ---
        contours, hierarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

        # --- DRAWING THE CONTOURS OF THE IMAGE ---
        image_color = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
        copy = image_color.copy()  # This copy of the color image is used for the bounding rectangle.
        cv.drawContours(image_color, contours, -1, (255, 0, 0), 2)
        # cv.imshow('CONTOURS OF THE IMAGE', image_color)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
        value = 0
        num = 0
        for contour in range(len(contours)):
            if len(contours[contour]) > value:
                num = contour
                value = len(contours[contour])
            else:
                pass
        # --- BOUNDING RECTANGLE ---
        x, y, w, h = cv.boundingRect(contours[num])
        # --- DRAW THE BOUNDING RECTANGLE ---
        cv.rectangle(copy, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print(x, y, w, h)
        cv.imshow('BOUNDING BOX', copy)
        cv.waitKey(0)
        cv.destroyAllWindows()

        # --- CROPPING OFF THE IMAGE ---
        boundrie = 10
        if x <= 10:
            crop = original[y:y + h, x:x + w]
        else:
            crop = original[y - boundrie:y + h + boundrie, x - boundrie:x + w + boundrie]
        print("The dimensions of the cropped image are: ", np.shape(crop))
        # cv.imshow('CROPPED IMAGE', crop)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        # --- RESIZE OF THE IMAGE ---
        # Resize of the cropped image
        height = 200
        width = 200
        dim = (height, width)
        frame = cv.resize(crop, dim, interpolation=cv.INTER_AREA)
        print("The dimensions of the new resized image are:,", np.shape(frame))
        cv.imshow('RESIZED IMAGE', frame)
        cv.waitKey(0)
        cv.destroyAllWindows()

        save = input()
        if save == 's':
            cv.imwrite('Resized_image.png', frame)
            print("Saved frame")
        else:
            print('Try again!')

input_image = "1Input_image.png"
img_prepro(input_image)