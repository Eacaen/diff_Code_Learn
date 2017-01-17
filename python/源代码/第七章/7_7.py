# 追加新的内容到文件
f = file("hello.txt", "a+")         # 写入方式为追加a+
new_context = "goodbye"
f.write(new_context)
f.close()
