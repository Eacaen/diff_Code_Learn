# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import turtle
import time
# draw polygon with 3 sides and fill with red
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.begin_fill()       # 3)
turtle.color("red")
turtle.circle(50,steps=4) # 4)
turtle.end_fill()         # 5)
time.sleep(2)