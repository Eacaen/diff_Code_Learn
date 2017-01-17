from tkinter import *
root = Tk()
root.title("顶层窗口")
l = [('red', 1, NORMAL), ('green', 2, NORMAL), ('black', 3, DISABLED), ('blue', 4, NORMAL), 05  ('yellow', 5, DISABLED)]
for text, value, status in l:
    foo = IntVar()
    c = Checkbutton(root, text=text, variable=foo, state=status)   # 使用state设定按钮的状09    态
    c.pack(anchor = W)
root.mainloop()
