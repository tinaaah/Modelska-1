import numpy as np
import math
import random
from decimal import Decimal, getcontext
getcontext().prec = 300


random.seed()
log = np.log

alpha = 1
def print_stanja(tabela , temperatura):
    for i in range(len(tabela)):
        print(i, tabela[i], temperatura, sep ='\t')
    print('')

def pos_or_neg():
    return 1 if random.random() < 0.5 else -1
def Dpot(alfa,x):
    return alfa*x
def Dpr(x,delta):
    return delta*(delta -x[0] + 2*x[1] - x[2])

def sprememba(N,veriga,dolzina,niv,t):
    count, vsi = 0,0
    Epot,Epr,E=[],[],[]
    epot,epr,e=0,0,0
    T=t
    while count < N:
        i = np.random.randint(1,dolzina-1)     #Zberem random mesto premika

        #P = pos_or_neg() # Diskretni nivoji premik za 1
        #nov = veriga[i] + P

        #nov = np.random.uniform(-niv,0)     # "Zvezni" nivoji
        nov = np.random.randint(-niv,0)     # "Diskretni" nivoji na katerikoli drugi nivo
        P = nov - veriga[i]

    
        dEpot = Dpot(alpha,P)
        dEpr = Dpr([veriga[i-1],veriga[i],veriga[i+1]],P)

        deltaE = dEpot + dEpr

        u = random.uniform(0,1)     # Nakljucno stevilo, da preverim al sprejmem al ne
        if deltaE <= T*log(1/u) and nov >= -niv and nov <= 0:
            veriga[i] = nov
            count += 1

            epr += dEpr
            epot += dEpot
            e += deltaE
            Epot.append(epot)
            Epr.append(epr)
            E.append(e)
            #print(epot, epr, e, T, sep='\t')
        vsi += 1
    povprecje = np.mean([Epot[9000:-1], Epr[9000:-1], E[9000:-1]], axis=1)
    #print(count/vsi, end='\t')
    return np.array(povprecje), np.array(veriga)


#   Nardim zacetno stanje verige, dolgo "dolzina" clenov kjer je vsak clenek lahko celo 
#   stevilo od 0 do 18 (skupaj niv + 1 = 19 nivojev). Prvi in zadnji clen sta fiksirana.

niv = 18
dolzina = 17

#veriga = np.array([np.random.randint(-niv,1) for _ in range(dolzina)]) #cel nivoji
#veriga = np.array([np.random.uniform(-niv,0) for _ in range(dolzina)]) #nivo ni nujno cel
#veriga[0], veriga[-1] = 0,0
veriga = np.zeros(dolzina)

#   V N-tih poskusih probam optimimzirat stanje. Zberem nakljucni clen v verigi in mu
#   pristejem/odstejem nivo

N = 10000
T=5

energija, naslednji = sprememba(N,veriga,dolzina,niv,T)
#print(energija)
for i in range(49,-1,-1):
    t = i/10
    pot, pr, en = 0,0,0
    energija, naslednji = sprememba(N,naslednji,dolzina,niv,t)
    #print(naslednji)
    pot = energija[0]
    pr = energija[1]
    en = energija[2]
    print(pot,pr,en, t,sep='\t')
