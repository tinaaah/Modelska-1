import cv2
import math
import numpy as np
from scipy.signal import gaussian, convolve2d
from numpy.fft import fft2, ifft2, ifftshift

pi = math.pi
def read_pgm(name):
    with open(name) as f:
        lines = f.readlines()
    ## Odstranim zakomentirane vrstice
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    ## Preverim format -- hocem P2:
    assert lines[0].strip() == 'P2'

    ## Podatke pretvorim v listo integerjev:
    data = []
    for line in lines[1_:]:
        data.extend([int(c) for c in line.split()])

    ## Vrne tabelo slike, velikost v x,y smeri in globino sivin
    return (np.array(data[3:]),(data[1],data[0]),data[2])

def gaussovka(mu,sigma,N):
    A = np.ones((N,N))
    for i in range(N):
        for j in range(N):
            A[j][i] =  np.exp((-(i-mu)**2-(j-mu)**2)/(2*sigma**2)) / np.sqrt(2*pi*sigma**2)
def wiener(slika, jedro, N, n=0):
    def erm(ermm):
        if ermm<0: return 0
        else: return ermm
    n = 512
    N = 256

    noise = gaussovka(256, 4, N=n)
    hrup = fft2(ifftshift(noise))

    jedro_abs = np.abs(fft2(jedro))**2
    signal = fft2(slika)

    K = np.abs(hrup)/np.abs(signal)
    phi = jedro_abs/(jedro_abs+K)
    phi = np.vectorize(erm)(phi)
    rez = np.ones((512,512))

    for i in range(512):
        for j in range(512):
            if ((i-256)**2 + (j-256)**2 < 300**2 or (i-256)**2 + (j-256)**2 > 362.5**2):
                rez[i][j] = 0

jedro1 = cv2.imread('lena_slike/kernel1.pgm')
jedro2 = cv2.imread('lena_slike/kernel2.pgm')
jedro3 = cv2.imread('lena_slike/kernel2.pgm')

slika1 = cv2.imread('lena_slike/lena_k1_n0.pgm')
#cisto = wiener(slika1,jedro1,K=0)

