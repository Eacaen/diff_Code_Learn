from tkinter import *
root = Tk()
root.title("顶层窗口")
l = Listbox(root, width=15)
l.pack()
for item in ['apple', 'orange', 'peach', 'banana', 'melon']:
    l.insert(END, item)
root.mainloop()
