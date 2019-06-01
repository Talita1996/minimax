from hash import Hash
import os

board = Hash()
board.getBoard()

i = int(input('Digite um número para a linha: '))
j = int(input('Digite um número para a coluna: '))

board.setBoard('X', i, j)
os.system('cls')
board.getBoard()
