#! python3
import os, re, shutil

path = ('C:\\Users\\Administrator\\Desktop\\updates\\')

os.chdir(path)

for name in os.listdir():
    #if not re.match(".*.lnk", name):
    if os.path.isdir(name):
        newname = name[:7] + ' ' + name[-11:]
        shutil.move(path + name, path + newname)  
