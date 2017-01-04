# 修改后缀名
import os  
files = os.listdir(".")
for filename in files:
    pos = filename.find(".")
    if filename[pos + 1:] == "html":
        newname = filename[:pos + 1] + "htm"
        os.rename(filename,newname)
