#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:27:43 2021

1. convert dicom v
2. field map v
3. realignment v
4. bias correction ????
5. coregister 
6. Normalize
7. Smooth

Physio????

PhysIO from TNU

STC? Yes!
Bias correct? 
ADD STC DONE 
Fix Normalization to use TPMs DONE

Outstanding: 

ADD BIAS CORRECTION    
Run PhysIO!

@author: loued
"""

import nipype.interfaces.spm as spm
import nipype.interfaces.fsl as fsl
import nibabel as nib
from nipype.interfaces.matlab import MatlabCommand
MatlabCommand.set_default_matlab_cmd('/Applications/MATLAB_R2018b.app/bin/matlab -nodesktop -nosplash')
spm.SPMCommand.set_mlab_paths(paths='/Users/loued/Documents/MATLAB/spm12', matlab_cmd='/Applications/MATLAB_R2018b.app/bin/matlab -nodesktop -nosplash')


print(spm.Info.name())
print(spm.SPMCommand().version)
from zipfile import ZipFile
import os 
import glob
import nipype.interfaces.spm.utils as spmu
import re
import shutil
import pandas as pd
from nipype.interfaces.base import (CommandLine, traits, TraitedSpec,
                                    BaseInterface, BaseInterfaceInputSpec, File)

myPath = '/Users/loued/Documents/ImagingData/Dicom'

os.chdir(myPath)
exp1 =glob.glob('*.zip')
folders = os.listdir()

#for i in range(0,len(exp1)):
for i in range(0,len(exp1)):
     os.chdir(myPath)
     subID = exp1[i][0:-4]

from nipype.interfaces.spm import FieldMap
os.chdir(myPath)
subs = []
markerFilePP = ('preProcDONE.txt')
#for i in range(0,len(exp1)):    
for i in range(1,2):  
    subs.append(exp1[i][0:-4])
    subjFolder = os.path.join(myPath, subs[i]) 
    os.chdir(subjFolder)
    subCon = glob.glob('*Images')
    subjIFolder = os.path.join(subjFolder, subCon[0]) 
    os.chdir(subjIFolder)
    
    if not glob.glob(markerFilePP):
        
        epiFileFolder1 = glob.glob('Run1*')
        epiFolder1 = os.path.join(subjIFolder,epiFileFolder1[0]) 
        epiFileFolder2 = glob.glob('Run2*')
        epiFolder2 = os.path.join(subjIFolder,epiFileFolder2[0]) 
        
        os.chdir(epiFolder1)
        
        run1 = glob.glob('f2021*.nii')
        epiFile = os.path.join(epiFolder1, run1[5])
        epiFiles1 = []
        for j in range(0, len(run1)):
            epiFiles1.append(os.path.join(epiFolder1, run1[j]))
            
        os.chdir(epiFolder2)
        run2 = glob.glob('f2021*.nii')
        epiFiles2 = []
        for j in range(0, len(run2)):
            epiFiles2.append(os.path.join(epiFolder2, run2[j]))
        
        from nipype.interfaces.spm import SliceTiming
        
        st = SliceTiming()
        st.inputs.in_files = epiFiles1
        st.inputs.num_slices = 72
        st.inputs.time_repetition = 1.1
        st.inputs.time_acquisition = 1.1 - 1.1/72
        st.inputs.slice_order = list(range(72,0,-1))
        st.inputs.ref_slice = 36
        st.run() 
        
        st = SliceTiming()
        st.inputs.in_files = epiFiles2
        st.inputs.num_slices = 72
        st.inputs.time_repetition = 1.1
        st.inputs.time_acquisition = 1.1 - 1.1/72
        st.inputs.slice_order = list(range(72,0,-1))
        st.inputs.ref_slice = 36
        st.run() 
        
        os.chdir(epiFolder1)
        run1 = glob.glob('af2021*.nii')
        epiFile = os.path.join(epiFolder1, run1[10])
        epiFiles1 = []
        for j in range(0, len(run1)):
            epiFiles1.append(os.path.join(epiFolder1, run1[j]))
            
        os.chdir(epiFolder2)
        run2 = glob.glob('af2021*.nii')
        epiFiles2 = []
        for j in range(0, len(run2)):
            epiFiles2.append(os.path.join(epiFolder2, run2[j]))
        
        
        epiFile = epiFiles1[10]
        
        os.chdir(subjIFolder)
        
        t1FolderName = glob.glob('t1*')
        t1Folder = os.path.join(subjIFolder, t1FolderName[0])
        os.chdir(t1Folder)
        t1File = glob.glob('s2021*.nii')
        t1FileFull = os.path.join(t1Folder, t1File[0])
        os.chdir(subjIFolder)
        fMapFolders = glob.glob('*gre_field_mapping*')
        fMapFolder1 = os.path.join(subjIFolder, fMapFolders[0])
        os.chdir(fMapFolder1)
        
        magFile = glob.glob('*-2.nii')
        magFileFull = os.path.join(fMapFolder1 , magFile[0])
        phaseFile = glob.glob('*-1.nii')
        phaseFileFull = os.path.join(fMapFolder1 , phaseFile[0])
    
        fm = FieldMap()
        fm.inputs.phase_file = phaseFileFull
        fm.inputs.magnitude_file = magFileFull 
        fm.inputs.echo_times = (10, 12.46)
        fm.inputs.blip_direction = -1
        fm.inputs.total_readout_time = 21.10
        fm.inputs.epi_file = epiFile
        fm.run() 
        vdmFile = glob.glob('vdm*.nii')
        vdmFile = os.path.join(fMapFolder1, vdmFile[0])
        
        
        
        
        realignUnwarp = spm.RealignUnwarp()
        realignUnwarp.inputs.in_files = epiFiles1
        realignUnwarp.inputs.phase_map = vdmFile
        realignUnwarp.inputs.register_to_mean = True
        realignUnwarp.run()
        
        realignUnwarp = spm.RealignUnwarp()
        realignUnwarp.inputs.in_files = epiFiles2
        realignUnwarp.inputs.phase_map = vdmFile
        realignUnwarp.inputs.register_to_mean = True
        realignUnwarp.run()
        
        os.chdir(epiFolder1)
        rrun1 = glob.glob('uaf2021*.nii')
        meanf1 = glob.glob('meanuaf2021*.nii')
        repiFiles1 = []
        for j in range(0, len(rrun1)):
            x = os.path.join(epiFolder1, rrun1[j])
            repiFiles1.append(x)
        meanf1 = os.path.join(epiFolder1, meanf1[0])
        repiFiles1.append(meanf1)
        
        os.chdir(epiFolder2)
        rrun2 = glob.glob('uaf2021*.nii')
        meanf2 = glob.glob('meanuaf2021*.nii')
        repiFiles2 = []
        for j in range(0, len(rrun2)):
            x = os.path.join(epiFolder2, rrun2[j])
            repiFiles2.append(x)
        meanf2 = os.path.join(epiFolder2, meanf2[0])
        repiFiles2.append(meanf2)
    
        mlab = MatlabCommand()
        mlab.inputs.paths = '/Users/loued/Documents/MATLAB/spm12/toolbox/biasCorrect'
        bcPath = '/Users/loued/Documents/MATLAB/spm12/toolbox/biasCorrect/'
        os.chdir(bcPath)
        bcScr = os.path.join(bcPath, 'bcorrectNP.m')
    
        repiFiles = repiFiles1
        repiFilesM =pd.DataFrame(repiFiles)
        repiFilesM.to_csv('/Users/loued/Documents/MATLAB/spm12/toolbox/biasCorrect/repiFiles.csv')
        
        mlab.inputs.script = "bcorrectNP"  
        res = mlab.run()
        
        repiFiles = repiFiles2
        repiFilesM =pd.DataFrame(repiFiles)
        repiFilesM.to_csv('/Users/loued/Documents/MATLAB/spm12/toolbox/biasCorrect/repiFiles.csv')
    
        res = mlab.run()
        
        os.chdir(epiFolder1)
        brrun1 = glob.glob('buaf2021*.nii')
        meanf1 = glob.glob('bmeanuaf2021*.nii')
        meanf1 = os.path.join(epiFolder1, meanf1[0])
        brepiFiles1 = []
        for j in range(0, len(brrun1)):
            x = os.path.join(epiFolder1, brrun1[j])
            brepiFiles1.append(x)
        brepiFiles1.append(meanf1)
            
        os.chdir(epiFolder2)
        brrun2 = glob.glob('buaf2021*.nii')
        meanf2 = glob.glob('bmeanuaf2021*.nii')
        meanf2 = os.path.join(epiFolder2, meanf2[0])
        brepiFiles2 = []
        for j in range(0, len(brrun2)):
            x = os.path.join(epiFolder2, brrun2[j])
            brepiFiles2.append(x)
        brepiFiles1.append(meanf2)
       
        
        coreg = spm.Coregister()
        coreg.inputs.target = meanf1
        coreg.inputs.source = t1FileFull
        coreg.inputs.apply_to_files = brepiFiles1
        coreg.run() 
       
        coreg = spm.Coregister()
        coreg.inputs.target = meanf2
        coreg.inputs.source = t1FileFull
        coreg.inputs.apply_to_files = brepiFiles2
        coreg.run() 
        
        os.chdir(epiFolder1)
        cbrrun1 = glob.glob('rbuaf2021*.nii')
        cbrepiFiles1 = []
        for j in range(0, len(cbrrun1)):
            x = os.path.join(epiFolder1, cbrrun1[j])
            cbrepiFiles1.append(x)
    
            
        os.chdir(epiFolder2)
        cbrrun2 = glob.glob('rbuaf2021*.nii')
        cbrepiFiles2 = []
        for j in range(0, len(cbrrun2)):
            x = os.path.join(epiFolder2, cbrrun2[j])
            cbrepiFiles2.append(x)
    
        seg = spm.NewSegment()
        seg.inputs.channel_files = t1FileFull
        seg.inputs.write_deformation_fields = [True, True]
        tissue1 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 1), 2, (True,True), (False, False))
        tissue2 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 2), 2, (True,True), (False, False))
        tissue3 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 3), 2, (True,False), (False, False))
        tissue4 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 4), 2, (False,False), (False, False))
        tissue5 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 5), 2, (False,False), (False, False))
        tissue6 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 6), 2, (False,False), (False, False))
        seg.inputs.tissues = [tissue1, tissue2, tissue3, tissue4, tissue5, tissue6]
        seg.run() 
        
#        seg = spm.NewSegment()
#        seg.inputs.channel_files = cbrepiFiles2
#        tissue1 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 1), 2, (True,True), (False, False))
#        tissue2 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 2), 2, (True,True), (False, False))
#        tissue3 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 3), 2, (True,False), (False, False))
#        tissue4 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 4), 2, (False,False), (False, False))
#        tissue5 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 5), 2, (False,False), (False, False))
#        tissue6 = (('/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii', 6), 2, (False,False), (False, False))
#        seg.inputs.tissues = [tissue1, tissue2, tissue3, tissue4, tissue5, tissue6]
#        seg.run() 
        
        os.chdir(t1Folder)
        forDeform = glob.glob('y_*.nii')
        forDeformFile = os.path.join(t1Folder, forDeform[0])
        
        norm12 = spm.Normalize12()
        norm12.inputs.image_to_align = forDeformFile 
        norm12.inputs.apply_to_files = cbrepiFiles1
        norm12.run() 
        
        
        norm12 = spm.Normalize12()
        norm12.inputs.image_to_align = forDeformFile 
        norm12.inputs.apply_to_files = cbrepiFiles2
        norm12.run() 
        
        os.chdir(epiFolder1)
        wcbrrun1 = glob.glob('wrbuaf2021*.nii')
        wcbrepiFiles1 = []
        for j in range(0, len(wcbrrun1)):
            x = os.path.join(epiFolder1, wcbrrun1[j])
            wcbrepiFiles1.append(x)
    
            
        os.chdir(epiFolder2)
        wcbrrun2 = glob.glob('wrbuaf2021*.nii')
        wcbrepiFiles2 = []
        for j in range(0, len(wcbrrun2)):
            x = os.path.join(epiFolder2, wcbrrun2[j])
            wcbrepiFiles2.append(x)
    
        
        
        smooth = spm.Smooth()
        smooth.inputs.in_files = wcbrepiFiles1
        smooth.inputs.fwhm = [8, 8, 8]
        smooth.run() 

        smooth = spm.Smooth()
        smooth.inputs.in_files = wcbrepiFiles2
        smooth.inputs.fwhm = [8, 8, 8]
        smooth.run() 

        
        os.chdir(subjIFolder)
        markerFilePP= open('preProcDONE.txt', 'w')
    else:
        continue
        
        
        
        
physPath =  '/Users/loued/Documents/ImagingData/physio';
os.chdir(physPath)     
physFilesRun1 = glob.glob('sOPP*_1.mat')
physFilesRun2 = glob.glob('sOPP*_2.mat')

        

#for i in range(0,len(exp1)):    
for i in range(0,1):  
    subID = exp1[i][0:-4]
    subPath = os.path.join(myPath, subID)
    os.chdir(subPath)   
    imFolder = os.listdir()
    for j in range(0, len(imFolder)):
        if os.path.isdir(imFolder[j]):
            tImFolder = imFolder[j]
        else:
            continue
    subPathI = os.path.join(myPath, subID, tImFolder)     
    os.chdir(subPathI)
    markerFilePhys = ('physCopied.txt')
    if not glob.glob(markerFilePhys):
        epi1 = glob.glob('Run1*')
        epi2 = glob.glob('Run2*')
        fepi1 = os.path.join(subPathI, epi1[0])
        fepi2 = os.path.join(subPathI, epi2[0])
        ssubID = 's' + subID
        for k in range(0, len(physFilesRun1)):
            if ssubID in physFilesRun1[k]:
                thisPhys = os.path.join(physPath,physFilesRun1[k])
                nextPhys = os.path.join(fepi1,physFilesRun1[k] )
                shutil.copyfile(thisPhys, nextPhys)
        for k in range(0, len(physFilesRun2)):
            if ssubID in physFilesRun2[k]:
                thisPhys = os.path.join(physPath,physFilesRun2[k])
                nextPhys = os.path.join(fepi2,physFilesRun2[k] )
                shutil.copyfile(thisPhys, nextPhys)

        
        os.chdir(subPathI)
        markerFilePhysCP = open('physCopied.txt', 'w')
    else:
        continue

os.chdir(myPath)        
#for i in range(0,len(exp1)):    
for i in range(0,1):  
    subID = exp1[i][0:-4]
    subPath = os.path.join(myPath, subID)
    os.chdir(subPath)
    imFolder = os.listdir()
    for j in range(0, len(imFolder)):
        if os.path.isdir(imFolder[j]):
            tImFolder = imFolder[j]
        else:
            continue
    os.rename(tImFolder, subID+ 'Images')  
    subPathI = os.path.join(myPath, subID, subID+ 'Images')     
    os.chdir(subPathI)
    markerFilePhysReg = ('physRegsDone.txt')
    ssubID = 's' + subID
    if not glob.glob(markerFilePhysReg):
        run1 = glob.glob('Run1*')
        fullPath = os.path.join(subPathI, run1[0])
        os.chdir(fullPath)
        #scans = glob.glob('wrbuaf2021*.nii')
        scans = glob.glob('f2021*.nii')
        nscans = len(scans)
        os.chdir(physPath)
        physFile = glob.glob(ssubID + '_1.mat')
        physFileFull = os.path.join(physPath, physFile[0])
        physPar = []
        physPar.append(fullPath)
        physPar.append(nscans)
        physPar.append(physFileFull)
        
        physParDF = pd.DataFrame(physPar)
        physParDF.to_csv('/Users/loued/Documents/Preprocessing/Physio/physPar.csv')
    
        physIOPath = '/Users/loued/Documents/Preprocessing/Physio'
        os.chdir(physIOPath)
        physScr = os.path.join(physIOPath, 'physTemplate')
            
        mlab.inputs.script = "physTemplate"  
        res = mlab.run()
        
        os.chdir(subPathI)    
        run2 = glob.glob('Run2*')
        fullPath = os.path.join(subPathI, run2[0])
        os.chdir(fullPath)
        #scans = glob.glob('wrbuaf2021*.nii')
        scans = glob.glob('f2021*.nii')
        nscans = len(scans)
        os.chdir(physPath)
        physFile = glob.glob(ssubID + '_2.mat')
        physFileFull = os.path.join(physPath, physFile[0])
        physPar = []
        physPar.append(fullPath)
        physPar.append(nscans)
        physPar.append(physFileFull)
        physParDF = pd.DataFrame(physPar)
        physParDF.to_csv('/Users/loued/Documents/Preprocessing/Physio/physPar.csv')
    
        physIOPath = '/Users/loued/Documents/Preprocessing/Physio'
        os.chdir(physIOPath)
        physScr = os.path.join(physIOPath, 'physTemplate')
            
        mlab.inputs.script = "physTemplate"  
        res = mlab.run()
        os.chdir(fullPath)
        markerFilePhysReg= open('physRegsDone.txt', 'w')
    else:
        continue