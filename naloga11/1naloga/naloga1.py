import numpy as np
import math
from numpy.linalg import inv
from numpy import linalg as LA
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt

# Kontrolna tabela pravih podatkov
DATA = np.loadtxt("../kalman_cartesian_kontrola.dat", delimiter=" ")

T = DATA[:,0]
Z = np.c_[DATA[:,1], DATA[:,2]]
V = np.c_[DATA[:,3], DATA[:,4]]

#Podatki imajo 7 stolpcev
data = np.loadtxt("../kalman_cartesian_data.dat", delimiter=" ")

t = data[:,0]
pozicija = np.c_[data[:,1], data[:,2]]
hitrost = np.c_[data[:,3], data[:,4]]
pospesek = np.c_[data[:,5], data[:,6]]

# Zacetni pogoji
vx0, vy0 = hitrost[0,0], hitrost[0,1]   # Hitrost
x0, y0 = pozicija[0,0], pozicija[0,1]     # Pozicija
dt = 1.783                  # Casovni korak

# Napake 
sigma_x = 25
sigma_a = 0.05

def sigma_v(v):
    return max(1/3.6, LA.norm(v)**2*0.01)

# Merske napake 
Q = np.diag([0, 0, sigma_a**2*dt**2, sigma_a**2*dt**2])
F = np.array([[1, 0, dt, 0], 
              [0, 1, 0, dt],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

# Nardim vec razlicnih okenskih funkcij
H1 = np.zeros(shape=(4,4))
H2 = np.array([[0,0,0,0],
               [0,0,0,0],
               [0,0,1,0],
               [0,0,0,1]])
H3 = np.identity(4)

def sum_meritev(v):
    sigmav = sigma_v(v)
    return np.diag([sigma_x**2, sigma_x**2, sigmav**2, sigmav**2])
 
def napoved2d(x, v, t, a, c):
    X = np.array([x[0], x[1], v[0], v[1]])
    B = np.array([[0.5*t**2, 0],
                  [0, 0.5*t**2],
                  [t, 0],
                  [0, t]])
    X_prime = np.dot(F,X) + np.dot(B,a)  # +c ----> ce dodam ta c dobim prevec odstopanja!
    return X_prime

def elipsa(P, s):      # Za izracun elipse zaupanja
    lambda_, q = LA.eig(P)
    a = math.sqrt(s*abs(lambda_[0])) if lambda_[0]!=0 else 0
    b = math.sqrt(s*abs(lambda_[1])) if lambda_[1]!=0 else 0
    c = math.sqrt(s*abs(lambda_[2])) if lambda_[2]!=0 else 0
    d = math.sqrt(s*abs(lambda_[3])) if lambda_[3]!=0 else 0
    #alpha = math.atan( LA.norm(q[0])/LA.norm(q[1])) 
    return np.array([a, b, c, d]) #alpha*180/math.pi])
def residual(z,H,x,K):
    return LA.norm(z - np.dot(H,x))

# Zacetni vektor stanja 
trajektorija = np.concatenate((pozicija[0], hitrost[0]))

x = np.concatenate((pozicija[0], hitrost[0]))
#x = np.ones(4)

# Zacetna kovarianca matrika
sigmav0 = sigma_v([vx0,vy0])
P = np.diag([sigma_x**2, sigma_x**2, sigmav0**2, sigmav0**2])

#P = np.ones(shape=(4,4))

#print("#Vzamem novo v in s na vsakem koraku: ")
#print("#Vzamem novo v na vsakem 5. koraku in s na vsakem 10.: ")
#print("#Zaupanje 90% ----> s=7.779")
#print("#Zaupanje 95% ----> s=9.488")
#print("#Zaupanje 99% ----> s=13.277")
n = len(t)

for i in range(1,n):
    c = np.array([0, 0, pospesek[i,0], pospesek[i,1]])

    # Nova napoved:
    x = napoved2d(x[0:2], x[2:4], dt, pospesek[i], c)
    P = np.dot(np.dot(F, P), F.T) + Q

    # Podatkov ne upostevam na vsakem koraku
    H = H1
    z = np.zeros(4)
    if i%5 == 0:            # Hitrost dobimo vsak 5. korak
        if i%10 == 0:       # Pozicijo dobimo vsak 10. korak
            H = H3
            z = np.concatenate((pozicija[i], hitrost[i]))
        else:
            H = H2
            z = np.concatenate(([0,0], hitrost[i]))
    # Vstavim podatke v Y in R
    y = z - np.dot(H,x)
    R = sum_meritev(x[2:4])                      #R je odvisen od hitrosti

    # Kalman ojacevalni faktor
    S = np.dot(H, np.dot(P, H.T)) + R
    K = np.dot( np.dot(P, H.T), LA.inv(S))

    # Printaj residual
    #res = residual( np.concatenate((pozicija[i], hitrost[i])), np.eye(4), x, K)
    res = residual(z, H, x, K)
    #print(t[i], res, sep='\t')

    # Izboljsana napoved
    x = x + np.dot(K, y)
    P = np.dot(np.dot(np.identity(4) - np.dot(K, H), P), 
            (np.identity(4) - np.dot(K, H)).T) + np.dot(np.dot(K, R), K.T)
    #P = np.dot(np.identity(4) - np.dot(K, H), P)

    trajektorija = np.vstack((trajektorija, [x[0], x[1], x[2], x[3]]))

    Pzadnji = np.array([[P[0,0], P[0,2]], [P[2,0], P[2,2]]])
    """
    # Printaj radij elipse

    #radij_elipse = elipsa(Pzadnji, 5.991)
    #radij_elipse = elipsa(P, 7.779)
    #radij_elipse = elipsa(P, 9.488)
    #radij_elipse = elipsa(P, 13.277)

    a, b, c, d = radij_elipse[0:4]
    print(t[i], radij_elipse[0], radij_elipse[1], radij_elipse[2], sep='\t')
    #print(t[i], x[0], Z[i,0], a, x[2], V[i,0], c, sep ='\t')
    #print(t[i], x[1], Z[i,1], b, x[3], V[i,1], d, sep ='\t')
    """
    
    # Printaj trajektorijo
    #print(t[i], x[0], x[1], sep ='\t')
    #print(t[i], P[0,0], P[0,2], P[2,2], sep='\t')
    print(t[i], np.linalg.norm(P), np.linalg.norm(K), sep ='\t')


############################################# Nardim primerjavo
"""
n = len(t)
for i in range(1,n):
    dr1 = Z[i] - pozicija[i]
    dv1 = np.abs(V[i] - hitrost[i])/V[i]
    dr2 = Z[i] - trajektorija[i,0:2]
    dv2 = np.abs((V[i] - trajektorija[i,2:4])/V[i])
    print(t[i],dr1[0],dr1[1],dv1[0],dv1[1],dr2[0],dr2[1],dv2[0],dv2[1],sep='\t')
    #print(t[i],Z[i,0], Z[i,1], sep='\t')
print('')
"""

# ----------------------------------------------------------------------------
# Hocem narisat elipsoido zaupanja
"""
def elipsa(P, X, Y):
    cov = P
    lambda_, v = np.linalg.eig(cov)
    lambda_ = np.sqrt(lambda_)
    ax = plt.subplot(111, aspect='equal') 
    for j in range(1, 4):
        ell = Ellipse(xy=(np.mean(X), np.mean(Y)), 
                width=lambda_[0]*j*2, height=lambda_[1]*j*2, 
                angle=np.rad2deg(np.arccos(v[0, 0]))) 
        ell.set_facecolor('none')
        ax.add_artist(ell)
    plt.scatter(X, Y)
    plt.show()
"""
#Pzadnji, trajektorija[:,0], trajektorija[:,1]
