# Bacteria AI
It's a simulation of a bacteria colony using Neural Network.
The idea behind the simulation is the following:
randomly spawn some bacteria (neural netoworks) on the world matrix and let them perform a fixed number of actions. 
Then run a Natural Selection function that deletes avery bacteria that does not satisfy a certain condition.
Store the survivors informations on an external `gen.json` file.
Run the next simulation by loading `gen.json` bacteria and duplicate their number, as if they are reproducing.

The project is aimed to show that Natural Selection forces the evolution of the bacteria and, after a certain number of iterations, they will all learn how to survive.
---
## Project
The project consists of multiple files:
- ***bacteria.py***: contains the Bacteria class and the basic functions to compute Neural Network decisions and visualize the Network as a graph.
- ***brain.py***: contains the Sensors and the Actions that all bacteria are able to use.
- ***graphics.py*** and ***debug.py***: manage all the visualization processes.
- ***requirements.txt***: the python requirements that must be installed on the enviroment.
- ***world.py***: contains the world class and all the basic functions needed to run the simulation.
- ***settings.py***: contains all the simulation settings and the basic json functions.
- ***main.py***: the main file that runs a certain number of simulations and stores the survivors informations on `log/gen.json`.
- ***visual.py***: runs a simulation based on the `log/gen.json` file and shows it on screen.
---
## Settings
- ***SIZE***: the size of the world square matrix
- ***POPULATION***: the starting bacteria population.
- ***MAX_POPULATION***: the maximum number of bacteria allowed.
- ***GENE_NUM***: the number of connections between the nodes of the neural network.
- ***NEURON_NUM***: the number of Neuron nodes
- ***LIFE_SPAN***: how many moves each bacteria does between Natural Selection is called.
- ***MAX_GEN***: how many iterations does the `main.py` execute before arresting.
- ***MUTATION***: the mutation probability, each time a bacteria reproduces this is the chance that a mutation will occur.
---
## Brain
Each bacteria consist of a small neural network brain with three layers:

### Sensor
The first is the Sensor layer and consists of a list of functions that outputs some information about the bacteria or the world. 
```python
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
```
Every sensor returns a float between 0 and 1.

### Neuron
The second is the Neuron layer and consists of some empty nodes that simply normalize their imput between 0 and 1 using a logistic function
```python
def sigma(vector, p = 4):
    """ Sigmoid normalization function """
    output = []
    for el in vector:
        y = m.exp(p * el) / (1 + m.exp(p * el))
        output.append(y)
    return output
```

### Action
The third is the Action layer and consists of a list of functions that are activated only if the input given is above a threshold i.e. above 0.5.
Such functions are actions made by the bacteria such as moving or eating.
```python
Actions = [
        MoveNorth, 
        MoveSouth, 
        MoveWest, 
        MoveEast, 
        MoveRandom, 
        Eat]
```
---
## Bacteria
Each bacteria consists of a simple neural network with the three layers described above.
The connections between the nodes are described as an hexadecimal string:
```python
"bact0": "fff5 d80a a440 6e1e cf19 f374 80bd 30fe c07c c2f9 53cf 7b93 38d0 1586 1a94 ce06 71e8 26f5 ff7f dcee"
```
The string consists of chunks of four characters that encodes the informations of a single connection:
each gene is converted to a 16 bits binary string that encodes a single connection between neurons, sensors and actions.
- bit 0:
    - 0 -> Starting from a Neuron 
    - 1 -> Starting from a Sensor
- bit 1:
    - 0 -> Starting from a Neuron 
    - 1 -> Starting from a Sensor
- bit 2 to 5:
    - Chooses which starting Neuron or Sensor
- bit 6 to 9:
    - Chooses which ending Neuron or Action
- bit 10 to 16:
    - Determines the weight of the connection, a normalized number between 0 and 1

This encoding method allows us to have a maximum of 16 Sensors, Neurons and Actions.
Given all connections we can build three matrices:
- NN: the matrix describing connections Neuron -> Neuron.
- NA: the matrix describing connections Neuron -> Action.
- SN: the matrix describing connections Sensor -> Neuron.
- SA: the matrix describing connections Sensor -> Action.

These matrices are used to compute what the bacteria will do given it's sensor outputs.
---
## World
The world consists of a square matrix on which some entries are occupied by a bacteria.
This file consists of functions that spawns bacteria, let them perform actions and then run the Natural Selection function to select the survivors.
There are two functions, Save and Load, that manage the data stored on `log/gen.json`.
---
## Main
The main file simply runs a complete simulation and stops after a certain number of iteration, as specified in the `MAX_GEN` variable.
If you don't want to reset the evolution and keep evolving from `log/gen.json` you can comment some lines as specified in the file.
---
## Visual
Simply shows on screen the current `log/gen.json` population, it doesn't modify the file in any way, is only a visualization tool.
---
## To do
Separate the graph visualization from the bacteria file and organize the code in folders.
