from hash import Hash
import copy

class TreeState(Hash):
    def __init__(self, board):
        self.current_state = board
        self.next_states = []
        self.utility = None

    def set_next_states(self, symbol):
            for row in range(3):
               for column in range(3):
                    if self.current_state.get_cell(row, column) == '*':
                        current_state_copy = copy.deepcopy(self.current_state)
                        current_state_copy.set_board(symbol, row, column)
                        tree_current_state = TreeState(current_state_copy)
                        self.next_states.append(tree_current_state)

    def get_next_states(self):
        for state in self.next_states:
            state.current_state.get_board()

    def finish_game(self):
        if self.current_state.wins('o'):
            self.utility = 1
            return True
        elif self.current_state.wins('X'):
            self.utility = -1
            return True
        elif (len(self.next_states) == 0):
            self.utility = 0
            return True
        else:
            return False