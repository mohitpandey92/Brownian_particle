import numpy as np

def quench_protocol(DeltaN):
    T1=40;#time to relax 
    N=DeltaN*T1; dt=float(T1)/N; 
    a=1.0;b=2.0
    kappa1=a*np.ones(N)
    t1=np.linspace(0,T1,N)
    tf=40 #time to relax
    T2=T1+tf; N=DeltaN*(T2-T1); dt=float(T2-T1)/N; 
    t2=np.linspace(T1+dt,T2,N)

    kappa2=b*np.ones(N)
    
    kappa_c=np.append(kappa1,kappa2)
    t_c=np.append(t1,t2)
    return t_c,kappa_c
    
    
def quench_langevin_dynamics(DeltaN,N_exp):
###input protocol and then output t,mean_x, mean_x2protocol
    t,kappa=quench_protocol(DeltaN)
    gamma=10.0
    omega=kappa/gamma
    D=10.0 # diffusion constant
    #N_exp=1000
    N=len(t)
    x=5*np.ones((N_exp,N))

    #N=number of steps in a single sim, N_exp=no. of times expt is repeated.
    dt=1./DeltaN
    rand_kick=np.random.randn(N_exp, N-1)

    dx_random=np.sqrt(2*D*dt)*rand_kick


    for j in range(N_exp):
        for i in range(N-1):
            x[j][i+1]=x[j][i]*(1-omega[i]*dt) + dx_random[j][i]
            
    #print x
    x_mean=np.mean(x,axis=0)
    x_var=np.mean(x**2,axis=0)#second raw moment, not variance
    
    return t,x_mean,x_var,kappa
   
   
   
