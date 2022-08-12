#!/usr/bin/python3
import numpy as np
import math
import os
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import random

## Ignoriraj error, da nimam graficne
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.keras.datasets import mnist
import tensorflow as tf

## Zloadaj podatke
# (train_slika, train_oznaka), (test_slika, test_oznaka) = mnist.load_data()
# slike_za_konec = train_slika

"""
## Display Nth element from the training set and its label
element = 4303
plt.imshow(train_slika[element], cmap='gray_r')
plt.savefig("element4303.png")
print("Oznaka slike:", train_oznaka[element])
"""

## Preoblikuj in normiraj podatke
# train_slika = np.asfarray(train_slika.reshape((-1,784))) /255 
# test_slika = np.asfarray(test_slika.reshape((-1,784))) /255 
# train_oznaka = np.asfarray(train_oznaka)
# test_oznaka = np.asfarray(test_oznaka)

"""
print("#Stevilo posameznih stevk v trening setu")
for i in range(10):
    print(i,np.sum(train_oznaka==i),sep='\t')
print("")
print("#Stevilo posameznih stevk v test setu")
for i in range(10):
    print(i,np.sum(test_oznaka==i),sep='\t')
"""

## Transformiraj oznake v one-hot reprezentacijo
# train_onehot = tf.one_hot(train_oznaka, depth=10)
# test_onehot = tf.one_hot(test_oznaka, depth=10)

## Definiraj sigmoidno funkcijo - ali exp ali tanh
def sigmoid(x):
    return np.tanh(x)
    ##return 1/(1 + np.e**(-x))
# activation_function = sigmoid

## Porazdelitev za utezi
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean)/sd, (upp - mean)/sd, loc=mean, scale=sd)

class NeuralNetwork:
   
    def __init__(self, network_structure, learning_rate, bias=None):
        self.network_structure = network_structure 
        self.learning_rate = learning_rate  
        self.bias = bias
        self.create_weight_matrices()
        
    def create_weight_matrices(self):
        X = truncated_normal(mean=0, sd=1, low=-0.5, upp=0.5) 

        bias_node = 1 if self.bias else 0
        self.weights_matrices = []
        layer_index = 1
        no_of_layers = len(self.network_structure)

        while layer_index < no_of_layers:
            nodes_in = self.network_structure[layer_index-1]
            nodes_out = self.network_structure[layer_index]

            n = (nodes_in + bias_node) * nodes_out
            rad = 1/np.sqrt(nodes_in)

            X = truncated_normal(mean=2, sd=1, low=-rad, upp=rad)
            current_weights = X.rvs(n).reshape((nodes_out, nodes_in + bias_node))
            self.weights_matrices.append(current_weights)
            layer_index += 1
    
    def train_single(self, input_vector, target_vector):
        ## Mnozim vsak i+output layer vektorje z matrikami utezi
        no_of_layers = len(self.network_structure)
        input_vector = np.array(input_vector, ndmin=2).T

        layer_index = 0

        ## Izhodni/vhodni vektor prejsnje plasti:
        res_vectors = [input_vector]
        while layer_index < no_of_layers - 1:
            in_vector = res_vectors[-1]
            x = np.dot(self.weights_matrices[layer_index], in_vector)
            out_vector = activation_function(x)
            res_vectors.append(out_vector)
            layer_index += 1

        layer_index = no_of_layers - 1
        target_vector = np.array(target_vector, ndmin=2).T

        ## Vhodni vektor plasti:
        output_errors = target_vector - out_vector
        self.output_errors_arr.append(1/2 * np.linalg.norm(output_errors)**2)

        while layer_index > 0:
            out_vector = res_vectors[layer_index]
            in_vector = res_vectors[layer_index-1]
            tmp = output_errors*(1 - out_vector**2) ## Za tanh
            #tmp = output_errors *out_vector* (1.0 - out_vector) ## Za sigma
            tmp = np.dot(tmp, in_vector.T)


            self.weights_matrices[layer_index-1] += self.learning_rate * tmp
            output_errors = np.dot(self.weights_matrices[layer_index-1].T,output_errors)

            layer_index -= 1

    def train(self, data_array, labels_one_hot_array, epochs=1, intermediate_results=False):
        self.output_errors_arr = []
        for epoch in range(epochs):
            for i in range(len(data_array)):
                self.train_single(data_array[i], labels_one_hot_array[i])
        return self.weights_matrices, self.output_errors_arr

    def run(self, input_vector):
        ## input vector rabi bit stolpec
        no_of_layers = len(self.network_structure)
        in_vector = np.array(input_vector, ndmin=2).T
        app = []
        app.append(in_vector)
        layer_index = 1

        ## Input vektorji vseh plasti:
        while layer_index < no_of_layers:
            x = np.dot(self.weights_matrices[layer_index-1], in_vector)
            out_vector = activation_function(x)
            app.append(out_vector)

            ## Input vektor naslednje plasti:
            in_vector = out_vector
            layer_index += 1
        return out_vector

    def run1(self,input_vector):
        ## input vector rabi bit stolpec
        no_of_layers = len(self.network_structure)
        in_vector = np.array(input_vector, ndmin=2).T
        app = []
        app.append(in_vector)
        layer_index = 1

        ## Input vektorji vseh plasti:
        while layer_index < no_of_layers:
            x = np.dot(self.weights_matrices[layer_index-1], in_vector)
            out_vector = activation_function(x)
            app.append(out_vector)

            ## Input vektor naslednje plasti:
            in_vector = out_vector
            layer_index += 1
        return app

    def evaluate(self, data, labels):
        ## Presteje kolikokrat je rezultat enak tistemu, ki ga zelimo. Rezultat je pravilen,
        ## ce je indeks maksimalne vrednosti enak indeksu z "1" v one_hot reprezentaciji
        corrects, wrongs = 0,0
        napake_prav = []
        napake_ugib = []
        prava = []
        vse = []
        for i in range(len(data)):
            res = self.run(data[i])
            res_max = res.argmax()
            if res_max == labels[i]:
                corrects += 1
                prava.append(res_max)
                vse.append(res_max)
            else:
                wrongs += 1
                napake_prav.append(i)
                napake_ugib.append(res_max)
                vse.append(res_max)
        return corrects, wrongs, napake_prav, napake_ugib, prava, vse
    
def delta(N, l, W, y, target_vector):
    if l== N-1:
        ops =  -(y[l+1]-target_vector)
        konst = ops
        #bobs = activation_function(np.dot(W[N-1],y[N-1]))*(1-activation_function(np.dot(W[N-1],y[N-1])))
        bobs = (1-activation_function(np.dot(W[l],y[l]))**2)
        konst =  np.multiply(ops,bobs[0])
        konst = np.reshape(konst, (10, 1))
        return konst
    else:
        #print(len(np.dot(W[0],y[0])[0]))
        #return np.multiply(np.dot(delta(N, l+1, W, y, target_vector).T,W[l+1]),np.transpose(activation_function(np.dot(W[l], y[l]))*(1-activation_function(np.dot(W[l], y[l])))))
        return np.multiply(np.dot(delta(N, l+1, W, y, target_vector).T,W[l+1]),np.transpose(1-activation_function(np.dot(W[l], y[l]))**2))

def deep_Dream(y_0, target_vector):
    error = 5
    N_it = 1
    app = []
    while(error>0.01 and N_it <= 300000):
        h_0 = ANN.run1(y_0.T)
        error = np.linalg.norm(h_0[len(h_0)-1]-target_vector)
        app.append(error)
        #print(error)
        delta1 = delta(2, 0, utezi, h_0, target_vector)
        prod = 0.01*np.dot(delta1, utezi[0])
        y_0 += prod.T
        N_it += 1
    return y_0, app

if main():
    if 0: ## Deep dream
        oblika = [784, 50, 10]
        ANN = NeuralNetwork(network_structure = oblika, learning_rate = 0.01, bias=None)
        utezi, out = ANN.train(train_slika, train_onehot, epochs=3, intermediate_results=False)

        y_0 = np.ones((784, 1))
        img = y_0.reshape((28,28))
        #plt.figure(3)
        #plt.imshow(img, vmin=0, vmax=1, cmap="Greys")
        #plt.show()
        y_0, h_0 = deep_Dream(np.reshape(y_0, (784,1)), np.reshape(test_onehot[18], (10, 1)))
        for i in range(len(h_0)):
            print(i, h_0[i], sep='\t')
        #plt.plot(h_0, "k--")
        #plt.xlabel("Število iteracij")
        #plt.ylabel("Norma napake")
        #plt.grid()
        #plt.savefig("proba.png")
        #print("I'm here")
        #plt.show()

    if 0: ## Samo enkrat ponovim racunanje
        oblika = [784, 28, 10]
        ANN = NeuralNetwork(network_structure = oblika, learning_rate = 0.01, bias=None)
        utezi, out = ANN.train(train_slika, train_onehot, epochs=3, intermediate_results=False)
        print(out[0:20])
        print(len(out))

        corrects, wrongs, napake_prav, napake_ugib, prava, vse = ANN.evaluate(train_slika, train_oznaka)
        if 0: ## Preverim natancnost testov in naredim histogram zadetih stevk
            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)
            print("#Oblika matrike:", oblika)
            print("#Natančnost treninga:", corrects / ( corrects + wrongs))
            print("#Faljene in zadete številke treninga:")
            for i in range(10):
                print(i,napake_ugib.count(i),prava.count(i),sep='\t')
            print("")

            corrects, wrongs,napake_prav, napake_ugib, prava = ANN.evaluate(test_slika, test_oznaka)
            print("Natančnost testa: ", corrects / ( corrects + wrongs))
            print("#Faljene in zadete številke testa:")
            for i in range(10):
                print(i,napake_ugib.count(i),prava.count(i),sep='\t')
        if 0: ## Faljene stevke narisem in shranim
            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)

            ## Display random element from the failed set and its label
            indeks = random.randint(0, len(napake_prav)-1)
            element = napake_prav[indeks]
            plt.imshow(slike_za_konec[element], cmap='gray_r')
            plt.savefig("faljena.png")
            print("Oznaka slike:", train_oznaka[element])
            print("Kaj misli mreža, da je:", napake_ugib[indeks])

    if 0: ## Heatmap zadetkov
        oblika = [784, 50, 10]
        ANN = NeuralNetwork(network_structure = oblika, learning_rate = 0.01, bias=None)
        utezi, out = ANN.train(train_slika, train_onehot, epochs=5, intermediate_results=False)
        corrects, wrongs, napake_prav, napake_ugib, prava, vse = ANN.evaluate(train_slika, train_oznaka)

        matrika = np.zeros((10,10), dtype='int')
        for i in range(len(vse)):
            I = int(vse[i])
            J = int(train_oznaka[i])
            matrika[I,J] += 1
        print(matrika)
        for i in range(10):
            for j in range(10):
                print(matrika[i,j], end='\t')
            print("")

    if 0: ## Spreminjam velikost skritega sloja in spremljam natancnost
        oblika = np.array([ [784, 10, 10],
                            [784, 20, 10],
                            [784, 30, 10],
                            [784, 40, 10],
                            [784, 50, 10],
                            [784, 60, 10],
                            [784, 70, 10],
                            [784, 80, 10],
                            [784, 90, 10],
                            [784, 100, 10],
                            [784, 200, 10],
                            [784, 400, 10],
                            [784, 784, 10] ])
        print("## Oblika matrike    Natančnost treninga     Natančnost testa")
        for dimenzija in oblika:
            ANN = NeuralNetwork(network_structure = dimenzija, learning_rate = 0.01, bias=None)
            utezi, out = ANN.train(train_slika, train_onehot, epochs=3, intermediate_results=False)

            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)
            print(dimenzija, corrects / ( corrects + wrongs), sep='\t', end='\t')

            corrects, wrongs,napake_prav, napake_ugib, prava = ANN.evaluate(test_slika, test_oznaka)
            print(corrects / ( corrects + wrongs))

    if 0: ## Spreminjam hitrost ucenja
        dimenzija = [784, 28, 10]
        eks = np.arange(-4,2)
        #eta = math.pow(10,n)
        eks = [ 1e-6, 2*1e-6, 5*1e-6,
                1e-5, 2*1e-5, 5*1e-5,
                1e-4, 2*1e-4, 5*1e-4,
                1e-3, 2*1e-3, 5*1e-3,
                1e-2, 2*1e-2, 5*1e-2,
                1e-1, 2*1e-1, 5*1e-1,
                1, 2, 5,
                10, 20, 50, 100]

        print("## Hitrost   Natančnost treninga     Natančnost testa")
        for n in eks:
            eta = n
            ANN = NeuralNetwork(network_structure = dimenzija, learning_rate = eta, bias=None)
            utezi, out = ANN.train(train_slika, train_onehot, epochs=3, intermediate_results=False)

            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)
            print(eta, corrects / ( corrects + wrongs), sep='\t', end='\t')

            corrects, wrongs,napake_prav, napake_ugib, prava = ANN.evaluate(test_slika, test_oznaka)
            print(corrects / ( corrects + wrongs))

    if 0: ## Spreminjam stevilo epoh
        dimenzija = [784, 50, 10]
        eta = 0.01

        plasti = np.arange(1,21)
        ANN = NeuralNetwork(network_structure = dimenzija, learning_rate = eta, bias=None)
        print("## St. epoh  Natančnost treninga     Natančnost testa")
        for n in plasti:
            utezi, out = ANN.train(train_slika, train_onehot, epochs=n, intermediate_results=False)

            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)
            print(n, corrects / ( corrects + wrongs), sep='\t', end='\t')

            corrects, wrongs,napake_prav, napake_ugib, prava = ANN.evaluate(test_slika, test_oznaka)
            print(corrects / ( corrects + wrongs))

    if 0: ## Spreminjam stevilo skritih plasti
        oblika = np.array([ [784, 50, 10],
                            [784, 50, 50, 10],
                            [784, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 50, 50, 50, 50, 10],
                            [784, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 10] ], dtype='object')
        print("## St. plasti    Natančnost treninga     Natančnost testa")
        for dimenzija in oblika:
            ANN = NeuralNetwork(network_structure = dimenzija, learning_rate = 0.01, bias=None)
            utezi, out = ANN.train(train_slika, train_onehot, epochs=3, intermediate_results=False)

            corrects, wrongs, napake_prav, napake_ugib, prava = ANN.evaluate(train_slika, train_oznaka)
            print(len(dimenzija)-2, corrects / ( corrects + wrongs), sep='\t', end='\t')

            corrects, wrongs,napake_prav, napake_ugib, prava = ANN.evaluate(test_slika, test_oznaka)
            print(corrects / ( corrects + wrongs))

    if 0: ## Racunam napake za razlicne parametre
        oblika = [784, 50, 10]
        eks = [ 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1 ]

        if 1:
            for eta in eks:
                ANN = NeuralNetwork(network_structure = oblika, learning_rate = eta, bias=None)
                utezi, out = ANN.train(train_slika, train_onehot, epochs=1, intermediate_results=False)
                print("## Learning rate =", eta)
                print("## Povprecje 1000ih zaporednih tock   \Delta E")
                dolzina = int(len(out)/1000)
                for i in range(dolzina):
                    print(i, np.average(out[i*1000:(i+1)*1000]), sep="\t")
                print("")
