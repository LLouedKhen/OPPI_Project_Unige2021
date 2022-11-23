
clear; 
clc;

dataPath = '/Users/loued/Documents/ImagingData/Behavioral';
cd(dataPath) 
load('AllSubject_Behavioral5.mat')
% reg = allSubjects;
% 
% load('AllSubject_Behavioral.mat')
% reg = allSubjects;
% load('AllSubject_Behavioral1.mat')
% rec = allSubjects;
% load('AllSubject_Behavioral2.mat')
% miss = allSubjects;
% load('AllSubject_Behavioral4.mat')
% rec2 = allSubjects;
% 
% reg = reg(17:end);

% allSubjects = [reg rec rec2];


choices = [];
choiceRT = [];
target = [];
bids = [];
bidRT = [];
painO = [];
ratings = [];
rateRT = [];

EP1 = [];
Risk1 = [];
H1 = [];
Conf1 = [];

EP2 = [];
Risk2 = [];
H2 = [];
Conf2 = [];

PainPE = [];
PainRiPE = [];
Surp = [];


RPE = []

subject = [];



for i = 1:length(allSubjects)
choices = [choices; allSubjects(i).self.Choice];
choiceRT = [choiceRT; allSubjects(i).self.gambleRT];
target = [target; allSubjects(i).self.Target];
bids = [bids; allSubjects(i).self.Bids];
bidRT = [bidRT; allSubjects(i).self.bidRT];
painO = [painO; allSubjects(i).self.PainOutcome];
ratings = [ratings; allSubjects(i).self.Rate];
rateRT =[rateRT; allSubjects(i).self.rateRT];

EP1 =[EP1; allSubjects(i).self.EP1];
EP2 =[EP2; allSubjects(i).self.EP2];
RPE =[RPE; allSubjects(i).self.RPE];

H1 =[H1; allSubjects(i).self.H1];
H2 =[H2; allSubjects(i).self.H2];

Risk1 =[Risk1; allSubjects(i).self.Risk1];
Risk2 =[Risk2; allSubjects(i).self.Risk2];

Conf1 =[Conf1; allSubjects(i).self.Conf1];
Conf2 =[Conf2; allSubjects(i).self.Conf2];

PainPE = [PainPE; allSubjects(i).self.PainPE];
PainRiPE = [PainRiPE; allSubjects(i).self.PainRiPE];
Surp = [Surp; allSubjects(i).self.Surp];

subject =[subject; allSubjects(i).self.Subject];


choices = [choices; allSubjects(i).other.Choice];
choiceRT = [choiceRT; allSubjects(i).other.gambleRT];
target = [target; allSubjects(i).other.Target];
bids = [bids; allSubjects(i).other.Bids];
bidRT = [bidRT; allSubjects(i).other.bidRT];
painO = [painO; allSubjects(i).other.PainOutcome];
ratings = [ratings; allSubjects(i).other.Rate];
rateRT =[rateRT; allSubjects(i).other.rateRT];

EP1 =[EP1; allSubjects(i).other.EP1];
EP2 =[EP2; allSubjects(i).other.EP2];
RPE =[RPE; allSubjects(i).other.RPE];

H1 =[H1; allSubjects(i).other.H1];
H2 =[H2; allSubjects(i).other.H2];

Risk1 =[Risk1; allSubjects(i).other.Risk1];
Risk2 =[Risk2; allSubjects(i).other.Risk2];

Conf1 =[Conf1; allSubjects(i).other.Conf1];
Conf2 =[Conf2; allSubjects(i).other.Conf2];

PainPE = [PainPE; allSubjects(i).other.PainPE];
PainRiPE = [PainRiPE; allSubjects(i).other.PainRiPE];
Surp = [Surp; allSubjects(i).other.Surp];

subject =[subject; allSubjects(i).other.Subject];

end

allMat = [choices choiceRT EP1 Risk1 H1 Conf1 bids bidRT EP2 Risk2 H2 Conf2 painO ratings rateRT PainPE PainRiPE Surp RPE  target subject];
allMat(allMat(:,1) == -1, :) = [];
allMatT = array2table(allMat);
allMatT.Properties.VariableNames = {'choices', 'choiceRT', 'EP1', 'Risk1', 'H1', 'Conf1', 'bids', 'bidRT', 'EP2', 'Risk2', 'H2', 'Conf2', 'painO', 'ratings', 'rateRT','PainPE', 'PainRiPE', 'Surp', 'RPE', 'target', 'subject'};

allMatT.EP1 = (allMatT.EP1 - mean(allMatT.EP1))./std(allMatT.EP1);
allMatT.EP2 = (allMatT.EP2 - mean(allMatT.EP2))./std(allMatT.EP2);

allMatT.Risk1 = (allMatT.Risk1 - mean(allMatT.Risk1))./std(allMatT.Risk1);
allMatT.Risk2 = (allMatT.Risk2 - mean(allMatT.Risk2))./std(allMatT.Risk2);

allMatT.H1 = (allMatT.H1 - mean(allMatT.H1))./std(allMatT.H1);
allMatT.H2 = (allMatT.H2 - mean(allMatT.H2))./std(allMatT.H2);

allMatT.Conf1 = (allMatT.Conf1 - mean(allMatT.Conf1))./std(allMatT.Conf1);
allMatT.Conf2 = (allMatT.Conf2  - mean(allMatT.Conf2 ))./std(allMatT.Conf2 );

allMatT.PainPE  = (allMatT.PainPE  - mean(allMatT.PainPE ))./std(allMatT.PainPE );
allMatT.PainRiPE = (allMatT.PainRiPE - mean(allMatT.PainRiPE))./std(allMatT.PainRiPE);

allMatT.Surp = (allMatT.Surp - mean(allMatT.Surp))./std(allMatT.Surp);

allMatT.target = categorical(allMatT.target);
% allMatT.choices(allMatT.choices ==1) = 1;
% allMatT.choices(allMatT.choices ==4) = 0;

lm1 = fitglme(allMatT, 'choices ~ target * EP1 + target * Risk1  + (target|subject)', 'Distribution', 'Binomial', 'BinomialSize', ones(height(allMatT),1), 'Link', 'logit');
%glm1 = fitglme(allMatT, 'choices ~ target * EP1 + target * Risk1  + (target|subject)');
glm2 = fitglme(allMatT, 'bids ~ target * EP1 + target * Risk1  + choices * target +(target|subject)');
%glm3 = fitglme(allMatT, 'ratings ~ target * PainPE + target * PainRiPE  +  painO  + bids * target +(target|subject)');

glm3 = fitglme(allMatT, 'ratings ~ target * PainPE + target * Risk2  +  target * painO  + bids * target +(target|subject)');

lm2 = fitglme(allMatT, 'choices ~ target * EP1 + target * H1  + (target|subject)', 'Distribution', 'Binomial', 'BinomialSize', ones(height(allMatT),1), 'Link', 'logit');
%glm1 = fitglme(allMatT, 'choices ~ target * EP1 + target * Risk1  + (target|subject)');
glm4 = fitglme(allMatT, 'bids ~ target * EP1 + target * H1  + choices * target +(target|subject)');
%glm3 = fitglme(allMatT, 'ratings ~ target * PainPE + target * PainRiPE  +  painO  + bids * target +(target|subject)');

glm5 = fitglme(allMatT, 'ratings ~ target * PainPE + target * H2  +  painO  + bids * target +(target|subject)');
glm6 = fitglme(allMatT, 'ratings ~ target * PainPE + target * Surp  +  painO  + bids * target +(target|subject)');
glm7 = fitglme(allMatT, 'ratings ~ target * PainPE + target * PainRiPE +  painO  + bids * target +(target|subject)');

allMatS = allMat(allMat(:,20) == 0,:);
allMatO = allMat(allMat(:,20) == 1,:);

figure 
bar([sum(allMatS(:,1)), sum(allMatO(:,1))]);

[choiceRTH, choiceRTp] = ttest2(allMatS(:,2), allMatO(:,2))

[bidsH, bidsp] = ttest2(allMatS(:,7), allMatO(:,7))

[bidRTH, bidRTp] = ttest2(allMatS(:,8), allMatO(:,8))

[painH, painp] = ttest2(allMatS(:,13), allMatO(:,13))

[ratingsH, ratingsp] = ttest2(allMatS(:,14), allMatO(:,14))

[rateRTH, rateRTp] = ttest2(allMatS(:,15), allMatO(:,15))
