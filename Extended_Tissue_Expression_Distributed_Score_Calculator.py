# This code calculates the proportional score of GPCR drug action based on their targets and their expression in different tissues.
### The formula for the drug score is equal to the sum of the drug level/KD X target expression X downstream effectors in each tissue. Similar tissues are grouped.

## Reading data from files
import csv
import os
# Setting path
path = "C:\\Users\\tvarusai\\EBI_Work\\BioModels\\GPCR\\GPCR project revived\\CSScore\\JUN18\\" #folder with input files
# Primary-Target data
PTFile = open(path+"All_Drug_Target_List_NEW.csv","r")
PTReader = csv.reader(PTFile)
PTReaderList = list(PTReader)
del(PTReaderList[0])
# Target-Effector data
TEFile = open(path+"Target_Effector_List_NEW.csv","r")
TEReader = csv.reader(TEFile)
TEReaderList = list(TEReader)
del(TEReaderList[0])
# Target-TissueExpression data
TTEFile = open(path+"Target_Tissue_Expression_List_NEW.csv","r")
TTEReader = csv.reader(TTEFile)
TTEReaderList = list(TTEReader)
# TissueType-Organ data
TOFile = open(path+"Tissue_Organ_Classification_List.csv","r")
TOReader = csv.reader(TOFile)
TOReaderList = list(TOReader)
del(TOReaderList[0])
# Score data
SFile = open(path+"eDES_Primary_Targets_Score_List_NEW.csv","r")
SReader = csv.reader(SFile)
SReaderList = list(SReader)
del(SReaderList[0])
# Drug-Target-KD data
DTKFile = open(path+"Drug_Target_KD.csv","r")
DTKReader = csv.reader(DTKFile)
DTKReaderList = list(DTKReader)
del(DTKReaderList[0])
# Drug-Level data
DLFile = open(path+"Drug_Level.csv","r")
DLReader = csv.reader(DLFile)
DLReaderList = list(DLReader)
del(DLReaderList[0])


## Preparing lists for drugs, targets & effectors
# Drug-target list
drugTarList = []
drugList = list(sorted(set([item[0] for item in PTReaderList])))
for drug in drugList:
    tarList = []
    for item in PTReaderList:
        if drug == item[0]:
            tarList.append(item[1])
    grp1 = [drug,list(set(tarList))]
    drugTarList.append(grp1)
# Target-effector list
tarEffDict = {}
for item in TEReaderList:
    tarEffDict[item[0]] = int(item[2])
# Tissue-Organ dictionary
tissOrg ={}
uniqOrg = set(sec[1] for sec in TOReaderList)
for org in uniqOrg:
    tissOrg[org] = [it[0] for it in TOReaderList if it[1]== org]
    
## Scores for only single drug
singleDrug = 'bromocriptine'
drugTarList = [drugTarList[[item[0] for item in drugTarList].index(singleDrug)]]
##
    
    
## Calculating the score
# Three loops for each drug, organ & target
TTEHeader = TTEReaderList[0]
del(TTEReaderList[0])
uniqOrgHead = list(uniqOrg)
uniqOrgHead.insert(0,"Drug")
drugCRScoreList = [uniqOrgHead]
for drug in drugTarList:
    rowIndexDL = [item[0] for item in DLReaderList].index(drug[0])
    drugScore = [ds[1] for ds in SReaderList if ds[0]==drug[0]]
    orgScore = []
    for org in uniqOrg:
        tarEff = 0.0
        for tis in tissOrg[org]:
            for target in drug[1]:
                effCount = tarEffDict.get(target)
                rowIndex = [item[0] for item in TTEReaderList].index(target)
                rowIndexKD = [item[1] for item in DTKReaderList].index(target)
                colIndex = TTEHeader.index(tis)
                tarEff = tarEff + float(float(DTKReaderList[rowIndexKD][2])*float(effCount)*float(TTEReaderList[rowIndex][colIndex])/float(DLReaderList[rowIndexDL][1]))
    #            print("Effector count for ",target," is ",float(effCount))
    #            print("Expression in: ",drugCRScoreList[0][tis]," is ",float(TTEReaderList[rowIndex][tis]))
    #            print("Score: ",float(float(effCount)*float(TTEReaderList[rowIndex][tis])))
        grp3 = [float(tarEff)*100/float(drugScore[0]) if float(drugScore[0])!=0.0 else 0]
        orgScore.append(grp3)
    orgScore.insert(0,[drug[0]])
    orgScoreFlat = [item for sublist in orgScore for item in sublist]
    drugCRScoreList.append(orgScoreFlat)

## Writing data into a file
DrugCRScoreFile = open(path+"eDES_AllDrugOrganCRScorePythonOPFile_NEW.csv",'w',newline="\n")
with DrugCRScoreFile:
    writer = csv.writer(DrugCRScoreFile)
    writer.writerows(drugCRScoreList)