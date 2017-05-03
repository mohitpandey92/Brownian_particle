
import numpy
from scipy import *
from pylab import *
import time
from visual import *


dt = 0.01
k = 1.0
T = 1.0/sqrt(dt)
x= 0.0
v=0;

floor = box (pos=(0,-4,-4), length=4, height=0.5, width=4, color=color.blue)
ball = sphere (pos=(0,0,0), radius=1, color=color.red)

for t in arange(0,100,dt):
   rate(100)
   v += dt*(-k*v + T*standard_normal())
   x += dt*v
   ball.pos = (x,0,0)


