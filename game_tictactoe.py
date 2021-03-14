from random import shuffle
from IPython.display import clear_output   ## this will only work in jupyter notebook

#row1 = [' ', ' ', ' ']
#row2 = [' ', ' ', ' ']
#row3 = [' ', ' ', ' ']

####################### play variables stored in Dictionary, for better tracking ########################################################################

d = {'value': 0, 'position': 0, 'start': 0}

#################### display Function ###########################################

def display():
    print(f"{row1[0]} |{row1[1]}| {row1[2]}")
    print("-------")
   
    print(f"{row2[0]} |{row2[1]}| {row2[2]}")
    print("-------")
   
    print(f"{row3[0]} |{row3[1]}| {row3[2]}")

######################## Below function kickstarts the game, taking inputs from user [yY] for yes [nN] for No################

######################## Below function will decide who will go first to play TicTacToe #####################################

def whowill():
    print("Lets see who will go first to play TicTacToe Board game")
    myval = 0
    mylist = []
    A = ''
    B = ''
    while A not in ['X','x','O','o']:
        
        A = input("Hi, Player 1 , pls. select the value either 'X' or 'O' \n")
        print('\n')
    while B not in ['X','x','O','o']:
        B = input("Hi, Player 2 , pls. select the value either 'X' or 'O' \n")
        print('\n')
        
    while B == A:
        
                
        print("Sorry Player 2 you can't select the same ID as Player 1")
        print('\n')
        B = input("Hi Player 2 , pls. select the value either 'X' or 'O' \n")
        print('\n')
            
    mylist.append(A)
    mylist.append(B)
        
    a = A.upper()
    b = B.upper()
        
    shuffle(mylist)
        
    if mylist[0] == A:
            print(f"Player 1 with ID '{a}' will Play first")
            print('\n')
            
    else: 
            print(f"Player 2 with ID '{b}' will Play first")
            print('\n')

#############################################################################################################################

def start_play():

    d['start'] = 0
    
    while d['start'] not in ['Y', 'y','N', 'n' ]:
        
        
        p = input("Please strike 'y' for starting and 'n' for quitting the Game!!! ")
        d['start'] = p
        if d['start'] in ['Y', 'y']:
            print('\n')
            print("Let's get started!!!!")
            print('\n')
            whowill()
            resets()
            reset_display()
            asking_input()
        elif d['start'] in ['N', 'n']:
            print('\n')
            print("Bye Bye!! Have a nice Day !!! Come again")
##############################################################################################################################

##################### Below function asks the user input for TicTacToe in the form of [oO] or [xX], alongwith position #######

def asking_input():
    if d['start'] == 'y' or d['start'] == 'Y':
        
        while d['value'] not in ['O', 'x', 'o', 'X']:
            
            z = input("Please input the value, either o or x: \n")
            d['value'] = z.upper()
            print('\n')

        while d['position'] not in range(1,10):
                
                t = input("Please input the position, select from 1-9: \n")
                
                if t.isalpha():
                    break
                else:
                    d['position'] = int(t)
        
        mapping_inputs()
###############################################################################################################################

################ Below function resets the value and position for TicTacToe ##############################################

def resets():
    d['value'] = 0
    d['position'] = 0
############################################################################################################################    
    
########################### below function resets display ##################################################################
    
def reset_display():
    global row1
    global row2
    global row3
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    print(f"{row1[0]} |{row1[1]}| {row1[2]}")
    print("-------")
   
    print(f"{row2[0]} |{row2[1]}| {row2[2]}")
    print("-------")
   
    print(f"{row3[0]} |{row3[1]}| {row3[2]}")
##############################################################################################################################    
        
####################################### Below one maps input in the TicTacToe matrix #####################################    

def mapping_inputs():
    clear_output()

    if d['position'] in [1,2,3]:
        if row1[d['position']-1] == ' ':
            row1[d['position']-1] = d['value']
            print('\n')
            display()
            
        
    elif d['position'] in [4,5,6]:
        if row2[d['position']-4] == ' ':
            row2[d['position']-4] = d['value']
            print('\n')
            display()
    elif d['position'] in [7,8,9]:
        if row3[d['position']-7] == ' ':
            row3[d['position']-7] = d['value']
            print('\n')
            display()
    else:
        asking_input()
    
    win()
############################################################################################################################    
    
############################ checks the win condition ######################################################################

def win():
    if row1 == ['X','X','X'] or row2 == ['X','X','X'] or row3 == ['X','X','X']:
        print('\n')
        print("Congratulations!!!! X is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
        
    elif row1 == ['O','O','O'] or row2 == ['O','O','O'] or row3 == ['O','O','O']:
        print('\n')
        print("Congratulations!!!! O is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    
    elif (row1[0] == row2[0] == row3[0] == 'O') or (row1[1] == row2[1] == row3[1] == 'O') or (row1[2] == row2[2] == row3[2] == 'O') or (row1[0] == row2[1] == row3[2] == 'O') or (row1[2] == row2[1] == row3[0] == 'O'):
        print('\n')
        print("Congratulations!!!! O is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    
    elif (row1[0] == row2[0] == row3[0] == 'X') or (row1[1] == row2[1] == row3[1] == 'X') or (row1[2] == row2[2] == row3[2] == 'X') or (row1[0] == row2[1] == row3[2] == 'X') or (row1[2] == row2[1] == row3[0] == 'X'):
        print('\n')
        print("Congratulations!!!! X is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    elif (' ' not in row1) and (' ' not in row2) and (' ' not in row3):
        print('\n')
        print("Great!!! it's a tie")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
        
    else:
        resets()
        asking_input()
        
