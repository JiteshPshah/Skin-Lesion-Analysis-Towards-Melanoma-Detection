#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:28:21 2017

@author: edward
"""


import cv2
import os
import matplotlib.pyplot as plt

def load_images(folder):
        image_list=[]
        for filename in os.listdir(folder):
            img=cv2.imread(os.path.join(folder,filename))
            if img is not None:
                image_list.append(img)
        return image_list

def resize_images(load_images(folder)):
    resize_image=[]
    for image in images:
        imag=cv2.resize(image,(512,512))
        resize_image.append(imag)
    return resize_image

Resizedimages=resize_images(images)

def save_images():
    for i in range(1,len(A)+1):
        cv2.imwrite(('imageresized_{}.jpg'.format(i)),Resizedimages[i-1])