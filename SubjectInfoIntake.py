#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:28:16 2019
Function for subject information 
@author: loued
"""

import os
import datetime as datetime
import re
import pandas as pd


def validate(subjDOB):
    while 1:
        try:
            datetime.datetime.strptime(subjDOB, '%Y-%m-%d')
        except ValueError:
            subjDOB= input('Incorrect date format. Please re-enter subject birthdate in YYYY-MM-DD format: ')
        else:
            break
        

 #Experiment Datapath
outputPath = '/Users/loued/Documents/PythonScripts/Experiment1_Output'
   
os.chdir(outputPath)

#What day are we today?
StudyDate = datetime.datetime.now()

#Enter subject number
subjectNum = input("Enter main participant identifier: ") 
while len(subjectNum) != 3:
    print("Error! Must enter 3 characters!")
    subjectNum  = input("Please re-enter main participant identifier: ")    
    print(subjectNum)
while os.path.exists(str('OPPM' + subjectNum)):
    print("Error! This subject directory exists already.")
    subjectNum  = input("Please re-enter main participant identifier: ")    
    print(subjectNum)
        
spouseNum = input("Enter spouse participant identifier: ") 
while len(spouseNum)!= 3:
    print("Error! Must enter 3 characters!")
    spouseNum=input("Please re-enter spouse participant identifier: ")     
    print(spouseNum)

while spouseNum != subjectNum:
    print("Participant numbers don't match. ")
    subjectNum  = input("Please re-enter main participant identifier: ") 
    spouseNum  = input("Please re-enter spouse participant identifier: ") 



#Enter subject birthdate
subjDOB= input('Enter subject birthdate in YYYY-MM-DD format: ')
validate(subjDOB)
now = datetime.datetime.strptime(str(StudyDate.date()), '%Y-%m-%d')
dob = datetime.datetime.strptime(subjDOB, '%Y-%m-%d')
Age = (now - dob)
Age = Age.days/365.2425
print (Age)

#Enter subject gender
subjGender= input("Enter main participant gender (M/F): ") 
while not re.match("^[MFmf]*$", subjGender):
    print ("Error! Only letters M, F allowed!")
    subjGender= input("Please re-enter main participant gender (M/F): ") 
    

    #Enter Likert Scale Ort
if int(subjectNum) % 2 == 0:
    RatScaleOr = 1;
elif int(subjectNum) % 2 != 0:
    RatScaleOr = 2;

subjectNum = 'OPPM' + subjectNum
spouseNum = 'OPPS' + spouseNum 

if not os.path.exists(subjectNum)  :
    os.makedirs(subjectNum)
subjPath = os.path.join(outputPath, subjectNum)
os.chdir(subjPath)
os.makedirs('Calibration')
os.makedirs('TaskOutput')
os.makedirs('Questionnaires')

testType= input("Is this sound (1), sound + LED (2), or sound + Laser (3)?") 
while not re.match("^[123]*$", testType):
    print ("Error! Only options 1,2,3 allowed!")
    testType= input("Is this sound (1), sound + LED (2), or sound + Laser (3)?") 
    

intakeData = [StudyDate, subjectNum, subjDOB, Age, subjGender, RatScaleOr, subjPath, testType]

intakeData = pd.DataFrame(intakeData)
intakeData.to_csv(subjectNum + '_IntakeData.csv')

#return (subjectNum, subjPath, RatScaleOr)