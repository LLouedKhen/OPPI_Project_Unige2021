clear; 
clc;


dataPath = '/Users/loued/Documents/ImagingData/Behavioral';

cd(dataPath)
Folders = dir(fullfile(dataPath, 'OPP*'));
subjFolders = [];
for i = 1:length(Folders)
subjFolders{i} = fullfile(dataPath, Folders(i).name);
end

subjPaths = subjFolders';

allSubjects = struct();

for i = 1:length(subjPaths)
    thisPath = char(subjPaths{i});
    sThisPath = char(thisPath);
    subID1 = sThisPath(end -6:end);
    subID2 = [sThisPath(end -6:end -4), sThisPath(end -2:end)];
    self =struct();
    cd(thisPath)
%     delete *regressors*
    cd(thisPath)
    
    
    RespSelf = dir('AllVariables*self_.csv');
    respSelf = readtable(RespSelf.name);
    
    if strfind(RespSelf.name,'_0_')
        order(i,1) = 1;
    elseif strfind(RespSelf.name,'_1_')
        order(i,1) = 2;
    end
     
    Pain = respSelf.Pain;
    pPain = respSelf.pPain;
    EP1 = respSelf.EP1;
    Bids = respSelf.Prices;
    Rate = respSelf.Rate;
    Choice = respSelf.Response;
    Outcome = respSelf.Outcome;
    
    bidStat = respSelf.BidStat;
    
    for j = 1:height(respSelf)
        Risk1(j) = (pPain(j) * (Pain(j)^2)) - (EP1(j)^2);
        RPE(j) = bidStat(j) - (Bids(j)/10);
        if bidStat(j) == 1 && Choice(j) == 1
           pPain2(j) = (pPain(j)/2);
           Pain2(j) = Pain(j);
        elseif bidStat(j) == 1 && Choice(j) == 4
           pPain2(j) = pPain(j);
           Pain2(j) = Pain(j) -1;
        else 
            Pain2(j) = Pain(j);
            pPain2(j) = pPain(j);
        end
        EP2(j) = Pain2(j) * pPain2(j);
        Risk2(j) = (pPain2(j) * (Pain2(j)^2)) - (EP2(j)^2);
        
        if Outcome(j) > 0
           PainOutcome(j) = Pain2(j);
        else 
           PainOutcome(j) = 0;
        end
        PainPE(j) = PainOutcome(j) - EP2(j);
        PainRiPE(j) = (PainPE(j)^2) - Risk2(j); 
        Target(j) = 0;
        Subject(j) = i;
    end
           
    TimesSelf = dir('Times*self_.csv');
    timesSelf = readtable(TimesSelf.name);
    ExpDuration = sum(timesSelf.durTrial);
    disp(timesSelf.startTrial(1))
    
    gambleRT = timesSelf.Timepoint3 -timesSelf.Timepoint2;
    
    bidRT = timesSelf.TPG;
    
    rateRT = timesSelf.RateRT;
    
    
    respTable = table(Choice,EP1, Risk1', gambleRT, Bids, bidRT, bidStat, RPE', EP2', Risk2', PainOutcome', PainPE', PainRiPE', Rate, rateRT, Target', Subject');
    respTable.Properties.VariableNames = {'Choice', 'EP1', 'Risk1', 'gambleRT', 'Bids', 'bidRT', 'bidStat', 'RPE', 'EP2', 'Risk2', 'PainOutcome', 'PainPE', 'PainRiPE', 'Rate', 'rateRT', 'Target', 'Subject'};
    
    allSubjects(i).self =respTable;

    
    
    %% Other regressors
    RespOther = dir('AllVariables*other_.csv');
    respOther = readtable(RespOther.name);
    
    if strfind(RespOther.name,'_0_')
       order(i,2) = 1;
    elseif strfind(RespOther.name,'_1_')
        order(i,2) = 2;
    end
    
    Pain = respOther.Pain;
    pPain = respOther.pPain;
    EP1 = respOther.EP1;
    Bids = respOther.Prices;
    Rate = respOther.Rate;
    Choice = respOther.Response;
    Outcome = respOther.Outcome;
    
    bidStat = respOther.BidStat;
    
    for j = 1:height(respOther)
        Risk1(j) = (pPain(j) * (Pain(j)^2)) - (EP1(j)^2);
        RPE(j) = bidStat(j) - (Bids(j)/10);
        if bidStat(j) == 1 && Choice(j) == 1
           pPain2(j) = (pPain(j)/2);
           Pain2(j) = Pain(j);
        elseif bidStat(j) == 1 && Choice(j) == 4
           pPain2(j) = pPain(j);
           Pain2(j) = Pain(j) -1;
        else 
            Pain2(j) = Pain(j);
            pPain2(j) = pPain(j);
        end
        EP2(j) = Pain2(j) * pPain2(j);
        Risk2(j) = (pPain2(j) * (Pain2(j)^2)) - (EP2(j)^2);
        
        if Outcome(j) > 0
           PainOutcome(j) = Pain2(j);
        else 
           PainOutcome(j) = 0;
        end
        PainPE(j) = PainOutcome(j) - EP2(j);
        PainRiPE(j) = (PainPE(j)^2) - Risk2(j); 
        Target(j) = 1;
        Subject(j) = i;
    end
           
    TimesOther = dir('Times*other_.csv');
    timesOther = readtable(TimesOther.name);
    ExpDuration = sum(timesOther.durTrial);
    
    gambleRT = timesOther.Timepoint3 -timesOther.Timepoint2;
    
    bidRT = timesOther.TPG;

    rateRT = timesOther.RateRT;
    
  

    
    respTable = table(Choice,EP1, Risk1', gambleRT, Bids, bidRT, bidStat, RPE', EP2', Risk2', PainOutcome', PainPE', PainRiPE', Rate, rateRT, Target', Subject');
    respTable.Properties.VariableNames = {'Choice', 'EP1', 'Risk1', 'gambleRT', 'Bids', 'bidRT', 'bidStat', 'RPE', 'EP2', 'Risk2', 'PainOutcome', 'PainPE', 'PainRiPE', 'Rate', 'rateRT', 'Target', 'Subject'};
    
    allSubjects(i).other =respTable;
    cd(dataPath)
    
end
cd(dataPath)

bigFile = 'AllSubject_BehavioralALL.mat';
save(bigFile, 'allSubjects')

    
