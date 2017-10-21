info = " "
def showFileProperties(path):
    f = open("record.log",'a+')
    import time,os
    global info
    for root,dirs,files in os.walk(path,True):
        print("path " + root)
        for filename in files:
            state = os.stat(os.path.join(root,filename))
            info = info + "name " + filename + "  "
            info = info + "size " + ("%d" % state[-4]) + "  "
            t = time.strftime("%Y-%m-%d  %X",time.localtime(state[-1]))
            info = info + "创建时间 " + t + "  "
            t = time.strftime("%Y-%m-%d  %X", time.localtime(state[-2]))
            info = info + "最后修改时间 " + t + "  "
            t = time.strftime("%Y-%m-%d  %X", time.localtime(state[-3]))
            info = info + "最后访问时间 " + t + "  "
            info = info +"\n"
            f.write(info)
            print(info)

if __name__ == "__main__":
    path = r"C:\Users\admin\Desktop\德意志银行开户-KIM"
    showFileProperties(path)
