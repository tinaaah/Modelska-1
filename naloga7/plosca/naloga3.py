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
    trki, kotiR, kotiT = [],[],[]
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

            p = sin(th) * cos(fi)

            x += p*s
            if x-p*s==0 and x<0: break
            if x < 0:
                R = R + 1
                kotiR.append([fi,th])
                stejem += 1
                break
            if x > d:
                T = T + 1
                kotiT.append([fi,th])
                break

            stejem += 1
        trki.append(stejem)
    trki = np.asarray(trki)
    return np.array([trki,T,R,kotiR,kotiT])        # Sprintaj t in r

def biniraj(x):                 ### Not vstavis array za nardit histogram
    stevilo =  32 ### Predalcki grejo od min do max x
    sredina = np.linspace(min(x), max(x), stevilo+1) ###Nardim bine
    hist, bin_edges = np.histogram(x, bins = sredina)
    for i in range(len(hist)):                          
        center = (sredina[i+1] + sredina[i])/2
        print(hist[i], center, Q, sep='\t')
    print('')

N = 100000
Q = 1
proba = triD(n=N, q=Q, xmin=0, xmax=1)
prepusceni_koti = np.array(proba[4])
odbiti_koti = np.array(proba[3])
#print(prepusceni_koti,prepusceni_koti[:,0])
#print(proba[1]/N,proba[2]/N, proba[3], proba[4])

#for i in range(500):
#    proba1 = triD(n=N, q=i/20, xmin=0, xmax=1)
#    proba2 = enaD(n=N, q=i/20, xmin=0, xmax=1)
#    print(abs(proba1[1]/N - proba2[1]/N), abs(proba1[2]/N - proba2[2]),proba1[1], proba1[2], i/100, sep ='\t') 

vsikoti = np.concatenate((prepusceni_koti[:,0], (odbiti_koti[:,0])))
#test = biniraj(vsikoti)
#test = biniraj(prepusceni_koti[:,0])
#test = biniraj(prepusceni_koti[:,1])
#test = biniraj(odbiti_koti[:,0])
test = biniraj(odbiti_koti[:,1])
