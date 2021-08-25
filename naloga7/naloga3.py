import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

acos = math.acos
log = math.log
cos = math.cos
sin = math.sin
sqrt = math.sqrt
pi = math.pi

d = 1
def enaD(n, q, xmin, xmax):
    R, T = 0, 0
    mu = d*q
    trki = []
    while R + T < n:                  # hocemo n stevilo pravih zadetkov
        x, stejem = 0, 0
        while x < d:
            t = np.random.uniform(xmin,xmax)
            s = - mu * log(1 - t)
            if stejem == 0:
                p = 1
            else: 
                p = (random.randint(0,100)%2) * 2 - 1
            x += p*s

            if x <= 0:
                R = R + 1
                break
            if x >= d:
                T = T + 1
                break
            stejem += 1                 
        trki.append(stejem)             #Tabela trkov
    trki = np.asarray(trki)
    return np.array([trki,T,R])        # Sprintaj t in r

def triD(n, q, xmin, xmax):
    R, T = 0, 0
    mu = d*q
    trki = []
    while R + T < n:                  # hocemo n stevilo pravih zadetkov
        stejem = 0                      #stejem stevilo trkov posameznega nevtrona
        x = 0
        while x < d:
            u = np.random.uniform(xmin,xmax)
            v = np.random.uniform(xmin,xmax)
            t = np.random.uniform(xmin,xmax)

            th = acos(2 * u - 1)
            fi = 2*pi*v
            s = - mu * log(1 - t)

            if stejem == 0:
                p = 1
            else: 
                p = sin(th) * cos(fi)
            x += p*s

            if x <= 0:
                R = R + 1
                break
            if x >= d:
                T = T + 1
                break
            stejem += 1
        trki.append(stejem)             #Tabela trkov
    trki = np.asarray(trki)
    return np.array([trki,T,R])        # Sprintaj t in r


N = 10000
Q = 1
proba = enaD(n=N, q=Q, xmin=0, xmax=1)
print(proba[1]/N,proba[2]/N)

tocke = [1, 2, 5, 7, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]

#for i in range(500):
#    proba1 = triD(n=N, q=i/20, xmin=0, xmax=1)
#    proba2 = enaD(n=N, q=i/20, xmin=0, xmax=1)
#    print(abs(proba1[1]/N - proba2[1]/N), abs(proba1[2]/N - proba2[2]),proba1[1], proba1[2], i/100, sep ='\t') 

stevilo = (max(proba[0]) - min(proba[0]) )
hist, bin_edges = np.histogram(proba[0], bins = stevilo)
#print(bin_edges)

sredina = []
for i in range(len(hist)):                          # Sprintam binniran BM 
    center = (bin_edges[i+1] + bin_edges[i])/2 
    sredina.append(center) 
    print(hist[i], center, Q, sep='\t') 
print('')
