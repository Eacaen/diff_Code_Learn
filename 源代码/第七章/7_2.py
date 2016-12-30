# 使用readline()读文件
f = open("hello.txt")
while True:
    line = f.readline()
    if line: 
        print (line)
    else:
        break
f.close()
