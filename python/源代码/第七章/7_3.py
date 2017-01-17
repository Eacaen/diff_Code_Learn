# 使用readlines()读文件
f = file('hello.txt')
lines = f.readlines()
for line in lines:              # 一次读取多行内容
    print (line)
f.close()       
