from hash import Hash
import os

board = Hash()
board.get_board()

while board.empty_cells():
    i = int(input('\nDigite um número para a linha: '))
    j = int(input('Digite um número para a coluna: '))
    board.set_board('X', i, j)
    if board.wins('X') or board.wins('o'):
        print('\nFim de jogo!')
        break
        
    aux = 0
    for row in range(3):
        for column in range(3):
            if board.get_cell(row, column) == 0 and aux == 0:
                board.set_board('o', row, column)
                aux = 1

    os.system('cls')
    board.get_board()
    if board.wins('X') or board.wins('o'):
        print('\nFim de jogo!')
        break
