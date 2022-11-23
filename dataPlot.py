#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:36:38 2019
Plot variables from experiment
@author: loued
"""
import matplotlib.pyplot as plt
import pylab as pl
import os
import numpy as np
import numpy.matlib 
import glob
import random
import re
import pandas as pd
from psychopy import visual, core, event, sound #import some libraries from PsychoPy
from psychopy.hardware import keyboard


def dataPlot(AllVariables, subjectNum, Condition):
    loPainU = AllVariables.loc[(AllVariables.Pain ==1), :];
    midPainU = AllVariables.loc[(AllVariables.Pain ==2), :];
    hiPainU = AllVariables.loc[(AllVariables.Pain ==3), :];
    
    RiskRange = np.unique(np.sort(AllVariables.RiskPain))
    
    RiskMeans = AllVariables.groupby('RiskPain').mean()
    probMeans = AllVariables.groupby('pPain').mean()
    
    loPainEP1 = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EP1), np.mean(loPainU.loc[loPainU.pPain ==0.25].EP1), np.mean(loPainU.loc[loPainU.pPain ==0.5].EP1), np.mean(loPainU.loc[loPainU.pPain ==0.75].EP1), np.mean(loPainU.loc[loPainU.pPain ==0.9].EP1)];
    midPainEP1 = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EP1), np.mean(midPainU.loc[midPainU.pPain ==0.25].EP1), np.mean(midPainU.loc[midPainU.pPain ==0.5].EP1), np.mean(midPainU.loc[midPainU.pPain ==0.75].EP1), np.mean(midPainU.loc[midPainU.pPain ==0.9].EP1)]
    hiPainEP1 = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EP1), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EP1), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EP1), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EP1), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EP1)];
    
    loPainEP2 = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EP2), np.mean(loPainU.loc[loPainU.pPain ==0.25].EP2), np.mean(loPainU.loc[loPainU.pPain ==0.5].EP2), np.mean(loPainU.loc[loPainU.pPain ==0.75].EP2), np.mean(loPainU.loc[loPainU.pPain ==0.9].EP2)];
    midPainEP2 = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EP2), np.mean(midPainU.loc[midPainU.pPain ==0.25].EP2), np.mean(midPainU.loc[midPainU.pPain ==0.5].EP2), np.mean(midPainU.loc[midPainU.pPain ==0.75].EP2), np.mean(midPainU.loc[midPainU.pPain ==0.9].EP2)]
    hiPainEP2 = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EP2), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EP2), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EP2), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EP2), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EP2)];
    
    loPainEVS = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EVS), np.mean(loPainU.loc[loPainU.pPain ==0.25].EVS), np.mean(loPainU.loc[loPainU.pPain ==0.5].EVS), np.mean(loPainU.loc[loPainU.pPain ==0.75].EVS), np.mean(loPainU.loc[loPainU.pPain ==0.9].EVS)];
    midPainEVS = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EVS), np.mean(midPainU.loc[midPainU.pPain ==0.25].EVS), np.mean(midPainU.loc[midPainU.pPain ==0.5].EVS), np.mean(midPainU.loc[midPainU.pPain ==0.75].EVS), np.mean(midPainU.loc[midPainU.pPain ==0.9].EVS)]
    hiPainEVS = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EVS), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EVS), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EVS), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EVS), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EVS)];
    
    loPainEVG = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EVG), np.mean(loPainU.loc[loPainU.pPain ==0.25].EVG), np.mean(loPainU.loc[loPainU.pPain ==0.5].EVG), np.mean(loPainU.loc[loPainU.pPain ==0.75].EVG), np.mean(loPainU.loc[loPainU.pPain ==0.9].EVG)];
    midPainEVG = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EVG), np.mean(midPainU.loc[midPainU.pPain ==0.25].EVG), np.mean(midPainU.loc[midPainU.pPain ==0.5].EVG), np.mean(midPainU.loc[midPainU.pPain ==0.75].EVG), np.mean(midPainU.loc[midPainU.pPain ==0.9].EVG)]
    hiPainEVG = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EVG), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EVG), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EVG), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EVG), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EVG)];
    
    loPainEA = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EA), np.mean(loPainU.loc[loPainU.pPain ==0.25].EA), np.mean(loPainU.loc[loPainU.pPain ==0.5].EA), np.mean(loPainU.loc[loPainU.pPain ==0.75].EA), np.mean(loPainU.loc[loPainU.pPain ==0.9].EA)];
    midPainEA = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EA), np.mean(midPainU.loc[midPainU.pPain ==0.25].EA), np.mean(midPainU.loc[midPainU.pPain ==0.5].EA), np.mean(midPainU.loc[midPainU.pPain ==0.75].EA), np.mean(midPainU.loc[midPainU.pPain ==0.9].EA)]
    hiPainEA = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EA), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EA), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EA), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EA), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EA)];
    
    loPainEVChoice = [np.mean(loPainU.loc[loPainU.pPain ==0.1].EVChoice), np.mean(loPainU.loc[loPainU.pPain ==0.25].EVChoice), np.mean(loPainU.loc[loPainU.pPain ==0.5].EVChoice), np.mean(loPainU.loc[loPainU.pPain ==0.75].EVChoice), np.mean(loPainU.loc[loPainU.pPain ==0.9].EVChoice)];
    midPainEVChoice = [np.mean(midPainU.loc[midPainU.pPain ==0.1].EVChoice), np.mean(midPainU.loc[midPainU.pPain ==0.25].EVChoice), np.mean(midPainU.loc[midPainU.pPain ==0.5].EVChoice), np.mean(midPainU.loc[midPainU.pPain ==0.75].EVChoice), np.mean(midPainU.loc[midPainU.pPain ==0.9].EVChoice)]
    hiPainEVChoice = [np.mean(hiPainU.loc[hiPainU.pPain ==0.1].EVChoice), np.mean(hiPainU.loc[hiPainU.pPain ==0.25].EVChoice), np.mean(hiPainU.loc[hiPainU.pPain ==0.5].EVChoice), np.mean(hiPainU.loc[hiPainU.pPain ==0.75].EVChoice), np.mean(hiPainU.loc[hiPainU.pPain ==0.9].EVChoice)];

    
    fig1 = plt.figure()
    plt.plot(AllVariables.EVS, 'k',  AllVariables.EVG,  'r', AllVariables.EP1, 'b', AllVariables.EP2, 'c', AllVariables.EA, 'g', AllVariables.Rate, 'm' )
    labels =('Expected Pain For Sure Choice', 'Expected Pain for Gamble', 'Initial Expected Pain', 'Expected Pain Following Decision', 'Pain Value in CHF', 'Pain Rating')
    plt.legend(labels)
    plt.ylabel('Cost (CHF)')
    plt.xlabel('Trial number')
    plt.title('Expected Pain Values')
    plt.show()
    fig1.savefig(subjectNum + '.jpg')
    
    fig2= plt.figure()
    plt.plot(np.nanmean([loPainEVChoice , midPainEVChoice , hiPainEVChoice], axis = 1), 'b')
    plt.plot(np.nanmean([loPainEVS , midPainEVS , hiPainEVS], axis = 1), 'g')
    plt.plot(np.nanmean([loPainEVG , midPainEVG , hiPainEVG], axis = 1), 'r')
    plt.show()
        
    
    fig3= plt.figure()
    plt.plot((probMeans.EP1), 'k')
    plt.plot((probMeans.EVChoice), 'b')
    plt.plot((probMeans.EVS), 'g')
    plt.plot((probMeans.EVG), 'r')
    plt.show()
    
    fig4= plt.figure()
    plt.plot((RiskMeans.EP1), 'k')
    plt.plot((RiskMeans.EVChoice), 'b')
    plt.plot((RiskMeans.EVS), 'g')
    plt.plot((RiskMeans.EVG), 'r')
    plt.show()
#        
    
#    
#    fig2= plt.figure()
#    pPainR =[0.1, 0.25, 0.5, 0.75, 0.9]
#    plt.plot(pPainR, loPainMu, '*')
#    plt.plot(pPainR, midPainMu, '*')
#    plt.plot(pPainR, hiPainMu, '*')
#    plt.plot(np.nanmean([loPainMu, midPainMu, hiPainMu], axis = 1), 'r')
#    plt.plot(np.nanmean([loPainEVS, midPainEVS, hiPainEVS], axis = 1), 'k')
#    labels = ('Low Pain Risk', 'Mid Pain Risk', 'High Pain Risk', 'Mean Risk Curve', 'Expected Value')
#    plt.legend(labels)
#    plt.title('Risk Preference Curve (n = 30)')
#    plt.xlabel('Pain Probability')
#    plt.ylabel('Expected Pain')
#    fig2.savefig(subjectNum + 'RiskCurve.jpg')
#  
