# ------- GRAPHICS -----------
WIDTH = 600
HEIGHT = 600

# ------- WORLD ------------
SIZE = 100
POPULATION = 500
GENE_NUM = 40
NEURON_NUM = 20
LIFE_SPAN = 150
MAX_GEN = 20
MAX_POPULATION = 300
MUTATION = 0.1

# Food settings
# FOOD = 1000
FOOD_COORDINATES = [[i,j] for i in range(40,60) for j in range(40,60)]
# FOOD_COORDINATES = [[i,j] for i in range(SIZE - 10,SIZE) for j in range(0,SIZE)]

# Natural selection condition
def Condition(bacteria):
    # Center condition
    boolean = (bacteria.pos[1] <= 60) and (bacteria.pos[1] >= 40) and (bacteria.pos[0] >= 40) and (bacteria.pos[0] <= 60)
    
    # Border condition
    # boolean = (bacteria.pos[0] >= SIZE - 5)

    # Food condition
    # boolean = bacteria.food
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
