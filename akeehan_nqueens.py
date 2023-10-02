#!/usr/bin/env python3
import sys
import random
import numpy as np

size = int(sys.argv[1])


# Get conflicts
def get_conflicts(board):
    # use num to iterate through board
    num = len(board)
    # Keep track of conflicts
    conflicts = 0

    

    for x in range(num):
        for y in range(x + 1, num):
            if board[x] == board[y]:
                conflicts += 1
            if board[x] - board[y] == x - y:
                conflicts += 1
            if board[x] - board[y] == y - x:
                conflicts += 1
    return conflicts

# Get possible successor states
def get_successor_states(board):
    # Use num to iterate through board
    num = len(board)
    # Keep track of successors
    successors = []

    for col in range(num):
        # Use row as the "random" number to generate successor states
        for row in range(num):
            # Don't generate same state as one we are in
            if board[col] != row:
                # Using list to copy board over
                temp_board = list(board)
                # Changing just the one col using row as the "random" number
                temp_board[col] = row

                successors.append(temp_board)
    return successors

def stochastic():
    visited = []
    for _ in range(restarts):
        curr_state = [random.randint(0, size - 1) for _ in range(size)]
        if curr_state in visited:
            continue
        get_conflicts_curr = get_conflicts(curr_state)
        visited.append(curr_state)

        for _ in range(limit):
            successors = get_successor_states(curr_state)
            

            weights = list(map(lambda state: 1 / (get_conflicts(state) + 1), successors))
            

            move = random.choices(successors, weights=weights, k=1)[0]
            str_array = [str(integer) for integer in move]
            output = (' '.join(str_array))
            print("[ " + output + " ]")
            get_conflict_successor = get_conflicts(move)

            if get_conflict_successor < get_conflicts_curr:
                curr_state = move
                get_conflicts_curr = get_conflict_successor
                if get_conflicts_curr == 0:
                    return curr_state
    return curr_state

def print_sol(board):
    print('\n')
    print("Solution:")
    
    num = (len(board) * 2) + 1
    
    output = "+"
    for _ in range(num):
        output += "-"
    output += "+"
    print(output)
    for col in range(len(board)):
        output = "| "
        for row in range(len(board)):
            if col == board[row]:
                output += "Q "
            else:
                output += "* "
        output += "|"
        print(output)
    output = "+"
    for _ in range(num):
        output += "-"
    output += "+"
    print(output)

    print(board)
limit = 200
restarts = 1000

ans = stochastic()
print_sol(ans)
