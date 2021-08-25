import numpy as np
import math
import random
from scipy.stats import chisquare
from scipy.stats import kstest

random.seed()

N = 10000

acos = math.acos
sqrt = math.sqrt
pi = math.pi

#----------------------------------------------- koordinate
def krogla(N):
    r = [(random.uniform(0,1))**(1/3) for _ in range(N)]
    fi = [(random.uniform(0,1) * 2 * pi) for _ in range(N)]
    theta = [acos(2 * (random.uniform(0,1)) - 1) for _ in range(N)]
    return np.array([r,fi,theta])
matrika = krogla(N)

R, Rrobovi = np.histogram(matrika[0], bins='auto', density='True')
print(np.sum(R * np.diff(Rrobovi)))
Fi, Firobovi = np.histogram(matrika[1], bins='auto', density='True')
Theta, Thetarobovi = np.histogram(matrika[2], bins='auto', density='True')

for i in range(len(R)):                          
    center1 = (Rrobovi[i+1] + Rrobovi[i])/2
#    print(R[i], center1, sep='\t')
#print('')
for i in range(len(Fi)):                        
    center2 = (Firobovi[i+1] + Firobovi[i])/2
#    print(Fi[i], center2, sep='\t')
#print('')
for i in range(len(Theta)):                    
    center3 = (Thetarobovi[i+1] + Thetarobovi[i])/2
#    print(Theta[i], center3, sep='\t')
#print('')



#-----------------------------------------------    chi^2
#print(chisquare(Gauss1,hist1))
#print(chisquare(Gauss2,hist2))

#-----------------------------------------------    kolmogorov-smirnov
#print(kstest(hist1, 'norm'))
#print(kstest(hist2, 'norm'))

