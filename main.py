from hash import Hash
from treeState import TreeState
import copy
import os

def main():
    os.system('cls')
    board = Hash()
    print('----------------------\n   Seu símbolo é o X\n----------------------')
    board.get_board()

    while (1):
        i = int(input('\nDigite um número para a linha: '))
        j = int(input('Digite um número para a coluna: '))
        board.set_board('X', i, j)

        if finish(board):
            break

        board = minimax(board)

        if finish(board):
            break

        os.system('cls')
        print('----------------------\n   Seu símbolo é o X\n----------------------')
        board.get_board()

def finish(board):
    os.system('cls')
    if board.wins('X'):
        board.get_board()
        print('\nFim de jogo! Vitória de X')
        return True
    elif board.wins('o'):
        board.get_board()
        print('\nFim de jogo! Vitória de o')
        return True
    elif not board.empty_cells():
        board.get_board()
        print('\nEmpate!')
        return True
    else:
        return False

def minimax(board):
    state = TreeState(copy.deepcopy(board))
    v = max_value(state)

    for next_state in state.next_states:
        if next_state.utility == v:
            return next_state.current_state

def max_value(state):
    state.set_next_states('o')

    if state.finish_game():
        return state.utility

    v = -9999999

    for each_state in state.next_states:
        v = max(v, min_value(each_state))

    state.utility = v
    return v


def min_value(state):
    state.set_next_states('X')

    if state.finish_game():
        return state.utility

    v = 9999999

    for each_state in state.next_states:
        v = min(v, max_value(each_state))

    state.utility = v
    return v

if __name__ == '__main__':
    main()