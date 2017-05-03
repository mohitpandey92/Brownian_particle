
import numpy
from scipy import *
from pylab import *
import time
graphics = 0
if graphics:
    from visual import *
import sys

def smooth(x,num):
   out = []
   for t in range(0,len(x),num):
      tmp = 0
      for i in range(num):
	     tmp += x[t+i]
      tmp = tmp/num
      out.append(tmp)
   return out
 

dt = 0.01
k = 1.0
T = sqrt(2.0/dt)
x= 0.0
x0=0
a = []

if (graphics):
   spring = helix(pos=(0,0,x0), axis=(1,0,0), radius=0.5)
   floor = box (pos=(0,-1,-1), length=10, height=0.5, width=1, color=color.blue)
   ball = sphere (pos=(0,0,0), radius=0.3, color=color.red)

for t in arange(0,10000,dt):
   x += dt*(-k*x + T*standard_normal())
   a.append(x)

   if (graphics):
      rate(10)
      ball.pos = (x,0,0)
      spring.pos = (x0,0,0)
      spring.axis=(x+x0,0,0)
      if scene.kb.keys:
	 key = scene.kb.getkey()
	 if (key == 'q'):
	    break
	    

n, bins, patches = hist(a, 100, normed=1)
sigma= std(a)
gauss = exp(-bins*bins/(2*sigma**2))/(sqrt(2*pi)*sigma)
plot(bins,gauss)
   
if graphics == 0:
    f = abs(fft(a))**2

    s = smooth(f,400)

    s_limit = 100
    small = s[0:s_limit]
    om = arange(0,s_limit,1.0,dtype=float)


    fitf = lambda p, omega: p[0]/(1+omega**2/p[1]**2) 
    errorf = lambda p, omega, data: fitf(p,omega)-data 
    p0 = [1000000.0,30.0]
    p1, success = optimize.leastsq(errorf,p0[:],args=(om,small))
    print p1

    plot(om,small,"b^",om,fitf(p1,om),"r-")


show()


