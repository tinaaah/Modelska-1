import os, math
import numpy as np
import scipy as sp
from numpy.linalg import solve
from scipy.linalg import toeplitz

val2 = np.loadtxt('val2.dat')
val3 = np.loadtxt('val3.dat')
co2 = np.loadtxt('co2.dat')


class okna():
    def brez(x):
        return 1

    def bartlett(x):
        N = x.size
        return 1 - abs((x-0.5*(N-1))/(0.5*(N-1)))

    def hann(x):
        N = x.size
        return np.sin(math.pi*x/(N-1))**2

    def welch(x):
        N = x.size
        return 1 - ((x-0.5*(N-1))/(0.5*(N-1)))**2

    def eksponent(x):
        N = x.size
        tau = 0.5*N/2*8.69/60
        return np.exp(-abs(x-0.5*(N-1))/tau)


class fourier_transform():
    def __init__(self, data):
        self.data = data
        self.N = self.data.size

    def MOC(self, okno=okna.brez):
        x = np.linspace(0, self.N, self.N)
        data = self.data * okno(x)

        Ft = np.fft.fft(data)
        Ft = abs(Ft)**2
        Ft = np.array_split(Ft, 2)
        P = 0.5 * (Ft[0] + Ft[1][::-1])
        return P


class MaksimalnaEntropija():
    def __init__(self,data):
        self.data = data
        self.N = self.data.size
        self.shrani_a = {}
        self.shrani_s = {}

    def korelacija(self,i):
        s = []
        if i in self.shrani_s:
            s = self.shrani_s[i] 
        else:
            s = self.data[:self.N-i]*self.data[i:]
            self.shrani_s[i] = s
        return sum(s)/(self.N-i)
    
    def koeficienti_a(self,p):        #aje rabim za min. napake
        R = np.asarray([self.korelacija(i) for i in range(p+1)])
        matrika = toeplitz(R[:-1],R[:-1])
        a = []
        if p in self.shrani_a:
            a = self.shrani_a[p]
        else:
            a = solve(matrika, -R[1:])
            self.shrani_a[p] = a
        return a
    
    def G_square(self, p):
        a = self.koeficienti_a(p)
        a = np.insert(a, 0, 1)
        error = [a[i]*self.korelacija(i) for i in range(p+1)]
        return np.sum(error)
    
    def eval_P(self, p, M):
        a = self.koeficienti_a(p)
        a = np.insert(a, 0, 1)
        a_ft = np.fft.fft(a, M)

        G = self.G_square(p)
        psd = 1/abs(a_ft)**2
        psd = np.real(psd)
        return psd

    def lin_pred(self, p):
        n = self.N//2
        a = self.koeficienti_a(p)
        signal = self.data[:n]

        for i in range(n):
            y = -np.sum(signal[:-p-1:-1] * a)
            signal = np.hstack([signal, y])
        return signal
    
    def preslikaj(self, zeros, dies_out=True):
        new_zeros= []
        for zero in zeros:
            if dies_out and np.abs(zero) < 1:
                new = zero/np.abs(zero)
            elif np.abs(zero) > 1:
                new = zero/np.abs(zero)
            else:
                new = zero
            new_zeros.append(new)
        return np.array(new_zeros)
    
def add_noise(data, mu, sigma):
    if sigma == 0:
        gauss = 0
    else:
        gauss = np.random.normal(mu, sigma, len(data))
    return data + gauss


if __name__ == "__main__":
    #data1 = MaksimalnaEntropija(val2)
    #print(data1.napaka(3))
    p = 10

    x = np.linspace(0,2*math.pi,512)
    y = np.sin(2*math.pi*x) + np.sin(4*math.pi*x) + np.sin(16*math.pi*x)
    
    sinusoid = MaksimalnaEntropija(y)
    a = sinusoid.koeficienti_a(p)
    G = sinusoid.G_square(p)

    entropy_val2 = MaksimalnaEntropija(val2)
    a = entropy_val2.koeficienti_a(p)
    G = entropy_val2.G_square(p)

    N = 20

    iks = np.linspace(0,256,N)
    P = [entropy_val2.eval_P(p, x) for x in iks]

#    with open("test.txt", "w") as outtxt:
#        for i in range(len(val2)):
#            # print(iks[i], P[i], sep='\t', file=outtxt)
#            print(val2[i], file=outtxt)