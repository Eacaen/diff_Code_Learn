# 递归遍历目录
import os
def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print (pathname)

if __name__ == "__main__":
    path = r"D:\developer\python\example\07"
    VisitDir(path)
