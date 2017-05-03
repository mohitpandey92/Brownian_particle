from linear_ramp import *    
import time
t1=time.time()
tf=0.01
DeltaN=2000
N_exp=1000


t,x_mean,x_var,kappa=langevin_dynamics(tf, DeltaN,N_exp)

t2=time.time()

t_code=(t2-t1)/60
f=open('ramp_0.01_lowerDeltaT.dat','w')
f.write(" t_f =%f, Deltat=1./%d,N_exp=%d,code time=%f (in min) \n"  %(tf,DeltaN,N_exp, t_code))
f.write('"t" \t "x_mean" \t "x2_mean" \t "kappa" \n')
for i in range(len(t)):
	f.write(" %.12f \t %.12f \t  %.12f \t %.12f  \n"  %(t[i],x_mean[i],x_var[i],kappa[i]))
f.close()

    
    
    
    
    
    
    
    
