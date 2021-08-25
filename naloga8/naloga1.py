import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

n = 20
N = 10000

sin = math.sin
cos = math.cos
exp = np.exp
log = math.log
sqrt = math.sqrt
pi = math.pi

#pricakovana gaussova porazdelitev
def gauss(x,mu,sigma):
    #return 1/(sqrt(2*pi)*sigma) * exp(-(x-mu)**2/(2.*sigma**2))
    return 1/(sqrt(2*pi)*sigma) * exp(-(float(x-mu))**2/(2.*sigma**2))

#----------------------------------------------- konvolucija
def konvolucija(n,m):
    x = np.zeros(n)
    for i in range(n):
        for j in range(m):
            x[i] += random.random()
        x[i] -= 6
    return np.array(x)

m = 12

tabela = konvolucija(N,m)

#bwth1 = 0.5
#stevilo1 = int(np.ceil(abs(max(tabela)-min(tabela))/bwth1))
#bins1 = np.linspace(min(tabela),max(tabela), stevilo1)

#hist1, bin_edges1 = np.histogram(tabela, bins1, bwth1)
hist1, bin_edges1 = np.histogram(tabela,density='True')

sredina1, Gauss1 = [], []

print('#Konvolucija')
for i in range(len(hist1)):                          # Sprintam binnirano konvolucijo
    center = (bin_edges1[i+1] + bin_edges1[i])/2
    delta = (bin_edges1[i+1] - bin_edges1[i])/2
    sredina1.append(center)
    Gauss1.append(gauss(center,0,1))
    print(hist1[i], gauss(center,0,1), center,sep='\t')
print('')

#----------------------------------------------- Box-Mueller

M=int(N/2)
def BM(mu,sigma):
    x1 = [random.uniform(0,1) for _ in range(M)]
    x2 = [random.uniform(0,1) for _ in range(M)]

    y1 = [sqrt(-2 * log(x1[i])) * cos(2 * pi * x2[i]) for i in range(len(x1))]
    y2 = [sqrt(-2 * log(x1[i])) * sin(2 * pi * x2[i]) for i in range(len(x2))]

    z1 = [mu + y1[i] * sigma for i in range(len(y1))]
    z2 = [mu + y2[i] * sigma for i in range(len(y2))]
    A = z1 + z2
    return np.array(A)


bm = BM(0,1)

#bwth2 = 0.5
#stevilo2 = int(np.ceil(abs(max(bm)-min(bm))/bwth2))
#bins2 = np.linspace(min(bm),max(bm), stevilo2)

#hist2, bin_edges2 = np.histogram(bm, bins2, bwth2)
hist2, bin_edges2 = np.histogram(bm, density = 'True')

sredina2, Gauss2 = [], []
print('#Box-Muller')
for i in range(len(hist2)):                          # Sprintam binniran BM
    center = (bin_edges2[i+1] + bin_edges2[i])/2
    Gauss2.append(gauss(center,0,1))
    sredina2.append(center)
    print(hist2[i], gauss(center,0,1), center, sep='\t')
print('')


#-----------------------------------------------    chi^2
print(chisquare(Gauss1,hist1))
print(chisquare(Gauss2,hist2))

#-----------------------------------------------    kolmogorov-smirnov
print(kstest(hist1, 'norm'))
print(kstest(hist2, 'norm'))

