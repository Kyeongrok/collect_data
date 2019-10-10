import time
from datetime import datetime
from elasticsearch import Elasticsearch
from log_object_maker import makeLogObject
from aux_info_maker import makeAuxInfo
import json

es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
# es = Elasticsearch()

es.indices.create(index="log_object")

for i in range(10000):
    now = datetime.now()
    logObj = makeLogObject(now)
    aux_info = makeAuxInfo()
    logObj.update(aux_info)
    res = es.create(index="log_object", id=aux_info['id'], body=logObj)
    print(i, res)
# 대전으로 가는 길에 뭐가 가장 많은가?


