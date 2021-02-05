# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:04:48 2020

@author: krenj
"""

# -*- coding: utf-8 -*-

import timeit
from PIL import Image
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from scipy.integrate import ode
import matplotlib
import matplotlib.pyplot as plt
from scipy import linalg as lin
from scipy.optimize import fsolve
from scipy.linalg import solve
from scipy.linalg import solve_banded
from scipy.special import jn_zeros #prvi parameter je order, drugi št. ničel
from scipy.special import jv #prvi order drugi argument
#from scipy.special import beta
import scipy.special as spec
import scipy.sparse
from scipy.optimize import root
from scipy.integrate import quad
from scipy.integrate import complex_ode
from scipy.optimize import linprog
import scipy.optimize as opt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy.linalg import svd
from matplotlib.patches import Ellipse
plt.close("all")
pi = np.pi
#signal = np.loadtxt("val3.dat")

def gama(x,k,theta):
    return x**(k-1)*np.exp(-x/theta) /(theta**k * spec.gamma(k))
#x = np.linspace(0,20,1000)
#plt.plot(x,gama(x,2,2))
    
def prenosna(x,tau=30,N=512):
    return 1/tau * np.exp(-x/tau)
    if x <=N/2:
        return 1/(tau)*np.exp(-np.abs(x)/tau)
    else:
        return 1/(tau)*np.exp(-np.abs(x-N)/tau)
    
def prenosna2(x,tau=16):
    return 1/(1+(tau*x)**2)

def okno(ime,x):
    N = x.size
    def turki(i):
        if i<(N-1)/4:
            return 0.5*(1+np.cos(pi*(4*i/(N-1) - 1)))
        elif i >= (N-1)/4 and i< (N-1)*(0.75):
            return 1
        else:
            return 0.5*(1+np.cos(pi*(4*i/(N-1) -3)))
    if ime == "tri":
        return 1 - np.absolute((x-0.5*(N-1))/(0.5*(N-1)))
    elif ime == "welch":
        return 1 - ((x-0.5*(N-1))/(0.5*(N-1)))**2
    elif ime == "hann":
        return np.sin(pi*x/(N-1))**2
    elif ime == "srs":
        return 1 - 1.93*np.cos((2*pi*x)/(N-1)) + 1.29*np.cos((4*pi*x)/(N-1)) - 0.388*np.cos((6*pi*x)/(N-1)) + 0.028* np.cos((8*pi*x)/(N-1))
    elif ime == "turkey":
        return np.vectorize(turki)(x)
    elif ime=="poisson":
        return np.exp(-np.absolute(x-0.5*(N-1))/(0.5*N*8.69/60))
    raise NameError("Napačno okno")

def spekterstari(x, ime=0):
    N = x.size
    if ime==0:
        fourier = np.fft.fft(x)
        moc = []
        for i in range(int(N/2 + 1)):
            if i==0:
                moc.append(np.absolute(fourier[0])**2)
                continue
            elif i==N/2:
                moc.append(np.absolute(fourier[i])**2)
                continue
            moc.append(0.5*(np.absolute(fourier[i])**2+np.absolute(fourier[N-i])**2))
        return [range(int(N/2+1)),moc]
    oknce = np.asarray(range(N))
    signal = x*okno(ime,oknce)
    fourier = np.fft.fft(signal)
    moc = []
    for i in range(int(N/2 + 1)):
        if i==0:
            moc.append(np.absolute(fourier[0])**2)
            continue
        elif i==N/2:
            moc.append(np.absolute(fourier[i])**2)
            continue
        moc.append(0.5*(np.absolute(fourier[i])**2+np.absolute(fourier[N-i])**2))
    return [range(int(N/2+1)),moc]

def gaussovka(x,mu,sigma):
    return 1/np.sqrt(2*pi*sigma**2) * np.exp(-(x-mu)**2/(2*sigma**2))

def avtokorelacija(x,i):
    N = x.size
    y = np.concatenate((x,np.zeros(N)))[i:i+N]
    return 1/(N-i)*np.sum(x*y)     
   
def aji(x,p):
    rji = np.asarray([avtokorelacija(x,i) for i in range(p)])
    matrika = scipy.linalg.toeplitz(rji,rji)
    return solve(matrika,-np.append(rji[1:],avtokorelacija(x,p)))

def spekter2(a,w):
    arej = np.exp(-1j * 2*pi*w/10000 * np.asarray(range(1,a.size+1)))
    return np.abs(1+np.sum(a*arej))**(-2)

def avtokonvolucija(x,i):
    N = x.size
    y = np.concatenate((np.zeros(N),x))[N+1-i:N+1+N-i]
    return 1/(N)*np.sum(x*y)    

def napaka(a,x):
    N = x.size
    E = np.sum(x**2)/N
    eji = np.asarray([avtokonvolucija(x,i) for i in range(1,a.size+1)])
    return E + np.sum(a*eji)

def napovej(x,a):
    signal = x
    N = x.size
    p = a.size
    pass
    for i in range(N):
        novi = - np.sum(a*signal[signal.size:signal.size-p-1:-1])
        signal = np.append(signal,novi)
    return signal

def preslikaj(x):
    novenicle = []
    for i in range(x.size):
        if np.abs(x[i]) > 1:
            x[i] = x[i]/np.abs(x[i])
            novenicle.append(x[i])
    return np.array(novenicle)

def napaka(data, p, normalizacija = True):
    coef = getCoef(data, p)
    a = np.correlate(data, data, mode = 'valid')
    if normalizacija:
        a /= data.size
        a += np.sum(coef * np.correlate(np.concatenate((data,np.zeros(p))), data, mode = "valid")[1:] / (data.size-np.arange(1, p+1)))
    else:
        a += np.sum(coef * np.correlate(np.concatenate((data,np.zeros(p))), data, mode = "valid")[1:])
    return a

def zasumi(x,mu,sigma):
    if sigma==0:
        return x
    gaussi = np.random.normal(mu,sigma,x.size)
    return x+gaussi


if 1:
    #LOCLJIVOST NE POZABI SPREMENIT NJA V SPEKTR2
    x = np.linspace(0,100,10000)
    y = np.sin(5*x) + np.sin(7*x) + np.sin(10*x)
    #plt.plot(x, y)
    omege = np.linspace(0,5000,10000)
    spektr = spekterstari(y,"hann")
    ap = np.linspace(0, 5000, 5001)
    #plt.yscale("log")
    plt.title(r"MEM - Spekter $sin(5 t)+sin(10t) + sin(15 t) + $")
    plt.ylabel(r"$|P(\omega)|^2$")
    plt.xlabel(r"$\omega$")
    plt.plot(np.array(spektr[0])*2*pi/100,spektr[1], label="FFT+Hann")
    a = aji(y,40)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.semilogy(omege*2*pi/100,spekter,label="p=50")
    a = aji(y,50)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.semilogy(omege*2*pi/100,spekter,label="p=50")
    a = aji(y,20)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.semilogy(omege*2*pi/100,spekter,label="p=20")
    plt.xlim(0,30)
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_locljivost_2.pdf")
    #plt.savefig("prva/locljivost5.pdf")
if 0:
    #POLI mogli bi bit pri k=46.5, k=93 in k=139
    podatki = np.loadtxt("co2.dat")
    negativne = np.where(podatki[:,1]<0)
    podatki = np.delete(podatki,negativne,0)
    koef = np.polyfit(podatki[:,0],podatki[:,1],1)
    podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    a = aji(podatki[:,1],3)
    nicle = np.roots(np.append(a[::-1],1)[::-1])
    plt.plot(np.real(nicle),np.imag(nicle),"bo",label="p=3")
    a = aji(podatki[:,1],6)
    x = np.linspace(-1,1,1000)
    nicle = np.roots(np.append(a[::-1],1)[::-1])
    plt.plot(x,np.sqrt(1-x**2),"b")
    plt.plot(x,-np.sqrt(1-x**2),"b")
    plt.plot(np.real(nicle),np.imag(nicle),"go",label="p=6")
    a = aji(podatki[:,1],15)
    nicle = np.roots(np.append(a[::-1],1)[::-1])
    plt.plot(np.real(nicle),np.imag(nicle),"mo",label="p=15")
    plt.axes().set_aspect("equal")
    plt.legend(loc="upper left")
    plt.savefig("Jan_Kren_112_poli.pdf")
if 1:
    #SPEKTER VAL2 VAL3 Z MEM
    podatki = np.loadtxt("1naloga/val2.dat")
    a = aji(podatki,15)
    spektrstari = spekterstari(podatki[:],"hann")
    plt.yscale("log")
    plt.plot(spektrstari[0],spektrstari[1],"k--",label="FFT+Hann")
    omege = np.linspace(0,303,10000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=10000")
    omege = np.linspace(0,303,1000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=1000")
    omege = np.linspace(0,303,100)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=100")
    omege = np.linspace(0,303,50)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=50")
    plt.title(r"Spekter $val3$, p=15")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_val3_N.pdf")
if 0:
    #SPEKTER VAL2 VAL3 Z MEM
    podatki = np.loadtxt("val3.dat")
    #pji = range(1,21)
    #ajcki = [aji(podatki,p) for p in pji]
    #napakce = [napaka(ajcek,podatki) for ajcek in ajcki]
    #plt.plot(pji,napakce)
    omege = np.linspace(0,256,10000)
    a = aji(podatki,15)
    spektrstari = spekterstari(podatki[:],"hann")
    plt.yscale("log")
    plt.plot(spektrstari[0],spektrstari[1],"k--",label="FFT+Hann")
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    a = aji(podatki,5)
    #omege = np.linspace(0,303,10000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=5")
    a = aji(podatki,10)
    #omege = np.linspace(0,303,1000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=10")
    a = aji(podatki,15)
    #omege = np.linspace(0,303,100)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=15")
    a = aji(podatki,20)
    #omege = np.linspace(0,303,50)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=20")
    plt.title(r"Spekter $val3$, N = 10000")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_val3_p.pdf")
if 0:
    if 1:
        podatki = np.loadtxt("co2.dat")
        negativne = np.where(podatki[:,1]<0)
        podatki = np.delete(podatki,negativne,0)
        print(podatki[:,0].size)
        koef = np.polyfit(podatki[:,0],podatki[:,1],1)
        podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    #pji = range(1,21)
    #ajcki = [aji(podatki,p) for p in pji]
    #napakce = [napaka(ajcek,podatki) for ajcek in ajcki]
    #plt.plot(pji,napakce)
    omege = np.linspace(0,303,10000)
    a = aji(podatki[:,1],15)
    spektrstari = spekterstari(podatki[:,1],"hann")
    plt.yscale("log")
    plt.plot(spektrstari[0],spektrstari[1],"--",label="FFT+Hann")
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    #plt.plot(omege,spekter,label="p=3")
    a = aji(podatki[:,1],5)
    #omege = np.linspace(0,303,10000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=5")
    a = aji(podatki[:,1],10)
    #omege = np.linspace(0,303,1000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=10")
    a = aji(podatki[:,1],15)
    #omege = np.linspace(0,303,100)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=15")
    a = aji(podatki[:,1],20)
    #omege = np.linspace(0,303,50)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="p=20")
    plt.title(r"Spekter $CO_2$, p=15")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_co2_p.pdf")
if 0:
    if 1:
        podatki = np.loadtxt("co2.dat")
        negativne = np.where(podatki[:,1]<0)
        podatki = np.delete(podatki,negativne,0)
        print(podatki[:,0].size)
        koef = np.polyfit(podatki[:,0],podatki[:,1],1)
        podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    #pji = range(1,21)
    #ajcki = [aji(podatki,p) for p in pji]
    #napakce = [napaka(ajcek,podatki) for ajcek in ajcki]
    #plt.plot(pji,napakce)
    omege = np.linspace(0,303,10000)
    a = aji(podatki[:,1],15)
    spektrstari = spekterstari(podatki[:,1],"hann")
    plt.yscale("log")
    plt.plot(spektrstari[0],spektrstari[1],"--",label="FFT+Hann")
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    #plt.plot(omege,spekter,label="p=3")
    #a = aji(podatki[:,1],5)
    omege = np.linspace(0,303,10000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=10000")
    #a = aji(podatki[:,1],10)
    omege = np.linspace(0,303,1000)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=1000")
    #a = aji(podatki[:,1],15)
    omege = np.linspace(0,303,100)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=100")
    #a = aji(podatki[:,1],20)
    omege = np.linspace(0,303,50)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter,label="N=50")
    plt.title(r"Spekter $CO_2$, p=15")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_co2_N.pdf")
if 0:
    if 1:
        podatki = np.loadtxt("co2.dat")
        negativne = np.where(podatki[:,1]<0)
        podatki = np.delete(podatki,negativne,0)
        koef = np.polyfit(podatki[:,0],podatki[:,1],1)
        #podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    plt.plot(podatki[:, 0], podatki[:, 1], "k")
    plt.xlabel("Leto")
    plt.ylabel(r"|$CO_2$|")
    plt.title(r"Koncentracija $CO_2$ v zraku")
    plt.savefig("Jan_Kren_co2_0.pdf")
if 0:
    t = np.linspace(0,1,512)
    y = np.sin(50*t)
    a = aji(y,10)
    omege = np.linspace(0,256,100)
    spekter = np.vectorize(spekter2,excluded={0})(a,omege)
    plt.plot(omege,spekter)    
    





#DRUGA NALOGA:
if 0:
    #ODSTOPANJE OD PRAVE VREDNOSTI
    podatki = np.loadtxt("val3.dat")
    #print(podatki.size)
    #negativne = np.where(podatki[:,1]<0)
    #podatki = np.delete(podatki,negativne,0)
    #koef = np.polyfit(podatki[:,0],podatki[:,1],1)
    #podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    #podatki = podatki[:,1]
    podatki2 = zasumi(podatki,5,0.1)
    a = aji(podatki2,27)
    nicle = np.roots(np.append(a[::-1],1)[::-1])            
    preslikaj(nicle)
    a = np.poly(nicle)[1:]
    polovica = podatki2[:int(podatki2.size/2)]
    napovedan = napovej(polovica,a)    
    if 1:
        sigme = [0,0.01,0.1,0.5, 0.8,1]
        for j in sigme:
            odstopanja = []
            for k in range(100):
                odstopanjatemp = []
                podatki2 = zasumi(podatki,1,j)
                pji = range(2,21)
                for i in pji:
                    a = aji(podatki2,i)
                    nicle = np.roots(np.append(a[::-1],1)[::-1])            
                    preslikaj(nicle)
                    a = np.poly(nicle)[1:]
                    polovica = podatki2[:int(podatki2.size/2)]
                    napovedan = napovej(polovica,a)
                    odstopanje= np.sum(np.abs(napovedan[int(podatki2.size/2):] - podatki2[int(podatki2.size/2):]))/polovica.size
                    odstopanjatemp.append(odstopanje)
                if k==0:
                    odstopanja = np.array(odstopanjatemp)
                else:
                    odstopanja = odstopanja + np.array(odstopanjatemp)
            
            plt.semilogy(pji,odstopanja/100,"o-",label=r"$\sigma = {0}$".format(str(j)))
    #plt.plot(range(podatki2.size),podatki2,label="Pravi")
    #plt.plot(range(podatki2.size),napovedan,label="Napovedan")
    plt.title(r"Odvisnost napake od šuma za val3, $\mu = 1$")
    plt.ylabel(r"$\Delta s$")
    plt.xlabel("p")
    #plt.yscale("log")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_sumi2.pdf")
#podatki = np.loadtxt("luna.dat",usecols=2)
#plt.xlabel("Čas [dan]")
#plt.ylabel("Dec[stopinje]")
#plt.title("Lunarne efemeride, 1995-2000")
#plt.plot(range(podatki.size),podatki)
#plt.savefig("druga/lunaraw2.pdf")
if 0:
    podatki = np.loadtxt("val2.dat")#,usecols=2)
    a = aji(podatki,25)
    if 1:
        #PREVERI POLE
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        preslikaj(nicle)
        a = np.poly(nicle)[1:]
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    plt.xlabel("Čas [s]")
    plt.ylabel("s(t)")
    plt.plot(range(podatki.size),podatki,label="Osnovni signal")
    plt.plot(range(podatki.size),napovedan,label="Napovedan signal")
    plt.title("Linearna napoved za val2, p=25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_val2_napoved_4.pdf")
if 0:
    podatki = np.loadtxt("val2.dat")#,usecols=2)
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        preslikaj(nicle)
        a = np.poly(nicle)[1:]
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    napaka = np.abs((napovedan[256:512] - podatki[256:512])/podatki[256:512])
    plt.semilogy(range(256),napaka,label="val2")
    podatki = np.loadtxt("val3.dat")#,usecols=2)
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        preslikaj(nicle)
        a = np.poly(nicle)[1:]
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    napaka = np.abs((napovedan[256:512] - podatki[256:512])/podatki[256:512])
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$\Delta$s(t)")
    plt.semilogy(range(256),napaka,label="val3")
    plt.title("Napaka pri linearni napovedi, val2, p=25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_val2_napoved_5.pdf")
if 0:
    podatki = np.loadtxt("val2.dat")#,usecols=2)
    lol = []
    l_l = []
    for l in range(5, 20):
        a = aji(podatki,l)
        #LINEARNA NAPOVED
        if 1:
            #PREVERI POLE
            nicle = np.roots(np.append(a[::-1],1)[::-1])            
            preslikaj(nicle)
            a = np.poly(nicle)[1:]
        polovica = podatki[:int(podatki.size/2)]
        napovedan = napovej(polovica,a)
        napaka = np.abs(napovedan[256:512] - podatki[256:512])
        lol.append(np.sum(napaka))
        l_l.append(l)
    plt.plot(l_l,lol,"k-o", label="val2")
    plt.xlabel("p")
    plt.ylabel("Vsota absolutnih napak")
    plt.title("val2")
    plt.savefig("Jan_Kren_val2_napoved_6.pdf")
if 0:
    podatki = np.loadtxt("co2.dat")#,usecols=2)
    negativne = np.where(podatki[:,1]<0)
    podatki = np.delete(podatki,negativne,0)
    koef = np.polyfit(podatki[:,0],podatki[:,1],1)
    podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    podatki = podatki[:,1]
    lol = []
    l_l = []
    for l in range(5, 40):
        a = aji(podatki,l)
        #LINEARNA NAPOVED
        if 1:
            #PREVERI POLE
            nicle = np.roots(np.append(a[::-1],1)[::-1])            
            preslikaj(nicle)
            a = np.poly(nicle)[1:]
        polovica = podatki[:int(podatki.size/2)]
        napovedan = napovej(polovica,a)
        napaka = np.abs(napovedan[256:512] - podatki[256:512])
        lol.append(np.sum(napaka))
        l_l.append(l)
    plt.plot(l_l,lol,"k-o", label="val2")
    plt.xlabel("p")
    plt.ylabel("Vsota absolutnih napak")
    plt.title(r"$CO_2$")
    plt.savefig("Jan_Kren_co2_napoved_6.pdf")
if 0:
    podatki = np.loadtxt("co2.dat")#,usecols=2)
    negativne = np.where(podatki[:,1]<0)
    podatki = np.delete(podatki,negativne,0)
    koef = np.polyfit(podatki[:,0],podatki[:,1],1)
    podatki[:,1] = podatki[:,1] - koef[0] * podatki[:,0] - koef[1]
    podatki2=podatki[:,0]
    podatki = podatki[:,1]
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        x = np.linspace(-1,1,1000)
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        #plt.plot(np.real(nicle),np.imag(nicle),"mo",label="p=15")
        preslikaj(nicle)
        #plt.plot(np.real(nicle),np.imag(nicle),"ro")        
        #plt.plot(x,np.sqrt(1-x**2),"b")
        #plt.plot(x,-np.sqrt(1-x**2),"b")
        #plt.savefig("druga/val33poli.pdf")
        a = np.poly(nicle)[1:]
    #raise NameError("Zaenkrat samo preverjamo pole")
    x = range(podatki.size)
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    plt.xlabel("Čas")
    plt.ylabel("s(t)")
    plt.plot(range(podatki.size),podatki,label="Osnovni signal")
    plt.plot(range(podatki.size),napovedan,label="Napovedan signal")
    plt.title(r"$CO_2$, p = 25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_112_C02_napoved_1.pdf")
if 0:
    podatki = np.loadtxt("luna.dat",usecols=2)
    lol = []
    l_l = []
    for l in range(5, 40):
        a = aji(podatki,l)
        #LINEARNA NAPOVED
        if 1:
            #PREVERI POLE
            nicle = np.roots(np.append(a[::-1],1)[::-1])            
            preslikaj(nicle)
            a = np.poly(nicle)[1:]
        polovica = podatki[:int(podatki.size/2)]
        napovedan = napovej(polovica,a)
        napaka = np.abs(np.array(napovedan[int(2192/2):2192]) - np.array(podatki[int(2192/2):2192]))
        lol.append(np.sum(napaka))
        l_l.append(l)
    plt.plot(l_l,lol,"k-o", label="val2")
    plt.xlabel("p")
    plt.ylabel("Vsota absolutnih napak")
    plt.title("Lunine efemeride")
    plt.savefig("Jan_Kren_luna_napoved_1.pdf")
if 0:
    podatki = np.loadtxt("luna.dat",usecols=2)
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        x = np.linspace(-1,1,1000)
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        #plt.plot(np.real(nicle),np.imag(nicle),"mo",label="p=15")
        preslikaj(nicle)
        #plt.plot(np.real(nicle),np.imag(nicle),"ro")        
        #plt.plot(x,np.sqrt(1-x**2),"b")
        #plt.plot(x,-np.sqrt(1-x**2),"b")
        #plt.savefig("druga/val33poli.pdf")
        a = np.poly(nicle)[1:]
    #raise NameError("Zaenkrat samo preverjamo pole")
    x = range(podatki.size)
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    plt.xlabel("Čas")
    plt.ylabel("s(t)")
    plt.plot(range(podatki.size),podatki,label="Osnovni signal")
    plt.plot(range(podatki.size),napovedan,label="Napovedan signal")
    plt.title(r"Lunine efemeride, p = 25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_112_luna_napoved_2.pdf")
if 0:
    podatki = np.loadtxt("borza.dat")#,usecols=2)
    lol = []
    l_l = []
    for l in range(5, 50):
        a = aji(podatki,l)
        #LINEARNA NAPOVED
        if 1:
            #PREVERI POLE
            nicle = np.roots(np.append(a[::-1],1)[::-1])            
            preslikaj(nicle)
            a = np.poly(nicle)[1:]
        polovica = podatki[:int(podatki.size/2)]
        napovedan = napovej(polovica,a)
        napaka = np.abs(np.array(napovedan[354:709]) - np.array(podatki[355:709]))
        lol.append(np.sum(napaka))
        l_l.append(l)
    plt.plot(l_l,lol,"k-o", label="val2")
    plt.xlabel("p")
    plt.ylabel("Vsota absolutnih napak")
    plt.title("Borza")
    plt.savefig("Jan_Kren_borza_napoved_2.pdf")
if 0:
    podatki = np.loadtxt("borza.dat")
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        x = np.linspace(-1,1,1000)
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        #plt.plot(np.real(nicle),np.imag(nicle),"mo",label="p=15")
        preslikaj(nicle)
        #plt.plot(np.real(nicle),np.imag(nicle),"ro")        
        #plt.plot(x,np.sqrt(1-x**2),"b")
        #plt.plot(x,-np.sqrt(1-x**2),"b")
        #plt.savefig("druga/val33poli.pdf")
        a = np.poly(nicle)[1:]
    #raise NameError("Zaenkrat samo preverjamo pole")
    x = range(podatki.size)
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    plt.xlabel("Čas")
    plt.ylabel("s(t)")
    plt.plot(range(podatki.size),podatki,label="Osnovni signal")
    plt.plot(range(podatki.size-1),napovedan,label="Napovedan signal")
    plt.title(r"Borza, p = 25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_112_borza_napoved_1.pdf")
if 0:
    podatki = np.loadtxt("Wolf_number.dat",usecols=2)
    lol = []
    l_l = []
    for l in range(5, 50):
        a = aji(podatki,l)
        #LINEARNA NAPOVED
        if 1:
            #PREVERI POLE
            nicle = np.roots(np.append(a[::-1],1)[::-1])            
            preslikaj(nicle)
            a = np.poly(nicle)[1:]
        polovica = podatki[:int(podatki.size/2)]
        napovedan = napovej(polovica,a)
        napaka = np.abs(np.array(napovedan[354:709]) - np.array(podatki[355:709]))
        lol.append(np.sum(napaka))
        l_l.append(l)
    plt.plot(l_l,lol,"k-o", label="val2")
    plt.xlabel("p")
    plt.ylabel("Vsota absolutnih napak")
    plt.title("Wolfovo število")
    plt.savefig("Jan_Kren_wolf_napoved_2.pdf")
if 0:
    podatki = np.loadtxt("Wolf_number.dat",usecols=2)
    a = aji(podatki,25)
    #LINEARNA NAPOVED
    if 1:
        #PREVERI POLE
        x = np.linspace(-1,1,1000)
        nicle = np.roots(np.append(a[::-1],1)[::-1])            
        #plt.plot(np.real(nicle),np.imag(nicle),"mo",label="p=15")
        preslikaj(nicle)
        #plt.plot(np.real(nicle),np.imag(nicle),"ro")        
        #plt.plot(x,np.sqrt(1-x**2),"b")
        #plt.plot(x,-np.sqrt(1-x**2),"b")
        #plt.savefig("druga/val33poli.pdf")
        a = np.poly(nicle)[1:]
    #raise NameError("Zaenkrat samo preverjamo pole")
    x = range(podatki.size)
    polovica = podatki[:int(podatki.size/2)]
    napovedan = napovej(polovica,a)
    plt.xlabel("Čas")
    plt.ylabel("s(t)")
    plt.plot(range(podatki.size),podatki,label="Osnovni signal")
    plt.plot(range(podatki.size-1),napovedan,label="Napovedan signal")
    plt.title(r"Wolfovo število, p = 25")
    plt.legend(loc="best")
    plt.savefig("Jan_Kren_112_wolf_napoved_1.pdf")
