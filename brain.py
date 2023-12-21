import random
from settings import *

# -------------------- SENSORS -------------------------
def DetectNorthBlock(world, bacteria):
    """ Detect North: is True if North is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0] - 1][pos[1]] != 0)

def DetectSouthBlock(world, bacteria):
    """ Detect South: is True if South is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0] + 1][pos[1]] != 0)

def DetectWestBlock(world, bacteria):
    """ Detect West: is True if West is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0]][pos[1] - 1] != 0)

def DetectEastBlock(world, bacteria):
    """ Detect East: is True if East is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0]][pos[1] + 1] != 0)

def DetectFoodNorth(world, bacteria):
    """ Detect Food North: is True if there is food North """
    pos = bacteria.pos
    return (world.food_map[pos[0] - 1][pos[1]] == "f")

def DetectFoodSouth(world, bacteria):
    """ Detect South: is True if there is food South """
    pos = bacteria.pos
    return (world.food_map[pos[0] + 1][pos[1]] == "f")

def DetectFoodWest(world, bacteria):
    """ Detect West: is True if there is food West """
    pos = bacteria.pos
    return (world.food_map[pos[0]][pos[1] - 1] == "f")

def DetectFoodEast(world, bacteria):
    """ Detect East: is True if there is food East """
    pos = bacteria.pos
    return (world.food_map[pos[0]][pos[1] + 1] == "f")

# def DetectLifeForms(world, bacteria):
#     """ Detect Life forms nearby """
#     living_num = int(DW(world, bacteria)) + int(DE(world, bacteria)) + int(DN(world, bacteria)) + int(DS(world, bacteria))
#     return living_num/4

def HorizontalPosition(world, bacteria):
    """ Horizontal Position: is a number between 0 and 1 rapresenting the distance from the west border """
    pos = bacteria.pos[0]
    return pos/SIZE

def VerticalPosition(world, bacteria):
    """ Vertical Position: is a number between 0 and 1 rapresenting the distance from the north border """
    pos = bacteria.pos[1]
    return pos/SIZE


# -------------------- ACTIONS -------------------------
def MoveNorth(action, world, bacteria):
    """ Move North """
    if action:
        pos = [bacteria.pos[0] - 1, bacteria.pos[1]]
        world.Dispose(bacteria, pos)

def MoveSouth(action, world, bacteria):
    """ Move South """
    if action:
        pos = [bacteria.pos[0] + 1, bacteria.pos[1]]
        world.Dispose(bacteria, pos)

def MoveWest(action, world, bacteria):
    """ Move West """
    if action:
        pos = [bacteria.pos[0], bacteria.pos[1] - 1]
        world.Dispose(bacteria, pos)

def MoveEast(action, world, bacteria):
    """ Move East """
    if action:
        pos = [bacteria.pos[0], bacteria.pos[1] + 1]
        world.Dispose(bacteria, pos)

def MoveRandom(action, world, bacteria):
    """ Move Random """
    if action:
        delta = [random.randint(-1, 1), random.randint(-1, 1)]
        pos = [bacteria.pos[0] + delta[0], bacteria.pos[1] + delta[1]]
        world.Dispose(bacteria, pos)

def Eat(action, world, bacteria):
    """ Eat food if on the same tile """
    if True:
        pos = bacteria.pos
        if world.food_map[pos[0]][pos[1]] == "f" and (not bacteria.food):
            world.food_map[pos[0]][pos[1]] = 0
            bacteria.food = True

def Kill(action, world, bacteria):
    """ Kill """
    pass

# -------------------- LISTS -------------------------
Sensors = [
        DetectNorthBlock,
        DetectSouthBlock,
        DetectWestBlock,
        DetectEastBlock,
        DetectFoodNorth,
        DetectFoodSouth,
        DetectFoodWest,
        DetectFoodEast,
        HorizontalPosition,
        VerticalPosition,
        ]
Actions = [
        MoveNorth, 
        MoveSouth, 
        MoveWest, 
        MoveEast, 
        MoveRandom, 
        Eat]
