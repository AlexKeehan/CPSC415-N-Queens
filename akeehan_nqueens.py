#!/usr/bin/env python3
import sys
import random
import numpy as np
import math

size = int(sys.argv[1])


# Get conflicts
def get_conflicts(board):
    # use num to iterate through board
    num = len(board)
    # Keep track of conflicts
    conflicts = 0

    
    # Nested for loops to check every row against every col
    for x in range(num):
        for y in range(x + 1, num):
            # Check if the queens are in the same row
            if board[x] == board[y]:
                conflicts += 1
            # Check for diagonals
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
    
    # Nested for loops
    for col in range(num):
        # Use row as the "random" number to generate successor states
        for row in range(num):
            # Don't generate same state as one we are in
            if board[col] != row:
                # Using list to copy board over
                temp_board = list(board)
                # Changing just the one col using row as the "random" number
                temp_board[col] = row
                # Add to successors
                successors.append(temp_board)
    return successors

# Function to solve the n queens problem
def stochastic():
    # Keep track of states we have restarted in
    visited_restarts = []
    # Keep track of states we have been
    visited = []

    # Loop essentially forever
    for _ in range(restarts):
        # Start off in random spot
        curr_state = [random.randint(0, size - 1) for _ in range(size)]
        # Choose again if we have started here before
        if curr_state in visited_restarts:
            continue
        # Get the conflicts for current state
        get_conflicts_curr = get_conflicts(curr_state)
        
        visited_restarts.append(curr_state)

        # Keep going until limit is reached, then random restart again
        for _ in range(limit):
            # Get all successors for current state
            successors = get_successor_states(curr_state)
            

            # Use a lambda function to give all successors a weight
            weights = list(map(lambda state: 1 / (get_conflicts(state) + 1), successors))
            
            # Randomly choose a successor to move too
            move = random.choices(successors, weights=weights, k=1)[0]
            
            # Don't go to places we have been before
            if move in visited:
                continue
            visited.append(move)
            
            # Convert move to a str to print it
            str_array = [str(integer) for integer in move]
            # Remove the [ ]
            output = (' '.join(str_array))
            # Print neatly
            print("[ " + output + " ]")

            # Get the conflicts for the successor
            get_conflict_successor = get_conflicts(move)
            
            # If successor conflicts
            if get_conflict_successor < get_conflicts_curr:
                curr_state = move
                get_conflicts_curr = get_conflict_successor
                if get_conflicts_curr == 0:
                    return curr_state

    return curr_state


# Function to print the solution neatly
def print_solution(board):
    print('\n')
    print("Solution:")
    
    # Increase num to keep track of added spaces and such
    num = (len(board) * 2) + 1
    
    # Print the +------+
    output = "+"
    for _ in range(num):
        output += "-"
    output += "+"
    print(output)

    # Print the actual board
    for col in range(len(board)):
        output = "| "
        for row in range(len(board)):
            if col == board[row]:
                output += "Q "
            else:
                output += "* "
        output += "|"
        print(output)

    # Print the +------+ again
    output = "+"
    for _ in range(num):
        output += "-"
    output += "+"
    print(output)
    
    # Finally, print the board
    print(board)

# Num of iterations before random restart
limit = 200

# Essentially unlimited restarts
restarts = 1000

# Call stochastic
ans = stochastic()
# Print the answer neatly
print_solution(ans)
