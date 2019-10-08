from os import listdir

mypath = "/home/dgxadmin"

from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath)]

for dd in onlyfiles:
    
    if(isfile(join(mypath, dd)) == False ):
        print(dd)

