from tkinter import *
root = Tk()
root.title("顶层窗口")
# 使用state参数来设定按钮的状态
Button(root, text="禁用", state=DISABLED).pack(side=LEFT)
Button(root, text="取消").pack(side=LEFT)
Button(root, text="确定").pack(side=LEFT)
Button(root, text="退出", command=root.quite).pack(side=RIGHT) # 绑定了退出的回调
root.mainloop()
