import numpy as np
from scipy.optimize import linprog
import math

tab = np.loadtxt('farmakoloski.dat', usecols=range(1,8))
L=len(tab)

with open('farmakoloski.dat') as data:
    next(data)
    next(data) 
    for line in data: 
        temp = line.split() 
        imena.append(temp[0])

