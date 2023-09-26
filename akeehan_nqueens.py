#!/usr/bin/env python3
import sys
import numpy as np
import random
size = int(sys.argv[1])

board = [[0]* size for _ in range(size)]


for i in range(size):
    
    rand = random.randint(0, size - 1)
    board[rand][i] = "Q"
print(board)


# Check for conflicts
conflicts = 0
pairs = 0
print(board[0])
for x in range(size):
    rqueens = 0
    for i in range(size):
    
        if board[x][i] == "Q":
            
        if rqueens == 4:
            conflicts = conflicts + 6
        elif rqueens == 3:
            conflicts = conflicts + 3
        elif rqueens == 2:
            conflicts = conflicts + 1
    
    
    x = x + 1
print("Conflicts", conflicts)
#print(conflicts)
