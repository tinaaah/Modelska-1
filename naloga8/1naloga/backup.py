import numpy as np
import math
import random
from decimal import Decimal, getcontext
getcontext().prec = 300


random.seed()

xi, k = 1,1
def print_stanja(tabela , temperatura):
    for i in range(len(tabela)):
        print(i, tabela[i], temperatura, sep ='\t')
    print('')
def pos_or_neg():
    return 1 if random.random() < 0.5 else -1

#   Nardim zacetno stanje verige, dolgo "dolzina" clenov kjer je vsak clenek lahko celo 
#   stevilo od 0 do 18 (skupaj niv + 1 = 19 nivojev). Prvi in zadnji clen sta fiksirana.

niv = 18
dolzina = 17

#veriga = np.array([np.random.randint(-niv,1) for _ in range(dolzina)]) #cel nivoji
#veriga = np.array([np.random.uniform(-niv,0) for _ in range(dolzina)]) #nivo ni nujno cel
#veriga[0], veriga[-1] = 0,0
veriga = np.zeros(dolzina)

#pot = np.array( [xi*a for a in veriga] )
#Epot = np.sum(pot)
Epot = 0

#pr = np.array( [k/2 * (veriga[i+1] - veriga[i])**2 for i in range(1,dolzina-1)] )
#Epr = np.sum(pr)
Epr = 0

E = Epr + Epot


#   V N-tih poskusih probam optimimzirat stanje. Zberem nakljucni clen v verigi in mu
#   pristejem/odstejem nivo

N = 100000
T = 0       # Nastimam temperaturo stanja, ki je v bistvu razmerje T/deltaE

print('"$T = ', T, '$"')
print(0, Epr, Epot, E, sep='\t')

count = 0
for poskus in range(N):
    i = np.random.randint(1,dolzina-1)

    #P = pos_or_neg() # Diskretni nivoji premik za 1
    #nov = veriga[i] + P

    nov = np.random.uniform(-niv,0)     # "Zvezni" nivoji
    #nov = np.random.randint(-niv,0)     # "Diskretni" nivoji na katerikoli drugi nivo
    P = nov - veriga[i]
    
    dEpot = xi*P
    dEpr = k * P * (2*veriga[i] + P - veriga[i+1] - veriga[i-1])

    deltaE = dEpot + dEpr

    u = random.uniform(0,1)     # Nakljucno stevilo, da preverim al sprejmem al ne
    if deltaE <= -T*abs(deltaE)*math.log(u) and nov >= -niv and nov <= 0:
        count += 1
        veriga[i] = nov
        Epr += dEpr
        Epot += dEpot
        E += deltaE

        #print_stanja(veriga,T)    # Printam vrednosti za narisat gif

print(count, Epr, Epot, E, sep='\t')
print('')
print('')
#print('"$T =', T,'$"')
#print_stanja(veriga, T)                #Sprintam koncno stanje molekule
#print("")
