#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:32:53 2019
Turn Timing Variables from end of block into dataframes
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

def dataFrameTimeVars(TP1,TP2, TP3, TP4, TP5, Rate, durTrial, startTrial):
    TP1 = pd.DataFrame(TP1)
    TP1.rename(columns = {0:'Timepoint1'}, inplace = True)
    TP2 = pd.DataFrame(TP2)
    TP2.rename(columns = {0:'Timepoint2'}, inplace = True)
    TP3 = pd.DataFrame(TP3)
    TP3.rename(columns = {0:'Timepoint3'}, inplace = True)
    TP4 = pd.DataFrame(TP4)
    TP4.rename(columns = {0:'Timepoint4'}, inplace = True)
    TP5 = pd.DataFrame(TP5)
    TP5.rename(columns = {0:'Timepoint5'}, inplace = True)

    durTrial= pd.DataFrame(durTrial)
    durTrial.rename(columns = {0:'durTrial'}, inplace = True)
    startTrial = pd.DataFrame(startTrial)
    startTrial.rename(columns = {0:'startTrial'}, inplace = True)
    
    Rate = pd.DataFrame(Rate)
    Rate.rename(columns = {0:'Rate'}, inplace = True)
    
    return (TP1,TP2, TP3, TP4, TP5, Rate, durTrial, startTrial)