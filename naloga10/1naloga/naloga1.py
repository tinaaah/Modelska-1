import numpy as np
import scipy as sp
import math
import random

val2 = np.loadtxt('val2.dat')
val3 = np.loadtxt('val3.dat')

pi = math.pi

def MOC(tabela):
    N = tabela.size
    Ft = np.fft.fft(tabela)
    P = [np.absolute(Ft[0])**2]
    for i in range(1,int(N/2)):
        P.append(0.5 * (np.absolute(Ft[i])**2 + np.absolute(Ft[N-i])**2))
    P.append(np.absolute(Ft[int(N/2)])**2)
    return P

#### Imam stiri okna na voljo:
def bartlett(x):
    N = x.size
    return 1 - np.absolute((x-0.5*(N-1))/(0.5*(N-1)))
def hann(x):
    N = x.size
    return np.sin(pi*x/(N-1))**2
def welch(x):
    N = x.size
    return 1 - ((x-0.5*(N-1))/(0.5*(N-1)))**2
def eksponent(x):
    N = x.size
    tau = 0.5*N/2*8.69/60
    return np.exp(-np.absolute(x-0.5*(N-1))/tau)

n = 512
os = np.asarray(range(n))
okno = welch(os)

moc2 = MOC(val2[0:n]*okno)
moc3 = MOC(val3[0:n]*okno)
for i in range(len(moc2)):
    print(moc2[i], moc3[i], i/n, sep='\t')
