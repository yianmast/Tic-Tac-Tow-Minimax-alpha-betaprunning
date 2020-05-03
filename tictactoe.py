#--------------------------------------------------------------------------------
# Name:      tictactoe.py
#
# Purpose:  Humans can play tictactoe against each other or against an ai. The ai uses either alpha-beta
#pruning or simple minimax
#
#
#Required libs: math and random
#
#Author:    Ioannis Mastoras
#
#Created:   11 April 2020
#
#-----------------------------------------------------------------------------------
from math import inf as infinity
import random

initial_state = ['-','-','-','-','-','-','-','-','-']

#tests if there is a winner
def win(state):
    #horizontal
    i = 0
    while i < 7:
        if state[i] != '-' and state[i] == state[i+1] and state[i] == state[i+2]:
            return True
            
        i+=3

    #vertical
    j = 0
    while j < 3:
        if state[j] != '-' and state[j] == state[j+3] and state[j] == state[j+6]:
            return True
        j+=1
        
    #diagonal
    if state[4] != '-' and ((state[2] == state[4] and state[2] == state[6])  or (state[0] == state[4] and state[0] == state[8])):
        return True

    
#checks if the move is valid
#ind is the index it checks for validity 
def valid(state,ind):
    if ind<0 or ind>8: #mut be i the reange
        return False
    elif state[ind] == '-':
        return True

#makes the move
#state is the current board
#ind is the index of the square
#player is 'x' or 'o'
def move(state,ind,player):
    if valid(state,ind): #checks for validity first
        state[ind] = player
    return state

#a function to print the list as a board
def prt(state):
    k = 1 #count    
    while k<4:  #loop to print the list as a NxN board
         print('',*state[3*(k-1):3*k]) #prints it row by row
         k += 1

#returns the score
def evaluate(state,player):

#player is the payer before the final move
#the machine is alwyays 'o'
    if win(state) and player=='o': #if win state and previous player was 'o', the machine lost
        score = -1
    elif win(state) and player=='x': #if win state and previous player was 'x', the machine won
        score = 1
    else:
        score = 0 #tie

    return score

#returns a list with the indices of the empty cells
def empty(state):
    empty_cells = []

    for i in range(9):
        if state[i] == '-':
            empty_cells.append(i)
    return empty_cells

#minimax algorithm
def minimax(state,depth,player):
    

    if player == 'o': #computer
        best = [-1,-infinity] #worst case scenarion from machine's perspective
    else:   #human
        best = [-1,infinity] #worst case scenarion from machine's perspective

    if depth == 0 or win(state): #if the board is full or sb won:
        score = evaluate(state,player)#get the score so we can know who
        return [-1,score]
    
    for cell in empty(state): #for every empty square
        
        state[cell] = player #fill the square 
        i = cell #index of square
        
        if player == 'o':
            score = minimax(state,depth-1,'x')#run minimax fot the other player
        else:
            score = minimax(state,depth-1,'o')
          
        state[cell] = '-' #set square to empty again
        score[0] = i #best index 

        if player == 'o':
            if score[1] > best[1]:
                best = score #max value

        elif player == 'x':
            if score[1]<best[1]:
                best = score #min value
                
    return best #[best index,best score]

#αβ-pruning algorithm
def alpha_beta(state,depth,player):
    alpha = -infinity #worst value for alpha
    beta = infinity #worst value for beta
    
    if player == 'o': #computer
        best = [-1,-infinity]#worst case scenarion from machine's perspective
    else:   #human
        best = [-1,infinity] #worst case scenarion from machine's perspective

    if depth == 0 or win(state): #if the board is full or sb won:
        score = evaluate(state,player) #get the score so we can know who       
        return [-1,score]
    
    for cell in empty(state): #for every empty square
        
        state[cell] = player #fill the square
        i = cell  #best index 
        
        if player == 'o':
            score = minimax(state,depth-1,'x')

        else:
            score = minimax(state,depth-1,'o')
          

        state[cell] = '-'
        score[0] = i


        if player == 'o':
            if score[1] > best[1]:
                best = score #max value

                if best[1] >= beta:
                    return best #prun
                if best[1] > alpha:
                    alpha = best[1]

        elif player == 'x':
            if score[1]<best[1]:
                best = score #min value

                if best[1] <= alpha:
                    return best #prun
                if best[1] < beta:
                    beta = best[1]
    return best

#machine plays the game
def ai1(alg): #alg is the algorithm: αβ or minimax
    de = len(empty(initial_state)) #depth

    print('Machine chose')
    i = alg(initial_state,de,'o')[0] #gets best index from the alforithm [best index, best score]
    move(initial_state,i,'o') #fills the square
    prt( initial_state) #prints the board

#same as ai1
def ai2(alg):
    print('')
    de = len(empty(initial_state))

    print('Second Machine chose')

    i = alg(initial_state,de,'x')[0]
    move(initial_state,i,'x')
    prt( initial_state)

#human1 plays the game
def h1():
    print('Player X choice? ')
    i = int(input('index 0..8 ')) 

    while i<0 or i>9 or i not in empty(initial_state): #checks validity and returns an error message
        if i<0 or i>9:
            print('Invalid! Expected [0-8]')
            
        else:
            print('Bad Choice! It is already filled')
            
            
        print('Player X choice? ')
        i = int(input('index 0..8 '))
    
    move(initial_state,i,'x')#fills the square
    prt( initial_state)#prints the board
          
                
#same as h1
def h2():
    i = int(input('index 0..8 '))

    while i<0 or i>9 or i not in empty(initial_state):
        if i<0 or i>9:
            print('Invalid! Expected [0-8]')
            
        else:
            print('Bad Choice! It is already filled') 
            
        print('Player O choice? ')
        i = int(input('index 0..8 '))
    
    move(initial_state,i,'o')
    prt( initial_state)

#human v human
def hvh(): 
    
    h1() #plays first
    while len(empty(initial_state))>0 and not win(initial_state): #while the board is not full and there is no winer
        h2() #human 2 plays
        if not win(initial_state):#checks for winner again
            h1() #human 1 plays

    c = len(initial_state)- len(empty(initial_state)) #filled squares
    if win(initial_state):
        if c%2!=0:
            print('Player X Wins!')
        elif c%2 == 0:
            print('Player O Wins!')
    else:
        print("Tie! Cat's win")
        

#human versus machine   
def hvai(alg): #human first
    h1()
    while len(empty(initial_state))>0 and not win(initial_state):
        ai1(alg)
        if not win(initial_state):
            h1()

    c = len(initial_state)- len(empty(initial_state))
    if win(initial_state):
        if c%2!=0:
            print('You Win!')
        elif c%2 == 0:
            print('Machine Wins!')
    else:
        print("Tie! Cat's win")
    

#human versus machine
def aivh(alg): #machine first
    print('Machine chose')
    i = random.randint(0,8) #random first move
    initial_state[i] = 'o'
    prt(initial_state)
    while len(empty(initial_state))>0 and not win(initial_state):
        h1()
        if not win(initial_state):
            ai1(alg)

    c = len(initial_state)- len(empty(initial_state))
    if win(initial_state):
        if c%2!=0:
            print('Machine Wins!')
        elif c%2 == 0:
            print('You Win!')
    else:
        print("Tie! Cat's win")

#machine versus machine
def aivai(alg):
    print('Machine O chose')
    i = random.randint(0,8)
    initial_state[i] = 'o'
    prt(initial_state)
    while len(empty(initial_state))>0 and not win(initial_state):
        ai2(alg)
        if not win(initial_state):
            ai1(alg)

    c = len(initial_state)- len(empty(initial_state))
    if win(initial_state):
        if c%2!=0:
            print('Machine O Wins!')
        elif c%2 == 0:
            print('Machine X Wins!')
    else:
        print("Tie! Cat's win")

#main function   
def main():
    print('This 3x3 TicTacToe game allow you to play \n',
          'against another human player or against the machine. \n',
          'Also, the machine can play against it slef! \n',
          'You will be promted for these choises. \n',
          'Should you choose to play against the machine,\n',
          'you will prompted whether you want the machine to go first.\n',
          'Also, you will be promted wheteher alpha-beta should be used.\n'
          'Should you choose the machine to compete itself, you will be promted wheteher alpha-beta should be used.\n')

    print('The TicTacToe will be indexed starting at 0 through 8 in a row major form.\n',
          '0 1 2 \n',
          '3 4 5 \n',
          '6 7 8 \n',
          'A human player will be promped for the square number 0-8. \n',
          'A human player will be promed again if they enter a square number out of range \n',
          'or already filled.\n')
    while True:

        twohumans = input('Two Humans (y/n)? ')
        if twohumans == 'y':
            hvh()
            break

        
        twomachines = input('Two Machines (y/n)? ')
        if twomachines == 'y':
            algorithm = input('Alpha-beta pruning on (y/n)?')
            if algorithm == 'y':
                aivai(alpha_beta)
                break
            else:
                aivai(minimax)
                break
            
            
        machinefirst = input('Machine goes first (y/n)? ')
        if machinefirst == 'y':
            algorithm = input('Alpha-beta pruning on (y/n)?')
            if algorithm == 'y':
                aivh(alpha_beta)
                break
            else:
                aivh(minimax)
                break
        else:
            algorithm = input('Alpha-beta pruning on (y/n)?')
            if algorithm == 'y':
                hvai(alpha_beta)
                break
            else:
                hvai(minimax)
                break
            
main()

    
