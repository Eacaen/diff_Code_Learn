try:
    s = "hello"
    try:                            # 嵌套异常
        print (s[0] + s[1])
        print (s[0] - s[1])
    except TypeError: 
        print ("字符串不支持减法运算")
except:
    print ("异常")
