import numpy as np
from scipy import integrate
import math

time = np.linspace(0,80,num=5000)
p4 = 1
p3 = 2
p2 = 4
p1 = 8
p5 = 0.9
p6 = 0.7
p7 = 0.6
p8 = 0.5
p9 = 0.4
def deriv(a, t):                    #definicija odvoda
    z, l = a
    p = 1
    zajci = p*z*(1 - l)
    lisice = l/p*(z - 1)
    return np.array([zajci, lisice])

def lineal(a, t):                    #limita za velike populacije
    z, l = a
    p = 1
    zajci = p*z*l
    lisice = z*l/p
    return np.array([zajci, lisice])

def jacobi(a):                      #matrika drugih odvodov: vidimo kaj so ekstremi
    z, l = a
    p = 1
    return np.array([[p*(1 - l), -p*z], [l/p, 1/p*(z - 1)]])

def initial(time, a0):              #integracija za razlicne zacetne pogoje
    a = integrate.odeint(deriv, a0, time)
    return a

a = initial(time, [0.001, 0.001]) #1 zajcec in 1.1 lisica

m = 1
a_f = np.array([m,m])
lambda1, lambda2 = np.linalg.eigvals(jacobi(a_f))
T = 2*math.pi/math.sqrt(abs(lambda1*lambda2))
print(T,a_f[0],sep='\t')


#for i in range(len(a)):
#    print(a[i][0],a[i][1],time[i],sep='\t')
#print('')
