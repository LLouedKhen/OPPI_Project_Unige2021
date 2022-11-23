#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:12:47 2019
Rating Scale 
@author: loued
"""

import os
import numpy as np
import numpy.matlib 
import glob
import random
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard

def ratingScale(mywin, Rate, TP5, TP4, clock, i, RatScaleOr):
    painMax = '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images/UnhappyHighArousal_QuestionMark.png'
    painMin=  '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images/SlightSmile.png'
    markStart = (random.randrange(2, 9, 1))
    if RatScaleOr == 1:
        rateItem= visual.TextStim(mywin, text='How painful was that?',pos=(0, 0.5))
        pain = visual.ImageStim(win=mywin, name='painMax', pos=(-9, -3.6),
        image=painMax, mask=None)
        noPain = visual.ImageStim(win=mywin, name='painMin', pos=(9, -3.6),
        image=painMin, mask=None)
    elif RatScaleOr == 2:
        rateItem= visual.TextStim(mywin, text='How painful was that?',pos=(0, 0.5))
        pain = visual.ImageStim(win=mywin, name='painMax', pos=(9, -3.6),
        image=painMax, mask=None)
        noPain = visual.ImageStim(win=mywin, name='painMin', pos=(-9, -3.6),
        image=painMin, mask=None)
    
    ratingScale = visual.RatingScale(win = mywin, low=0, high=10, precision= 0.1, 
    pos=(0, -0.4), markerStart=markStart,choices =None,scale= None, acceptPreText =None, 
    showValue = None, showAccept = None, labels=None, stretch=2.0, 
    leftKeys='left', rightKeys='right',acceptKeys ='return', maxTime=5)
    while ratingScale.noResponse:
        rateItem.draw()
        pain.draw()
        noPain.draw()
        ratingScale.draw()
        mywin.flip()
    TP4[i] = clock.getTime()
    Rating= ratingScale.getRating()
    Rate[i] = Rating
    print(Rate[i])
    TP5[i] = ratingScale.getRT()
        
    return (Rate, TP5, TP4)
