# ------- GRAPHICS -----------
WIDTH = 600
HEIGHT = 600

# ------- WORLD ------------
SIZE = 100
POPULATION = 200
GENE_NUM = 20
NEURON_NUM = 4
LIFE_SPAN = 150
MAX_GEN = 10
MAX_POPULATION = 300
MUTATION = 0.01

def Condition(bacteria):
    # radius = 15
    # boolean = (bacteria.pos[1] - 50 <= 15) and (bacteria.pos[1] - 50 >= -15) and (bacteria.pos[0] - 50 >= -15) and (bacteria.pos[0] - 50 <= 15)
    boolean = (bacteria.pos[0] >= SIZE - 5)
    return boolean

# ------------ UTILS -----------
import json
import os

def load_data_file(file):
    """ Extract a dictionary from data file """
    with open(file, 'rb') as f:
        if f.read(2) != '[]':
            f.seek(0)  # it may be redundant but it does not hurt
            data = json.load(f)
            return data

def write_data_file(file, data):
    """ Dump the data dictionary to the json file """
    with open(file, 'w') as f:
            json.dump(data, f, indent = 6)

def reset_data_file(file):
    """ Properly format the input file into empty json """
    open(file, 'w').close()
    with open(file, 'w') as f:
            json.dump({}, f, indent = 6)

def printm(matrix, name = ""):
    """ Prints a matrix in a comfortable way """
    print(name)
    for row in matrix: 
        string = ""
        for el in row: 
            if type(el) == float: string += str(round(el,4)) + "\t"
            else: string += str(el) + "\t"
        print(string)
    print()
