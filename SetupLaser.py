#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:50:50 2019

@author: loued
"""
import fakeSerial1 as serial
import time
from random import randint
import numpy as np

def SetupLaser(pains):

    LaserFootPulse = 4; # ms not clear at all 
    LaserFootSpotsize =4 ; # mm
#    LaserFootPulseCode = LaserFootPulse - 1;
#    LaserFootSpotsizetCode = LaserFootSpotsize - 4;
#    
    high = pains[-1]
    medium =  pains[-2]
    low = pains[-3]
    thresh = pains[-4]
    
    if pain == 3:
        LaserFootEnergy = high;
    elif pain == 2:
        LaserFootEnergy = medium;
    elif pain == 1:
        LaserFootEnergy = low;
    elif pain == 0:
        LaserFootEnergy = thresh;
