import random
from make_file_io import makeFileIo

import time
from datetime import datetime
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts=["ec2-54-180-123-238.ap-northeast-2.compute.amazonaws.com"])
# es = Elasticsearch()

# es.indices.create(index="io_log")

doc = makeFileIo("poc1.mobis.com", "", "FR_CAM", "/ifs/raw_10/FR_CAM", "inactive", "2019-10-10 10:10:10")

res = es.create(index="io_log", id=doc['datetime'], body=doc)


