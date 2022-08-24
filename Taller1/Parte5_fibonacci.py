# -*- coding: utf-8 -*-
"""
@author: EdwinXd
"""

"""parte 5"""

import matplotlib.pyplot as plt
import numpy as np

def sucesion_fibonacci(n:int):
    if n == 0:
        res= 0
    elif n == 1:
        res= 1
    else:
        res= sucesion_fibonacci(n - 1) + sucesion_fibonacci(n - 2)
    return res

def fibonacci_20():
    lista=[]
    for n in range(21):
        lista.append(sucesion_fibonacci(n))
    ejex=np.arange(len(lista))
    plt.figure()
    plt.plot(ejex,lista)
    plt.show()
    
fibonacci_20()

def numero_aureo(x):
    return (1+5**(1/2))/2

def aureo():
    lista=np.zeros(19)
    for n in range(2,21):
        lista[n-2]=sucesion_fibonacci(n)/sucesion_fibonacci(n-1)
    x= range(-1,20)
    plt.figure()
    plt.plot(lista)
    plt.plot(x, [numero_aureo(i) for i in x], "r--", linewidth=1.75)
    plt.xlim(-0.75,18.5)
    plt.legend(["Estimación usando la serie","Número aureo"])
    
aureo()
