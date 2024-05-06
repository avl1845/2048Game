import numpy as np
import random

board = (np.zeros(16)).reshape(4, 4) # Creating 4x4 matrix
print(board)
command_start = ' '; command_up = 'w'; command_down = 's'; command_left = 'a'; command_right = 'd' # Making user input commands
lst_of_twos = ([2] * 17); lst_of_fours = [4, 4, 4] # There is a 15% chance of getting a 4 after each turn. 85% chance of getting a 2.
lst_total = lst_of_twos; lst_total.extend(lst_of_fours) # Creating list to pick from with 3 4's and 17 2's.

# This function is used for adding the extra entry after each move. 
def add_random():
    while True:
        select_row = random.randint(0, 3) # Choosing row entry
        select_column = random.randint(0, 3) # Choosing column entry
        if board[select_row, select_column] == 0: # Can only add a number in an entry that is 0.
            board[select_row, select_column] = random.choice(lst_total)
            break
        else:
            continue
    print(board)
    
def move_up():
    for x in range(3):
        for i in range(1, 4):
            for j in range(4):
                if board[i-1, j] == 0:
                    board[i-1, j] = board[i, j]
                    board[i, j] = 0
    for i in range(1, 4):
        for j in range(4):        
            if board[i-1, j] == board[i, j]:
                board[i-1, j] *= 2
                board[i, j] = 0
    for x in range(3):
        for i in range(1, 4):
            for j in range(4):
                if board[i-1, j] == 0:
                    board[i-1, j] = board[i, j]
                    board[i, j] = 0
    print(board)

def move_down():
    for x in range(3):
        for i in range(2, -1, -1):
            for j in range(4):
                if board[i+1, j] == 0:
                    board[i+1, j] = board[i, j]
                    board[i, j] = 0
    for i in range(2, -1, -1):
        for j in range(4):        
            if board[i+1, j] == board[i, j]:
                board[i+1, j] *= 2
                board[i, j] = 0
    for x in range(3):    
        for i in range(2, -1, -1):
            for j in range(4):
                if board[i+1, j] == 0:
                    board[i+1, j] = board[i, j]
                    board[i, j] = 0
    print(board)

def move_left():
    for x in range(3):
        for i in range(4):
            for j in range(1, 4):
                if board[i, j-1] == 0:
                    board[i, j-1] = board[i, j]
                    board[i, j] = 0
    for i in range(4):
        for j in range(1, 4):        
            if board[i, j-1] == board[i, j]:
                board[i, j-1] *= 2
                board[i, j] = 0
    for x in range(3):    
        for i in range(4):
            for j in range(1, 4):
                if board[i, j-1] == 0:
                    board[i, j-1] = board[i, j]
                    board[i, j] = 0
    print(board)

def move_right():
    for x in range(3):
        for i in range(4):
            for j in range(2, -1, -1):
                if board[i, j+1] == 0:
                    board[i, j+1] = board[i, j]
                    board[i, j] = 0
    for i in range(4):
        for j in range(2, -1, -1):        
            if board[i, j+1] == board[i, j]:
                board[i, j+1] *= 2
                board[i, j] = 0
    for x in range(3):    
        for i in range(4):
            for j in range(2, -1, -1):
                if board[i, j+1] == 0:
                    board[i, j+1] = board[i, j]
                    board[i, j] = 0
    print(board)

def command_center():
    while True:
        user_command = input("Press the command: ")
        if user_command == command_up:
            move_up()
            add_random()
        if user_command == command_down:
            move_down()
            add_random()
        if user_command == command_left:
            move_left()
            add_random()
        if user_command == command_right:
            move_right()
            add_random()


user_command = input("Press space to start! ")
if user_command == ' ':
    add_random()
    command_center()


