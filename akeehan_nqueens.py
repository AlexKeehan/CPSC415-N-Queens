#!/usr/bin/env python3
import sys
import random

size = int(sys.argv[1])
board = []

for i in range(size):
    rand = random.randint(0, size - 1)
    board.append(rand)
print(board)


# Get conflicts
def get_conflicts(board):
    # use num to iterate through board
    num = len(board)
    # Keep track of conflicts
    conflicts = 0

    
    for col in range(num):
        for i in range(col + 1, num):
            # Check for queens in same row        
            if board[col] == board[i]:
                conflicts += 1
            # Check if queens are in same diagonal from top left down
            elif board[col] - board[i] == col - i:
                conflicts += 1
            # Check if queens are in same diagonal from top right down
            elif board[col] - board[i] == i - col:
                conflicts += 1
    return conflicts

# Get possible successor states
def get_successor_states(board):
    # Use num to iterate through board
    num = len(board)
    # Keep track of successors
    successors = []

    for col in range(num):
        curr_row = board[col]
        # Use row as the "random" number to generate successor states
        for row in range(num):
            # Don't generate same state as one we are in
            if row == curr_row:
                continue
            # Usin list to copy board over
            temp_board = list(board)
            # Changing just the one col using row as the "random" number
            temp_board[col] = row
                
            # Add to successors
            successors.append(temp_board)
    return successors

conflicts = get_conflicts(board)
print("Conflicts", conflicts)
successors = get_successor_states(board)
print("Successors", successors)



