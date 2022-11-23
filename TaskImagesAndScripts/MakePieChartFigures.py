#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:05:30 2019
Try blend pain intensity (lightning bolts) with pie charts

@author: loued
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pylab as pl
import os
import numpy as np
from PIL import Image
import cv2
import glob
import random

ImgPath = '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images'
os.chdir(ImgPath)
StimPath = '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images/Stim'

PieChartList= glob.glob('Pain*.tiff')
PieChartList=sorted(PieChartList , key=lambda x: (x[0].isdigit(), x))
PainIList = glob.glob('Bolt*.png')
PainIList=sorted(PainIList , key=lambda x: (x[0].isdigit(), x))


for i in range(0, len(PieChartList)):
    for j in range(0, len(PainIList)):
        background = Image.open(PieChartList[i])
        print(background.size)
        overlay = Image.open(PainIList[j])
        print(overlay.size)
        size =background.size
        size1 = int(size[0]/2)
        size2 = int(size[1]/2)
        newSize =(size1, size2)
        background = background.resize(newSize, Image.ANTIALIAS)
        size =overlay.size
        size1 = int(size[0]/3)
        size2 = int(size[1]/3)
        newSize =(size1, size2)
        overlay = overlay.resize(newSize, Image.ANTIALIAS)
#        x = random.randrange(0, 1000, 100)
        xx = [100, 700]
        yy = [100, 400]
        x = random.choice(xx)
        y = random.choice(yy)
        print(x)
        print(y)
        background.paste(overlay, (x, y), overlay)
        num1 = str(i +1)
        num2 = str(j +1)
        os.chdir(StimPath)
        background.save('Stim' + num2 + num1,  "PNG")   
        os.chdir(ImgPath)