#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:29:47 2019
Fixed Parameters for experiment
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

def CFG():
    

    
    
    nTrials = 30
    durCue = 3
    durDecision = 2
    durPostDecision = 3
    durOutcome = 3 
    Endowment = 60;
    
    ABin = np.zeros([nTrials,2]);
    TP1 = np.zeros([nTrials,1]);
    TP2 = np.zeros([nTrials,1]);
    TP3 = np.zeros([nTrials,1]);
    TP4 = np.zeros([nTrials,1]);
    TP5 = np.zeros([nTrials,1]);
    startTrial = np.zeros([nTrials,1]);
    endTrial = np.zeros([nTrials,1]);
    durTrial = np.zeros([nTrials,1]);
    Rate = np.zeros([nTrials,1]);
    Outcome = np.zeros([nTrials,1]);
    
    
    
    cfg= {}
    cfg["params"] = {}
    cfg["params"]["ABin"] = ABin
    cfg["params"]["TP1"] =TP1 
    cfg["params"]["TP2"] =TP2
    cfg["params"]["TP3"] =TP3  
    cfg["params"]["TP4"] =TP4
    cfg["params"]["TP5"] =TP5    
    cfg["params"]["Rate"]= Rate
    cfg["params"]["startTrial"]= startTrial 
    cfg["params"]["endTrial"]= endTrial
    cfg["params"]["durTrial"]= durTrial 
    cfg["params"]["Endowment"]= Endowment 
    cfg["params"]["durOutcome"]=  durOutcome 
    cfg["params"]["durPostDecision"]=  durPostDecision
    cfg["params"]["durDecision"]=  durDecision 
    cfg["params"]["durOutcome"]=  durOutcome 
    return (Endowment, nTrials, ABin,Outcome, TP1, TP2, TP3, TP4, TP5, Rate, startTrial, endTrial, durTrial, durPostDecision, durDecision, durOutcome, durCue) 