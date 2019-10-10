import datetime
from random import randint

def makeAuxInfo():
    # id생성하기
    login_ids = ["Driver Unavailable", "clare", "harry"]
    routes = ["Seoul", "Daegu", "Daejeon", "Busan"]
    configurations = ["mobis", "hyundai", "kia"]
    vins = ["1438", "1259", "000000"]
    vin = vins[randint(0, 2)]
    now = datetime.datetime.now()
    formattedDate = now.strftime("%Y%m%d_%H%M%S%_%f")

    dict = {"id":"dw_{}_{}".format(vin, formattedDate),
            "configuration":configurations[randint(0, len(configurations) - 1)],
            "login_id":login_ids[randint(0, len(login_ids) - 1)],
            "time":formattedDate,
            "vin":vin,
            "route":routes[randint(0, len(routes)-1)]
            }
    return dict


def saveToFileByLine(fileName, dict):
    list = [
        "id:"+dict['id'],
        "configuration:"+dict['configuration'],
        "peername:None",
        "login_id:"+dict['login_id'],
        "time:"+dict['time'],
        "vin:"+dict['vin'],
        "route: "+dict['route']
    ]
    file = open(fileName, "w+")
    for content in list:
        file.write("{}\n".format(content))

    file.close()

# saveToFileByLine("aux_info", auxInfo)

