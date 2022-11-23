#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:30:56 2019

@author: loued
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:01:19 2019

@author: loued
"""

#wavTones.com.unregistred.burst_75Hz_-6dBFS_x3.wav

import sounddevice as sd
import soundfile as sf
import os
import glob
import numpy as np
import re
import numpy.matlib
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
from psychopy import visual, core, event, sound, logging #import some libraries from PsychoPy
from psychopy.hardware import keyboard

def subjIntake():
    subNum = input("Enter participant identifier: ") 
    while len(subNum)!= 3:
        print("Error! Must enter 3 characters!")
        input("Please re-enter participant identifier: ")     
        print(subNum)
    
    participant = input("Spouse or main participant? Enter 1 for main, 2 for spouse: ") 
    
    while len(participant) > 1:
        print("Error! Must enter 1 or 2!")
        participant = input("Spouse or main participant? Enter 1 for main, 2 for spouse:  ")    
        print(participant)
        
    if participant == '1':
        string = 'OPPM'
    elif participant == '2':
        string = 'OPPS'
        
    return(string, subNum)

procPath = '/Users/loued/Documents/PythonScripts/Experiment1_Scripts/Calibration' 
dataPath = '/Users/loued/Documents/Testing_StairCase_Sound/Sounds'
os.chdir(dataPath)   

string, subNum = subjIntake() 
    
subject = string  + subNum + '_Thresh'
savePath =os.path.join('/Users/loued/Documents/PythonScripts/Experiment1_Output/' + string + subNum + '/Calibration') 

os.chdir(savePath)
if not glob.glob('*.csv'):
    print("All clear.")
    os.chdir(dataPath)
else:
    subjIntake() 

filenames = glob.glob('*.wav')
fileDBs = np.zeros(len(filenames))

regex = re.compile(r'\d+')
for i in range(0,len(filenames)):
    fileDBs[i] = regex.findall(filenames[i])[1]
fileDBs[fileDBs.any==5] = 5
fileDBs = fileDBs.astype(int)
idx1 = np.argsort(fileDBs)
fileDB = fileDBs[idx1]
soundFiles = pd.DataFrame(np.transpose([fileDBs, filenames]))
soundFiles[0] = soundFiles[0].astype('int') 
soundFiles = soundFiles.sort_values(by =[0], ascending = False)


stairCase1 = soundFiles
stairCase1 = stairCase1.reset_index(drop=True)
stairCase1 = stairCase1.iloc[4:]

#
## Extract data and sampling rate from file
#data, fs = sf.read(filename, dtype='float32')  
#sd.play(data, fs)
#status = sd.wait()  # Wait until file is done playing

Rate1 = pd.Series(np.zeros([75]))
sounds1 = pd.Series(np.zeros([75]))
dbs1 = pd.Series(np.zeros([75]))


#Timing 
clock = core.Clock()
#Keyboard
kb = keyboard.Keyboard()
kb.clock.reset()

#Screen
mywin = visual.Window([900,900], [0, 0], monitor="testMonitor", units="deg")

markStart = (random.randrange(2, 9, 1))
myScale = range(10)

rateSound = visual.TextStim(win=mywin, text=('How loud is the sound to you?'),font='', pos=(0, 0),
depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
ori=1.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)

ratingScale = visual.RatingScale(win = mywin, low=0, high=10, precision= 0.1, 
pos=(0, -0.4),choices =None,scale= None, acceptPreText =None,  singleClick = True,
showValue = None, markerStart=random.choice(myScale), showAccept = None, labels=None, stretch=2.0, 
leftKeys='left', rightKeys='right',acceptKeys ='return', maxTime=5)

stairCase = []

fs =44100

i = 0



stairCase = pd.concat([stairCase1]*5)
stairCase  = stairCase.sample(frac=1).reset_index(drop=True)

tic = time.time()

for i in range (0, len(stairCase)):
    file= stairCase.iloc[i,1]
    db= stairCase.iloc[i,0]
    print(file)
    data, fs = sf.read(stairCase.iloc[i,1], dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    ratingScale = visual.RatingScale(win = mywin, low=0, high=10, precision= 0.1, 
    pos=(0, -0.4),choices =None,scale= None, acceptPreText =None, singleClick = True,
    showValue = None, markerStart=random.choice(myScale), showAccept = None, labels=None, stretch=2.0, 
    leftKeys='left', rightKeys='right',acceptKeys ='return', maxTime=5)
    while ratingScale.noResponse:
        rateSound.draw()
        ratingScale.draw()
        mywin.flip()
    Rating= ratingScale.getRating()
    ratingScale.reset()
    Rate1.iloc[i] = Rating
    sounds1.iloc[i] = file
    dbs1.iloc[i] = db
    print(Rate1[i])
    fdbk = visual.TextStim(win=mywin, text=(str(Rate1.iloc[i])),font='', pos=(0, 0))
    fdbk.draw()
    mywin.flip()
    core.wait(3.0)

toc = time.time() - tic

allTypes = pd.concat([Rate1, stairCase], axis = 1)
allTypes.columns = ['rating', 'dB', 'file']
allTypes.dB = np.negative(allTypes.dB)
allTypes = allTypes.iloc[:55,:]

meanResp = allTypes.groupby('dB').mean()

fig = plt.figure()
plt.plot((meanResp.index), meanResp.rating)
plt.xlabel('dB')
plt.ylabel('Rating')
fig.savefig(subject + '.jpg')

minThresh = (np.abs(meanResp.rating- 1)).argmin()
mindimThresh = minThresh - (np.abs(minThresh/3))
mindimThresh = mindimThresh - (np.mod(mindimThresh, 5))

midThresh = (np.abs(meanResp.rating- 5)).argmin()
middimThresh = midThresh - (np.abs(midThresh/3))
middimThresh = middimThresh - (np.mod(middimThresh, 5))

maxThresh = (midThresh + (((np.abs(meanResp.rating- 10)).argmin() - midThresh)/2))
maxThresh = maxThresh - (np.mod(maxThresh, 5))
maxdimThresh = maxThresh - (np.abs(maxThresh/3))
maxdimThresh = maxdimThresh - (np.mod(maxdimThresh, 5))


DangerMax = 0
if maxThresh > 0:
    maxThresh = 0
    
minmidmaxVal = pd.DataFrame([minThresh, mindimThresh, midThresh, middimThresh, maxThresh, maxdimThresh])
minmidmaxFiles = pd.DataFrame(np.zeros([len(minmidmaxVal)]))

minmidmaxFilesIdx = soundFiles[soundFiles[0].isin(abs(minmidmaxVal[0]))]

for j in range (0,6):
    for i in range(0,5):
        if abs(minmidmaxVal.iloc[j,0]) == minmidmaxFilesIdx.iloc[i,0]:
            print('TRUE')
            minmidmaxFiles.iloc[j,0] =os.path.join(dataPath, minmidmaxFilesIdx.iloc[i,1])
            
        else:     
            print('False')
            
        

minmidmaxVal = pd.concat([minmidmaxVal, minmidmaxFiles], axis = 1)
minmidmaxVal.columns = ['dB', 'soundFile']

duration = pd.DataFrame([toc/60])


if not os.path.exists(savePath):
    os.makedirs(savePath)
os.chdir(savePath) 
allTypes.to_csv(os.path.join(savePath, subject + '_All_BrutCalibration.csv'))
duration.to_csv(os.path.join(savePath, subject + '_CalibrationDuration.csv'))

minmidmaxVal.to_csv(os.path.join(savePath, subject + '_BrutPainCalibration_Values.csv'))

mywin.close()