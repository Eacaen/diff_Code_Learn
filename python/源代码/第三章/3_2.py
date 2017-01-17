# if elif else语句
score = float( input("score:"))  # 接受用户输入并转换为float类型,当输入的为小数时，使用int转换会报错
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 60 <= score < 80:
    print("C")
else:
    print("D")
