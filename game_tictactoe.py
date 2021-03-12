#!/usr/bin/env python
# coding: utf-8

# In[200]:


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

####################### play variables stored in Dictionary, for better tracking ########################################################################

d = {'value': 0, 'position': 0, 'start': 0}

#################### display Function ###########################################

def display():
    print(row1)
    print(row2)
    print(row3)

######################## Below function kickstarts the game, taking inputs from user [yY] for yes [nN] for No################

def start_play():
    d['start'] = 0
    
    while d['start'] not in ['Y', 'y','N', 'n' ]:
        
        p = input("Please strike 'y' for starting and 'n' for quitting the Game!!! ")
        d['start'] = p
        if d['start'] in ['Y', 'y']:
            print('\n')
            print("Let's get started!!!!")
            print('\n')
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
            
            z = input("Please input the value, either o or x: ")
            d['value'] = z.upper()

        while d['position'] not in range(1,10):
            t = input("Please input the position, select from 1-9: ")
            d['position'] = int(t)
        
        mapping_inputs()
###############################################################################################################################

################ Below function resets the value and position for TicTacToe ##############################################

def reset():
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
    print(row1)
    print(row2)
    print(row3)
##############################################################################################################################    
        
####################################### Below one maps input in the TicTacToe matrix #####################################    

def mapping_inputs():

    if d['position'] in [1,2,3]:
        if row1[d['position']-1] == ' ':
            row1[d['position']-1] = d['value']
            display()
            
        
    elif d['position'] in [4,5,6]:
        if row2[d['position']-4] == ' ':
            row2[d['position']-4] = d['value']
            display()
    else:
        if row3[d['position']-7] == ' ':
            row3[d['position']-7] = d['value']
            display()
    
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
    
    elif (row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O') or (row1[1] == 'O' and row2[1] == 'O' and row3[1] == 'O') or (row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O'):
        print('\n')
        print("Congratulations!!!! O is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    
    elif (row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X') or (row1[1] == 'X' and row2[1] == 'X' and row3[1] == 'X') or (row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X'):
        print('\n')
        print("Congratulations!!!! X is the Winner")
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    elif (' ' not in row1) and (' ' not in row2) and (' ' not in row3):
        print('\n')
        print('Sorry its a Tie between you two')
        print("\n")
        print("Lets Play again! ")
        print("\n")
        start_play()
    else:
        reset()
        asking_input()

        





start_play()






