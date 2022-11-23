#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:01:20 2019

@author: loued
"""
import os
import datetime as datetime
import numpy as np
import numpy.matlib 
import glob
import random
import re
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard


def IndividualPainLevels(outputPath, subjectNum, subjPath):

#  #Enter subject pain thresholds
#    subjMidPain= input("Enter main participant mid pain: ") 
#    while int(subjMidPain) > 4.5:
#        print("Error! Pain intensity cannot be higher than 4.5.")
#        subjMidPain = input("Please re-enter main participant mid pain: ")    
#        
#    #Enter subject pain thresholds
#    subjHiPain= input("Enter main participant high pain: ") 
#    while int(subjHiPain) > 4.5:
#        print("Error! Pain intensity cannot be higher than 4.5.")
#        subjHiPain  = input("Please re-enter main participant high pain: ") 
#        
#    #Enter spouse pain thresholds
#    spouseMidPain= input("Enter spouse mid pain: ") 
#    while int(spouseMidPain) > 4.5:
#        print("Error! Pain intensity cannot be higher than 4.5.")
#        spouseMidPain  = input("Please re-enter spouse mid pain: ")    
#        
#    #Enter spouse pain thresholds
#    spouseHiPain= input("Enter spouse high pain: ") 
#    while int(spouseHiPain) > 4.5:
#        print("Error! Pain intensity cannot be higher than 4.5.")
#        spouseHiPain  = input("Please re-enter spouse high pain: ")    
    calPath = os.path.join(subjPath, 'Calibration')
    os.chdir(calPath)
    painCSV = glob.glob('*_BrutPainCalibration_Values.csv')
    painVals = pd.read_csv(painCSV[0])
    
    #Don't forget to switch signs for laser pain!!!
    subjMinPain = painVals.iloc[0,1]
    subjMinDimPain = painVals.iloc[1,1]
    subjMidPain = painVals.iloc[2,1]
    subjMidDimPain = painVals.iloc[3,1]
    subjMaxPain = painVals.iloc[4,1]
    subjMaxDimPain = painVals.iloc[5,1]

    subjMinPainFile = painVals.iloc[0,2]
    subjMinDimPainFile  = painVals.iloc[1,2]
    subjMidPainFile  = painVals.iloc[2,2]
    subjMidDimPainFile  = painVals.iloc[3,2]
    subjMaxPainFile  = painVals.iloc[4,2]
    subjMaxDimPainFile  = painVals.iloc[5,2]
    
    
    return (subjMinPain, subjMinDimPain, subjMidPain, subjMidDimPain, subjMaxPain, subjMaxDimPain, subjMinPainFile, subjMinDimPainFile, subjMidPainFile, subjMidDimPainFile, subjMaxPainFile, subjMaxDimPainFile)