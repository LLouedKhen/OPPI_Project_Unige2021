clear; 
clc;

% fMRI experiment folder
dataPath = '/Users/loued/Documents/ImagingData/';
dataPathI = '/Users/loued/Documents/ImagingData/Dicom';
cd(dataPathI)


% Subjects



subjFoldersI = dir('OPP*');
subjPathsI = [];

for i = 1:length(subjFoldersI)
    subjPathsI{i} = fullfile(dataPathI,subjFoldersI(i).name);
end

subjPathsI = subjPathsI';

cd(dataPath)
% subject =  {,};
subject =  subjPathsI;

nSubject = numel(subject);
% nSession = numel(session); 



for i = 32:nSubject
%     for j = 1:nSession 
    thisPathI = subjPathsI{i};
    subID = thisPathI(end -6:end);
    thisPathI = fullfile(thisPathI, [char(subID),'Images']);
    subjectDataFolder = thisPathI;

    % Change directory
    cd(subjectDataFolder);
%     cd(sessionDataFolder);
    
    % Perform analysis
    preprocess_OPP(subjectDataFolder);
%     end
end