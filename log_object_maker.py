import datetime
import random
from aux_info_maker import makeAuxInfo


def makeLogObject(now):
    logItems = [
        {"key": "RoadBoundry", "value": ["Pole-Group(Traffic Cone Group)", "Unknown or Multiple Case"]},
        {"key": "Cyclist", "value": ["Bicycle"]},
        {"key": "Motorcyclist", "value": ["Motorcycle"]},
        {"key": "RoadHazard", "value": ["Traffic Cone", "Unknown"]},
        {"key": "StructuralElement", "value": ["Turnnel"]},
        {"key": "RoadSurface", "value": ["Puddle"]},
        {"key": "Pedestrian", "value": ["Unknown"]}
    ]
    rndItem = lambda list: list[random.randint(0, len(list)-1)]
    logItem = rndItem(logItems)
    level2logItems = logItem['value']
    formattedDate = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    return {"datetime":formattedDate, "level1":logItem['key'], "level2":rndItem(level2logItems)}

def makeLogObjects():
    # aux_info를 생성한다
    # aux_info의 id를 key로 넣는다.
    # aux_info를 만들었으면 파일로 생성한다.
    file = open("./log.txt", "w+")
    now = datetime.datetime.now()
    for i in range(30):
        now += datetime.timedelta(seconds=random.randint(1, 100))
        logObj = makeLogObject(now)
        file.write("{},{},{}\n".format(now,logObj["level1"], logObj["level2"]))
    file.close()


