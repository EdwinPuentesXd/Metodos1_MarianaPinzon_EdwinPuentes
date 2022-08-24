# -*- coding: utf-8 -*-
"""
@author: EdwinXd
"""

import matplotlib.pyplot as plt
import numpy as np

def es_primo(n:int):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def numeros_primos():
    primos = []
    i=2
    while len(primos)<1000:
        if es_primo(i):
            primos.append(i)
        i+=1
    for n in primos[:10]:
        print(n)
    ejex=np.arange(len(primos))
    plt.figure()
    plt.plot(ejex,primos, "r")
    plt.show()

numeros_primos()
