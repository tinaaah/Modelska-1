import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import math
import random
from matrika import racunaj

pi = math.pi

random.seed()

def print_stanja(tabela, dt):
    print('"$ \\\Delta t = ', dt, '$"', sep ='')
    for i in range(len(tabela)):
        print(cas[i], tabela[i], sep ='\t')
    print('')

def gauss(x,mu,sigma):
    return 1/(2*pi*sigma**2)**0.5 * np.exp(-(x-mu)**2/(2*sigma**2))

def naredi_matriko(br,bs,delta,N): 
    def funkcija(x,y):
        if x == y: 
            return 1-(br+bs)*delta*y 
        elif x == y+1: 
            return br*y*delta 
        elif y == x+1: 
            return bs*y*delta 
        else: 
            return 0

    matrika = np.matrix(np.fromfunction(np.vectorize(funkcija), (N,N)))
    return matrika

def prehodna(N,betar,betas,delta,povprecje=False,spremljaj=False):
    cas = 0
    counter = 0

    zacetni = np.zeros(N)
    zacetni[-1] = 1
    zacetni = np.matrix(zacetni).T
    matrika = naredi_matriko(betar,betas,delta,N)

    while zacetni[0]<0.99:
        zacetni = matrika*zacetni
        cas += delta
        counter+=1
        """if counter == 1:
            print('"$t = %.3f $"' % cas)
            for i in range(len(zacetni)):
                print(i, zacetni[i,0], sep = '\t')
            print('\n')

        if counter%500==0:
            print('"$t = %.2f$"' % cas)
            for i in range(len(zacetni)):
                print(i, zacetni[i,0], sep = '\t')
            print('\n') """
    return zacetni, cas        

beta = 1
betar = 0 #4*beta
betas = 1 #5*beta
N0 = 250
dt = 0.001
#deltat = [ 1/10**n for n in range(5)]
#deltat = [0.001, 0.005, 0.01, 0.015, 0.1, 0.5]
deltat = np.linspace(0.001, 1, 25)
#deltat = [0.01, 0.05, 0.1, 0.5]
casi = np.zeros((len(deltat)))
for i in range(len(deltat)):
    dt = deltat[i]
    for j in range(500):
        tabela, t0 = prehodna(N0, betar, betas, dt, False, False)
        casi[i] += t0
    print(dt,casi[i]/500)
#print(tabela)

"""
timer, count = 0,0
spremljaj, povprecje, cas = [], [], []
while zacetni[0]<0.99:
    if count%250==0: spremljaj.append(zacetni)
    if count%1000==0: 
        cas.append(timer)
        #povprecje.append(variraj(zacetni))
    zacetni = matrika*zacetni
    count += 1
    timer += dt
print(zacetni)
"""
