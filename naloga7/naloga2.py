import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

N = 10000

acos = math.acos
log = math.log
cos = math.cos
sin = math.sin
sqrt = math.sqrt
pi = math.pi

R = 1
def pobeg(n, q, xmin, xmax):
    vsi, pravi = 0, 0
    mu = q*R
    ran=[]                          # output list of random numbers  
    while pravi<n:                  # hocemo n stevilo pravih zadetkov
        u = np.random.uniform(xmin,xmax) # x'  
        v = np.random.uniform(xmin,xmax) # y'  
        t = np.random.uniform(xmin,xmax) # y'  

        r = (u)**(1/3)
        th = acos(2 * v - 1)
        s = - mu * log(1-t)

        d = - r * cos(th) + sqrt( R**2 - r**2 * sin(th)) 

        if d <= s:
            ran.append([d,s])  
            pravi += 1  
        vsi += 1
    ran = np.asarray(ran)                   # To vzami da dobis ven proste poti
    return np.array([ran,vsi,pravi])        # Sprintaj vse zadetke in njihovo stevilo

Q = 1
N = 10000

proba = pobeg(n=N, q=Q, xmin=0, xmax=1)
m = proba[2]
M = proba[1]
verjetnost = m/M
napaka = sqrt(m*(M-m)/M**2)/sqrt(M)
#print(verjetnost,napaka,Q,sep='\t')

for i in range(0,1000):              # Sprintam za razlicne vrednosti q
    proba = pobeg(n=N, q=i/100, xmin=0, xmax=1)
    m = proba[2]
    M = proba[1]
    verjetnost = m/M
    napaka = sqrt(m*(M-m)/M**2)/sqrt(M)
    print(verjetnost,napaka,i/100,sep='\t')
