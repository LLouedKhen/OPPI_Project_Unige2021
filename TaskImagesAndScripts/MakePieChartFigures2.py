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
labels = 'Pain', 'No Pain'
sizes = [8, 792]
colors = ['black', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig1 = plt.gcf()
fig1.savefig('Pain10.tiff', bbox_inches='tight', dpi = 300)
plt.axis('equal')
plt.show()



#Pie 25%
labels = 'Pain', 'No Pain'
sizes = [200, 600]
colors = ['black', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig2 = plt.gcf()
fig2.savefig('Pain25.tiff', bbox_inches='tight', dpi = 300)
plt.axis('equal')
plt.show()



#Pie 50%
labels = 'Pain', 'No Pain'
sizes = [400, 400]
colors = ['black', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig3 = plt.gcf()
fig3.savefig('Pain50.tiff', bbox_inches='tight', dpi = 300)
plt.axis('equal')
plt.show()



#Pie 75%
labels = 'Pain', 'No Pain'
sizes = [600, 200]
colors = ['black', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig4 = plt.gcf()
fig4.savefig('Pain75.tiff', bbox_inches='tight', dpi = 300)
plt.axis('equal')
plt.show()



#Pie 75%
labels = 'Pain', 'No Pain'
sizes = [792, 8]
colors = ['black', 'gold']

# Plot
plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=90,   wedgeprops   = { 'linewidth' : 1,'edgecolor' : "black" })
fig5 = plt.gcf()
fig5.savefig('Pain90.tiff', bbox_inches='tight', dpi = 300 )
plt.axis('equal')
plt.show()

