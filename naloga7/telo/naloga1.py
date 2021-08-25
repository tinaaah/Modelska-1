import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

acos = math.acos
cos = math.cos
sin = math.sin
sqrt = math.sqrt
pi = math.pi


def kartezicne(n, xmin, xmax):
    vsi = 0
    pravi = 0
    ran=[]                          # output list of random numbers  
    I,r = [],[]
    while pravi<n:                  # hocemo n stevilo pravih zadetkov
        x = np.random.uniform(xmin,xmax) # x'  
        y = np.random.uniform(xmin,xmax) # y'  
        z = np.random.uniform(xmin,xmax) # y'  
        if  sqrt(abs(x)) + sqrt(abs(y)) + sqrt(abs(z)) <= 1:
            R = np.asarray([x,y,z])
            ran.append(R)
            I.append([y**2+z**2, x**2+z**2, y**2+z**2, -x*y, -x*z, -y*z])
            r.append(sqrt(np.sum(R**2)))
            pravi += 1  
        vsi += 1
    ran = np.asarray(ran)             # To vzami da dobis ven volumen
    I = np.array(I)
    r = np.array(r)
    return np.array([ran,vsi,pravi,I,r])        # Sprintaj vse zadetke in njihovo stevilo

def sfericne(n, p, xmin, xmax):
    vsi = 0
    pravi = 0
    radij = []
    R = 1                           # Gledam tako ocrtano sfero
    ran=[]                          # output list of random numbers  
    I = []                          # output so vtrajnosnti momenti
    Y10, Y11, Y20, Y21, Y22 = 0,0,0,0,0
    epsilon = 10e-2
    while pravi<n:                  # hocemo n stevilo pravih zadetkov
        u = np.random.uniform(xmin,xmax) 
        v = np.random.uniform(xmin,xmax) 
        w = np.random.uniform(xmin,xmax)

        r = u**(1/3)
        #r = 1
        th = acos(2 * v - 1)
        fi = 2*pi*w

        x = r * cos(fi) * sin(th)
        y = r * sin(fi) * sin(th)
        z = r * cos(th)
        enacba =  sqrt(abs(x)) + sqrt(abs(y)) + sqrt(abs(z))

        if  enacba<=1+epsilon and enacba>=1-epsilon:
            ran.append([x,y,z])  
            radij.append(sqrt(x**2 + y**2+z**2))
            I.append([r**p*(y**2 + z**2), r**p*(x**2 + z**2), r**p*(x**2 + y**2), 
                r**p*(-x*y), r**p*(-x*z), r**p*(-y*z)])
            pravi += 1  

            Y10 += sqrt(2/(4*pi))*cos(th)*r**p
            Y11 += -sqrt(3/(8*pi))*cos(th)*cos(fi)*r**p
            Y20 += sqrt(3/(16*pi))*(3*cos(th)**2-1)*r**p
            Y21 += -sqrt(15/(8*pi))*cos(th)*sin(th)*cos(fi)*r**p
            Y22 += sqrt(15/(8*pi))*sin(th)**2*cos(2*fi)*r**p
        vsi += 1
    ran = np.asarray(ran)             # To vzami da dobis ven volumen
    I = np.asarray(I)           # To je za dobit ven vztrajnosnti moment 
    Y = [Y10,Y11,Y20,Y21,Y22]
    #return np.array([ran,vsi,pravi,I,radij])    # Sprintaj vse zadetke in njihovo stevilo
    return np.array([ran,vsi,pravi,Y])    # Sprintaj vse zadetke in njihovo stevilo


N, P = 100000, 4
#proba = kartezicne(n=N, xmin=-1, xmax=1)

proba = sfericne(n=N, p=P, xmin=0, xmax=1)

prostor = proba[0]
#i,r = np.array(proba[3]), np.array(proba[4])
n = proba[2]
N = proba[1]

#V = 8       #za kocko 
#V = pi*4/3      #za kroglo 
##### Izracunam volumen
#volumen = V * n/N           
#varianca = V * n/N * sqrt(1/n - 1/N)
#print(n, N, volumen, varianca)

S = 4*pi
##### Izracunam povrsino
povrsina = S * n/N           
varianca = S * n/N * sqrt(1/n - 1/N)
#print(n, N, volumen, varianca)

##### Izracunam sfericne harmonike
print(n, N)
Y = np.array(proba[3])*S/N
print(Y)


###### Izracunam maso
#M = np.sum(r**P)*volumen
#print(M)
"""
##izracunam tezisce
xt = V/N* np.sum(prostor[:,0]*r**P)
xt2 = V/N* np.sum(prostor[:,0]**2*r**(2*P))
dxt = sqrt(xt2-xt**2)/sqrt(N)

yt = V/N* np.sum(prostor[:,1]*r**P)
yt2 = V/N* np.sum(prostor[:,1]**2*r**(2*P))
dyt = sqrt(yt2-yt**2)/sqrt(N)/M

zt = V/N* np.sum(prostor[:,2]*r**P)
zt2 = V/N* np.sum(prostor[:,2]**2*r**(2*P))
dzt = sqrt(zt2-zt**2)/sqrt(N)

print(xt,dxt, sep='\t')
print(yt,dyt, sep='\t')
print(zt,dzt, sep='\t')
###########################################
"""


"""
tocke = [1,2,5,7,10,25,50,75,100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000,250000,500000] #,750000,1000000]
for i in tocke:
    proba = kartezicne(n=i, xmin=-1, xmax=1)
    n = proba[2]
    N = proba[1]
    volumen = V * n/N
    varianca = V * n/N * sqrt(1/n - 1/N)
    print(volumen, varianca, n, sep='\t')
"""
"""
for korak in range(0, 51, 1):
    P = korak/10
    I = [np.sum( i[:,j]*r[j]**P *V/N) for j in range(6)]
    I2 = [np.sum( np.square(i[:,j])*r[j]**(2*P) *V/N) for j in range(6)]
    dI = np.sqrt(abs(I2-np.square(I)))/sqrt(N)
    for t in range(6):
        print(abs(I[t]), dI[t], P, sep ='\t')
    print('')
"""
#hist, hist_edges = np.histogram(proba, bins='auto', density='True')
#print(np.sum(hist * np.diff(hist_edges)))

#for i in range(len(hist)):                          
#    center = (hist_edges[i+1] + hist_edges[i])/2
#    print(hist[i], center, sep='\t')
#print('')

#-----------------------------------------------    chi^2
#print(chisquare(Gauss1,hist1))
#print(chisquare(Gauss2,hist2))

#-----------------------------------------------    kolmogorov-smirnov
#print(kstest(hist1, 'norm'))
#print(kstest(hist2, 'norm'))
