# This code calculates the score of GPCR drug action based on their targets and their expression in different tissues.
### The formula for the drug score is equal to the sum of the target expression X downstream effectors in each tissue.

## Reading data from files
import csv
import os
# Setting path
path = "C:\\Users\\tvarusai\\EBI_Work\\BioModels\\GPCR\\GPCR project revived\\CSScore\\JUN18\\" #folder with input files
# Primary-Target data
#PTFile = open(path+"All_Drug_Target_List_NEW.csv","r")
PTFile = open(path+"Primary_Drug_Target_List_NEW.csv","r")
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
    

## Calculating the score
# Three loops for each drug, tissue & target
drugCRScoreList = [TTEReaderList[0]]
del(TTEReaderList[0])  
for drug in drugTarList:
    tissScore = []
    for tis in range(1,len(TTEReaderList[0])):
        tarEff = 0.0
        for target in drug[1]:
            effCount = tarEffDict.get(target)
            rowIndex = [item[0] for item in TTEReaderList].index(target) 
            tarEff = tarEff + float(float(effCount)*float(TTEReaderList[rowIndex][tis]))
#            print("Effector count for ",target," is ",float(effCount))
#            print("Expression in: ",drugCRScoreList[0][tis]," is ",float(TTEReaderList[rowIndex][tis]))
#            print("Score: ",float(float(effCount)*float(TTEReaderList[rowIndex][tis])))
        tissScore.append(tarEff)
    grp3 = [[drug[0]],tissScore]
    grp4Flat = [item for sublist in grp3 for item in sublist]
    drugCRScoreList.append(grp4Flat)

    
## Writing data into a file
#DrugCRScoreFile = open(path+"AllDrugCRScorePythonOPFile_NEW.csv",'w',newline="\n")
DrugCRScoreFile = open(path+"PrimaryDrugCRScorePythonOPFile_NEW.csv",'w',newline="\n")
with DrugCRScoreFile:
    writer = csv.writer(DrugCRScoreFile)
    writer.writerows(drugCRScoreList)