# 使用read()、write()实现拷贝
# 创建文件hello.txt
src = file("hello.txt", "w")
li = ["hello world\n", "hello China\n"]
src.writelines(li) 
src.close()
# 把hello.txt拷贝到hello2.txt
src = open("hello.txt", "r")
dst = open("hello2.txt", "w")
dst.write(src.read())
src.close()
dst.close()
