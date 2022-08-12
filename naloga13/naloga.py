#!/usr/bin/python3
import numpy as np
import math
import os
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import random
from tensorflow.keras.datasets import mnist
import tensorflow as tf


class NeuralNetwork:
    def __init__(self, network_structure, learning_rate, activation_function, bias=None):
        self.network_structure = network_structure 
        self.learning_rate = learning_rate  
        self.bias = bias
        self.create_weight_matrices()
        self.activation_function = activation_function
        
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
            out_vector = self.activation_function(x)
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

    def run(self, input_vector, dream=False):
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

        if dream == True:
            return app
        return out_vector

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


## Porazdelitev za utezi
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean)/sd, (upp - mean)/sd, loc=mean, scale=sd)

## Definiraj sigmoidno funkcijo - ali exp ali tanh
def sigmoid(x):
    return np.tanh(x)
    ##return 1/(1 + np.e**(-x))
activation_function = sigmoid

## Porazdelitev za utezi
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean)/sd, (upp - mean)/sd, loc=mean, scale=sd)

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
    while(error > 0.01 and N_it <= 300000):
        h_0 = ANN.run1(y_0.T)
        error = np.linalg.norm(h_0[len(h_0)-1]-target_vector)
        app.append(error)
        #print(error)
        delta1 = delta(2, 0, utezi, h_0, target_vector)
        prod = 0.01*np.dot(delta1, utezi[0])
        y_0 += prod.T
        N_it += 1
    return y_0, app
