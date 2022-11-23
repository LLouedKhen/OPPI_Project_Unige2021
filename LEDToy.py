#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:17:08 2019

@author: loued
"""

# testSerialSimulator.py
# This program energizes the fakeSerial simulator using example code taken
# from http://pyserial.sourceforge.net/shortintro.html
#

# import the simulator module (it should be in the same directory as this program)
import serial as serial
import time
from random import randint
import numpy as np

# Example 1  from http://pyserial.sourceforge.net/shortintro.html
def LEDToy(pain):  
    LaserFootPulse = 6; # ms
    LaserFootSpotsize = 7; # mm
    LaserFootPulseCode = LaserFootPulse - 1;
    LaserFootSpotsizetCode = LaserFootSpotsize - 4;
    
    high = 8
    medium = 5
    trial =np.zeros([10,1])
    
    for i in range(0,10):
        trial[i] = randint(0, 10)
        if trial[i] < 3:
            LaserFootEnergy = high;
        else:
            LaserFootEnergy = medium;
          
    
    LaserFootEnergyCode = int((LaserFootEnergy-0.5)/0.25+1)
    
    ser = serial.Serial('/dev/cu.usbmodem14301')  # open first serial port
    print(ser.name )       # check which port was really used
    print('\n Start connection...Switch to Serial NOW!')
    t0=time.time();
    
    time.sleep(2)
    
    #firstIn =raw_input()
    #if firtIn == '1':
    #L111 means the laser is ON state

    if pain == '1':
        ser.write(b'1,H')
        time.sleep(1)
    elif pain == '2':
        ser.write(b'2,H')
        time.sleep(1)
    elif pain == '3':
        ser.write(b'3,H')
        time.sleep(1)
    elif pain == '0':
        ser.write(b'0,H')
        time.sleep(1)
    elif pain == '4':
        ser.write(b'4,H')
        time.sleep(1)
    elif pain == '5':
        ser.write(b'5,H')
        time.sleep(1)
    elif pain == '6':
        ser.write(b'6,H')
        time.sleep(1)
        
