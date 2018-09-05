import os
import os.path
import re
import sys
import codecs

 


def list_all_files(rootdir):
    _files = []
    files = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    # print(files)
    for i in range(0,len(files)):
           path = os.path.join(rootdir,files[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files
 

Path = '/media/eacaen/EACAEN-32'
# files = os.listdir(Path)
# # print(files)

f = list_all_files(Path) 
print('------>' )
# print(f)


for i in range(0 , len(f)):
	ff = f[i].split('/')
	print(ff[-1])