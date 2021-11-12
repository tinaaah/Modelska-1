import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

#Podatki imajo 7 stolpcev
data = np.loadtxt("../kalman_relative_data.dat", delimiter=" ")

t = data[:,0]
pozicija = np.c_[data[:,1], data[:,2]]
pospesek = np.c_[data[:,3], data[:,4]]

# Zacetni pogoji
x0, y0 = pozicija[0,0], pozicija[0,1]   # Pozicija
dt = 1.783                              # Casovni korak

# Napake 
sigma_x = 25
sigma_a = 0.05

# Merske napake zaradi ortogonalne transformacije
def Bn(v):
    vx, vy = v
    vn = LA.norm(v)
    return np.array([[vx, -vy], [vy, vx]])/vn

# Sum meritve
def sigma_v(v):
    return max(1/3.6, LA.norm(v)*0.01)

def sum_meritev(v):
    sigmav = sigma_v(v)
    return np.diag([sigma_x**2, sigma_x**2, sigmav**2, sigmav**2])

# Pogoste matrike
I = np.eye(2)
nicle = np.zeros(shape=(2,2))

# Prehodna matrika
F = np.block([[I, I*dt],
              [nicle, I]])

# Nimam podatkov o hitrostih
H1 = np.block([[I, nicle],
              [nicle, nicle]])
H2 = np.zeros(shape=(4,4))

# Rotacija vektorja
def perp(v):
    x,y = v
    return np.array([-y, x])
 
def napoved(x, v, a):
    X = np.array([x[0], x[1], v[0], v[1]])
    u = np.concatenate(([0,0], a*dt))

    A = Bn(v)
    B = np.block([[I, nicle],
                  [nicle, A]])
    X_prime = np.dot(F, X) + np.dot(B, u) 
    return X_prime

def Q(x, v, P, a):
    norma = LA.norm(v)
    vT = perp(v)
    aT = perp(a)
    pn = P[2:4, 2:4]
     
    Q = dt**2 * (sigma_a**2 * I + np.dot(np.dot(vT, pn), vT)/norma**4 * 
            np.tensordot(np.dot(Bn(v), aT), np.dot(Bn(v), aT), axes=0))
    return Q

# Zacetni vektor stanja 
x = np.ones(4)
trajektorija = x

# Zacetna kovarianca matrika
#P = np.diag([sigma_x**2, sigma_x**2, sigmav0**2, sigmav0**2])
P =  np.ones((4, 4))
#P =  np.eye(4)

n = len(t)

for i in range(1,n):
    s = x[0:2]
    v = x[2:4]

    # Nova napoved:
    x = napoved(s, v, pospesek[i])

    Qn = np.block([[nicle, nicle], 
                  [nicle, Q(s, v, P, pospesek[i])]])
    P = np.dot(np.dot(F, P), F.T) + Qn

    # Ne dobivam podatkov o hitrostih 
    H = H1
    z = np.concatenate((pozicija[i], [0,0]))

    # Vstavim podatke v y
    y = z - np.dot(H, x)
    R = sum_meritev(v)

    # Kalman ojacevalni faktor
    S = np.dot(H, np.dot(P, H.T)) + R
    K = np.dot( np.dot(P, H.T), LA.inv(S))

    # Izboljsana napoved
    x = x + np.dot(K, y)
    P = np.dot(np.dot(np.identity(4) - np.dot(K, H), P), (np.identity(4) - np.dot(K, H)).T) 
    + np.dot(np.dot(K, R), K.T)
    #P = np.dot(np.identity(4) - np.dot(K, H), P)

    trajektorija = np.vstack((trajektorija, [x[0], x[1], x[2], x[3]]))

    #print(t[i], x[0], x[1], sep ='\t')
    #print(t[i], P[0,0], P[0,2], P[2,2], sep='\t')
#print('')
############################################# Nardim primerjavo
DATA = np.loadtxt("../kalman_cartesian_kontrola.dat", delimiter=" ")

T = DATA[:,0]
Z = np.c_[DATA[:,1], DATA[:,2]]
V = np.c_[DATA[:,3], DATA[:,4]]
n = len(t)
for i in range(1,n):
    dr1 = Z[i] - pozicija[i]
    dr2 = Z[i] - trajektorija[i,0:2]
    print(t[i],dr1[0],dr1[1],dr2[0],dr2[1],sep='\t')
    #print(t[i],Z[i,0], Z[i,1], sep='\t')
print('')
