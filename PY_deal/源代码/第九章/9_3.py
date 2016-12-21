# finally错误的用法
try:
    f = open("hello.txt", "r")
    print ("读文件")
except FileNotFoundError:                           # 捕获FileNotFoundError异常
    print ("文件不存在")
finally:                                # 其他异常情况
    f.close()

try:
    f = open("hello.txt", "r") 
    try:                 
        print (f.read(5))
    except:
       print ("读取文件错误")
    finally:                            # finally子句一般用于释放资源
        print ("释放资源")    
        f.close()
except FileNotFoundError: 
    print ("文件不存在")
