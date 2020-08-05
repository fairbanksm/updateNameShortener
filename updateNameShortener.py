#! python3
import os, re, shutil

path = ('C:\\Users\\Administrator\\Desktop\\updates\\')

for name in os.listdir(path):
    if not re.match(".*.lnk", name):
        print(name)
        newname = name[:7] + ' ' + name[-11:]
        shutil.move(path + name, path + newname)
