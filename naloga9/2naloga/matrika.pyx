import numpy as np
import scipy as sp
from scipy.optimize import curve_fit
import math
import random

pi = math.pi
random.seed()

cpdef gauss(x,mu,sigma):
    return 1/(2*pi*sigma**2)**0.5 * np.exp(-(x-mu)**2/(2*sigma**2))
def naredi_matriko(br,bs,delta,N): 
    def funkcija(x, y):
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

def racunaj(betar, betas, N0, dt):
    cdef zacetni = np.zeros(N0)
    zacetni[-1] = 1
    zacetni = np.matrix(zacetni).T
    cdef matrika = naredi_matriko(betar,betas,dt,N0)

    cdef count = 0
    while zacetni[0] < 0.99:
        zacetni = matrika*zacetni
        count += 1
    return np.array([count, zacetni])
