#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:11:36 2019
Compute starting pain decision variables
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

def startPainVars(imgPath,stimPath):
    pPain =np.transpose(np.matlib.repmat([0.1, 0.25, 0.5, 0.75, 0.9], 1, 6))
    Pain = np.transpose(np.matlib.repmat([1, 2, 3], 1, 10))
    Pain=sorted(Pain)
    allPain = pd.DataFrame(np.concatenate((Pain, pPain), axis = 1))
    allPain.columns = 'Pain', 'pPain'
    #np.random.shuffle(allPain)
    EP1= pd.DataFrame(np.transpose(allPain.Pain *allPain.pPain))
    EP1.columns = ['EP1']
    EVS = pd.DataFrame(np.transpose((allPain.Pain -1)*allPain.pPain))
    EVS.columns = ['EVS']
    EVG = pd.DataFrame(np.transpose(allPain.Pain*(allPain.pPain * 0.5)))
    EVG.columns = ['EVG']
    
    
       
    os.chdir(imgPath)
    painList= glob.glob('Bolt*')
    painList = painList * 10
    painList = pd.DataFrame(sorted(painList , key=lambda x: (x[0].isdigit(), x)))
    painList.rename(columns = {0:'Pain Delivered'}, inplace = True)
    
    noPain = glob.glob('noPain*')
    noPain = noPain * 30
    noPain = pd.DataFrame(noPain)
    noPain.columns = ['Pain Avoided']
    
    os.chdir(stimPath)
    stimList = glob.glob('Stim*') 
    stimList = stimList * 2
    stimList = pd.DataFrame(sorted(stimList, key=lambda x: (x[0].isdigit(), x)))
    stimList.columns = ['Stim']
    
    
    redpainList= glob.glob('Bolt*3.png')
    redpainList =redpainList * 10
    redpainList = pd.DataFrame(sorted(redpainList , key=lambda x: (x[0].isdigit(), x)))
    redpainList.columns = ['Pain Reduced']
    
    pPainRed =pd.DataFrame(np.transpose(np.matlib.repmat([0.05, 0.125, 0.25, 0.375, 0.45], 1, 6)))
    pPainRed.columns = ['pPainRed']
    
    allPain = pd.concat([allPain, stimList, painList, noPain, redpainList, EP1, EVS, EVG,pPainRed], axis =1)
    allPain = allPain.sample(frac=1).reset_index(drop=True)
#   allPain.columns = {'Pain', 'pPain', 'Stim', 'Pain Delivered', 'Pain Avoided', 'Pain Reduced', 'EP1', 'EVS', 'EVG', 'pPainRed'}
#    allPain.rename(columns = {0:'pPainNew'}, inplace = True)
#    allPain = allPain.sample(frac=1).reset_index(drop=True)
#    allPain.rename(columns = {0:'pPainNew'}, inplace = True)
    
    return (allPain)