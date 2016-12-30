f = open("hello.txt")
context = f.read(5)           # 读取文件前5个字节内容
print (context)
print (f.tell())                # 返回文件对象当前指针位置
context = f.read(5)          # 继续读取5个字节内容
print (context)
print (f.tell())               # 输出文件当前指针位置
f.close()
