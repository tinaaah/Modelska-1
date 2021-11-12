import numpy as np
import math
import random
from decimal import Decimal, getcontext
getcontext().prec = 300

random.seed()

def inic():
    return np.random.choice( spin, size=(nx,ny))

def print_stanja(tabela):
    Nx = len(tabela)
    Ny = len(tabela[0])
    for i in range(Nx):
        for j in range(Ny):
            print(tabela[i][j],end='\t')
        print('')

def pos_or_neg():
    return 1 if random.random() < 0.5 else -1

def energija(tab, J, H):
    Nx = len(tab)
    Ny = len(tab[0])
    enH = -H*np.sum(tab)

    sosedi = np.zeros_like(tab)
    sosedi += np.roll(tab,1,0) + np.roll(tab,-1,0) + np.roll(tab,1,1) + np.roll(tab,-1,1)
    enJ = -J*np.sum(tab*sosedi)

    return enJ+enH
        
def spremeni(mreza, temperatura, nx, ny, N): 
    count = 0 
    konec = [] 
    E = energija(mreza, J, H)
    for t in range(int(N)):
        izberem = random.choice
        i = random.choice(range(nx))
        j = random.choice(range(ny))
        Si = mreza[i,j]
        sum_Sj = mreza[i,(j+1)%ny] + mreza[(i+1)%nx,j] + mreza[i,(j-1)%ny] + mreza[(i-1)%nx,j]
        deltaE = 2 * Si * (J * sum_Sj + H)

        u = np.random.random()
        if deltaE <= -temperatura* math.log(u):
            mreza[i,j] *= -1
            count += 1
            E += deltaE
    S = np.sum(mreza)
    return mreza,E,S

dimenzija = [10,10]
nx = dimenzija[0]
ny = dimenzija[1]
vozli = nx*ny
spin = [-1,1]
J = 1
H = 0.5

n=10e4
T = 5

#mreza = mreza_zacetek = np.random.choice( spin, size=(nx,ny))
#print_stanja(mreza)
#print('')

#nov = spremeni(mreza,T,nx,ny,n)
#print_stanja(nov[0])
"""
for i in range(50,-1,-1):
    t = i/10
    nov = spremeni(mreza, t, nx, ny, n)
    print_stanja(nov[0])
    print('')
"""

repeat = 100

for i in range(1,200):
    E, S, E2, S2 = 0,0,0,0
    temperatura = i/20
    for j in range(repeat):
        zacetek = np.ones([nx,ny])
        nov,e,s = spremeni(zacetek, temperatura, nx,ny,n)
        E += e/(nx*ny)
        S += s/(nx*ny)
        E2 += e**2/(nx*ny)**2
        S2 += s**2/(nx*ny)**2
    E,E2 = E/repeat, E2/repeat
    S,S2 = S/repeat, S2/repeat
    khi = (S2 - S**2)/(n*temperatura)
    c = (E2 - E**2)/(n*temperatura**2)
    print(E, c, S, khi, temperatura, sep = '\t')
