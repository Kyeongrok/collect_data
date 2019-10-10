import random
from make_isilon_info import makeIsilonInfo

import time
from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
# es = Elasticsearch()

#es.indices.create(index="isilon_info")

doc = makeIsilonInfo()

res = es.create(index="isilon_info", id=doc['cluster_id'], body=doc)


