# -*- coding: utf-8 -*-
"""



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
from psychopy import visual, core, event, sound, logging #import some libraries from PsychoPy
from psychopy.hardware import keyboard


from IndividualPainLevels import IndividualPainLevels 
from startPainVars import startPainVars
from soundToPain import soundToPain
from targetSelection import targetSelection    
from CFG import CFG
from fixAndBetStims import fixAndBetStims
from ratingScale import ratingScale
from computeDecVars import computeDecVars
from dataFrameTimeVars import dataFrameTimeVars
from dataPlot import dataPlot
from MainExpS import MainExpS
from MainExpSLED import MainExpSLED
from MainExpSLASER import MainExpSLASER
from Thanks import Thanks



"""

"""

 #Experiment Datapath
outputPath = '/Users/loued/Documents/PythonScripts/Experiment1_Output'

subjectFULL = input("Enter main participant identifier (Number and Role, eg OPPM007): ")
while not re.match("[OPMS][0-9]*$", subjectFULL) and len(subjectFULL)!= 7:
    print ("Error! Only letters O, P, M, S allowed. Indentifier must be 7 characters long.")
    subjGender= input("Please re-enter main participant identifier (Number and Role, eg OPPM007): ") 


os.chdir(os.path.join(outputPath, subjectFULL))
intake = pd.read_csv(subjectFULL + '_IntakeData.csv', index_col=0)
 
subjectNum = intake.iloc[1][0]
subjPath = intake.iloc[6][0]
RatScaleOr= int(intake.iloc[5][0])
testType= int(intake.iloc[7][0])
log = logging.LogFile([str(subjectNum) + '.txt'], level=30, filemode='w')

stimPath =  '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images/Stim'
imgPath = '/Users/loued/Documents/PythonScripts/TaskImagesAndScripts/Images'
os.chdir(stimPath)

    
#Timing 
clock = core.Clock()
#Keyboard
kb = keyboard.Keyboard()
kb.clock.reset()

#Screen
mywin = visual.Window([900,900], [0, 0], monitor="testMonitor", units="deg")

[subjMinPain, subjMinDimPain, subjMidPain, subjMidDimPain, subjMaxPain, subjMaxDimPain, subjMinPainFile, subjMinDimPainFile, subjMidPainFile, subjMidDimPainFile, subjMaxPainFile, subjMaxDimPainFile]= IndividualPainLevels(outputPath, subjectNum, subjPath)
pains = [subjMinPain, subjMinDimPain, subjMidPain, subjMidDimPain, subjMaxPain, subjMaxDimPain]
painsFiles = [subjMinPainFile, subjMinDimPainFile, subjMidPainFile, subjMidDimPainFile, subjMaxPainFile, subjMaxDimPainFile]
blockOrder = random.sample([1, 2, 3], 3)

startExp = clock.getTime()
for j in range(0,3):
    sessionNum = j
    thisBlock = blockOrder[j]
    if testType == 1:
        MainExpS(imgPath,stimPath, clock, kb, mywin, pains, painsFiles, subjectNum, subjPath, sessionNum, thisBlock, RatScaleOr)
    elif testType == 2:
        MainExpSLED(imgPath,stimPath, clock, kb, mywin, pains, painsFiles, subjectNum, subjPath, sessionNum, thisBlock, RatScaleOr)
    elif testType == 3:
        MainExpSLASER(imgPath,stimPath, clock, kb, mywin, pains, painsFiles, subjectNum, subjPath, sessionNum, thisBlock, RatScaleOr)

ThankYou = Thanks(mywin)
ThankYou.draw()
mywin.flip()
core.wait(2) 
mywin.close()


