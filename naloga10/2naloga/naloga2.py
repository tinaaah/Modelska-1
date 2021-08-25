import numpy as np
import math
import random
from decimal import Decimal, getcontext
getcontext().prec = 300


random.seed()

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
    enJ = 0
    for i in range(Nx):
        for j in range(Ny):
            sum_Sj = tab[i,(j+1)%Ny] + tab[(i+1)%Nx,j] + tab[i,(j-1)%Ny] + tab[(i-1)%Nx,j]
            enJ += - sum_Sj * J * tab[i,j]
    return enJ+enH
        
def spremeni(mreza, T, nx, ny, N): 
    count = 0 
    konec = [] 
    E = energija(mreza, J=1, H=0)
    for t in range(int(N)):
        izberem = random.choice
        i = random.choice(range(nx))
        j = random.choice(range(ny))
        Si = mreza[i,j]
        sum_Sj = mreza[i,(j+1)%ny] + mreza[(i+1)%nx,j] + mreza[i,(j-1)%ny] + mreza[(i-1)%nx,j]
        deltaE = 2 * Si * (J * sum_Sj + H)

        u = np.random.random()
        if deltaE <= -T* math.log(u):
            mreza[i,j] *= -1
            count += 1
            E += deltaE
    return mreza,E

dimenzija = [10,10]
nx = dimenzija[0]
ny = dimenzija[1]
vozli = nx*ny
spin = [-1,1]
J = 1
H = 0

n=10e4
T = 0

mreza = mreza_zacetek = np.random.choice( spin, size=(nx,ny))
#print( energija(mreza, J=1, H=0))

#print_stanja(mreza)
#print('')

nov = spremeni(mreza,T,nx,ny,n)
#print_stanja(nov[0])

#for i in range(30):
#    t = i/10
#    nov = spremeni(mreza, t, nx, ny, n)
#    print_stanja(nov[0])
#    print('')

E = np.zeros(100)
E2 = np.zeros(100)
for j in range(50):
    for i in range(100):
        t = i/10
        nov = spremeni(mreza, t, nx, ny, n)
        E[i] += nov[1]
        E2[i] += nov[1]**2
E = E/50
E2 = E2/50
for i in range(50):
    print(i,E[i])
