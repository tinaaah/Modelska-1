import numpy as np
import scipy as sp
import math
import random


random.seed()

def print_stanja(tabela, dt):
    print('"$ \\\Delta t = ', dt, '$"', sep ='')
    for i in range(len(tabela)):
        print(cas[i], tabela[i], sep ='\t')
    print('')

beta = 1.0
N0 = 250

def poisson(N,dt):
    lam = beta*N*dt
    if lam<=0:
        P = N
    else: 
        P = sp.random.poisson(lam)
    return P
def umiranje(N,dt):
    betas = 5*beta
    betar = 4*beta
    lams = betas*N*dt
    lamr = betar*N*dt
    if lams<=0 or lamr<=0:
        P = N
    else: 
        Ps = sp.random.poisson(lams)
        Pr = sp.random.poisson(lamr)
        P = Ps - Pr
    return P

konec, dt = 10, 0.01
cas = np.linspace(0, konec, int(konec/dt)+1)

N, izumrtje = [], []
for j in range(100):
    temp = []
    for i in cas:
        if i == 0:
            temp.append(N0)
        else: 
            nov = umiranje(temp[-1],dt)
            #if temp[-1] - nov == 0:
                #izumrtje.append(i)
                #break
            temp.append(temp[-1] - nov)
    print_stanja(temp, dt)
    N.append(temp)
    #print('')
povprecje = np.average(N, axis=0)
print_stanja(povprecje,dt)
#print('')

#delanje histograma

#bwth = 0.5
#stevilo = int(np.ceil(abs(max(izumrtje)-min(izumrtje))/bwth))
#bins = np.linspace(min(izumrtje),max(izumrtje), stevilo)

#hist, bin_edges = np.histogram(izumrtje, density = 'False')
#hist, bin_edges = np.histogram(izumrtje, bins, bwth)

#sredina = []
#print('"$ \\\Delta t = ',dt,'$"',sep='')
#for i in range(len(hist)):
#    center = (bin_edges[i+1] + bin_edges[i])/2
#    sredina.append(center)
#    print(hist[i], center, sep='\t')
#print('')
#print('')
