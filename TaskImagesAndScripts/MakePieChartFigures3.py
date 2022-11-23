#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:21:26 2019

@author: loued
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:18:03 2019

@author: loued
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pylab as pl
import os
import numpy as np
from PIL import Image
import cv2

ImgPath = '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images'
os.chdir(ImgPath)


#Make Pie charts
# Pain 10%

sizes = [8, 792]
colors = ['firebrick', 'grey']

# Plot
plt.pie(sizes, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig1 = plt.gcf()
fig1.set_facecolor('grey')
fig1.savefig('Pain10.tiff',  transparent=True, dpi = 300)
plt.axis('equal')
plt.show()



#Pie 25%

sizes = [200, 600]
colors = ['firebrick', 'grey']

# Plot
plt.pie(sizes, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig2 = plt.gcf()
fig2.set_facecolor('grey')
fig2.savefig('Pain25.tiff',  transparent=True, dpi = 300)
plt.axis('equal')
plt.show()



#Pie 50%

sizes = [400, 400]
colors = ['firebrick', 'grey']

# Plot
plt.pie(sizes, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig3 = plt.gcf()
fig3.set_facecolor('grey')
fig3.savefig('Pain50.tiff',  transparent=True, dpi = 300)
plt.axis('equal')
plt.show()



#Pie 75%

sizes = [600, 200]
colors = ['firebrick', 'grey']

# Plot
plt.pie(sizes, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig4 = plt.gcf()
fig4.set_facecolor('grey')
fig4.savefig('Pain75.tiff',  transparent=True, dpi = 300)
plt.axis('equal')
plt.show()



#Pie 75%

sizes = [792, 8]
colors = ['firebrick', 'grey']

# Plot
plt.pie(sizes, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig5 = plt.gcf()
fig5.set_facecolor('grey')
fig5.savefig('Pain90.tiff',  transparent=True, dpi = 300 )
plt.axis('equal')
plt.show()

