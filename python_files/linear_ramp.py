import numpy as np


def protocol(tf,DeltaN):
###protocol for how spring constant is varied

    T1=10; N=(DeltaN*T1); dt=float(T1)/N; 
    a=1.0
    kappa1=a*np.ones(N)
    t1=np.linspace(0,T1,N)
    #tf=5
    T2=T1+tf; N=int(DeltaN*(T2-T1)); dt=float(T2-T1)/N; 
    t2=np.linspace(T1,T2,N)

    kappa2=np.zeros(N)
    for i in range(N):
        kappa2[i]=1.0+ (t2[i]-T1)/tf

    kappa_c=np.append(kappa1,kappa2)
    t_c=np.append(t1,t2)

    t_relax=10
    T3=T2+t_relax; N=int(DeltaN*(T3-T2)); dt=float(T3-T2)/N; 
    t3=np.linspace(T2,T3,N)

    kappa3=kappa2[-1]*np.ones(N)

    kappa_cc=np.append(kappa_c,kappa3)
    t_cc=np.append(t_c,t3)
    return t_cc,kappa_cc
    

def langevin_dynamics(tf, DeltaN,N_exp):
###input protocol and then output t,mean_x, mean_x2protocol
    t,kappa=protocol(tf, DeltaN)
    gamma=1.0
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
    print "x_mean"
    #print x_mean
    print "x_var"
    #print x_var
    return t,x_mean,x_var,kappa

    
