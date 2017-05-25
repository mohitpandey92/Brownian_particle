from quench_ramp import *    
import time
t1=time.time()

DeltaN=500
N_exp=1000

print "quench",  "dt", 1./DeltaN,"N_exp", N_exp
t,x_mean,x_var,kappa=quench_langevin_dynamics(DeltaN,N_exp)

t2=time.time()

t_code=(t2-t1)/60
f=open('quench.dat','w')
f.write(" Deltat=1./%d,N_exp=%d,code time=%f (in min) \n"  %(DeltaN,N_exp, t_code))
f.write('"t" \t "x_mean" \t "x2_mean" \t "kappa" \n')
for i in range(len(t)):
	f.write(" %.12f \t %.12f \t  %.12f \t %.12f  \n"  %(t[i],x_mean[i],x_var[i],kappa[i]))
f.close()
