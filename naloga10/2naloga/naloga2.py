import numpy as np
from numpy.fft import fft, ifft
import scipy as sp
import math
import random

data0 = np.loadtxt('signal0.dat')
data1 = np.loadtxt('signal1.dat')
data2 = np.loadtxt('signal2.dat')
data3 = np.loadtxt('signal3.dat')

pi = math.pi

def r(x):
    if x<=n/2:
        y = np.exp(-np.abs(x)/16)/32
    else:
        y = np.exp(-np.abs(x-n)/16)/32
    return y

def wiener(x,N):
    rez = aux = [1 for i in range(N)] + [0 for i in range(512-2*N)] + [1 for i in range(N)]
    rez = np.asarray(rez)

    x /= np.sum(x)
    jedro = fft(x)
    noise = np.ones(x.size)*np.sum(x[100:412])/312
    signal = np.abs(jedro)**2 - noise
    fi = np.abs(jedro)**2 / ( np.abs(jedro)**2 + noise**2 )
    R = fft(prenosna(os))
    return np.real(ifft( jedro / R * rez )) #* fi))
def wiener2(x,N):
    rez = [1 for i in range(N)] + [0 for i in range(512-2*N)] + [1 for i in range(N)]
    rez = np.asarray(rez)

    x /= np.sum(x)
    jedro = fft(x)
    noise = np.ones(x.size)*np.sum(x[100:412])/312
    signal = np.abs(jedro)**2 - noise
    fi = np.abs(jedro)**2 / ( np.abs(jedro)**2 + noise**2 )
    R = fft(prenosna(os))
    return np.real(ifft( jedro / R * fi*rez))

n = 512
os = np.arange(n)
prenosna = np.vectorize(r)

#c0 = MOC(data0)
#c1 = MOC(data1)
#c2 = MOC(data2)
#c3 = MOC(data3)

m = 25
u0 = wiener(data0,m)
u1 = wiener2(data1,m)
u2 = wiener2(data2,m)
u3 = wiener2(data3,m)

for i in range(len(u0)):
    #print(c0[i], c1[i], c2[i], c3[i], i, sep='\t')
    print(u0[i], u1[i], u2[i], u3[i], i, sep='\t')
