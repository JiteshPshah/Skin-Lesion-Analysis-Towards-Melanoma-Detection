#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
I=cv2.imread('imageresized_16.jpg')

def RemoveBackground(Image):
    IGray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    ret,BW=cv2.threshold(IGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret1,thresh1 = cv2.threshold(th,127,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(BW,127,255,cv2.THRESH_BINARY_INV)
    maskedImage=cv2.bitwise_and(Image,Image,mask=thresh2)
    return maskedImage,IGray

BGImage,A=RemoveBackground(I)
#cv2.imshow("BGRImage",BGImage)
#cv2.waitKey()