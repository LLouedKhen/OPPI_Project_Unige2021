function preprocess_OPP(subjectDataFolder)
%% Subject-specific
fprintf('Preprocessing data of subject %s\n',subjectDataFolder);


% Get gre-fieldmap folders
% (For some subjects gre-field data are organized in 2 folders and in
% others in 1)
greFolder_1 = dir(fullfile(subjectDataFolder,'/gre*'));
if numel(greFolder_1) == 2
    gre_magnFolder = fullfile(subjectDataFolder,greFolder_1(1).name);
    gre_phaseFolder = fullfile(subjectDataFolder,greFolder_1(2).name);
else
    greFolder_2 = dir(fullfile(subjectDataFolder,greFolder_1.name,'0*'));
    gre_magnFolder = fullfile(subjectDataFolder,greFolder_1.name,greFolder_2(1).name);
    gre_phaseFolder = fullfile(subjectDataFolder,greFolder_1.name,greFolder_2(2).name);
end

% Gre-fieldmap data
magnitude = dir(fullfile(gre_magnFolder,'*1.nii'));
magnitude = fullfile(gre_magnFolder,magnitude.name);
phase = dir(fullfile(gre_phaseFolder,'*.nii'));
phase = fullfile(gre_phaseFolder,phase.name);

%Functional Data 
EPIFolder1 = dir(fullfile(subjectDataFolder, '/Run1*'));
EPIFolder2 = dir(fullfile(subjectDataFolder, '/Run2*'));
% cd (EPIFolder.name);

EPI_Session1Folder = fullfile(subjectDataFolder, EPIFolder1.name);
EPI_Session2Folder = fullfile(subjectDataFolder, EPIFolder2.name);

% Get first file of functional data
funData1 = dir(fullfile(EPI_Session1Folder,'f*.nii'));
funDataFifthFile1 = fullfile(EPI_Session1Folder, funData1(5).name);
funData2 = dir(fullfile(EPI_Session2Folder,'f*.nii'));
funDataFifthFile2 = fullfile(EPI_Session2Folder, funData2(5).name);

clear funData % Don't need them. We will pass them later using spm_select




%% Subject-specific
fprintf('Preprocessing data of subject %s\n',subjectDataFolder);

% Get gre-fieldmap folders
% (For some subjects gre-field data are organized in 2 folders and in
% others in 1)
greFolder = dir(fullfile(subjectDataFolder,'/gre*'));

gre_magnFolder = fullfile(subjectDataFolder,greFolder(1).name);
gre_phaseFolder = fullfile(subjectDataFolder,greFolder(1).name);


% Gre-fieldmap data
magnitude = dir(fullfile(gre_magnFolder,'s*-2.nii'));
magnitude = fullfile(gre_magnFolder,magnitude.name);
phase = dir(fullfile(gre_phaseFolder,'s*-1.nii'));
phase = fullfile(gre_phaseFolder,phase.name);

    
% Structural data
structFolder_1 = dir(fullfile(subjectDataFolder,'t1*'));
structFolder_2 = dir(fullfile(subjectDataFolder,structFolder_1.name));
structData = dir(fullfile(subjectDataFolder,structFolder_1.name,'s2021*.nii'));
t1 = fullfile(subjectDataFolder,structFolder_1.name,structData.name);


%-----------------------------------------------------------------------
% Job saved on 14-Feb-2016 13:06:47 by cfg_util (rev $Rev: 6460 $)
% spm SPM - SPM12 (6470)
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
%% Start SPM analysis
spm('Defaults','fMRI');
spm_jobman('initcfg');

funDataSession1 = cellstr(spm_select('FPList', fullfile(EPI_Session1Folder), '^f.*\.nii$'));
funDataSession2 = cellstr(spm_select('FPList', fullfile(EPI_Session2Folder), '^f.*\.nii$'));

matlabbatch{1}.spm.temporal.st.scans = {funDataSession1 funDataSession2}';

%%
matlabbatch{1}.spm.temporal.st.nslices = 72;
matlabbatch{1}.spm.temporal.st.tr = 1.1;
matlabbatch{1}.spm.temporal.st.ta = 1.0847;
matlabbatch{1}.spm.temporal.st.so = 1:72;
matlabbatch{1}.spm.temporal.st.refslice = 36;
matlabbatch{1}.spm.temporal.st.prefix = 'a';
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.data.presubphasemag.phase = {phase};
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.data.presubphasemag.magnitude = {magnitude};
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.defaults.defaultsfile = {'/Users/loued/Documents/MATLAB/spm12/toolbox/FieldMap/pm_defaults.m'};
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.session(1).epi = {funDataFifthFile1};
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.session(2).epi = {funDataFifthFile2};
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.matchvdm = 1;
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.sessname = 'session';
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.writeunwarped = 0;
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.anat = '';
matlabbatch{2}.spm.tools.fieldmap.calculatevdm.subj.matchanat = 0;
matlabbatch{3}.spm.spatial.realignunwarp.data(1).scans(1) = cfg_dep('Slice Timing: Slice Timing Corr. Images (Sess 1)', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{3}.spm.spatial.realignunwarp.data(1).pmscan(1) = cfg_dep('Calculate VDM: Voxel displacement map (Subj 1, Session 1)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','vdmfile', '{}',{1}));
matlabbatch{3}.spm.spatial.realignunwarp.data(2).scans(1) = cfg_dep('Slice Timing: Slice Timing Corr. Images (Sess 2)', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{2}, '.','files'));
matlabbatch{3}.spm.spatial.realignunwarp.data(2).pmscan(1) = cfg_dep('Calculate VDM: Voxel displacement map (Subj 1, Session 2)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','vdmfile', '{}',{2}));
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.quality = 0.9;
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.sep = 4;
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.fwhm = 5;
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.rtm = 0;
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.einterp = 2;
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.ewrap = [0 0 0];
matlabbatch{3}.spm.spatial.realignunwarp.eoptions.weight = '';
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.basfcn = [12 12];
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.regorder = 1;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.lambda = 100000;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.jm = 0;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.fot = [4 5];
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.sot = [];
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.uwfwhm = 4;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.rem = 1;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.noi = 5;
matlabbatch{3}.spm.spatial.realignunwarp.uweoptions.expround = 'Average';
matlabbatch{3}.spm.spatial.realignunwarp.uwroptions.uwwhich = [2 1];
matlabbatch{3}.spm.spatial.realignunwarp.uwroptions.rinterp = 4;
matlabbatch{3}.spm.spatial.realignunwarp.uwroptions.wrap = [0 0 0];
matlabbatch{3}.spm.spatial.realignunwarp.uwroptions.mask = 1;
matlabbatch{3}.spm.spatial.realignunwarp.uwroptions.prefix = 'u';
matlabbatch{4}.spm.tools.biasCorrect.data{1}(1) = cfg_dep('Realign & Unwarp: Unwarped Images (Sess 1)', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','sess', '()',{1}, '.','uwrfiles'));
matlabbatch{5}.spm.tools.biasCorrect.data{1}(1) = cfg_dep('Realign & Unwarp: Unwarped Images (Sess 2)', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','sess', '()',{2}, '.','uwrfiles'));
matlabbatch{6}.spm.tools.biasCorrect.data{1}(1) = cfg_dep('Realign & Unwarp: Unwarped Mean Image', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','meanuwr'));
matlabbatch{7}.spm.spatial.coreg.estimate.ref(1) = cfg_dep('Bias correction: Bias corrected images', substruct('.','val', '{}',{6}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files'));
matlabbatch{7}.spm.spatial.coreg.estimate.source = {t1};
matlabbatch{7}.spm.spatial.coreg.estimate.other = {''};
matlabbatch{7}.spm.spatial.coreg.estimate.eoptions.cost_fun = 'nmi';
matlabbatch{7}.spm.spatial.coreg.estimate.eoptions.sep = [4 2];
matlabbatch{7}.spm.spatial.coreg.estimate.eoptions.tol = [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{7}.spm.spatial.coreg.estimate.eoptions.fwhm = [7 7];
matlabbatch{8}.spm.spatial.preproc.channel.vols(1) = cfg_dep('Coregister: Estimate: Coregistered Images', substruct('.','val', '{}',{7}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','cfiles'));
matlabbatch{8}.spm.spatial.preproc.channel.biasreg = 0.001;
matlabbatch{8}.spm.spatial.preproc.channel.biasfwhm = 60;
matlabbatch{8}.spm.spatial.preproc.channel.write = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(1).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,1'};
matlabbatch{8}.spm.spatial.preproc.tissue(1).ngaus = 1;
matlabbatch{8}.spm.spatial.preproc.tissue(1).native = [1 0];
matlabbatch{8}.spm.spatial.preproc.tissue(1).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(2).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,2'};
matlabbatch{8}.spm.spatial.preproc.tissue(2).ngaus = 1;
matlabbatch{8}.spm.spatial.preproc.tissue(2).native = [1 0];
matlabbatch{8}.spm.spatial.preproc.tissue(2).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(3).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,3'};
matlabbatch{8}.spm.spatial.preproc.tissue(3).ngaus = 2;
matlabbatch{8}.spm.spatial.preproc.tissue(3).native = [1 0];
matlabbatch{8}.spm.spatial.preproc.tissue(3).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(4).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,4'};
matlabbatch{8}.spm.spatial.preproc.tissue(4).ngaus = 3;
matlabbatch{8}.spm.spatial.preproc.tissue(4).native = [1 0];
matlabbatch{8}.spm.spatial.preproc.tissue(4).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(5).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,5'};
matlabbatch{8}.spm.spatial.preproc.tissue(5).ngaus = 4;
matlabbatch{8}.spm.spatial.preproc.tissue(5).native = [1 0];
matlabbatch{8}.spm.spatial.preproc.tissue(5).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(6).tpm = {'/Users/loued/Documents/MATLAB/spm12/tpm/TPM.nii,6'};
matlabbatch{8}.spm.spatial.preproc.tissue(6).ngaus = 2;
matlabbatch{8}.spm.spatial.preproc.tissue(6).native = [0 0];
matlabbatch{8}.spm.spatial.preproc.tissue(6).warped = [0 0];
matlabbatch{8}.spm.spatial.preproc.warp.mrf = 1;
matlabbatch{8}.spm.spatial.preproc.warp.cleanup = 1;
matlabbatch{8}.spm.spatial.preproc.warp.reg = [0 0.001 0.5 0.05 0.2];
matlabbatch{8}.spm.spatial.preproc.warp.affreg = 'mni';
matlabbatch{8}.spm.spatial.preproc.warp.fwhm = 0;
matlabbatch{8}.spm.spatial.preproc.warp.samp = 3;
matlabbatch{8}.spm.spatial.preproc.warp.write = [0 1];
matlabbatch{9}.spm.spatial.normalise.write.subj(1).def(1) = cfg_dep('Segment: Forward Deformations', substruct('.','val', '{}',{8}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','fordef', '()',{':'}));
matlabbatch{9}.spm.spatial.normalise.write.subj(1).resample(1) = cfg_dep('Bias correction: Bias corrected images', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files'));
matlabbatch{9}.spm.spatial.normalise.write.subj(2).def(1) = cfg_dep('Segment: Forward Deformations', substruct('.','val', '{}',{8}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','fordef', '()',{':'}));
matlabbatch{9}.spm.spatial.normalise.write.subj(2).resample(1) = cfg_dep('Bias correction: Bias corrected images', substruct('.','val', '{}',{5}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files'));
matlabbatch{9}.spm.spatial.normalise.write.woptions.bb = [-78 -112 -70
                                                          78 76 85];
matlabbatch{9}.spm.spatial.normalise.write.woptions.vox = [2 2 2];
matlabbatch{9}.spm.spatial.normalise.write.woptions.interp = 4;
matlabbatch{10}.spm.spatial.smooth.data(1) = cfg_dep('Normalise: Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{9}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{10}.spm.spatial.smooth.fwhm = [8 8 8];
matlabbatch{10}.spm.spatial.smooth.dtype = 0;
matlabbatch{10}.spm.spatial.smooth.im = 0;
matlabbatch{10}.spm.spatial.smooth.prefix = 's8';
matlabbatch{11}.spm.spatial.smooth.data(1) = cfg_dep('Normalise: Write: Normalised Images (Subj 2)', substruct('.','val', '{}',{9}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{2}, '.','files'));
matlabbatch{11}.spm.spatial.smooth.fwhm = [8 8 8];
matlabbatch{11}.spm.spatial.smooth.dtype = 0;
matlabbatch{11}.spm.spatial.smooth.im = 0;
matlabbatch{11}.spm.spatial.smooth.prefix = 's8';


%% Save batch and run
save('matlabbatch');
spm_jobman('run',matlabbatch);
