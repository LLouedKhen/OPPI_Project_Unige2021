#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:01:04 2019

@author: loued
"""

import os
import numpy as np
import numpy.matlib 
import glob
import random
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware.emulator import launchScan
from psychopy.hardware import keyboard


from startPainVars import startPainVars
from targetSelection import targetSelection    
from CFG import CFG
from fixAndBetStims import fixAndBetStims
from ratingScale import ratingScale
from computeDecVars import computeDecVars
from dataFrameTimeVars import dataFrameTimeVars
from dataPlot import dataPlot


def MainExpfMRI(imgPath,stimPath, clock, kb, mywin, pains, subjectNum, subjPath, sessionNum, thisBlock, MR_settings, RatScaleOr):
    
    targetSelection(mywin, stimPath, thisBlock)
     
    if thisBlock == 1:
        Condition = "_self_"        
    elif thisBlock == 2:
        Condition = "_cother_"        
    elif thisBlock== 3:
        Condition = "_dother_"
        
    os.chdir(subjPath)
    Endowment, nTrials, ABin,Outcome, TP1, TP2, TP3, TP4, TP5, Rate, startTrial, endTrial, durTrial, durPostDecision, durDecision, durOutcome, durCue = CFG()
    FixationText, GambleText, NextText = fixAndBetStims(mywin)
    
    allPain = startPainVars(imgPath,stimPath)
    startBlock = clock.getTime()
    vol = launchScan(mywin, MR_settings, globalClock=clock, mode='Scan', esc_key='escape', wait_msg='waiting for scanner ...', wait_timeout=300)
        #create some stimuli
    for i in range (0,nTrials):
        
        startTrial[i] = clock.getTime()
        jitterITI = (random.randrange(10, 25, 1))/10
        os.chdir(stimPath)
        stim = allPain['Stim'].iloc[i]
    
        FixationText.draw()
        mywin.flip()
        core.wait(jitterITI)
        
        jitterISI1 = (random.randrange(5, 8, 1))/10
        TRIAL_IMAGE = visual.ImageStim(win=mywin, name='TRIAL_IMAGE', 
        image=stim, mask=None)
        TRIAL_IMAGE.draw()
        mywin.flip()
        TP1[i] = clock.getTime()
        core.wait(durCue + jitterISI1)
        
        
        GambleText.draw()
        mywin.flip()
        keys = event.waitKeys(keyList=["1", "2", "3"], timeStamped = True)
        ABin[i] = keys[0]
        print(keys)
        core.wait(2.0)
        
        if ABin[i,0] == 1:
            Endowment = Endowment -1
            allPain['pPain'][i] = (allPain['pPain'][i])/2
        elif ABin[i,0] == 2:
            Endowment = Endowment -2
        elif ABin[i,0] == 0:
            Endowment = Endowment
        
        
        FeedbackText =  visual.TextStim(win=mywin, text=('You have ' + str(Endowment) + ' CHF remaining.'),font='', pos=(0, 0),
        depth=0, rgb=None, color=(1.0, 1.0, 1.0), colorSpace='rgb', opacity=1.0, contrast=1.0, units='', 
        ori=1.0, height=None, antialias=True, bold=False, italic=False, alignHoriz='center', alignVert='center',
        fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False, languageStyle='LTR', name=None, autoLog=None)
        FeedbackText.draw()
        mywin.flip()
        
        core.wait(2)
        
        if ABin[i,0] == 2:
            Outcome[i] = np.random.choice([2,0], 1, p=[allPain['pPain'][i], 1 - allPain['pPain'][i]])
        else:
            Outcome[i] = np.random.choice([1,0], 1, p=[allPain['pPain'][i], 1 - allPain['pPain'][i]])
        
        jitterISI2 = (random.randrange(5, 8, 1))/10
        outcome = Outcome[i]
        if Outcome[i] == 1:
            os.chdir(imgPath)
            outStim = allPain['Pain Delivered'].iloc[i]
            EXP_IMAGE = visual.ImageStim(win=mywin, name='EXP_IMAGE', 
            image=outStim, mask=None)
            EXP_IMAGE.draw()
            mywin.flip()
            TP3[i] = clock.getTime()
            if allPain['Pain'].iloc[i] == 1:
                pains[0].play()
            elif allPain['Pain'].iloc[i] == 2:
                pains[1].play()
            elif allPain['Pain'].iloc[i] == 3:
                pains[2].play()
            core.wait(durOutcome + jitterISI2)  
            
        elif Outcome[i] ==0:
            os.chdir(imgPath)
            outStim = allPain['Pain Avoided'].iloc[i]
            EXP_IMAGE = visual.ImageStim(win=mywin, name='EXP_IMAGE', 
            image=outStim, mask=None)
            EXP_IMAGE.draw()
            mywin.flip()
            TP3[i] = clock.getTime()
            core.wait(durOutcome + jitterISI2) 
            
                
        elif Outcome[i] ==2:
            os.chdir(stimPath)
            outStim = allPain['Pain Reduced'].iloc[i]
            EXP_IMAGE = visual.ImageStim(win=mywin, name='EXP_IMAGE', 
            image=outStim, mask=None)
            EXP_IMAGE.draw()
            mywin.flip()
            TP3[i] = clock.getTime()
            if allPain['Pain'].iloc[i] == 1:
                pains[3].play()
            elif allPain['Pain'].iloc[i] == 2:
                pains[4].play()
            elif allPain['Pain'].iloc[i] == 3:
                pains[5].play()
            core.wait(durOutcome + jitterISI2)
    
           
            
        Rate, TP5, TP4 = ratingScale(mywin, Rate, TP5, TP4, clock, i, RatScaleOr)    
        core.wait(2.0)
        endTrial[i] = clock.getTime()
        durTrial[i] = endTrial[i] - startTrial[i]
        print('The trial took ' + str(durTrial[i]) + ' seconds.')


            
    
    RiPE, PPE, EP2, pRelief, Cost, vPain, RiskPain, RiskPain2, EA, Outcome, ABin= computeDecVars(ABin, Outcome, i, nTrials, allPain)    
    
    TP1,TP2, TP3, TP4, TP5, Rate, durTrial, startTrial = dataFrameTimeVars(TP1,TP2, TP3, TP4, TP5, Rate, durTrial, startTrial)
    
    
    
    #save results
    cwd = os.getcwd()
    if cwd != subjPath:
        os.chdir(subjPath)
        
    AllVariables = pd.concat([allPain, RiPE, PPE, EP2, pRelief, Cost, vPain, RiskPain, RiskPain2, EA, Outcome, ABin, TP1,TP2, TP3, TP4, TP5, Rate, durTrial, startTrial ], axis = 1);
    
                
    AllVariables.to_csv('AllVariables' + subjectNum + '_' + str(sessionNum) + Condition + '.csv')
    
    dataPlot(AllVariables)
    if sessionNum < 6:
        NextText.draw()
        mywin.flip()
        core.wait(3.0)