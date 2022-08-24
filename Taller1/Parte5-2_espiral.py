# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 13:18:52 2022

@author: mpinz
"""

import numpy as np
import matplotlib.pyplot as plt

a=0
b=1
t=np.linspace(0,6*np.pi,2000)
r=a+(b*t)
plt.figure(figsize=(7,4))
y=r*np.sin(t)
x=r*np.cos(t)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

    
