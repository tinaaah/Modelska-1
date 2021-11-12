from PIL import Image
import numpy as np
from matplotlib import cm
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.signal import gaussian
 
plt.close("all")

pi = np.pi

def readpgm(name):
    with open(name) as f:
        lines = f.readlines()

    ## Ignorira komentarje:
    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    ## Preverim, da je tak format ki ga rabim -- P2
    assert lines[0].strip() == 'P2' 

    ## Pretvori v integer listo
    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])

    return (np.array(data[3:]),(data[1],data[0]),data[2])

def wienerlena(x,kernel, N, sigma, n=0):
    def erm(ermm):
        if ermm<0:
            return 0
        else:
            return ermm
    n = 512
    N = 100
    #sigma = 16
    noise = np.outer(gaussian(512, sigma**2), gaussian(512, sigma**2))

    plt.figure(5)
    #plt.imshow(noise)

    noise = np.fft.fft2(np.fft.ifftshift(noise))
    kernel_abs = np.abs(np.fft.fft2(kernel))**2
    signal_abs = np.fft.fft2(x)

    daj = np.abs(noise)/np.abs(signal_abs)
    daj = daj
    phi = kernel_abs/(kernel_abs+daj)
    #phi = np.ones(512)
    phi = np.vectorize(erm)(phi)

    #aux = [1 for i in range(N)] + [0 for i in range(n-2*N)] + [1 for i in range(N)]
    aux = np.ones((512, 512))

    for i in range(n):
        for j in range(n):
            if((i-N)**2+(j-N)**2<300**2 or (i-N)**2+(j-N)**2>362.5**2):
                aux[i][j] = 0
                
    plt.figure(4)
    plt.imshow(aux)
    
    #aux = [aux for i in range(512)]
    #fi =np.ones(512, 512)#*np.asarray(aux
    phi = aux*phi
    dummy = np.fft.fft2(x)
    kernel = np.fft.fft2(kernel)
    dummy = dummy/ kernel
    #dummy = dummy[30:482, 30:482]
    dummy2 = np.abs(dummy)
    dummy2 = np.log(dummy2)
    plt.figure(3)
    #plt.imshow(dummy2)
    #plt.title("Absolutna vrednost v k prostoru, k2")
    #plt.savefig("proba_log_fft_k2_2.pdf")
    dummy = np.abs(np.fft.ifft2(dummy))
    #plt.figure(3)
    #plt.imshow(dummy, "gray")
    return dummy

def wienerlena1(signal, kernel, N, sigma, n=0):
    def erm(ermm):
        if ermm<0:
            return 0
        else:
            return ermm
    n = 256
    N = 250
    noise = gaussovka1(128, sigma)
    noise = np.fft.fft2(noise)
    kernel_abs = np.abs(np.fft.fft2(kernel))**2
    signal_abs = np.fft.fft2(signal)
    #noise = np.ones((512, 512))*np.sum(signal_abs[100:200])/100
    daj = np.abs(noise/(signal_abs-noise))
    phi = kernel_abs/(kernel_abs+daj)
    phi = np.vectorize(erm)(phi)
    #sumcek = np.abs(np.fft.fft(gaussovka(np.arange(0, 512, 1), 256, 0)))#np.ones(x.size)*np.sum(spektr[100:200])/100
    #signal = np.vectorize(erm)(signal)
    aux = [1 for i in range(N)] + [0 for i in range(n-2*N)] + [1 for i in range(N)]
    aux = [aux for i in range(256)]
    #fi =np.ones(512, 512)#*np.asarray(aux
    phi = aux*phi
    dummy = np.fft.fft2(signal)
    kernel = np.fft.fft2(kernel)
    dummy = dummy*aux/ kernel
    dummy = np.abs(np.fft.ifft2(dummy))
    return dummy

def transformiraj2(signal,kernel, n,N=60):
    def uredi(xx):
        if np.real(xx)>255:
            return 255
        elif np.real(xx)<0:
            return 0
        else:
            return np.real(xx)
    y = wienerlena(signal,kernel, N,sigma,n)
    print(2)
    return np.vectorize(uredi)(y)
def gaussovka(mu,sigma):
    A = np.ones((512, 512))
    for i in range(512):
        for j in range(512):
            A[j][i] = 1/np.sqrt(2*pi*sigma**2) * np.exp(-(i-mu)**2/(2*sigma**2))#-(j-mu)**2/(2*sigma**2))
    plt.figure(2)
    plt.imshow(A)
    return A
def gaussovka1(mu,sigma):
    A = np.ones((256, 256))
    for i in range(256):
        for j in range(256):
            A[j][i] = 1/np.sqrt(2*pi*sigma**2) * np.exp(-(i-mu)**2/(2*sigma**2))#-(j-mu)**2/(2*sigma**2))
    plt.figure(2)
    plt.imshow(A)
    return A
def skonvuliraj(x,sigma): 
    N = x.size
    #k = N/2/(sigma)
    iksi = np.array(range(N))
    def pravagaussovka(x):
        if x<=N/2:
            return gaussovka(N/2+x,N/2,sigma)
        elif x>N/2:
            return gaussovka(x-N/2,N/2,sigma)
    def pravagama(x):
        if x<=N/2:
            return gama(N/2+x,k,sigma)
        elif x>N/2:
            return gama(x-N/2,k,sigma)
    #gaussi = np.fft.fft(np.vectorize(pravagama)(iksi))        
    gaussi = np.fft.fft(np.vectorize(pravagaussovka)(iksi))
    #gaussi = np.fft.fft(gaussovka(iksi,mu,sigma))
    return np.real(np.fft.ifft(np.fft.fft(x)*gaussi))
def zgladi(x,sigma):    
    transformiranka = np.apply_along_axis(skonvuliraj,0,x,sigma)
    transformiranka2 = np.apply_along_axis(skonvuliraj,1,transformiranka,sigma)
    return transformiranka2

if 1:
    data = readpgm("lena_slike/lena_k2_n16.pgm")
    sigma = 16
    slika = np.reshape(data[0],data[1])
    N = data[1][1]
    n = data[1][0]
    data1 = readpgm("lena_slike/kernel1.pgm")
    kernel1 = np.reshape(data1[0],data1[1])
    N1 = data[1][1]
    n1 = data[1][0]

    if 0:
        array = [0, 4, 8, 16]
        for i in array:
            data = readpgm("lena_slike/lena_k2_n%d.pgm" %i)
            slika = np.reshape(data[0],data[1])
            signal = slika[1:512, 256]
            plt.plot(spekter(signal)[0],spekter(signal)[1], label = "RMS = %d" %i)
        data = readpgm("lena_slike/lena_k2_nx.pgm")
        slika = np.reshape(data[0],data[1])
        signal = slika[0:512, 256]
        plt.plot(spekter(signal)[0],spekter(signal)[1], label = "Periodična motnja")
        plt.yscale("log")
        #plt.xscale("log")
        plt.xlabel("Frekvenca")
        plt.ylabel("|P|")
        plt.legend()
        plt.title("Frekvenčni spekter na stolpcu na robu slike, k2")
        plt.savefig("proba1.pdf")
        
    if 1:
        a = transformiraj2(slika, kernel1, n,sigma)
        b = np.amax(a)
        a = a/b
        d = []

        m = 256
        lol = np.ones((m,m))
        for i in range(m):
            for j in range(m):
                lol[i][j] = a[i+m][j+m]
        lol2 = np.ones((m,m))
        for i in range(m):
            for j in range(m):
                lol2[i][j] = a[i+m][j]
        lol3 = np.ones((m,m))
        for i in range(m):
            for j in range(m):
                lol3[i][j] = a[i][j+m]
        lol4 = np.ones((m,m))
        for i in range(m):
            for j in range(m):
                lol4[i][j] = a[i][j]
        V1 = np.concatenate((lol, lol3))
        V2 = np.concatenate((lol2, lol4))
        V = np.concatenate((V1, V2), 1)
        #V = V[80:420, 100:400]
        b = np.amax(V)
        V = V/b
        #V2 = np.transpose(V2)
        plt.figure(1)
        plt.imshow(V, "gray")
        plt.axis("off")
        plt.savefig("ociscena_lena_k2_n16.pdf")
    if 0:
        slika = slika[128:512-128, 128:512-128]
        kernel1 = kernel1[128:512-128, 128:512-128]
        a = transformiraj2(slika, kernel1, n,sigma)
        b = np.amax(a)
        a = a/b
        d = []
        lol = np.ones((128,128))
        for i in range(128):
            for j in range(128):
                lol[i][j] = a[i+128][j+128]
        lol2 = np.ones((128,128))
        for i in range(128):
            for j in range(128):
                lol2[i][j] = a[i+128][j]
        lol3 = np.ones((128,128))
        for i in range(128):
            for j in range(128):
                lol3[i][j] = a[i][j+128]
        lol4 = np.ones((128,128))
        for i in range(128):
            for j in range(128):
                lol4[i][j] = a[i][j]
        V1 = np.concatenate((lol, lol3))
        V2 = np.concatenate((lol2, lol4))
        V = np.concatenate((V1, V2), 1)
        #V = V[80:420, 100:400]
        b = np.amax(V)
        V = V/b
        #V2 = np.transpose(V2)
        plt.figure(1)
        plt.imshow(V, "gray")
        plt.axis("off")
        plt.savefig("ociscena-k1-nx.pdf")  
