import numpy as np
import scipy as sp
import math
import random
from scipy.linalg import solve, toeplitz
import matplotlib
import matplotlib.pyplot as plt


val2 = np.loadtxt('val2.dat')
val3 = np.loadtxt('val3.dat')
co2 = np.loadtxt('co2.dat')

pi = math.pi

def MOC(tabela):
    N = tabela.size
    Ft = np.fft.fft(tabela)
    P = [np.absolute(Ft[0])**2]
    for i in range(1,int(N/2)):
        P.append(0.5 * (np.absolute(Ft[i])**2 + np.absolute(Ft[N-i])**2))
    P.append(np.absolute(Ft[int(N/2)])**2)
    return P

def hann(x):
    N = x.size
    return np.sin(pi*x/(N-1))**2

def fourier(x):
    N = x.size
    os = np.asarray(range(N))
    moc = MOC(x*hann(os))
    return [np.asarray(range(int(N/2+1))),moc]

def avtokorelacija(x,i):
    N = x.size
    y = np.concatenate((x,np.zeros(N)))[i:i+N]
    return 1/(N-i)*np.sum(x*y)
def aji(x,p):
    rji = np.asarray([avtokorelacija(x,i) for i in range(p)])
    matrika = toeplitz(rji,rji)
    return solve(matrika,-np.append(rji[1:],avtokorelacija(x,p)))
def spekter(a,w,N):
    arej = np.exp(-1j * 2*pi*w/100 * np.asarray(range(1,a.size+1)))
    return np.abs(1+np.sum(a*arej))**(-2)


if 1:

