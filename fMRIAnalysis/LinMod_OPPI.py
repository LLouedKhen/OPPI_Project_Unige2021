
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:22:48 2020

@author: sysadmin
"""
import pandas as pd
import os
import statsmodels.api as sm 
import statsmodels.formula.api as smf
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import numpy as np
from sklearn import preprocessing
from statsmodels.genmod.bayes_mixed_glm import BinomialBayesMixedGLM
import statsmodels.genmod.bayes_mixed_glm as smgb
import matplotlib.pyplot as plt
import seaborn as sns


os.chdir('/Users/loued/Documents/ImagingData/Behavioral')
data1 = pd.read_csv('All_Data.csv')
data2 = pd.read_csv('Self_Data.csv')
data3 = pd.read_csv('Other_Data.csv')

#data1.Target = data1.Target.replace({1: 'aSelf' , 0: 'bLover', 2: 'cBeloved',3:'dStranger'  })
#data1.Target2 = data1.Target2.replace({0: 'aSelf' , 1: 'cBeloved',2:'dStranger'  })

#data1.EP1 = preprocessing.scale(data1.EP1, with_mean=True)
#data1.EP2 = preprocessing.scale(data1.EP2, with_mean=True)
#data1.Prices = preprocessing.scale(data1.Prices, with_mean=True)
#data1.Rate = preprocessing.scale(data1.Rate, with_mean=True)
#data1.RiskAversion = preprocessing.scale(data1.RiskAversion, with_mean=True)
##data1.Outcome= preprocessing.scale(data1.Outcome_1, with_mean=True)
#data1.PainO= preprocessing.scale(data1.PainO, with_mean=True)
#data1.PaintoRatingDist= preprocessing.scale(data1.PaintoRatingDist, with_mean=True)
#data1.H1= preprocessing.scale(data1.H1, with_mean=True)
#data1.H2= preprocessing.scale(data1.H2, with_mean=True)
#data1.PE= preprocessing.scale(data1.PE, with_mean=True)
#data1.APE= preprocessing.scale(data1.APE, with_mean=True)
#data1.RiskPE= preprocessing.scale(data1.RiskPE, with_mean=True)
#data1.Surp= preprocessing.scale(data1.Surp, with_mean=True)
#data1.RiskPain= preprocessing.scale(data1.RiskPain, with_mean=True)
#data1.RiskPain2chk= preprocessing.scale(data1.RiskPain2chk, with_mean=True)
#data1.Precision= preprocessing.scale(data1.Precision, with_mean=True)
#data1.EmpathyC = preprocessing.scale(data1.EmpathyC, with_mean=True)
#data1.EmpathyA = preprocessing.scale(data1.EmpathyA, with_mean=True)
## data1.iloc[:, -22:-7] = preprocessing.scale(data1.iloc[:,-22:-7], with_mean=True)
#data2 = data2.rename(columns = {"RiskPain2chk": "Pain Risk 1","RiskPain":"Pain Risk 0", "Response": "Choice", "Rate": "Rating", "PainO": "Pain Outcome"})

#data1['Response'] = pd.get_dummies(data1['Response'])
# data1 = data1.drop(columns = 'Empathy')
# data1 = data1.drop(columns = 'EmpathyA')

#Names = {'RiskPain2chk', 'H2', 'Precision', 'RiskPE', 'Surp', 'APE'}
#Uncertainties = list({'RiskPain2chk', 'H2', 'Precision', 'RiskPE', 'Surp', 'APE'})
#UncertainData = pd.concat([data1.RiskPain2chk,data1.H2, data1.Precision, data1.RiskPE, data1.Surp, data1.APE], axis = 1)
#BICs = pd.DataFrame(np.zeros(6,))
#BICs = BICs.rename(index = {0 :'RiskPain2chk',1: 'H2',2: 'Precision',3: 'RiskPE',4: 'Surp',5: 'APE'})
#
#for i in range(0,len(Uncertainties)):
#    md = smf.mixedlm(" Rate~  C(Target2) * PainO  + C(Target2)*" + UncertainData[Uncertainties[i]].name + "+ C(Gender) +C(GenderSame) +  C(Target2)*Prices", data1, groups=data1["Subject"])
#    mdf =md.fit()
#    print(mdf.summary())
#    coefOfInterest = mdf.fe_params;
#    f2 = pd.DataFrame(np.zeros([len(coefOfInterest)]))
#    # for i in range(0,len(coefOfInterest)):
#    #     f2.iloc[i] = coefOfInterest.iloc[i]**2/(1- coefOfInterest.iloc[i]**2)
#    #     a = f2.iloc[i] > 0.1
#    #     if a.iloc[0]:
#    #         print(coefOfInterest.index[i])
#    plt.rc('figure',  figsize=(8, 12))
#    #plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
#    plt.text(0.01, 0.05, str(mdf.summary()), {'fontsize': 10}, fontproperties = 'monospace') # approach improved by OP -> monospace!
#    plt.axis('off')
#    plt.tight_layout()
#    plt.savefig('Model' + str(Uncertainties[i]) + '.png')
#    plt.close()
#    BICs.iloc[i,0] = (- 2 * mdf.llf) + (md.k_params * (np.log(md.nobs)))
#    
#BICs = BICs.rename(index = {0 :'RiskPain2chk',1: 'H2',2: 'Precision',3: 'RiskPE',4: 'Surp',5: 'APE'})
#
#BICs.to_csv('/Users/sysadmin/Documents/UniGe_ToPLaB/OPPM/BiCS_UncertaintyRatings_20210323.csv')



data2 = data2.rename(index = {'NPSSig': 'NPS'})
data3 = data3.rename(index = {'VPSSig': 'VPS'})

Targets = ['Self',  'Stranger']

os.chdir('/Users/loued/Documents/ImagingStudy_Draft/Figures_OPPI')


ax14= sns.lmplot(x="EP1",y="choices", hue="target", data=data1, scatter= False, logistic = True, legend_out = False);
ax14.set(yticks=(0,1))
ax14.set_yticklabels(("Gamble", "Sure"))
ax14.set_xlabels(("Expected Pain"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2a.svg', format='svg', dpi=1200)

ax15= sns.lmplot(x="Risk1",y="choices", hue="target", data=data1, scatter= False,  logistic = True, legend_out = False);
ax15.set(yticks=(0,1))
ax15.set_yticklabels(("Gamble", "Sure"))
ax15.set_xlabels(("Risk "))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2b.svg', format='svg', dpi=1200)

ax16 = sns.lmplot(x="choiceRT",y="choices", hue="target", data=data1, scatter= False, logistic = True, legend_out = False);
ax16.set(yticks=(0,1))
ax16.set_yticklabels(("Gamble", "Sure"))
ax16.set_xlabels(("Choice RT"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2c.svg', format='svg', dpi=1200)

md5a = smf.mixedlm("bids~  C(target)* EP1   +  C(target)* C(choices) + C(Gender) ", data1, groups=data1["subject"])
mdf5a =md5a.fit()

print(mdf5a.summary())

adjBids = mdf5a.resid

data1 = pd.concat([data1, adjBids], axis = 1)
data1 = data1.rename(columns = {0:"Adjusted Bids"})



ax17= sns.lmplot(x="EP1",y="bids", hue="target", data=data1, scatter= False, legend_out = False);
ax17.set_xlabels(("Expected Pain"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2d.svg', format='svg', dpi=1200)

ax18= sns.lmplot(x="Risk1",y="Adjusted Bids", hue="target", data=data1, scatter= False, legend_out = False);
ax18.set_xlabels(("Risk"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2e.svg', format='svg', dpi=1200)

md5b = smf.mixedlm("bids~  C(target)* Risk1 +C(target)* EP1   +  C(target)* C(choices) + C(Gender) ", data1, groups=data1["subject"])
mdf5b =md5b.fit()

print(mdf5b.summary())

adjBids2 = mdf5b.resid

data1 = pd.concat([data1, adjBids2], axis = 1)
data1 = data1.rename(columns = {0:"Adjusted Bids (2)"})

ax19 = sns.lmplot(x="bidRT",y="Adjusted Bids (2)", hue="target", data=data1, scatter= False, legend_out = False);
ax19.set_xlabels(("Bid RT"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2f.svg', format='svg', dpi=1200)




ax20= sns.lmplot(x="painO",y="ratings", hue="target", data=data1, scatter= False, legend_out = False);
ax20.set_xlabels(("Pain Outcome"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2g.svg', format='svg', dpi=1200)

md6a = smf.mixedlm("ratings~  C(target)* painO    + C(Gender) ", data1, groups=data1["subject"])
mdf6a =md6a.fit()

print(mdf6a.summary())

adjRatings = mdf6a.resid

data1 = pd.concat([data1, adjRatings], axis = 1)
data1 = data1.rename(columns = {0:"Adjusted Ratings"})

ax21= sns.lmplot(x="PainPE",y="Adjusted Ratings", hue="target", data=data1, scatter= False, legend_out = False);
ax21.set_xlabels(("Pain PE"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2h.svg', format='svg', dpi=1200)


md6b = smf.mixedlm("ratings~  C(target)* painO  +C(target)* PainPE  + C(Gender) ", data1, groups=data1["subject"])
mdf6b =md6b.fit()

print(mdf6b.summary())

adjRatings2 = mdf6b.resid

data1 = pd.concat([data1, adjRatings2], axis = 1)
data1 = data1.rename(columns = {0:"Adjusted Ratings (2)"})

ax22 = sns.lmplot(x="Surp",y="Adjusted Ratings (2)", hue="target", data=data1, scatter= False, legend_out = False);
ax22.set_xlabels(("Surprise"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2i.svg', format='svg', dpi=1200)

md6c = smf.mixedlm("ratings~  C(target)* painO  +C(target)* PainPE +C(target)* Surp  + C(Gender) ", data1, groups=data1["subject"])
mdf6c =md6c.fit()

print(mdf6c.summary())

adjRatings3 = mdf6c.resid


data1 = pd.concat([data1, adjRatings3], axis = 1)
data1 = data1.rename(columns = {0:"Adjusted Rating (3)"})

ax23 = sns.lmplot(x="rateRT",y="Adjusted Rating (3)", hue="target", data=data1, scatter= False, legend_out = False);
ax23.set_xlabels(("Rate RT"))
plt.legend(title='Target', loc='upper right', labels=Targets)
plt.savefig('Figure2j.svg', format='svg', dpi=1200)


#NPS 


ax24 = sns.lmplot(x="painO",y="NPS", data=data2, scatter= False, legend_out = False) 
ax24.set_xlabels(("Rate RT"))
plt.savefig('Figure4a.svg', format='svg', dpi=1200)

md7a = smf.mixedlm("NPSSig ~ painO ", data2, groups=data2["subject"])
mdf7a =md7a.fit()

print(mdf7a.summary())

adjNPS = mdf7a.resid

data2 = pd.concat([data2, adjNPS], axis = 1)
data2 = data2.rename(columns = {0:"Adjusted NPS"})

ax25 = sns.lmplot(x="PainPE",y="Adjusted NPS", data=data2, scatter= False, legend_out = False) 
ax25.set_xlabels(("Pain PE"))
plt.savefig('Figure4b.svg', format='svg', dpi=1200)

md7b = smf.mixedlm("NPSSig ~ PainPE + painO", data2, groups=data2["subject"])
mdf7b =md7b.fit()

print(mdf7b.summary())

adjNPS2 = mdf7b.resid

data2 = pd.concat([data2, adjNPS2], axis = 1)
data2 = data2.rename(columns = {0:"Adjusted NPS (2)"})

ax26 = sns.lmplot(x="Surp",y="Adjusted NPS (2)", data=data2, scatter= False, legend_out = False) 
ax26.set_xlabels(("Surprise"))
plt.savefig('Figure4c.svg', format='svg', dpi=1200)



#VPS 


ax27 = sns.lmplot(x="painO",y="VPS", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax27.set_xlabels(("Pain Outcome"))
plt.savefig('Figure4d.svg', format='svg', dpi=1200)

md8a = smf.mixedlm("VPSSig ~ painO ", data3, groups=data3["subject"])
mdf8a =md8a.fit()

print(mdf8a.summary())

adjVPS = mdf8a.resid

data3 = pd.concat([data3, adjVPS], axis = 1)
data3 = data3.rename(columns = {0:"Adjusted VPS"})

ax28 = sns.lmplot(x="PainPE",y="Adjusted VPS", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax28.set_xlabels(("Pain PE"))
plt.savefig('Figure4e.svg', format='svg', dpi=1200)

md8b = smf.mixedlm("VPSSig ~ PainPE + painO", data3, groups=data3["subject"])
mdf8b =md8b.fit()

print(mdf8b.summary())

adjVPS2 = mdf8b.resid

data3 = pd.concat([data3, adjVPS2], axis = 1)
data3 = data3.rename(columns = {0:"Adjusted VPS (2)"})

ax29 = sns.lmplot(x="Surp",y="Adjusted VPS (2)", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax29.set_xlabels(("Surprise"))
plt.savefig('Figure4f.svg', format='svg', dpi=1200)




#NPS 


ax30 = sns.lmplot(x="painO",y="ratings", data=data2, scatter= False, legend_out = False) 
ax30.set_xlabels(("Pain Outcome"))
plt.savefig('Figure5a.svg', format='svg', dpi=1200)

md9a = smf.mixedlm("ratings ~ painO ", data2, groups=data2["subject"])
mdf9a =md9a.fit()

print(mdf9a.summary())

adjRating = mdf9a.resid

data2 = pd.concat([data2, adjRating], axis = 1)
data2 = data2.rename(columns = {0:"Adjusted Rating"})

ax31 = sns.lmplot(x="PainPE",y="Adjusted Rating", data=data2, scatter= False, legend_out = False) 
ax31.set_xlabels(("Pain PE"))
plt.savefig('Figure5b.svg', format='svg', dpi=1200)

md9b = smf.mixedlm("ratings ~ PainPE + painO", data2, groups=data2["subject"])
mdf9b =md9b.fit()

print(mdf9b.summary())

adjRating2 = mdf9b.resid

data2 = pd.concat([data2, adjRating2], axis = 1)
data2 = data2.rename(columns = {0:"Adjusted Rating (2)"})

ax32 = sns.lmplot(x="Surp",y="Adjusted Rating (2)", data=data2, scatter= False, legend_out = False) 
ax32.set_xlabels(("Surprise"))
plt.savefig('Figure5c.svg', format='svg', dpi=1200)

md9c = smf.mixedlm("ratings ~ PainPE + painO + Surp", data2, groups=data2["subject"])
mdf9c =md9c.fit()

print(mdf9c.summary())

adjRating3 = mdf9c.resid

data2 = pd.concat([data2, adjRating3], axis = 1)
data2 = data2.rename(columns = {0:"Adjusted Rating (3)"})

ax33 = sns.lmplot(x="NPS",y="Adjusted Rating (3)", data=data2, scatter= False, legend_out = False) 
plt.savefig('Figure5d.svg', format='svg', dpi=1200)

##NPS 


ax34 = sns.lmplot(x="painO",y="ratings", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax34.set_xlabels(("Pain Outcome"))
plt.savefig('Figure5e.svg', format='svg', dpi=1200)

md10a = smf.mixedlm("ratings ~ painO ", data3, groups=data3["subject"])
mdf10a =md10a.fit()

print(mdf10a.summary())

adjRating = mdf10a.resid

data3 = pd.concat([data3, adjRating], axis = 1)
data3 = data3.rename(columns = {0:"Adjusted Rating"})

ax35 = sns.lmplot(x="PainPE",y="Adjusted Rating", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax35.set_xlabels(("Pain PE"))
plt.savefig('Figure5f.svg', format='svg', dpi=1200)

md10b = smf.mixedlm("ratings ~ PainPE + painO", data3, groups=data3["subject"])
mdf10b =md10b.fit()

print(mdf10b.summary())

adjRating2 = mdf10b.resid

data3 = pd.concat([data3, adjRating2], axis = 1)
data3 = data3.rename(columns = {0:"Adjusted Rating (2)"})

ax36 = sns.lmplot(x="Surp",y="Adjusted Rating (2)", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
ax36.set_xlabels(("Surprise"))
plt.savefig('Figure5g.svg', format='svg', dpi=1200)

md10c = smf.mixedlm("ratings ~ PainPE + painO + Surp", data3, groups=data3["subject"])
mdf10c =md10c.fit()

print(mdf10c.summary())

adjRating3 = mdf10c.resid

data3 = pd.concat([data3, adjRating3], axis = 1)
data3 = data3.rename(columns = {0:"Adjusted Rating (3)"})

ax37 = sns.lmplot(x="VPS",y="Adjusted Rating (3)", data=data3, scatter= False, legend_out = False, line_kws={'color': 'orange'}) 
plt.savefig('Figure5h.svg', format='svg', dpi=1200)

#

#df = pd.concat([data2.rename(columns={'NPSSig':'x','adjRating3':'y'})
#                .join(pd.Series(['data2']*len(data2), name='df')), 
#                data3.rename(columns={'VPSSig':'x','adjRating3':'y'})
#                .join(pd.Series(['data3']*len(data3), name='df'))],
#               ignore_index=True)
#
#pal = dict(data2="red", data3="cyan")
#g = sns.FacetGrid(df, hue='df', palette=pal, size=5);
#g.map(plt.scatter, "x", "y", s=50, alpha=.7, linewidth=.5, edgecolor="white")
#g.map(sns.regplot, "x", "y", ci=None, robust=1)
#g.add_legend();



axRT1 = sns.boxplot(x="target", y="choiceRT", data=data1)
#plt.legend(title='Target', loc='upper right', labels=Targets)
axRT1.set_xticklabels(("Self", "Other"))
axRT1.set_ylabel(("Choice RT"))
axRT1 = sns.swarmplot(x="target", y="choiceRT", data=data1, color=".5")
plt.savefig('Figure2k.svg', format='svg', dpi=1200)

axRT2 = sns.boxplot(x="target", y="bidRT", data=data1)
#plt.legend(title='Target', loc='upper right', labels=Targets)
axRT2.set_xticklabels(("Self", "Other"))
axRT2.set_ylabel(("Bid RT"))
axRT2 = sns.swarmplot(x="target", y="bidRT", data=data1, color=".5")
plt.savefig('Figure2l.svg', format='svg', dpi=1200)


axRT3 = sns.boxplot(x="target", y="rateRT", data=data1)
#pltlegend(title='Target', loc='upper right', labels=Targets)
axRT3.set_xticklabels(("Self", "Other"))
axRT3.set_ylabel(("Rate RT"))
axRT3 = sns.swarmplot(x="target", y="rateRT", data=data1, color=".5")
plt.savefig('Figure2m.svg', format='svg', dpi=1200)
