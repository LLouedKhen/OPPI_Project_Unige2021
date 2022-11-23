# -*- coding: utf-8 -*-
"""
Spyder Editor
still need to add
1.Serial commands
2.subject number DONE
3.trigger DONE 
4.would be nice to have functions
5.Add thank you slide DONE
6.Embed photo DONE
7.Instructions DONE


"""
import os
import numpy as np
import glob
import random
import pandas as pd
from psychopy import visual, core, event, sound, logging #import some libraries from PsychoPy
from psychopy.hardware import keyboard

from SubjectInfoIntake import SubjectInfoIntake
from IndividualPainLevels import IndividualPainLevels 
from soundToPain import soundToPain
from MainExpfMRI import MainExpfMRI
from Thanks import Thanks



"""
Same as behavioral but include scanner trigger
"""
MR_settings = { 
    'TR': 1.100, # duration (sec) per volume
    'volumes': 375, # number of whole-brain 3D volumes / frames
    'sync': '5', # character to use as the sync timing event; assumed to come at start of a volume
    'skip': 0, # number of volumes lacking a sync pulse at start of scan (dummies)
    'sound': True    # in test mode: play a tone as a reminder of scanner noise
    }

 #Experiment Datapath
outputPath = '/Users/loued/Documents/PythonScripts/Experiment1_Output'

subjectNum, subjPath, RatScaleOr= SubjectInfoIntake(outputPath)
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

[subjMinPain, subjMinDimPain, subjMidPain, subjMidDimPain, subjMaxPain, subjMaxDimPain]= IndividualPainLevels(outputPath, subjectNum, subjPath)
pains = soundToPain()  
blockOrder = random.sample([1, 2, 3, 1, 2 ,3], 6)

startExp = clock.getTime()
for j in range(1,7):
    sessionNum = j
    thisBlock = blockOrder[j]
    MainExpfMRI(imgPath,stimPath, clock, kb, mywin, pains, subjectNum, subjPath, sessionNum, thisBlock, MR_settings, RatScaleOr)

ThankYou = Thanks(mywin)
ThankYou.draw()
mywin.flip()
core.wait(2) 
mywin.close()


