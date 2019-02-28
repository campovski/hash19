# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:53:21 2019

@author: Jan Jezersek
"""

from filereader import filereader
import numpy as np

hashes,imgs = filereader("../testcases/a_example.txt")
Vs = imgs['V']
Hs = imgs['H']

def combine_Vs(v1,v2):
    w = list(set(v1 + v2))
    return w
    

def generate_Ws(Vs):
    Ws = []
    
    if len(Vs) % 2 == 1:
        del Vs[-1]
        
    for i in range(len(Vs)//2):
        Ws.append(combine_Vs(Vs[i],Vs[-(i+1)]))
    
    return Ws

#Ws = generate_Ws(Vs)