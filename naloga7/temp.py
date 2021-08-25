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

def enaD(n, d, xmin, xmax):
    R, T = 0, 0
    mu = d/2
    trki = []
    while R + T < n:                  # hocemo n stevilo pravih zadetkov
        x, stejem = 0, 0
        while x < d:
            t = np.random.uniform(xmin,xmax)
            s = - mu * log(1 - t)
            if stejem == 0:
                p = 1
            else: 
                p = (random.randint(0,100000)%2) * 2 - 1
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

def triD(n, d, xmin, xmax):
    R, T = 0, 0
    mu = d/2
    trki = []
    while R + T < n:                  # hocemo n stevilo pravih zadetkov
        stejem = 0
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

proba = triD(n=100000, d=1, xmin=0, xmax=1)
