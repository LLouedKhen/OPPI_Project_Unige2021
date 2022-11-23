%OPP project model 43: In this model, we test for BOLD response at cue onset, choice
%onset, bid onset, bid outcome onset, pain onset and rating onset. These
%onsets are modulated by: EP1 precision weighted; EP2, precision weighted;
%Pain, PainPE, Pain Surprise; Rating, using 6s duration for cue and bid outcome onsets and 
%a delta function (0 duration) for pain outcome for SELF and 6s duration for cue and bid outcome onsets and 
%(6s duration) for pain outcome for OTHER. Model 43 extracts betas for each
%individual trial at the pain outcome.

clear; 
clc;
dataPath = '/Users/loued/Documents/ImagingData/';
dataPathAnalysis = '/Users/loued/Documents/ImagingData/Imaging_Analysis';
cd(dataPathAnalysis)
conmat = readtable('Model42_ConMatrix.csv');
conmatARR = table2array(conmat(:,2:end));
dataPathB ='/Users/loued/Documents/ImagingData/Behavioral';
cd(dataPathB)
load MasterOrder.mat
subjFoldersB = dir('OPP*');
subjPathsB = [];

for i = 1:length(subjFoldersB)
    subjPathsB{i} = fullfile(dataPathB,subjFoldersB(i).name);
end

subjPathsB = subjPathsB';

dataPathI = '/Users/loued/Documents/ImagingData/Dicom';
cd(dataPathI)

subjFoldersI = dir('OPP*');
subjPathsI = [];

for i = 1:length(subjFoldersI)
    subjPathsI{i} = fullfile(dataPathI,subjFoldersI(i).name);
end

subjPathsI = subjPathsI';

% skip = {'OPPM114', 'OPPM125'};
% NotThese = find(contains(order.Subject,skip));
% order(NotThese,:) = [];
% skip = {'OPP114', 'OPP125'};
% subjPathsI(NotThese,:) = [];
% subjPathsB(NotThese,:) = [];
% subjFoldersI(NotThese,:) = [];
% subjFoldersB(NotThese,:) = [];

for i = 1:length(subjPathsI)
%for i = 23:23
if order.FullData{i} == 1
    cd(subjPathsB{i})
    thisPathB = subjPathsB{i};
    regs1 = dir('*selfRegressors*');
    regs1n = fullfile(thisPathB,regs1.name);
    load (regs1n)
    Regs1n = allRegs;
    trnumS = height(Regs1n);
    clear allRegs
    regs2 = dir('*otherRegressors*');
    regs2n = fullfile(thisPathB,regs2.name);
    load (regs2n)
    Regs2n = allRegs;
    trnumO = height(Regs2n);
    clear allRegs
     
    thisPathI = subjPathsI{i};
    subID = thisPathI(end -6:end);
    thisPathI = fullfile(thisPathI, [char(subID),'Images']);
    cd(thisPathI)
    
    subjectDataFolder = thisPathI;
    if ~isfile('resDoneModel43.txt')
    mkdir('ResultsModel43')
    resDir =fullfile(thisPathI,'/', 'ResultsModel43');
    
    if order.FirstRun{i} == 1
    
        EPI1 = dir('Run1*');
        EPI1Full = fullfile(thisPathI, EPI1.name);
        cd(EPI1Full)
        EP1Files = dir('s8*.nii');
        rpFile1 = dir('rp*.txt');
        rpFile1n = fullfile(EPI1Full,rpFile1.name);
        for j = 1:length(EP1Files)
            EP1FilesF{j} = fullfile(EPI1Full, EP1Files(j).name);
        end
        cd ..
        EPI2 = dir('Run2*');
        EPI2Full = fullfile(thisPathI, EPI2.name);
        cd(EPI2Full)
        EP2Files = dir('s8*.nii');
        rpFile2 = dir('rp*.txt');
        rpFile2n = fullfile(EPI2Full,rpFile2.name);
        for j = 1:length(EP2Files)
            EP2FilesF{j}  = fullfile(EPI2Full, EP2Files(j).name);
        end
        
    elseif order.FirstRun{i} == 2
        EPI1 = dir('Run2*');
        EPI1Full = fullfile(thisPathI, EPI1.name);
        cd(EPI1Full)
        EP1Files = dir('s8*.nii');
        rpFile1 = dir('rp*.txt');
        rpFile1n = fullfile(EPI1Full,rpFile1.name);
        for j = 1:length(EP1Files)
            EP1FilesF{j} = fullfile(EPI1Full, EP1Files(j).name);
        end   
        cd ..
        EPI2 = dir('Run1*');
        EPI2Full = fullfile(thisPathI, EPI2.name);
        cd(EPI2Full)
        EP2Files = dir('s8*.nii');
        rpFile2 = dir('rp*.txt');
        rpFile2n = fullfile(EPI2Full,rpFile2.name);
        for j = 1:length(EP2Files)
            EP2FilesF{j}  = fullfile(EPI2Full, EP2Files(j).name);
        end
    end
    cd (resDir)
    
%% Subject-specific
fprintf('First-Level analysis of subject %s\n', subID);

%% Start SPM analysis
spm('Defaults','fMRI');
spm_jobman('initcfg');

EP1FilesF = cellstr(spm_select('FPList', fullfile(EPI1Full), '^s8.*\.nii$'));
EP2FilesF = cellstr(spm_select('FPList', fullfile(EPI2Full), '^s8.*\.nii$'));

matlabbatch{1}.spm.stats.fmri_spec.dir = cellstr(resDir);
matlabbatch{1}.spm.stats.fmri_spec.timing.units = 'secs';
matlabbatch{1}.spm.stats.fmri_spec.timing.RT = 1.1;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t = 72;
matlabbatch{1}.spm.stats.fmri_spec.timing.fmri_t0 = 36;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).scans = EP1FilesF;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).name = 'cueOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).onset = Regs1n.cueOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).duration = 6;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).pmod(1).name = 'EP1 precision weighted';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).pmod(1).param = Regs1n.EP1.*Regs1n.Conf1;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(1).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).name = 'gambleOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).onset = Regs1n.gambleOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).tmod = 0;

matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).pmod(1).name = 'GambleRT';
%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).pmod(1).param = Regs1n.gambleRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(2).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).name = 'bidOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).onset = Regs1n.bidOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).pmod(1).name = 'bidRT';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).pmod(1).param =Regs1n.bidRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(3).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).name = 'bidOTime';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).onset = Regs1n.bidOOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).duration = 6;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).pmod(1).name = 'EP2 precision weighted';
%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).pmod(1).param =  Regs1n.EP2.*Regs1n.Conf2;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).pmod(1).poly = 1;

matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4).orth = 1;


for trs = 1:trnumS
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).name = ['trialOOnsets_Self',num2str(trs)];
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).onset = Regs1n.trialOOnsets(trs);
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).pmod = struct('name', {}, 'param', {}, 'poly', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(4+trs).orth = 1;
end


matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).name = 'rateOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).onset = Regs1n.rateOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(1).name = 'Rate';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(1).param = Regs1n.Rate;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(2).name = 'rateRT';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(2).param =Regs1n.rateRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).pmod(2).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(1).cond(trs +5).orth = 1;


matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi = {''};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(1).multi_reg = {rpFile1n};
matlabbatch{1}.spm.stats.fmri_spec.sess(1).hpf = 128;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).scans = EP2FilesF;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).name = 'cueOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).onset = Regs2n.cueOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).duration = 6;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).pmod(1).name = 'EP1 precision weighted';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).pmod(1).param = Regs2n.EP1 .*Regs2n.Conf1;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(1).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).name = 'gambleOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).onset = Regs2n.gambleOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).tmod = 0;

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).pmod(1).name = 'GambleRT';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).pmod(1).param = Regs2n.gambleRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(2).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).name = 'bidOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).onset = Regs2n.bidOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).tmod = 0;

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).pmod(1).name = 'bidRT';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).pmod(1).param = Regs2n.bidRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(3).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).name = 'bidOTime';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).onset = Regs2n.bidOOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).duration = 6;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).tmod = 0;

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).pmod(1).name = 'EP2 precision weighted ';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).pmod(1).param =  Regs2n.EP2 .* Regs2n.Conf2;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).pmod(1).poly = 1;

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4).orth = 1;

for tro = 1:trnumO
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).name = ['trialOOnsets_Other',num2str(tro)];
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).onset = Regs2n.trialOOnsets(tro);
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).duration = 6;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).pmod = struct('name', {}, 'param', {}, 'poly', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(4+tro).orth = 1;
end

matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).name = 'rateOnsets';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).onset = Regs2n.rateOnsets;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).duration = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).tmod = 0;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(1).name = 'Rate';
%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(1).param = Regs2n.Rate;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(1).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(2).name = 'rateRT';
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(2).param = Regs2n.rateRT;
%%
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).pmod(2).poly = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).cond(tro +5).orth = 1;
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi = {''};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).regress = struct('name', {}, 'val', {});
matlabbatch{1}.spm.stats.fmri_spec.sess(2).multi_reg = {rpFile2n};
matlabbatch{1}.spm.stats.fmri_spec.sess(2).hpf = 128;
matlabbatch{1}.spm.stats.fmri_spec.fact = struct('name', {}, 'levels', {});
matlabbatch{1}.spm.stats.fmri_spec.bases.hrf.derivs = [0 0];
matlabbatch{1}.spm.stats.fmri_spec.volt = 1;
matlabbatch{1}.spm.stats.fmri_spec.global = 'None';
matlabbatch{1}.spm.stats.fmri_spec.mthresh = 0.3;
matlabbatch{1}.spm.stats.fmri_spec.mask = {'/Users/loued/Documents/MATLAB/spm12/tpm/mask_ICV.nii'};
matlabbatch{1}.spm.stats.fmri_spec.cvi = 'FAST';
matlabbatch{2}.spm.stats.fmri_est.spmmat(1) = cfg_dep('fMRI model specification: SPM.mat File', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','spmmat'));
matlabbatch{2}.spm.stats.fmri_est.write_residuals = 0;
matlabbatch{2}.spm.stats.fmri_est.method.Classical = 1;

%% Save batch and run
save('matlabbatch');
spm_jobman('run',matlabbatch);
cd ..
file = 'resDoneModel43.txt';
save(file)
    else 
        continue
    end
else
    continue
end

end