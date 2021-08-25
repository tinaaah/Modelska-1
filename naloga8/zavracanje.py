import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

N = 10000

acos = math.acos
cos = math.cos
sqrt = math.sqrt
pi = math.pi

#----------------------------------------------- kosinusna funkcija
def h(y): #------------------------------------- ven dobim kosinus
    temp = 3/4*(cos(y) - cos(y)**3/3) + 1/2
    return temp
def g(y): #------------------------------------- ven dobim kot
    temp = 3/4*(y - y**3/3) + 1/2
    return temp


def reject(pdf,n,xmin,xmax):
    x = np.linspace(xmin,xmax,n)
    y = np.zeros(n)
    y[:] = [pdf(x[i]) for i in range(n)]
    pmin = y.min()
    pmax = y.max()
    
    # Counters  
    naccept=0  
    ntrial=0  
    
    # Keeps generating numbers until we achieve the desired n  
    ran=[] # output list of random numbers  
    while naccept<n:  
        x = np.random.uniform(xmin,xmax) # x'  
        y = np.random.uniform(pmin,pmax) # y'  
        if y>pdf(x):  
            ran.append(x)  
            naccept=naccept+1  
        ntrial=ntrial+1  
    
    ran=np.asarray(ran)  
    
    return ran      # lahko dodas se uspehe ntrial 
#proba = reject(g,n=1000,xmin=-1,xmax=1)
proba = reject(h,n=1000,xmin=0,xmax=2*pi)

hist, hist_edges = np.histogram(proba, bins='auto', density='True')
#print(np.sum(hist * np.diff(hist_edges)))

for i in range(len(hist)):                          
    center = (hist_edges[i+1] + hist_edges[i])/2
    print(hist[i], center, sep='\t')
print('')

#-----------------------------------------------    chi^2
#print(chisquare(Gauss1,hist1))
#print(chisquare(Gauss2,hist2))

#-----------------------------------------------    kolmogorov-smirnov
#print(kstest(hist1, 'norm'))
#print(kstest(hist2, 'norm'))

