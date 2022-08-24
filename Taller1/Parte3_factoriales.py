# -*- coding: utf-8 -*-
"""
@author: EdwinXd
"""

""" Parte 3"""
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
def primeros20_factoriales():
    for n in range(20):
        print(factorial(n))
primeros20_factoriales()

def variacion_sin_repeticion(n:int, r:int):
    return factorial(n) / (factorial(n - r))
#print(variacion_sin_repeticion(6, 3))
def combinacion_sin_repeticion(n:int, r:int):
    return factorial(n) / (factorial(r) * factorial(n - r))
#print(combinacion_sin_repeticion(21,11))
