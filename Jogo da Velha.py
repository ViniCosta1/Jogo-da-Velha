def display_board(board):
    print('   |   |   ')
    print(' '+ board[7]+' | '+ board[8]+' | '+ board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+ board[4]+' | '+ board[5]+' | '+ board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+ board[1]+' | '+ board[2]+' | '+ board[3])
    print('   |   |   ')

def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Jogador 1: Você quer ser X ou O?\n").upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or
            (board[6] == mark and board[5] == mark and board[4] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

import random
import re
from turtle import position
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = " "
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input("Escolha sua jogada (1-9):\n")
    return int(position)

def replay():
    return input("Querem jogarm novamente? Sim ou Não").lower().startswith('s')

print("Bem vindo ao jogo da velha!")

while True:
    board = [' '] * 10
    player1_maker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'começa!')
    
    game_on = True
    
    while game_on:
        #Vez do jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_maker, position)
            
        # Checar vitória
        if win_check(board, player1_maker):
            display_board(board)
            print("Parabéns, Você venceu")
            game_on = False
        else:
            if full_board(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 2'
        
        # Vez do jogador 2
        if turn == 'Player 2':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
        # Checar vitória
        if win_check(board, player2_marker):
            display_board(board)
            print("Parabéns, Você venceu")
            game_on = False
        else:
            if full_board(board):
                display_board(board)
                print('Empate!')
                break
            else:
                turn = 'Player 1'
    if not replay():
        break