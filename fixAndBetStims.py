#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:04:56 2019

@author: loued
"""
import matplotlib.pyplot as plt
import os
import numpy as np
import numpy.matlib 
import glob
import random
import re
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard

def fixAndBetStims(mywin):
    

    FixationText = visual.TextStim(win=mywin, text='+',                             
    font='', pos=(0, 0),
    depth=0, rgb=None, color='black', colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
    ori=0.0, height=None, antialias=True, bold=True, italic=False, alignHoriz='center', alignVert='center',
    fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
    
    GambleText = visual.TextStim(win=mywin, text='Gamble 1 CHF to win a chance to eliminate pain?\nPress 1.\n\nPay 2 chf to reduce pain by 33%?\nPress 2.\n\nPay nothing?\nPress 3.\n\n', 
    font='', pos=(0, 0),
    depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
    ori=0.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
    fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
    
    NextText =  visual.TextStim(win=mywin, text=('Please wait for the next block...'),font='', pos=(0, 0),
    depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
    ori=1.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
    fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)

    
    return (FixationText, GambleText, NextText)