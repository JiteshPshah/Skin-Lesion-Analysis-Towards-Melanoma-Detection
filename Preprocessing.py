#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:28:21 2017

@author: edward
"""


import cv2
import os
def load_images(folder):
        image_list=[]
        for filename in sorted(os.listdir(folder)):
            img=cv2.imread(os.path.join(folder,filename))
            image_list.append(img)
        return image_list
def resize_images(images):
    resize_image=[]
    for image in images:
        imag=cv2.resize(image,(64,64))
        resize_image.append(imag)
    return resize_image

def RemoveBackground(Image):
    IGray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    ret,BW=cv2.threshold(IGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret1,thresh1 = cv2.threshold(th,127,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(BW,127,255,cv2.THRESH_BINARY_INV)
    maskedImage=cv2.bitwise_and(Image,Image,mask=thresh2)
    return maskedImage

def save_images(Image):
    for i in range(1,len(Image)+1):
        cv2.imwrite(('imageresized_{}.jpg'.format(i)),Image[i-1])
        
