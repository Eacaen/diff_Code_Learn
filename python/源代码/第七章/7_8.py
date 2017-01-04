import os

file("hello.txt", "w")
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
