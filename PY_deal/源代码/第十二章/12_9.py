from tkinter import *
root = Tk()
root.title("顶层窗口")
l = Listbox(root, height=6, width=15)     # 设定一个列表组件，列表组件在下一小节介绍
scroll = Scrollbar(root, command=l.yview)  # 定义滚动条，并绑定一个回调
l.configure(yscrollcommand=scroll.set)
l.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
for item in range(20):
    l.insert(END, item)
root.mainloop()
