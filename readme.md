# Bacteria AI
It's a simulation of a bacteria colony using Neural Network.

## World
The world consists of a square matrix in which are randomly spawned some bacteria.

## Brain
Each bacteria consist of a small neural network brain with three layers:
- The first is the Sensor layer and consists of a list of functions that outputs some information about the bacteria or the world. 
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

- The second is the Neuron layer and consists of some empty nodes that simply normalize their imput between 0 and 1 using a logistic function
```python
def sigma(vector, p = 4):
    """ Sigmoid normalization function """
    output = []
    for el in vector:
        y = m.exp(p * el) / (1 + m.exp(p * el))
        output.append(y)
    return output
```

- The third is the Action layer and consists of a list of functions that are activated only if the input given is above a threshold i.e. above 0.5.
```python
Actions = [
        MoveNorth, 
        MoveSouth, 
        MoveWest, 
        MoveEast, 
        MoveRandom, 
        Eat]
```
Such functions are actions made by the bacteria such as moving or eating.
