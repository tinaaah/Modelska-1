import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

#Podatki imajo 7 stolpcev
zasumljen = np.loadtxt("../kalman_cartesian_data.dat", delimiter=" ")

t = zasumljen[:,0]
pozicija = np.c_[zasumljen[:,1], zasumljen[:,2]]
hitrost = np.c_[zasumljen[:,3], zasumljen[:,4]]
pospesek = np.c_[zasumljen[:,5], zasumljen[:,6]]

# Zacetni pogoji
vx, vy = hitrost[0,0], hitrost[0,1]         # Hitrost
sx, sy = pozicija[0,0], pozicija[0,1]       # Pozicija
global dt                                   #Casovni korak
dt = 1.783

# Napake 
global sigma_a
sigma_a = 0.05
global sigma_xy
sigma_xy = 25
global sigma_v 
sigma_v = 0.01

# Merske napake 
Q = np.diag([0, 0, sigma_a**2*dt**2, sigma_a**2*dt**2])
F = np.array([[1, 0, dt, 0], 
              [0, 1, 0, dt],
              [0, 0, 1, 0],
              [0, 0, 0, 1],])

B = np.array([[0.5*t**2, 0],
              [0, 0.5*t**2],
              [t, 0],
              [0, t]])
R = np.array([[sigma_xy**2, 0, 0, 0], 
              [0, sigma_xy**2, 0, 0], 
              [0, 0, sigma_v**2, 0], 
              [0, 0, 0, sigma_v**2]]) #spodaj popravljena

# Nardim vec razlicnih okenskih funkcij
H1 = np.identity(4)
H2 = np.zeros(shape=(4,4))
H3 = np.array([[0,0,0,0],
               [0,0,0,0],
               [0,0,1,0],
               [0,0,0,1]])

def predict(x, F, B, P, Q, u):
    n = len(F)
    m = len(H)
    x = np.dot(F, x) + np.dot(B, u)
    P = np.dot(np.dot(F, P), F.T) + Q
    return x, P

def update(z, F, H, Q, R, B, P, x):
    n = len(F)
    m = len(H)
    y = z - np.dot(H, x)
    S = R + np.dot(H, np.dot(P, H.T))
    K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
    x = x + np.dot(K, y)
    I = np.eye(n)
    P = np.dot(np.dot(I - np.dot(K, H), P), 
    	(I - np.dot(K, H)).T) + np.dot(np.dot(K, R), K.T)
    return x, P, K, S, y

# Zacetna kovarianca matrika
P =  np.ones(shape=(4, 4))

# Zacetni vektor stanja 
x, trajektorija = np.ones(4), [pozicija[0]]

#print("#Vzamem novo v in s na vsakem koraku: ")
#print("#Vzamem novo v na vsakem koraku in s na vsakem 5.: ")
print("#Vzamem novo v na vsakem 5. koraku in s na vsakem 10.: ")
n = len(t)

for i in range(1,n):
    z = np.concatenate((pozicija[i], hitrost[i]))
    u = pospesek[i]
    v = LA.norm([x[2],x[3]])

    if(v<1/3.6): 
        v = 1/3.6 
    if(i%5==0 and i%10!=0): 
        H = H2 
    elif(i%10==0): 
        H = H1 
    else: 
        H = H3

    R = np.array([[sigma_xy**2, 0, 0, 0], 
                  [0, sigma_xy**2, 0, 0], 
                  [0, 0, sigma_v**2*v**2, 0], 
                  [0, 0, 0, sigma_v**2*v**2]])

    # Nova napoved:
    x, P = predict(x, F, B, P, Q, u)

    # Kalman ojacevalni faktor
    # Izboljsana napoved
    x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
    
    trajektorija.append([x[0], x[1]])

    #print(t[i], x[0], x[1], sep ='\t')
    #print(t[i], P[0,0], P[0,2], P[2,2], sep='\t')

trajektorija=np.array(trajektorija)
print(np.shape(trajektorija))
print(trajektorija)
############################################# Nardim primerjavo
DATA = np.loadtxt("../kalman_cartesian_kontrola.dat", delimiter=" ")


Tk = DATA[:,0]
Zk = np.c_[DATA[:,1], DATA[:,2]]
Vk = np.c_[DATA[:,3], DATA[:,4]]
n = len(t)
for i in range(1,n):
    dx1 = Zk[i,0] - pozicija[i,0]
    dy1 = Zk[i,1] - pozicija[i,1]
    dx2 = Zk[i,0] - trajektorija[i,0]
    dy2 = Zk[i,1] - trajektorija[i,1]
    #print(t[i],dx1,dx2,dy2,dy2,sep='\t')
    #print(Tk[i],trajektorija[i,0],trajektorija[i,1],sep='\t')
print('')
