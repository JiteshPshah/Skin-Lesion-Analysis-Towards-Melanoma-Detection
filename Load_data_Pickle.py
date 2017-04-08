#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:55:39 2017

@author: edward
"""

import os
import Tkinter as tk
import tkFileDialog
from PIL import Image
import cPickle
import numpy
import time
#import hickle
tk.Tk().withdraw()
path=tkFileDialog.askdirectory()
print path
#path = '/path/to/file'

# we use Python Imaging Library to read the jpeg file
# we store the read image as a numpy array

# routine to recursively traverse a folder and save list of file names

#def main():


#fileList = [os.path.join(dirpath, f)
#	for dirpath, dirnames, files in os.walk(path)
#	for f in files if f.endswith('.jpg')]
def load_images(folder):
        image_list=[]
        for filename in sorted(os.listdir(folder)):
            filename=os.path.join(folder,filename)
            image_list.append(filename)
        return image_list
#fileList=sorted(os.listdir(path))
fileList=load_images(path)
print "Preparing your pickle files. Pls wait..."
t0 = time.time()
for file_ in fileList:
    #nonlocal arr        
	print file_
	img = Image.open(file_)

	# the next two lines use cPickle or the hickle to store the array
	# for simplicity, I just commented out either one to choose
cPickle.dump(img,open(file_+"prot0"+".pkl","wb"),protocol=0)
	#	hickle.dump(arr,file_+"-prot"+".hkl",mode='w')

t1=time.time()
total = t1-t0
print "P(h)ickling execution time: %.2f sec" % total

	# routine to recursively traverse a folder and save list of file names
tk.Tk().withdraw()
path3=tkFileDialog.askdirectory()
#print path3
pklList = [os.path.join(dirpath, f)
	for dirpath, dirnames, files in os.walk(path3)
	for f in files if f.endswith('.pkl')]

	# here we load the pickle file back into memoryss
t3 = time.time()
for file_ in pklList:
	arr2 = cPickle.load(open(file_,"rb"))
	#print arr2.shape
	img2 = Image.fromarray(numpy.squeeze(arr2))
	img2.save(file_ +'.jpg')
	print file_ + '.jpg'


t4=time.time()

total2 = t4-t3

print "Unp(h)ickling execution time: %.2f sec" % total2

#if __name__ == "__main__":
#	main()