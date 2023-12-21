from settings import *
from world import World
from brain import Sensors, Actions
from bacteria import Bacteria, Act, SaveGraph
import numpy as np


world = World(Condition, Bacteria, size = SIZE, population = POPULATION, life_span = LIFE_SPAN)

###### Comment these lines to keep evolving gen.json
reset_data_file("log/gen.json")
world.Spawn(GENE_NUM, NEURON_NUM, len(Sensors), len(Actions), food_coordinates = FOOD_COORDINATES)
world.Save(file = f"log/gen.json")

# Generation loop
for i in range(1, MAX_GEN):
    world.Load(
            file = "log/gen.json", 
            gene_num = GENE_NUM, 
            neuron_num = NEURON_NUM, 
            sensor_num = len(Sensors), 
            action_num = len(Actions),
            food_coordinates = FOOD_COORDINATES
            )

    reset_data_file("log/gen.json")
    for _ in range(LIFE_SPAN):
        world.LifeCycle(Sensors, Actions)

    world.NaturalSelection()
    world.Save(file = f"log/gen.json")


# SaveGraph(world.life_form_list[0])


 
