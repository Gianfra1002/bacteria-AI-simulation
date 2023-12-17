from settings import *
from world import World
from brain import Sensors, Actions
from bacteria import Bacteria, Act, SaveGraph
import numpy as np

reset_data_file("log/gen.json")
world = World(Condition, Bacteria, size = SIZE, population = POPULATION, life_span = LIFE_SPAN)
# world.Spawn(GENE_NUM, NEURON_NUM, len(Sensors), len(Actions))

for i in range(1, MAX_GEN):
    world.Load(
            file = "log/gen.json", 
            gene_num = GENE_NUM, 
            neuron_num = NEURON_NUM, 
            sensor_num = len(Sensors), 
            action_num = len(Actions)
            )

    reset_data_file("log/gen.json")
    for _ in range(LIFE_SPAN):
        world.LifeCycle(Sensors, Actions)

    world.NaturalSelection()
    world.Save(file = f"log/gen.json")


# SaveGraph(world.life_form_list[0])


 
