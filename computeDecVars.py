#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:22:12 2019

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

def computeDecVars(ABin, Outcome, i, nTrials, allPain):
    pRelief = np.zeros([nTrials,1]);
    Cost = np.zeros([nTrials,1]);
    vPain = np.zeros([nTrials,1]);
    EP2 = np.zeros([nTrials,1]);
    EP2p = np.zeros([nTrials,1]);
    EVChoice = np.zeros([nTrials,1]);
    RiskPain2 = np.zeros([nTrials,1]);
    PPE = np.zeros([nTrials,1]);
    RiPE = np.zeros([nTrials,1]);
            
    pRelief[ABin[:,0] == 0] = 0;
    pRelief[ABin[:,0] == 1] = 0.5;
    pRelief[ABin [:,0]== 2] = 1;
    Cost[ABin[:,0] == 0] = 0;
    Cost[ABin[:,0] == 1] = 1;
    Cost[ABin [:,0] == 2] = 2;
    vPain[ABin[:,0] == 0] = 0;
    ix1 = ABin[:,0] == 1
    vPain[ix1,0] = np.negative(np.transpose(allPain.Pain[ix1]))
#    vPain[ABin[:,0] == 1] = 1;
    vPain[ABin[:,0] == 2] = -1;
#    ix2 = ABin[:,0] == 2
#    vPain[ix2,0] =np.transpose(allPain.Pain[ix2] -1)
            
    RiskPain= (allPain['pPain'] * ((allPain['Pain'] -allPain['EP1'])**2)) + ((1 - allPain['pPain']) * ((0 -allPain['EP1'])**2)) 
    EA = Cost* pRelief * vPain
    for i in range (0, nTrials):
        if Cost[i] == 1:
          EP2[i] = allPain['pPainRed'].iloc[i] * allPain['Pain'].iloc[i]
          RiskPain2[i] = allPain['pPainRed'].iloc[i] * (((allPain['Pain'].iloc[i] -EP2[i])**2) + ((1 - allPain['pPainRed'].iloc[i]) * ((0 -EP2[i])**2))) 
          EVChoice[i] = allPain.EVG[i]
          EP2p[i] = EP2[i] + EA[i]
        elif Cost[i] == 2:
          EP2[i] = allPain['pPain'].iloc[i] * (allPain['Pain'].iloc[i] -1)
          RiskPain2[i] = (allPain['pPain'].iloc[i] * (((allPain['Pain'].iloc[i] - 1)-EP2[i])**2)) + ((1 - (allPain['pPain'].iloc[i])) * ((0 - EP2[i])**2))
          EVChoice[i] = allPain.EVS[i]
          EP2p[i] = EP2[i] + EA[i]
        else:
          EP2[i] = allPain['EP1'].iloc[i]
          RiskPain2[i] =  RiskPain[i]
          EVChoice[i] = allPain.EP1[i]
          EP2p[i] = EP2[i] + EA[i]
          
    for i in range (0, nTrials):   
     
      PPE[i] = Outcome[i] * EP2[i];
      RiPE[i] = ((Outcome[i] -EP2[i])**2) - RiskPain2[i];
          
    RiskPain = pd.DataFrame(RiskPain)
    RiskPain.columns = ['RiskPain']
    RiskPain2 = pd.DataFrame(RiskPain2)
    RiskPain2.columns = ['RiskPain2']
    RiPE = pd.DataFrame(RiPE)
    RiPE.columns = ['RiPE']
    PPE = pd.DataFrame(PPE)
    PPE.columns = ['PPE']
    Outcome = pd.DataFrame(Outcome)
    Outcome.columns =['Outcome']
    Cost = pd.DataFrame(Cost)
    Cost.columns = ['Cost']
    EP2 = pd.DataFrame(EP2)
    EP2.columns = ['EP2']
    EP2p = pd.DataFrame(EP2p)
    EP2p.columns = ['EP2p']
    EVChoice = pd.DataFrame(EVChoice)
    EVChoice.columns = ['EVChoice']
    EA = pd.DataFrame(EA)
    EA.columns = ['EA']
    ABin = pd.DataFrame(ABin)
    ABin.columns = ['Response', 'ResponseTime']
    vPain = pd.DataFrame(vPain)
    vPain.columns =['vPain']
    pRelief= pd.DataFrame(pRelief)
    pRelief.columns = ['pRelief']
    
    return (RiPE, PPE, EP2, pRelief, Cost, vPain, RiskPain, RiskPain2, EA, Outcome, ABin, EVChoice, EP2p)