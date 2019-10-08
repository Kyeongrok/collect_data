from os import listdir
from elasticsearch import Elasticsearch

es = Elasticsearch()

#mypath = "/ifs2/mfc/data/mobis/L4_FR_CMR/10_raw"
mypath = "/mnt/L4_FR_CMR/10_raw"

from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath)]

def getAuxInfo(filePath):
	#print(filePath)
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
	#print(filePath)
	file = open(filePath)
	splittedLines = [line.replace("\n","").split(",") for line in file.readlines()]
	file.close()

	objs = []
	for line in splittedLines:
		if len(line) > 2:
			obj ={}
			obj['datetime'] = line[0]
			obj['level1'] = line[1]
			obj['level2'] = line[2]
			objs.append(obj)

	return objs

def esCreate(logObj):
	res = es.create(index="log_object", id=logObj["vin"]+logObj["datetime"], body=logObj)
	print(res)



#es.indices.create(index="log_object")

cnt = 0
for dirName in onlyfiles:
	try:
		filePath = join(mypath, dirName)
		yyyymmdd = dirName.split("_")
		yymmdd = yyyymmdd[2][2:]
		
		if(isfile(filePath) == False ):
			try:
				print(dirName, filePath)
				auxInfo = getAuxInfo(filePath + "/aux_info")
				print(auxInfo)

				logObjPath = "{}/{}/{}_Data_Log_Object.csv".format(filePath, yymmdd, yymmdd)
				#print(logObjPath)
				logObjs = getLogObjects(logObjPath)
				for logObj in logObjs:
					logObj.update(auxInfo)
					#print(logObj)
					esCreate(logObj)
				cnt += 1
				print(cnt)
			except:
				print("---------error lv2 ------")
	except:
		print("------ error lv1 --------")


