import numpy as np
from scipy.optimize import minimize
import math
import random

random.seed()
N = 20-1 #Definiram stevilo nabojev, s tem da je en fiksen
R = 1 #Polmer prevodne krogle
sin = math.sin
cos = math.cos
pi = math.pi
sqrt = math.sqrt

def E(x):
    W = 0
    N = int(len(x)/2)
    for i in range(-1,N):
        for j in range(i+1,N):
            if i == -1:
                difx = abs(cos(x[2*j])*sin(x[2*j+1]))**2
                dify = abs(sin(x[2*j])*sin(x[2*j+1]))**2
                difz = abs(1 - cos(x[2*j+1]))**2
            else:
                difx = abs(cos(x[2*i])*sin(x[2*i+1]) - cos(x[2*j])*sin(x[2*j+1]))**2 
                dify = abs(sin(x[2*i])*sin(x[2*i+1]) - sin(x[2*j])*sin(x[2*j+1]))**2 
                difz = abs(cos(x[2*i+1]) - cos(x[2*j+1]))**2
            norma = sqrt(difx**2+dify**2+difz**2)
            W += 1/norma
    return(W)

theta = [random.uniform(0,pi) for _ in range(N)] ## Naredim random zacetno
phi = [random.uniform(0,2*pi) for _ in range(N)] ## pozicijo elektronov
#randkoti = [0,0]
randkoti = []
for i in range(N):
    randkoti.append(phi[i])
    randkoti.append(theta[i])

result = minimize(fun=E, x0=randkoti, method='Powell')
angle = result.x
#print(angle)

r = []
print(0,0,1,sep='\t')
for i in range(N):
    x = cos(angle[2*i]) * sin(angle[2*i+1]) 
    y = sin(angle[2*i]) * sin(angle[2*i+1]) 
    z = cos(angle[2*i+1])
    r.append([x,y,z])
    print(x,y,z,sep='\t')
b = [0,R]
B = tuple(map(tuple,np.vstack([b]*3)))
