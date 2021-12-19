from copy import deepcopy
import numpy as np
path = "day15.txt"

def parse_data(): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return(lines)

input = parse_data()
data = [[x for x in input[y]] for y in range(len(input))]
data = np.asarray(data)
#print(data)

criticalPath = []
CPX = CPY = 0
MPX = data.shape[1]
MPY = data.shape[0]



