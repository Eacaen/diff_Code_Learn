try:
    open("hello.txt", "r")             # 尝试读取一个不存在的文件
    print ("读文件")
except FileNotFoundErrorr:                      # 捕获FileNotFoundError异常
    print ("文件不存在")
except:                         # 其他异常情况
    print ("程序异常")
