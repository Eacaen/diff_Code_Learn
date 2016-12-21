# linux 
import subprocess

pingP=subprocess.Popen(args=’ping –c 4 www.sina.com.cn’, shell=True)    #生成ping进程
print (pingP.pid)                 #打印进程ID
print (pingP.returncode)          #打印进程返回值

# windows
pingP=subprocess.Popen(args=’ping –n 4 www.sina.com.cn’, shell=True)    #生成ping进程
pirnt (pingP.pid)                #打印进程ID
print (pingP.returncode)         #打印进程返回值
