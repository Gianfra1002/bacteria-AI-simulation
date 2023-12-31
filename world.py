from bacteria import Bacteria, Act, Reproduce
from brain import Sensors, Actions
from settings import *
import random
import json

class World():
    def __init__(self, Condition, Bacteria, size = 8, population = 1, life_span = 300):
        """ 
        The world class that will host the living forms. 
        It stores all the informations about the living forms.
        """
        self.map = [
                [1 for _ in range(size)] if (col==0 or col==size-1) else [1 if (row==0 or row==size-1) else 0 for row in range(size)] for col in range(size)]
        self.food_map = [
                [1 for _ in range(size)] if (col==0 or col==size-1) else [1 if (row==0 or row==size-1) else 0 for row in range(size)] for col in range(size)]
        self.population = population
        self.life_form_list = []
        self.condition = Condition

    def NaturalSelection(self):
        """ The module that selects who wil reproduce """
        new_list = []
        for life_form in self.life_form_list:
            if self.condition(life_form): 
                new_list.append(life_form)
        self.life_form_list = new_list

    def MakeFood(self, coordinates = []):
        """ Spawn food on certain tiles """
        # Initialize food matrix, all the food left from previus generetions is deleted
        size = len(self.food_map)
        self.food_map = [
                [1 for _ in range(size)] if (col==0 or col==size-1) else [1 if (row==0 or row==size-1) else 0 for row in range(size)] for col in range(size)]

        # Fill the matrix according to given coordinates or random
        if len(coordinates) != 0:
            for i in range(len(coordinates)):
                pos = coordinates[i]
                self.food_map[pos[0]][pos[1]] = "f"
        else:
            i = 0
            while i < FOOD:
                pos = [random.randint(0, len(self.food_map) - 1), random.randint(0, len(self.food_map) - 1)]
                if self.food_map[pos[0]][pos[1]] == 0:
                    self.food_map[pos[0]][pos[1]] = "f"
                    i+=1

    def Spawn(self, gene_num, neuron_num, sensor_num, action_num, food_coordinates = []):
        """ The function that starts the simulation by populating the world with random creatures """
        self.MakeFood(food_coordinates)
        for _ in range(self.population):
            while 1:
                pos = [random.randint(0, len(self.map) - 1), random.randint(0, len(self.map) - 1)]
                if self.map[pos[0]][pos[1]] == 0: break
            bacteria = Bacteria(gene_num, neuron_num, sensor_num, action_num, pos)
            self.life_form_list.append(bacteria)
            self.Dispose(bacteria, pos)
            # self.MakeFood([[1,1], [2,2], [3,3]])

    def Dispose(self, bacteria, pos):
        """ 
        The function that places a bacteria to the correct position, if possibile. 
        For now it's void, maybe it will become boolean.
        """
        if self.map[pos[0]][pos[1]] == 0:
            self.map[bacteria.pos[0]][bacteria.pos[1]] = 0
            self.map[pos[0]][pos[1]] = bacteria
            bacteria.pos = pos

    def LifeCycle(self, sensors, actions):
        """ Every bacteria does one Act """
        for bacteria in self.life_form_list:
            Act(bacteria, self, sensors, actions)

    def Save(self, file):
        """ Saves a genetic backup to an external .json file """
        generation = {}
        maximum = min(len(self.life_form_list), MAX_POPULATION)
        for i in range(maximum):
            bact = self.life_form_list[i]
            generation[f"bact{i}"] = bact.genetic
        write_data_file(file, data=generation)
        

    def Load(self, gene_num, neuron_num, sensor_num, action_num, file, food_coordinates = []):
        """ Loads the generation data from the json file and generates new bacteria with that genetic """
        data = load_data_file(file) # The data dictionary
        size = len(data)
        if len(data):
            self.MakeFood(food_coordinates)
            for i in range(size):
                while 1:
                    pos = [random.randint(0, len(self.map) - 1), random.randint(0, len(self.map) - 1)]
                    if self.map[pos[0]][pos[1]] == 0: break

                bacteria = Reproduce(
                            gene_num, 
                            neuron_num, 
                            sensor_num, 
                            action_num, 
                            pos, 
                            genetic = data[f"bact{i}"], 
                            mutation = MUTATION
                            )
                self.life_form_list.append(bacteria)
                self.Dispose(bacteria, pos)
        else:
            # self.Spawn(gene_num, neuron_num, sensor_num, action_num)
            print("No one survived")

        # delta = len(data) - self.population         
        # while delta < 0:
        #     while 1:
        #         pos = [random.randint(0, len(self.map) - 1), random.randint(0, len(self.map) - 1)]
        #         if self.map[pos[0]][pos[1]] == 0: break
        #     bacteria = Bacteria(                            
        #                     gene_num, 
        #                     neuron_num, 
        #                     sensor_num, 
        #                     action_num, 
        #                     pos 
        #                     )
        #     self.life_form_list.append(bacteria)
        #     self.Dispose(bacteria, pos)
        #     delta += 1




# GENE_NUM = 20
# NEURON_NUM = 4
# SENSON_NUM = len(Sensors)
# ACTION_NUM = len(Actions) 
# w = World(Condition, Bacteria, population=10)

# printm(w.food_map)
# w.Spawn(GENE_NUM, NEURON_NUM, SENSON_NUM, ACTION_NUM)
# printm(w.food_map)


# # print(w.life_form_list)


