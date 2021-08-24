import numpy as np
from scipy.optimize import linprog
import math

tab = np.loadtxt('tabela-zivil.dat', usecols=range(1,11))
L=len(tab)
B = np.array([(0,2)]*L, dtype=float)
cena, kcal, CO, meat, Ca, Fe, C, K, Na_min, Na_max, kg = [],[],[],[],[],[],[],[],[],[],[]
for i in range(len(tab)): 
    cena.append(tab[i][9])
    kcal.append(-tab[i][0])
    CO.append(-tab[i][2])
    meat.append(-tab[i][3])
    Ca.append(-tab[i][4]/1000)
    Fe.append(-tab[i][5]/1000)
    C.append(-tab[i][6]/1000)
    K.append(-tab[i][7]/1000)
    Na_min.append(-tab[i][8]/1000)
    Na_max.append(tab[i][8]/1000)
    kg.append(1)
c = cena
A = [kg, kcal, CO, meat, Ca, Fe, C, K, Na_min, Na_max]
b = [20., -2000, -310.0, -50.0, -1.0, -0.018, -0.06, -3.5, -0.5, 2.4]
#A = [kg, fat, CO, meat, Ca, Fe]
#b = [20., -70.0, -310.0, -50.0, -1.0, -0.018]
result = linprog(c, A_ub=A, b_ub=b)
#result = linprog(c, A_ub=A, b_ub=b, bounds=B)

imena = []
kol, temp1, temp2, temp3, temp4, temp5 = 0,0,0,0,0,0
temp6, temp7, temp8, temp9 = 0,0,0,0

with open("tabela-zivil.dat") as data:
    next(data)
    next(data) 
    for line in data: 
        temp = line.split() 
        imena.append(temp[0])
for i in range(len(tab)):
    k=result.x[i]
    if k==0:
        continue
    else: 
        print(imena[i], '%.3f' % (k*100), k*cena[i], sep=',')
        kol+=k*cena[i]
        temp1 += kcal[i]*k
        temp2 += CO[i]*k
        temp3 += meat[i]*k
        temp4 += Ca[i]*k
        temp5 += Fe[i]*k
        temp6 += C[i]*k
        temp7 += K[i]*k
        temp8 += Na_min[i]*k
#print("Tako pojemo %.0fg hrane od tega %.2fg maščob, %.2fg ogljikovih hidratov, %.2fg proteinov, %.2fg kalcija in %.2fg železa." % (kol, -temp1, -temp2, -temp3, -temp4, -temp5,))
print("Tako pojemo %.2f€ hrane od tega %.2fg maščob, %.2fg ogljikovih hidratov, %.2fg proteinov, %.2fg kalcija, %.2fg železa, %.2fg vitamina C, %.2fg kalija in %.2fg natrija." % (kol, -temp1, -temp2, -temp3, -temp4, -temp5, -temp6, -temp7, -temp8))
