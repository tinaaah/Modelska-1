# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 19:55:40 2019

@author: krenj
"""
import numpy as np
import matplotlib.pyplot as plt

def preberi_zasumljen(file):
    with open('../kalman_cartesian_data.dat', 'r') as f:
        array = [[float(x) for x in line.split()] for line in f]
    return array
def preberi_pravi(file):
    with open('../kalman_cartesian_kontrola.dat', 'r') as f:
        array = [[float(x) for x in line.split()] for line in f]
    return array
def preberi_pospesek(file):
    with open('../kalman_relative_data.dat', 'r') as f:
        array = [[float(x) for x in line.split()] for line in f]
    return array

global sigma_a
sigma_a = 0.05
global sigma_v 
sigma_v = 0.01
global sigma_xy
sigma_xy = 25
global deltat 
deltat = 1.783

zasumljen = np.array(preberi_zasumljen(1))
pravi = np.array(preberi_pravi(1))
relative = np.array(preberi_pospesek(1))
"""
plt.figure(1)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 1], "ro")
plt.xlabel("Čas")
plt.ylabel("x-smer")
plt.savefig("Jan_Kren_111_1.pdf")
plt.figure(2)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400,2], "ro")
plt.xlabel("Čas")
plt.ylabel("y-smer")
plt.savefig("Jan_Kren_111_2.pdf")
plt.figure(3)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400,3], "ro")
plt.xlabel("Čas")
plt.ylabel("$v_x$")
plt.savefig("Jan_Kren_111_3.pdf")
plt.figure(4)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400,4], "ro")
plt.xlabel("Čas")
plt.ylabel("$v_y$")
plt.savefig("Jan_Kren_111_4.pdf")
plt.figure(5)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400,5], "ro")
plt.xlabel("Čas")
plt.ylabel("$a_x$")
plt.savefig("Jan_Kren_111_5.pdf")
plt.figure(6)
plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400,6], "ro")
plt.xlabel("Čas")
plt.ylabel("$a_y$")
plt.savefig("Jan_Kren_111_6.pdf")
"""
    


def predict(x, F, B, P, Q, u):
    x = np.dot(F, x) + np.dot(B, u)
    P = np.dot(np.dot(F, P), F.T) + Q
    return x, P

def update(z, F, H, Q, R, B, P, x):
    n = len(F)
    y = z - np.dot(H, x)
    S = R + np.dot(H, np.dot(P, H.T))
    K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
    x = x + np.dot(K, y)
    I = np.eye(n)
    if y[0]!=0 or y[2]!=0:
        P = np.dot(np.dot(I - np.dot(K, H), P), 
        	(I - np.dot(K, H)).T) + np.dot(np.dot(K, R), K.T)
    return x, P, K, S, y
H1 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) #znano
H2 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) #znano
H4 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) #znano
H3 = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]) #znano
F = np.array([[1, 0, deltat, 0], [0, 1, 0, deltat], [0, 0, 1, 0], [0, 0, 0, 1]]) #Se ne spreminja

if 0:
    P = 1*np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    Q = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2*deltat**2, 0], [0, 0, 0, sigma_a**2*deltat**2]]) #po navodilih
    R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, sigma_v**2, 0], [0, 0, 0, sigma_v**2]]) #spodaj popravljena
    B = np.array([[1/2 *deltat**2, 0], [0, 1/2 *deltat**2], [deltat, 0], [0, deltat]]) #vredika
    measurements = np.array(zasumljen[0:1400, 1:5])
    c = zasumljen[0:1400, 5:7]
    #measurements[0:1400, 2:4] = 0
    predictions = []
    P_matrikca = []
    z_hx = []
    x = [1, 1, 1, 1]
    for i in range(len(measurements)):
        z = measurements[i]
        u = c[i]
        v = np.sqrt(x[2]**2+x[3]**2)
        H = H1
        if(v**2*sigma_v**2<1/3.6):
            gup = 1/3.6
        else:
            gup = v**2*sigma_v**2
        R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, gup, 0], [0, 0, 0, gup]])
        x, P = predict(x, F, B, P, Q, u)
        z_hx.append(z-x)
        P_matrikca.append(np.linalg.norm(P))
        x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
        predictions.append(x)
        print(zasumljen[i,0], P_matrikca[i])
    z_hx = np.array(z_hx)
    predictions = np.array(predictions)
    plt.figure(0)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 1]-pravi[0:1400, 1], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 0]-pravi[0:1400, 1], "o", markersize = 2,label = 'Kalmanov filter, vsaka meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $x_{prava}-x_{kal}$")
    #plt.savefig("Jan_Kren_111_7.pdf")
    plt.figure(1)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 2]-pravi[0:1400, 2], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 1]-pravi[0:1400, 2],"o", markersize = 2,label = 'Kalmanov filter, vsaka meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $y_{prava}-y_{kal}$")
    #plt.savefig("Jan_Kren_111_8.pdf")
    plt.figure(2)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 3]-pravi[0:1400, 3], "o",markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 2]-pravi[0:1400, 3])/pravi[0:1400, 3]), "o",markersize = 2, label = 'Kalmanov filter, vsaka meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(u_{prava}-u_{kal})/u_{prava}||$")
    #plt.savefig("Jan_Kren_111_9.pdf")
    plt.figure(3)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 4]-pravi[0:1400, 4], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 3]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o",markersize = 2,label = 'Kalmanov filter, vsaka meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(v_{prava}-v_{kal})/v_{prava}||$")
    #plt.savefig("Jan_Kren_111_10.pdf")
    ap = np.sqrt((predictions[0:1400, 0]-pravi[0:1400, 1])**2+(predictions[0:1400, 1]-pravi[0:1400, 2])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 1]-pravi[0:1400, 1])**2+(zasumljen[0:1400, 2]-pravi[0:1400, 2])**2)
    plt.figure(4)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Kalmanov filter, vsaka meritev")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||x-x_0, y-y_0||$")
    #plt.savefig("Jan_Kren_111_odstop.pdf")
    plt.figure(5)
    plt.semilogy(zasumljen[0:1400, 0], P_matrikca, "o", markersize = 2,  label = "Kalmanov filter, vsaka meritev")
    plt.xlabel("Čas [s]")
    plt.ylabel("|P|")
    #plt.savefig("Jan_Kren_111_P.pdf")
    ap = np.sqrt((predictions[0:1400, 2]-pravi[0:1400, 3])**2+(predictions[0:1400, 3]-pravi[0:1400, 4])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 3]-pravi[0:1400, 3])**2+(zasumljen[0:1400, 4]-pravi[0:1400, 4])**2)
    plt.figure(6)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Kalmanov filter, vsaka meritev")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||u-u_0, v-v_0||$")
    #plt.savefig("Jan_Kren_111_odstop_v.pdf")
if 0:
    P = 1*np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    Q = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2*deltat**2, 0], [0, 0, 0, sigma_a**2*deltat**2]]) #po navodilih
    R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, sigma_v**2, 0], [0, 0, 0, sigma_v**2]]) #spodaj popravljena
    B = np.array([[1/2 *deltat**2, 0], [0, 1/2 *deltat**2], [deltat, 0], [0, deltat]]) #vredika
    measurements = np.array(zasumljen[0:1400, 1:5])
    c = zasumljen[0:1400, 5:7]
    #measurements[0:1400, 2:4] = 0
    predictions = []
    P_matrikca = []
    z_hx = []
    x = [1, 1, 1, 1]
    for i in range(len(measurements)):
        z = measurements[i]
        u = c[i]
        v = np.sqrt(x[2]**2+x[3]**2)
        if(v**2*sigma_v**2<1/3.6):
            gup = 1/3.6
        else:
            gup = v**2*sigma_v**2
        R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, gup, 0], [0, 0, 0, gup]])
        if(i%5==0 and i%10!=0):
            z[0:2] = 0
            H = H4
        elif(i%10==0):
            z = z
            H = H1
        else:
            z[0:4] = 0
            H = H3
        x, P = predict(x, F, B, P, Q, u)
        z_hx.append(z-x)
        x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
        P_matrikca.append(np.linalg.norm(P))
        predictions.append(x)
    predictions = np.array(predictions)
    plt.figure(0)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 1]-pravi[0:1400, 1], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 0]-pravi[0:1400, 1], "o", markersize = 2,label = 'Kalmanov filter, vsaka 5/10 meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $x_{prava}-x_{kal}$")
    #plt.savefig("Jan_Kren_111_11.pdf")
    plt.figure(1)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 2]-pravi[0:1400, 2], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 1]-pravi[0:1400, 2],"o", markersize = 2,label = 'Kalmanov filter, vsaka 5/10 meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $y_{prava}-y_{kal}$")
    #plt.savefig("Jan_Kren_111_12.pdf")
    plt.figure(2)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 3]-pravi[0:1400, 3], "o",markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 2]-pravi[0:1400, 3])/pravi[0:1400, 3]), "o",markersize = 2, label = 'Kalmanov filter, vsaka 5/10 meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(vu_{prava}-u_{kal})/u_{prava}||$")
    #plt.savefig("Jan_Kren_111_13.pdf")
    plt.figure(3)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 4]-pravi[0:1400, 4], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 3]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o",markersize = 2,label = 'Kalmanov filter, vsaka 5/10 meritev')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(v_{prava}-v_{kal})/v_{prava}||$")
    #plt.savefig("Jan_Kren_111_14.pdf")
    ap = np.sqrt((predictions[0:1400, 0]-pravi[0:1400, 1])**2+(predictions[0:1400, 1]-pravi[0:1400, 2])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 1]-pravi[0:1400, 1])**2+(zasumljen[0:1400, 2]-pravi[0:1400, 2])**2)
    plt.figure(4)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Kalmanov filter, vsaka 5/10 meritev")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||x-x_0, y-y_0||$")
    #plt.savefig("Jan_Kren_111_odstop_a.pdf")
    plt.figure(5)
    plt.semilogy(zasumljen[0:1400, 0], P_matrikca, "o", markersize = 2, label = "Kalmanov filter, vsaka 5/10 meritev")
    plt.xlabel("Čas [s]")
    plt.ylabel("|P|")
    plt.legend()
    plt.savefig("Jan_Kren_111_P_a.pdf")
    ap = np.sqrt((predictions[0:1400, 2]-pravi[0:1400, 3])**2+(predictions[0:1400, 3]-pravi[0:1400, 4])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 3]-pravi[0:1400, 3])**2+(zasumljen[0:1400, 4]-pravi[0:1400, 4])**2)
    plt.figure(6)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Kalmanov filter, vsaka 5/10 meritev")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||u-u_0, v-v_0||$")
    #plt.savefig("Jan_Kren_111_odstop_v_a.pdf")
if 0:
    P = 1*np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    Q = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2*deltat**2, 0], [0, 0, 0, sigma_a**2*deltat**2]]) #po navodilih
    R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, sigma_v**2, 0], [0, 0, 0, sigma_v**2]]) #spodaj popravljena
    B = np.array([[1/2 *deltat**2, 0], [0, 1/2 *deltat**2], [deltat, 0], [0, deltat]]) #vredika
    measurements = np.array(zasumljen[0:1400, 1:5])
    c = zasumljen[0:1400, 5:7]
    measurements[0:1400, 2:4] = 0
    predictions = []
    P_matrikca = []
    Q_matrikca = []
    K_matrikca = []
    z_hx = []
    x = [1, 1, 1, 1]
    for i in range(len(measurements)):
        z = measurements[i]
        u = c[i]
        v = np.sqrt(x[2]**2+x[3]**2)
        H = H2
        if(v**2*sigma_v**2<1/3.6):
            gup = 1/3.6
        else:
            gup = v**2*sigma_v**2
        R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, gup, 0], [0, 0, 0, gup]])
        x, P = predict(x, F, B, P, Q, u)
        z_hx.append(z-x)
        P_matrikca.append(np.linalg.norm(P))
        Q_matrikca.append(np.linalg.norm(Q))
        x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
        K_matrikca.append(np.linalg.norm(K))
        predictions.append(x)
    z_hx = np.array(z_hx)
    predictions = np.array(predictions)
    plt.figure(0)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 1]-pravi[0:1400, 1], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 0]-pravi[0:1400, 1], "o", markersize = 2,label = 'Samo pozicije')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $x_{prava}-x_{kal}$")
    plt.savefig("Jan_Kren_111_7.pdf")
    plt.figure(1)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 2]-pravi[0:1400, 2], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 1]-pravi[0:1400, 2],"o", markersize = 2,label = 'Samo pozicije')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $y_{prava}-y_{kal}$")
    #plt.savefig("Jan_Kren_111_8.pdf")
    plt.figure(2)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 3]-pravi[0:1400, 3], "o",markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 2]-pravi[0:1400, 3])/pravi[0:1400, 3]), "o",markersize = 2, label = 'Samo pozicije')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(vu_{prava}-u_{kal})/u_{prava}||$")
    #plt.savefig("Jan_Kren_111_9.pdf")
    plt.figure(3)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 4]-pravi[0:1400, 4], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 3]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o",markersize = 2,label = 'Samo pozicije')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(v_{prava}-v_{kal})/v_{prava}||$")
    #plt.savefig("Jan_Kren_111_10.pdf")
    ap = np.sqrt((predictions[0:1400, 0]-pravi[0:1400, 1])**2+(predictions[0:1400, 1]-pravi[0:1400, 2])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 1]-pravi[0:1400, 1])**2+(zasumljen[0:1400, 2]-pravi[0:1400, 2])**2)
    plt.figure(4)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Samo pozicije")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||x-x_0, y-y_0||$")
    #plt.savefig("Jan_Kren_111_odstop.pdf")
    plt.figure(5)
    plt.semilogy(zasumljen[0:1400, 0], P_matrikca, "o", markersize = 2,  label = "Samo pozicije")
    plt.xlabel("Čas [s]")
    plt.ylabel("|P|")
    #plt.savefig("Jan_Kren_111_P.pdf")
    ap = np.sqrt((predictions[0:1400, 2]-pravi[0:1400, 3])**2+(predictions[0:1400, 3]-pravi[0:1400, 4])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 3]-pravi[0:1400, 3])**2+(zasumljen[0:1400, 4]-pravi[0:1400, 4])**2)
    plt.figure(6)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Samo pozicije")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||u-u_0, v-v_0||$")
    #plt.savefig("Jan_Kren_111_odstop_v_c.pdf")
    plt.figure(7)
    plt.semilogy(zasumljen[0:1400, 0], Q_matrikca, "o", markersize = 2, label = "Samo pozicije")
    plt.xlabel("Čas [s]")
    plt.ylabel("|Q|")
    plt.legend()
    plt.figure(8)
    plt.semilogy(zasumljen[0:1400, 0], K_matrikca, "o", markersize = 2, label = "Samo pozicije")
    plt.xlabel("Čas [s]")
    plt.ylabel("|K|")
    plt.legend()
if 1:
    P = 1*np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    print(P)
    Q = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2*deltat**2, 0], [0, 0, 0, sigma_a**2*deltat**2]]) #po navodilih
    R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, sigma_v**2, 0], [0, 0, 0, sigma_v**2]]) #spodaj popravljena
    B = np.array([[1/2 *deltat**2, 0], [0, 1/2 *deltat**2], [deltat, 0], [0, deltat]]) #vredika
    measurements = np.array(zasumljen[0:1400, 1:5])
    c = zasumljen[0:1400, 5:7]
    measurements[0:1400, 0:2] = 0
    predictions = []
    P_matrikca = []
    z_hx = []
    x = [1, 1, 1, 1]
    for i in range(len(measurements)):
        z = measurements[i]
        u = c[i]
        v = np.sqrt(x[2]**2+x[3]**2)
        if(v**2*sigma_v**2<1/3.6):
            gup = 1/3.6
        else:
            gup = v**2*sigma_v**2
        H = H4
        R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, gup, 0], [0, 0, 0, gup]])
        x, P = predict(x, F, B, P, Q, u)
        z_hx.append(z-x)
        P_matrikca.append(np.linalg.norm(P))
        x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
        predictions.append(x)

    predictions = np.array(predictions)
    plt.figure(0)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 1]-pravi[0:1400, 1], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 0]-pravi[0:1400, 1], "o", markersize = 2,label = 'Samo hitrosti')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $x_{prava}-x_{kal}$")
    plt.savefig("Jan_Kren_111_v_11.pdf")
    plt.figure(1)
    #plt.plot(zasumljen[0:1400, 0], zasumljen[0:1400, 2]-pravi[0:1400, 2], "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 1]-pravi[0:1400, 2],"o", markersize = 2,label = 'Samo hitrosti')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $y_{prava}-y_{kal}$")
    #plt.savefig("Jan_Kren_111_v_12.pdf")
    plt.figure(2)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 3]-pravi[0:1400, 3], "o",markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 2]-pravi[0:1400, 3])/pravi[0:1400, 3]), "o",markersize = 2, label = 'Samo hitrosti')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||u_{prava}-u_{kal})/u_{prava}||$")
    #plt.savefig("Jan_Kren_111_v_13.pdf")
    plt.figure(3)
    #plt.semilogy(zasumljen[0:1400, 0], zasumljen[0:1400, 4]-pravi[0:1400, 4], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 3]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o",markersize = 2,label = 'Samo hitrosti')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||(v_{prava}-v_{kal})/v_{prava}||$")
    #plt.savefig("Jan_Kren_111_v_14.pdf")
    ap = np.sqrt((predictions[0:1400, 0]-pravi[0:1400, 1])**2+(predictions[0:1400, 1]-pravi[0:1400, 2])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 1]-pravi[0:1400, 1])**2+(zasumljen[0:1400, 2]-pravi[0:1400, 2])**2)
    plt.figure(4)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Samo hitrosti")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||x-x_0, y-y_0||$")
    #plt.savefig("Jan_Kren_111_odstop_b.pdf")
    plt.figure(5)
    plt.semilogy(zasumljen[0:1400, 0], P_matrikca, "o", markersize = 2, label = "Samo hitrosti")
    plt.xlabel("Čas [s]")
    plt.ylabel("|P|")
    plt.legend()
    plt.savefig("Jan_Kren_111_P_b.pdf")
    ap = np.sqrt((predictions[0:1400, 2]-pravi[0:1400, 3])**2+(predictions[0:1400, 3]-pravi[0:1400, 4])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 3]-pravi[0:1400, 3])**2+(zasumljen[0:1400, 4]-pravi[0:1400, 4])**2)
    plt.figure(6)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Samo hitrosti")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||u-u_0, v-v_0||$")
    #plt.savefig("Jan_Kren_111_odstop_v_b.pdf")
if 0:
    P = 1*np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    Q = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2*deltat**2, 0], [0, 0, 0, sigma_a**2*deltat**2]]) #po navodilih
    R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, sigma_v**2, 0], [0, 0, 0, sigma_v**2]]) #spodaj popravljena
    B = np.array([[1/2 *deltat**2, 0], [0, 1/2 *deltat**2], [deltat, 0], [0, deltat]]) #vredika
    x = [1, 1, 1, 1]
    measurements = np.array(relative[0:1400, 1:5])
    c = np.zeros((1400, 4))
    c[0:1400, 2:4] = relative[0:1400, 3:5]*deltat
   # measurements[0:1400, 2:4] = 0
    predictions = []
    x = [1, 1, 1, 1]
    P_matrikca = []
    Q_matrikca = []
    K_matrikca = []
    for i in range(len(measurements)):
        z = measurements[i]
        u = c[i]
        konst = 1/(np.sqrt(x[2]**2+x[3]**2))
        B = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, x[2]*konst, -x[3]*konst], [0, 0, x[3]*konst, x[2]*konst]]) #znano

        an_prav = [-np.float(u[3]), np.float(u[2])]
        vn_prav = [-np.float(x[3]), np.float(x[2])]

        out = np.outer(np.dot([[x[2]*konst, -x[3]*konst], [x[3]*konst, x[2]*konst]],an_prav), np.dot([[x[2]*konst, -x[3]*konst], [x[3]*konst, x[2]*konst]],an_prav))
        
        lup = np.dot(vn_prav, np.dot(P[2:4, 2:4], vn_prav))*konst**4
        Q = deltat**2*np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, sigma_a**2+lup*out[0, 0], lup*out[0, 1]], [0, 0, lup*out[1, 0], sigma_a**2+lup*out[1, 1]]])
        Q_matrikca.append(np.linalg.norm(Q))

        v = np.sqrt(x[2]**2+x[3]**2)

        if(v**2*sigma_v**2<1/3.6):
            gup = 1/3.6
        else:
            gup = v**2*sigma_v**2

        H = np.zeros((4,4))
        if i%10 == 0:
            H = H2

        R = np.array([[sigma_xy**2, 0, 0, 0], [0, sigma_xy**2, 0, 0], [0, 0, gup, 0], [0, 0, 0, gup]])
        x, P = predict(x, F, B, P, Q, u)
        P_matrikca.append(np.linalg.norm(P))
        x, P, K, S, y = update(z, F, H, Q, R, B, P, x)
        K_matrikca.append(np.linalg.norm(K))
        predictions.append(x)
        #print(zasumljen[i,0], x[0], x[1], x[2], x[3], sep='\t')
        #print(zasumljen[i,0], x[0]-pravi[i,1], x[1]-pravi[i,2], np.abs( (x[2]-pravi[i,3])/pravi[i,3]) , np.abs( (x[3]-pravi[i,4])/pravi[i,4]), sep='\t')
        #print(zasumljen[i,0], P_matrikca[i], K_matrikca[i], Q_matrikca[i], sep='\t')
    predictions = np.array(predictions)
    plt.figure(0)
    #plt.plot(zasumljen[0:1400, 0], relative[0:1400, 1]-pravi[0:1400, 1], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 0]-pravi[0:1400, 1], "o", markersize = 2, label = "Akcelerometer")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $x_{prava}-x_{kal}$")
    #plt.savefig("Jan_Kren_111_15.pdf")
    plt.figure(1)
    #plt.plot(zasumljen[0:1400, 0], relative[0:1400, 2]-pravi[0:1400, 2], "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.plot(zasumljen[0:1400, 0], predictions[0:1400, 1] - pravi[0:1400, 2], "o", markersize = 2, label = 'Akcelerometer')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $y_{prava}-y_{kal}$")
    #plt.savefig("Jan_Kren_111_16.pdf")
    plt.figure(2)
    #plt.semilogy(zasumljen[0:1400, 0], np.abs((zasumljen[0:1400, 3]-pravi[0:1400, 3])/pravi[0:1400,3]), "o", markersize = 2,label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 2]-pravi[0:1400, 3])/pravi[0:1400,3]), "o", markersize = 2, label = 'Akcelerometer')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||u_{prava}-u_{kal})/u_{prava}||$")
    #plt.savefig("Jan_Kren_111_17.pdf")
    plt.figure(3)
    #plt.semilogy(zasumljen[0:1400, 0], np.abs((zasumljen[0:1400, 4]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o", markersize = 2, label = 'Odstopanja osnovne meritve')
    plt.semilogy(zasumljen[0:1400, 0], np.abs((predictions[0:1400, 3]-pravi[0:1400, 4])/pravi[0:1400, 4]), "o", markersize = 2, label = 'Akcelerometer')
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"Odstopanje $||v_{prava}-v_{kal})/v_{prava}||$")
    ##plt.savefig("Jan_Kren_111_18.pdf")
    ap = np.sqrt((predictions[0:1400, 0]-pravi[0:1400, 1])**2+(predictions[0:1400, 1]-pravi[0:1400, 2])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 1]-pravi[0:1400, 1])**2+(zasumljen[0:1400, 2]-pravi[0:1400, 2])**2)
    plt.figure(4)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Akcelerometer")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||x-x_0, y-y_0||$")
    #plt.savefig("Jan_Kren_111_odstop_c.pdf")
    plt.figure(5)
    plt.semilogy(zasumljen[0:1400, 0], P_matrikca, "o", markersize = 2, label = "Akcelerometer")
    plt.xlabel("Čas [s]")
    plt.ylabel("|P|")
    plt.legend()
    plt.savefig("Jan_Kren_111_P_c.pdf")
    ap = np.sqrt((predictions[0:1400, 2]-pravi[0:1400, 3])**2+(predictions[0:1400, 3]-pravi[0:1400, 4])**2)
    ap_sum = np.sqrt((zasumljen[0:1400, 3]-pravi[0:1400, 3])**2+(zasumljen[0:1400, 4]-pravi[0:1400, 4])**2)
    plt.figure(6)
    #plt.semilogy(zasumljen[0:1400, 0], ap_sum, "o", markersize = 2,  label = "Odstopanje osnovne meritve")
    plt.semilogy(zasumljen[0:1400, 0], ap, "o", markersize = 2, label = "Akcelerometer")
    plt.legend()
    plt.xlabel("Čas [s]")
    plt.ylabel(r"$||u-u_0, v-v_0||$")
    #plt.savefig("Jan_Kren_111_odstop_v_c.pdf")
    plt.figure(7)
    plt.semilogy(zasumljen[0:1400, 0], Q_matrikca, "o", markersize = 2, label = "Akcelerometer")
    plt.xlabel("Čas [s]")
    plt.ylabel("|Q|")
    plt.legend()
    plt.savefig("Jan_Kren_111_Q_c.pdf")
    plt.figure(8)
    plt.semilogy(zasumljen[0:1400, 0], K_matrikca, "o", markersize = 2, label = "Samo pozicije")
    plt.xlabel("Čas [s]")
    plt.ylabel("|K|")
    plt.legend()
    plt.savefig("Jan_Kren_111_K_c.pdf")
