class Hash:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def set_board(self, symbol, i, j):
        self.board[i][j] = symbol

    def get_board(self):
        print('\n     0 | 1 | 2 ')
        print('    ------------')

        for row in range(3):
            print('{}  |'.format(row), end='')
            for column in range(3):
                symbol = self.board[row][column]
                print(f' {symbol} |', end='')
            print()

    def get_cell(self, i, j):
        return self.board[i][j]

    def wins(self, player):
        win_state = [[self.get_cell(0, 0), self.get_cell(0, 1), self.get_cell(0, 2)],
                     [self.get_cell(1, 0), self.get_cell(1, 1), self.get_cell(1, 2)],
                     [self.get_cell(2, 0), self.get_cell(2, 1), self.get_cell(2, 2)],
                     [self.get_cell(0, 0), self.get_cell(1, 0), self.get_cell(2, 0)],
                     [self.get_cell(0, 1), self.get_cell(1, 1), self.get_cell(2, 1)],
                     [self.get_cell(0, 2), self.get_cell(1, 2), self.get_cell(2, 2)],
                     [self.get_cell(0, 0), self.get_cell(1, 1), self.get_cell(2, 2)],
                     [self.get_cell(0, 2), self.get_cell(1, 1), self.get_cell(2, 0)]]

        if [player, player, player] in win_state:
            return True
        else:
            return False

    def empty_cells(self):
        for row in range(3):
            for column in range(3):
                if self.get_cell(row, column) == 0:
                    return True
        return False