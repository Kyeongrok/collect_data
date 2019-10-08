from os import listdir
from elasticsearch import Elasticsearch

mypath = "/ifs/mfc/data/mobis/L4_FR_CMR/10_raw"

from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath)]

def getAuxInfo(filePath):
    print(filePath)
    file = open(filePath)
    aa = [line.replace("\n","") for line in file.readlines()]
    splittedItems = [item.split(": ") for item in aa]
    file.close()
    obj = {}
    for splittedItem in splittedItems:
        if len(splittedItem) > 1:
            obj[splittedItem[0]] = splittedItem[1]
    return obj
    
def getLogObjects(filePath):
    print(filePath)
    file = open(filePath)
    print(file.read())
    file.close()


for dirName in onlyfiles:
    filePath = join(mypath, dirName)
    yyyymmdd = dirName.split("_")
    yymmdd = yyyymmdd[2][2:]
    print("yymmdd=>", yymmdd)
    
    if(isfile(filePath) == False ):
        print(dirName, filePath)
        auxInfo = getAuxInfo(filePath + "/aux_info")
        print(auxInfo)

        logObjPath = "{}/{}/{}_Data_Log_Object.csv".format(filePath, yymmdd, yymmdd)
        #print(logObjPath)
        #getLogObjects(logObjPath)



