# shutil模块实现文件的复制
import shutil

shutil.copyfile("hello.txt","hello2.txt")
shutil.move("hello.txt","../") 
shutil.move("hello2.txt","hello3.txt")
