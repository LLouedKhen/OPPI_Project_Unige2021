#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:05:06 2019
Assign target and relevant instructions 
@author: loued
"""

import os
import numpy as np
import numpy.matlib 
import glob 
import random
import re
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard

def targetSelection(mywin, stimPath, thisBlock):

 
    
    os.chdir(stimPath)
    
    if thisBlock == 1:
        condition = "_self"
        targetPic = 'Self.jpg'
        target = 1
        instrText =  visual.TextStim(win=mywin, text='In the following experiment, you will face the possibility of experiencing pain. \n  How likely you are to experience pain, and which level of pain you are facing, will be indicated by an initial cue.\n You will then have the chance to reduce or try to avoid the possible pain.\n You will then be asked to rate the pain delivered.\n\n', 
        font='', pos=(0, 0),depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', ori=0.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
        fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
        targetImage = visual.ImageStim(win=mywin, name='Self', ori =90, pos = (-10, -10),
        image=targetPic, mask=None)
        targetImage.size = [targetImage.size[0]/8, targetImage.size[1]/12]
        instrText.draw()
        targetImage.draw()
        mywin.flip()
        keys = event.waitKeys()

    elif thisBlock == 2:
        condition = "_cother"
        targetPic = 'Cother.jpg'
        target = 2
        instrText =  visual.TextStim(win=mywin, text='In the following experiment, you will face the possibility that your spouse will be in pain. \n  How likely that is, and which level of pain, will be indicated by an initial cue.\n You will then have the chance to reduce or try to avoid pain for your spouse.\n You will then be asked to rate the pain delivered.\n\n', 
        font='', pos=(0, 0),depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', ori=0.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
        fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
        targetImage = visual.ImageStim(win=mywin, name='CloseOther', ori = 0, pos = (-10, -10),
        image=targetPic, mask=None)
        targetImage.size = [targetImage.size[0]/6, targetImage.size[1]/8]
        instrText.draw()
        targetImage.draw()
        mywin.flip()
        keys = event.waitKeys()
        
    elif thisBlock == 3:
        condition = "_dother"
        targetPic = 'Dother.jpg'
        target = 3
        instrText =  visual.TextStim(win=mywin, text='In the following experiment, you will face the possibility that another, in the photo, will be in pain. \n  How likely that is, and which level of pain, will be indicated by an initial cue.\n You will then have the chance to reduce or try to avoid pain for the other.\n You will then be asked to rate the pain delivered.\n\n',
        font='', pos=(0, 0),depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', ori=0.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
        fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
        targetImage = visual.ImageStim(win=mywin, name='DistantOther', pos= (-10, -10),
        image=targetPic, mask=None)
        targetImage.size = [targetImage.size[0]/6, targetImage.size[1]/8]
        instrText.draw()
        targetImage.draw()
        mywin.flip()
        keys = event.waitKeys()
        
    
    
    
