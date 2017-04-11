#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:28:21 2017

@author: edward
"""

import cv2
import os
from PIL import Image
def load_images(folder):
        image_list=[]
        for filename in sorted(os.listdir(folder)):
            img=cv2.imread(os.path.join(folder,filename))
            image_list.append(img)
        return image_list
        print "Images are loaded"

def RemoveBackground(Image):
    IGray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    ret,BW=cv2.threshold(IGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret1,thresh1 = cv2.threshold(th,127,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(BW,127,255,cv2.THRESH_BINARY_INV)
    maskedImage=cv2.bitwise_and(Image,Image,mask=thresh2)
    return maskedImage

def Resize_Images(path,path2):
    for x in os.listdir(path):
        base = x
        x=path + '/' + x
    
    	if os.path.isdir(x) == True:
		print "Skipping directory " + x
		continue
        print x
	im1 = Image.open(x)
	im2 = im1.resize((64, 64))    
	im2.save(path2+"/"+base)
    print "Images are stored at {}".format(path2) 
