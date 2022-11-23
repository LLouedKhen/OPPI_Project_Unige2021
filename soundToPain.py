#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:44:32 2019
Configuration file for experimental parameters
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

def soundToPain():
    #Set tritone
    #F Sharp Hz
    f1 = 739.99
    #C Hz
    f2 = 523.25
    #Sampling Rate 
    fs = 44100
    #duration
    seconds = 0.5
    #Volume
    volume = 0.5
    #Create Sound, combine both notes (I think this is how to do it)
    DevilSound = (np.sin(2*np.pi*np.arange(fs*seconds)*f1/fs)).astype(np.float32) +(np.sin(2*np.pi*np.arange(fs*seconds)*f2/fs)).astype(np.float32)
    DevilSound1 = sound.Sound(value = DevilSound, secs = 0.5, sampleRate = 44100, stereo = True)
    DevilSound2 = sound.Sound(value = DevilSound, secs = 1, sampleRate = 44100, stereo = True)
    DevilSound3 = sound.Sound(value = DevilSound, secs = 1.5, sampleRate = 44100, stereo = True)
    DevilSound1red = sound.Sound(value = DevilSound, secs = 0.5*(2/3), sampleRate = 44100, stereo = True)
    DevilSound2red = sound.Sound(value = DevilSound, secs = 2/3, sampleRate = 44100, stereo = True)
    DevilSound3red = sound.Sound(value = DevilSound, secs = 1.5*(2/3), sampleRate = 44100, stereo = True)
    Pains = [DevilSound1, DevilSound2, DevilSound3, DevilSound1red, DevilSound2red, DevilSound3red]
    return Pains