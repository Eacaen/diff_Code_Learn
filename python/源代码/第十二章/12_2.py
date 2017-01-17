from tkinter import *
root = Tk()
root.title("顶层窗口")
for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    f = Frame(root, borderwidth=2, relief=relief)     # 定义框架
     # 定义标签，并且使用side参数设定排列方式
    Label(f, text=relief, width=10).pack(side=LEFT)  
    # 显示框架，并设定向左排列，x和y轴的宽度均为5个像素
    f.pack(side=LEFT, padx=5, pady=5)  
root.mainloop()
