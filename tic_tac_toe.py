import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import stddraw
import stdio


def play_board():
    board = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append('-')
        board.append(row)
    return board

def place_piece(board, row, column, player):
    if board[row][column] == '-':
        board[row][column] = player
        return True
    else: return False

def check_wins(board, player):
    # Check for row wins
    for row in board:
        win = True
        for cell in row:
            if cell != player:
                win = False
                break
        if win: return True

    # Check for column wins
    for column in range(4):
        win = True
        for row in board:
            if row[column] != player:
                win = False
                break 
        if win: return True

    # Check for diagonal wins
    win = True
    for i in range(4):
        if board[i][i] != player:
            win = False
            break
    if win: return True

    # Check secondary diagonal
    win = True
    for i in range(4):
        if board[i][3-i] != player:
            win = False
            break
    if win: return True

    return False

def check_tie(board):
    for row in board:
        if '-' in row:
            return False
    return True

def draw_board(board):
    stddraw.setXscale(0, 4)
    stddraw.setYscale(0, 4)

    # Draw the horizontal and vertical grid lines
    for i in range(5):
        stddraw.line(i, 0, i, 4)
        stddraw.line(0, i, 4, i)

    # Draw the pieces on the board
    for i in range(4):
        for j in range(4):
            if board[i][j] != '-':
                stddraw.text(j + 0.5, 3 - i + 0.5, board[i][j])

    # Show the drawing to the screen
    stddraw.show(1000)

    

def main():
    ##Display the empty board that will be played first to the players
    board = play_board()
    game = sys.argv[1]
    
    with open(game, 'r') as file:
        for line in file:
            player, row, col = line.split()
            row = int(row)
            col = int(col)
            
            placed = place_piece(board, row, col, player)
            if not placed: 
                print("The cell is already occupied. Please pick another cell.")
            else: 
                draw_board(board)  # Draw the updated board after a move
            for row in board:
                print(' '.join(row))
            
            if check_wins(board, player):
                print(player + " has won the game")
                return
            elif check_tie(board):
                print("The game is a tie!")
                return

if __name__ == '__main__':main()
