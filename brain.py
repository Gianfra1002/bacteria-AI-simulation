import random
# -------------------- SENSORS -------------------------
def DN(world, bacteria):
    """ Detect North: is True if North is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0] - 1][pos[1]] != 0)

def DS(world, bacteria):
    """ Detect South: is True if South is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0] + 1][pos[1]] != 0)

def DW(world, bacteria):
    """ Detect West: is True if West is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0]][pos[1] - 1] != 0)

def DE(world, bacteria):
    """ Detect East: is True if East is blocked, else its False """
    pos = bacteria.pos
    return (world.map[pos[0]][pos[1] + 1] != 0)

def DL(world, bacteria):
    """ Detect Life forms nearby """
    living_num = int(DW(world, bacteria)) + int(DE(world, bacteria)) + int(DN(world, bacteria)) + int(DS(world, bacteria))
    return living_num/4

def DM(world, bacteria):
    """ Detect Movement nearby """
    pass

# -------------------- ACTIONS -------------------------
def MN(action, world, bacteria):
    """ Move North """
    if action:
        pos = [bacteria.pos[0] - 1, bacteria.pos[1]]
        world.Dispose(bacteria, pos)

def MS(action, world, bacteria):
    """ Move South """
    if action:
        pos = [bacteria.pos[0] + 1, bacteria.pos[1]]
        world.Dispose(bacteria, pos)

def MW(action, world, bacteria):
    """ Move West """
    if action:
        pos = [bacteria.pos[0], bacteria.pos[1] - 1]
        world.Dispose(bacteria, pos)

def ME(action, world, bacteria):
    """ Move East """
    if action:
        pos = [bacteria.pos[0], bacteria.pos[1] + 1]
        world.Dispose(bacteria, pos)

def MR(action, world, bacteria):
    """ Move Random """
    if action:
        delta = [random.randint(-1, 1), random.randint(-1, 1)]
        pos = [bacteria.pos[0] + delta[0], bacteria.pos[1] + delta[1]]
        world.Dispose(bacteria, pos)

def K(action, world, bacteria):
    """ Kill """
    pass

# -------------------- LISTS -------------------------
Sensors = [DN, DS, DW, DE, DL]
Actions = [MN, MS, MW, ME, MR]
