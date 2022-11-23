#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:50:59 2019

@author: loued
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:04:56 2019

@author: loued
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pylab as pl
import os
import numpy as np
import numpy.matlib 
from PIL import Image
import cv2
import glob
import random
import re
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard

def Thanks(mywin):
        
    ThankYou =  visual.TextStim(win=mywin, text=('Thank you for participating.'),font='', pos=(2.5, 1),
    depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
    ori=1.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
    fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)

    
    return (ThankYou)