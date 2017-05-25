import numpy as np
import time
t1=time.time()



T=100; N=500*T; dt=float(T)/N; 
kappa=1.0
gamma=10
omega=kappa/gamma
D=10.0 # diffusion constant
t=np.linspace(0,T,N)

N_exp=1000
x=5*np.ones((N_exp,N))

#N=number of steps in a single sim, N_exp=no. of times expt is repeated.

rand_kick=np.random.randn(N_exp, N-1)

dx_random=np.sqrt(2*D*dt)*rand_kick


for j in range(N_exp):
    for i in range(N-1):
        x[j][i+1]=x[j][i]*(1-omega*dt) + dx_random[j][i]
        
x_mean=np.mean(x,axis=0)
x_var=np.mean(x**2,axis=0) #note that it's not variance, but second raw moment

t2=time.time()
t_code=(t2-t1)/60
f=open('k_c.dat','w')
f.write(" t_f =%f, Deltat=1./%d,N_exp=%d,code time=%f (in min) \n"  %(T,1000.0,N_exp, t_code))
f.write('"t" \t "x_mean" \t "x2_mean" \t "kappa" \n')
for i in range(len(t)):
	f.write(" %.12f \t %.12f \t  %.12f  \n"  %(t[i],x_mean[i],x_var[i]))
f.close()

