# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:38:06 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

def lissajous(nsides):
    desf=[0,np.pi/4,np.pi/2]
    for ind in range(3):
        A=1
        d=desf[ind]
        thetha=np.linspace(0,2*np.pi,10000)
        nx=nsides
        ny=nsides
        k=1
        a=0
        for i in range(nx):
            i+=1
            for j in range(a,ny):
                j+=1
                x=A*np.sin(i*thetha)
                y=A*np.sin(j*thetha+d)
                plt.subplot(nx,ny,k) 
                plt.axis("off")
                plt.plot(x,y)
                k+=1
            a+=1
            k+=a
        plt.show()

lissajous(5)
#las figuras salen por separado dependiendo de su desfase

