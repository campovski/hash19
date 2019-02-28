# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:53:21 2019

@author: Jan Jezersek
"""

from filereader import filereader
import numpy as np

if __name__ == "__main__":
    hashes,imgs = filereader("../testcases/a_example.txt")
    Vs = imgs['V']
    Hs = imgs['H']

def toNs(A):
    Ns = [0 for j in range(len(A))]
    for i in range(len(A)):
        Ns[i] = [len(A[i][:-1])] + [str(A[i][-1])]
    return Ns
    

def combine_Vs(v1,v2):
    w = list(set(v1[:-1] + v2[:-1]))
    return w
    
def generate_Ws(Vs):    
    if len(Vs) % 2 == 1:
        del Vs[0]
        
    N = len(Vs)//2
                
    Ws = [0 for i in range(N)]
        
    for i in range(N):
        Ws[i] = combine_Vs(Vs[i],Vs[-(i+1)]) + [str(Vs[i][-1]) + " " + str(Vs[-(i+1)][-1])]
    
    return sorted(Ws,key=len)
