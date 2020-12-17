#created by A. Leleu the 17th of December 2020

import numpy as np
import matplotlib.pyplot as plt

pi=np.pi

def prior_intersection(a1,a2,e1,e2,w1,w2):
    p1=a1*(1-e1**2)
    p2=a2*(1-e2**2)
    Dw=w1-w2
    d1=p1*e2*np.cos(Dw)-p2*e1
    d2=p1*e2*np.sin(Dw)
    crit=(p1-p2)/np.sqrt(d1**2+d2**2)
    print(crit)
    return abs(crit)>1


def dist_to_star(a,e,w,theta):
    p=a*(1-e**2)
    r=p/(1+e*np.cos(theta-w))
    return r
    
    
def plot_intersection(a1,a2,e1,e2,w1,w2):
    theta=np.arange(0,2*pi,.001)
    r1=dist_to_star(a1,e1,w1,theta)
    r2=dist_to_star(a2,e2,w2,theta)
    
    plt.figure()
    plt.plot(r1*np.cos(theta),r1*np.sin(theta))
    plt.plot(r2*np.cos(theta),r2*np.sin(theta))
    plt.title('not intersecting: '+str(prior_intersection(a1,a2,e1,e2,w1,w2)) )

def test():
    plot_intersection(1,2,.6,.4,-pi/5,pi/4)
    plot_intersection(1,2,.8,.4,-pi/5,pi/4)
test()
