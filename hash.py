class Hash:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def setBoard(self, symbol, i, j):
        self.board[i][j] = symbol

    def getBoard(self):
        print('     0 | 1 | 2 ')
        print('    ------------')

        for row in range(3):
            print('{}  |'.format(row), end='')
            for column in range(3):
                symbol = self.board[row][column]
                print(f' {symbol} |', end='')
            print()