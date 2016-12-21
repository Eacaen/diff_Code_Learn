# 输出转义字符
path = "hello\tworld\n"
print (path)
print (len(path))  
path = r"hello\tworld\n"
print (path)
print (len(path))  

# strip()去掉转义字符
word = "\thello world\n"
print ("直接输出:", word)
print ("strip()后输出:", word.strip())
print ("lstrip()后输出:", word.lstrip())
print ("rstrip()后输出:", word.rstrip())

# 使用"+"连接字符串
str1 = "hello "
str2 = "world "
str3 = "hello "
str4 = "China "
result = str1 + str2 + str3
result += str4
print (result)

# 使用join()连接字符串
strs = ["hello ", "world ", "hello ", "China "]
result = "".join(strs)
print (result)

# 使用reduce()连接字符串
from functools import reduce
import operator
strs = ["hello ", "world ", "hello ", "China "]
result = reduce(operator.add, strs, "")
print (result)

# 使用索引截取子串
word = "world"
print (word[4])

# 特殊切片截取子串
str1 = "hello world"
print (str1[0:3])
print (str1[::2])
print (str1[1::2])

# 使用split()获取子串
sentence = "Bob said: 1, 2, 3, 4"
print ("使用空格取子串:", sentence.split())
print ("使用逗号取子串:", sentence.split(","))
print ("使用两个逗号取子串:", sentence.split(",", 2))

# 字符串的比较
str1 = 1
str2 = "1"
if str1 == str2:
    print ("相同")
else:
    print ("不相同")
if str(str1) == str2:
    print ("相同")
else:
    print ("不相同")

# 比较字符串的开始和结束处
word = "hello world"
print ("hello" == word[0:5])
print (word.startswith("hello"))
print (word.endswith("ld", 6))
print (word.endswith("ld", 6, 10))
print (word.endswith("ld", 6, len(word)))

# 查找字符串
sentence = "This is a apple."
print (sentence.find("a"))
sentence = "This is a apple."
print (sentence.rfind("a"))

# 字符串的替换
centence = "hello world, hello China"
print (centence.replace("hello", "hi"))
print (centence.replace("hello", "hi", 1))
print (centence.replace("abc", "hi"))

import time,datetime

# 时间到字符串的转换
print (time.strftime("%Y-%m-%d %X", time.localtime()))
# 字符串到时间的转换
t = time.strptime("2008-08-08", "%Y-%m-%d")
y, m, d = t[0:3]
print (datetime.datetime(y, m, d))
