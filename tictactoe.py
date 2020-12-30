# -*- coding: utf-8 -*-
#tictactoe.py
#tony schwebach
#11/10/2020
#game of tic tac toe

import random

#ui - board setup
board = ['0','1','2','3','4','5','6','7','8','9']
def printBoard():
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print("-----")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-----")
    print(f"{board[7]}|{board[8]}|{board[9]}")

#possible moves
def possMoves():
    global possibleMoves 
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' ]

#user move
def userMove():
    possMoves()
    umove = input("User, choose space 1-9: ")
    while 0==0:
        try:
            if int(umove) in possibleMoves:
                return umove
            else:
               umove = input(f"Invalid space. Choose: {possibleMoves}: ") 
        except:
            umove = input(f"Invalid space. Choose: {possibleMoves}: ")
    
#check for winner
def winner(let, board =board):
    return( 
    (board[1] == let and board[2] == let and board[3] == let) or #win top row
    (board[4] == let and board[5] == let and board[6] == let) or #win mid row
    (board[7] == let and board[8] == let and board[9] == let) or #win bot row
    (board[1] == let and board[4] == let and board[7] == let) or #win left col
    (board[2] == let and board[5] == let and board[8] == let) or #win mid col
    (board[3] == let and board[6] == let and board[9] == let) or #win right col
    (board[1] == let and board[5] == let and board[9] == let) or #win \
    (board[3] == let and board[5] == let and board[7] == let))   #win /
    
#computer move
def compMove():
    possMoves()
    move = 0
    
    #make winning move or block
    for let in ['O','X']:
        for move in possibleMoves:
            boardcopy = board[:]
            boardcopy[move] = let
            if winner(let,boardcopy):
                return move
    
    #corner moves
    corners = []
    for c in (1,3,6,9):
        if c in possibleMoves:
            corners.append(c)
    if corners != []:
        move = random.choice(corners)
        return move
    
    #middle
    elif 5 in possibleMoves:
        move = 5
        return move
 
    #edges (corners and middle already coded)
    else: 
        move = random.choice(possibleMoves)
        return move

def gameplay():
    print()
    printBoard()

    while 0==0:
        board[int(userMove())]='X'
        if winner('X',board):
            printBoard()
            print("USER WINS!")
            break
        elif ' ' not in board:
            printBoard()
            print("Tie game.")
            break

        board[int(compMove())]='O'
        if winner('O',board):
            printBoard()
            print("Computer Wins!")
            break
        elif ' ' not in board:
            printBoard()
            print("Tie game.")
            break

        printBoard()


#game initiation & main  
print("Welcome to Tic-Tac-Toe!") 
printBoard()

again = 'Y'
while again.upper() == 'Y':
    board = ['Z',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    gameplay()
    again = input("Play again? Y / N: ")
    
else:
    exit()






