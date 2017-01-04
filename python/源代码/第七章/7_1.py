# 创建文件
context = '''hello world'''
           
f = open('hello.txt', 'w')          # 打开文件
f.write(context)                # 把字符串写入文件
f.close()                       # 关闭文件
