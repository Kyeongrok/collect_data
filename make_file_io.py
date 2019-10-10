import datetime
import random
from aux_info_maker import makeAuxInfo

def makeFileIo(station, location, device, mount, status, datetime):
    aa = {
        "station":station,
        "location":location,
        "device":device,
        "mount":mount,
        "status":status,
        "datetime":datetime
    }
    return aa
