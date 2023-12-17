import random
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np
import math as m
from settings import *
from brain import Sensors, Actions

def Generate_Genetic(gene_num):
    """ Generates a random genetic string of "gene_num" chunks made by 4 hex characters """
    # Hex alphabet
    Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    genetic = ""
    for _ in range(gene_num):
        genetic += "".join([random.choice(Hex) for _ in range(4)]) + " "
    return genetic[:-1] # get rid of the final space

def Convert_hex_to_bin(string):
    """ Convert hex string to properly formatted binary """
    binary = "{0:b}".format(int(string,16))
    diff = 4*len(string) - len(binary) 
    return "0"*diff + binary

def Color(genetic):
    """ Returns a color that encodes the genetic of the bacteria """
    genes = genetic.split(" ")
    mean = sum([int(gene,16) for gene in genes])/len(genes)
    color = "#" + hex(int(mean))[2:] + f"{genes[0][0:2]}"
    return color

def Convert_genetic_to_matrix(genetic, neuron_num, sensor_num, action_num):
    """ 
    The genetic string is made up of N genes, every gene is a 4 hex characters string.
    Each gene is converted to a 16 bits binary string that encodes a single connection between neurons, sensors and actions.
    0th bit:
        0 -> Starting from a Neuron 
        1 -> Starting from a Sensor
    1t bit:
        0 -> Starting from a Neuron 
        1 -> Starting from a Sensor
    bit 2 to 5:
        Chooses which starting Neuron or Sensor
    bit 6 to 9:
        Chooses which ending Neuron or Action
    bit 10 to 16:
        Determines the weight of the connection
    """
    genes = genetic.split(" ")
    
    matrix = [[0 for _ in range(action_num + neuron_num)] for _ in range(sensor_num + neuron_num)]

    for gene in genes:
        binary = Convert_hex_to_bin(gene)
        # print(f"decoding: {binary}")

        if int(binary[0]) == 0:
            row = int(binary[2:6],2) % neuron_num
        else:
            row = int(binary[2:6],2) % sensor_num + neuron_num
        # print(f"row: {row}")

        if int(binary[1]) == 0:
            col = int(binary[6:10],2) % neuron_num
        else:
            col = int(binary[6:10],2) % action_num + neuron_num 
        # print(f"col: {col}")

        matrix[row][col] = int(binary[10:],2)/63
    return matrix

def Convert_matrix_to_graph(matrix,neuron_num, sensor_num, action_num):
    """ Turns the matrix into a properly formatted adjacency matrix and returns the associated graph"""
    array = np.array(matrix)
    # array = np.array([[1 for _ in range(neuron_num + action_num)] for _ in range(neuron_num + sensor_num)])
    for _ in range(sensor_num): array = np.insert(array, neuron_num, 0, axis=1)
    array = np.pad(array, [(0,action_num),(0,0)], mode="constant")

    G = ig.Graph.Weighted_Adjacency(array)
    return G

def SaveGraph(bacteria, file = ""):
    """ Shows the graph on a specified file or simply onscreen """
    G = Convert_matrix_to_graph(bacteria.matrix, bacteria.neuron_num, bacteria.sensor_num, bacteria.action_num)

    vertex_color = []
    vertex_label = []
    for i in range(G.vcount()):
        if i < bacteria.neuron_num:
            vertex_label.append(f"N{i}")
            vertex_color.append("lightblue")
        elif i < bacteria.neuron_num + bacteria.sensor_num: 
            vertex_label.append(f"S{i - bacteria.neuron_num}")
            vertex_color.append("green")
        else: 
            vertex_label.append(f"A{i - bacteria.neuron_num - bacteria.sensor_num}")
            vertex_color.append("red")

    fig, ax = plt.subplots()
    ig.plot(
        G,
        target=ax,
        layout="circle",
        vertex_size=40,
        vertex_label=vertex_label,
        vertex_color=vertex_color,
        # edge_color = ["green" if i>= 0.5 else "red" for i in G.es['weight']],
        edge_color = "lightgreen",
        edge_width = [ i * 5 for i in G.es['weight']],
    )
    plt.title(bacteria.genetic)
    plt.show()


def Cleanup(matrix):
    """ Removes all useless connections, such as neurons not connected to any sensors """
    pass

def sigma(vector, p = 4):
    """ Sigmoid normalization function """
    output = []
    for el in vector:
        y = m.exp(p * el) / (1 + m.exp(p * el))
        output.append(y)
    return output

def Act(bacteria, world, sensors, actions):
    """ 
    The basic action, the sonesor provides some infomration that are elaborated by the neurons and then produce and action 
    """
    S = [sensor(world, bacteria) for sensor in sensors]
    # S = np.array(sensors)
        
    NN = np.transpose(bacteria.NN)
    NA = np.transpose(bacteria.NA)
    SN = np.transpose(bacteria.SN)
    SA = np.transpose(bacteria.SA)
        
    N0 = np.dot(SN,S)
    N = np.dot(NN,sigma(N0))
    A = np.dot(NA,sigma(N)) + np.dot(SA,S)
    A = sigma(A)

    for i in range(len(A)):
        actions[i](A[i] > 0.5, world, bacteria)
    return A

def Reproduce(gene_num, neuron_num, sensor_num, action_num, pos, genetic, mutation):
    Hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

    genetic_list = list(genetic)
    RNG = random.randint(0, 100)
    if RNG < mutation*100:
        while 1:
            index = random.randint(0, len(genetic_list) - 1)
            if genetic_list[index] != " ": 
                genetic_list[index] = random.choice(Hex)
                break
    new_genetic = "".join(genetic_list)
    return Bacteria(gene_num, neuron_num, sensor_num, action_num, pos, genetic = new_genetic)


class Bacteria():
    def __init__(self, gene_num, neuron_num, sensor_num, action_num, pos = [0,0], genetic = ""):
        
        if genetic == "":
            self.genetic = Generate_Genetic(gene_num)
        else:
            self.genetic = genetic

        self.pos = pos
        self.matrix =  np.array(Convert_genetic_to_matrix(self.genetic, neuron_num, sensor_num, action_num))

        self.color = Color(self.genetic)

        self.NN = self.matrix[:neuron_num, :neuron_num]
        self.NA = self.matrix[:neuron_num, neuron_num:]
        self.SN = self.matrix[neuron_num:, :neuron_num]
        self.SA = self.matrix[neuron_num:, neuron_num:]
        
        self.neuron_num = neuron_num
        self.sensor_num = sensor_num
        self.action_num = action_num


# GENE_NUM = 15
# NEURON_NUM = 3
# SENSON_NUM = 3 # length of future sensor vector
# ACTION_NUM = 3 # length of future action vector

# bact1 = Bacteria(GENE_NUM, NEURON_NUM, SENSON_NUM, ACTION_NUM, [0,0])

# print(type(bact1))

# print(Color(bact1.genetic))

# SaveGraph(bact1)

# data = load_data_file("log/gen.json")
# bact = Bacteria(GENE_NUM, NEURON_NUM, len(Sensors), len(Actions), genetic = data["bact0"])
# SaveGraph(bact)




