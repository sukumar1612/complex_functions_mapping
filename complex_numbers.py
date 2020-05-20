# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:38:56 2020

@author: Sukumar Ganesan
"""

# graph for complex functions
import turtle
import math

z=[(i,j) for i in range(-50,50) for j in range(-50,50)]
#graph for z^2
z2=[(z[i][0]**2-z[i][1]**2 , 2*z[i][0]*z[i][1]) for i in range(0,100*100)]
#graph for e^z
ez=[(math.exp(z[i][0])*math.cos((math.pi/180)*z[i][1]) , math.exp(z[i][0])*math.sin((math.pi/180)*z[i][1]) ) for i in range(0,100*100)]
#graph for z^3
z3=[(z[i][0]**3 - 3*z[i][0]*z[i][1]**2 , 3*z[i][0]**2*z[i][1] - z[i][1]**3) for i in range(0,100*100)]
#graph for cos(z)
csz=[(math.cos(z[i][0])*math.cosh(z[i][1]) , math.sin(z[i][0])*math.sinh(z[i][1]) ) for i in range(0,100*100)]

zplot=[ez,z2,z3,csz]
a=1

turtle.speed(0)
turtle.penup()
turtle.tracer(0, 0)
for i in range(0,10000):
    turtle.goto(zplot[a][i][0],zplot[a][i][1])
    turtle.dot("red")
"""for i in range(0,10000):
    turtle.goto(z[i][0],z[i][1])
    turtle.dot("yellow")
"""
turtle.done()