# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:53:21 2019

@author: Jan Jezersek
"""

from filereader import filereader
import numpy as np
from scipy.optimize import linear_sum_assignment

if __name__ == "__main__":
    hashes,imgs = filereader("../testcases/c_memorable_moments.txt")
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

def combine_Ws_with_indices():
    pass
    
def generate_Ws(Vs):    
    if len(Vs) % 2 == 1:
        del Vs[0]
        
    N = len(Vs)//2
                
    Ws = [0 for i in range(N)]
        
    for i in range(N):
        Ws[i] = combine_Vs(Vs[i],Vs[-(i+1)]) + [str(Vs[i][-1]) + " " + str(Vs[-(i+1)][-1])]
    
    return sorted(Ws,key=len)

if 0:
    Ws = generate_Ws(Vs)
    
    while True:
        Ws = generate_Ws(Ws)
        if len(Ws) ==  1:
            break
        
    res = Ws[0][-1].split(" ")
        
    with open("../out/e_testJJ.txt", 'w') as f:
        f.write("{}\n".format(len(res)//2))
        for i in range(len(res)//2):
            f.write("{} {}\n".format(res[2*i],res[2*i + 1]))
            
def dist(a,b):
    v1 = set(a[:-1]).intersection(b[:-1])
    v2 = len(set(a[:-1]) - v1)
    v3 = len(set(b[:-1]) - v1)
    return min([len(v1),v2,v3])

def dist2(a, b):
    inter = len(set(a).intersection(set(b)))
    return min([inter, len(a)-inter, len(b)-inter])

def correct_hs(Hs):
    for i in range(len(Hs)):
        Hs[i][-1] = str(Hs[i][-1])
    
if 0:
    N_opt = 10
    
    Ws = generate_Ws(Vs)
    imgs = Ws + Hs
    
        
    for ind in range(0,len(imgs),N_opt):
        vals = [[0 for i in range(N_opt)] for j in range(N_opt)]
        for i in range(N_opt):
            for j in range(N_opt):
                if i == j:
                    vals[i][j] = 0
                d = dist(imgs[ind+i],imgs[ind+j])
                vals[i][j] = d
                
        row_ind, col_ind = linear_sum_assignment(np.array(vals))
        
        
                
    
    
    
    
    
        
    
        
    
    
        
        
    
    
    
    