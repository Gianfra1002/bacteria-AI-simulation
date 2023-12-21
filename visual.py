import pygame
from debug import debug
from settings import *
from graphics import Board
from world import World
from brain import Sensors, Actions
from bacteria import Bacteria, Act
import numpy as np

world = World(Condition, Bacteria, size = SIZE, population = POPULATION, life_span = LIFE_SPAN)
# world.Spawn(GENE_NUM, NEURON_NUM, len(Sensors), len(Actions))
# generation = input("Gen: ")

world.Load(
        file = "log/gen.json", 
        gene_num = GENE_NUM, 
        neuron_num = NEURON_NUM, 
        sensor_num = len(Sensors), 
        action_num = len(Actions),
        food_coordinates=FOOD_COORDINATES
        )

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = Board(matrix = world.map, food_matrix = world.food_map)

i = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()

    screen.fill("black")
    
    board.disp()
    if i < LIFE_SPAN:
        world.LifeCycle(Sensors, Actions)
        board.update(world.map)
    i += 1
    debug(len(world.life_form_list))
    
    pygame.display.update()
    pygame.time.Clock().tick(20)
