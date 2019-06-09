import numpy
intValues = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
            8: 'I' }
class Sudoku:
    master_number = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    board = []
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = ""
    squares = {}
    unit_list = {}
    units = {}
    peers = {}

    board = []
    def __init__(self):
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


    def toMap(self):
        for i in range(9):
            for j in range(9):

                val =  intValues[i] + str(j+1)
                print(val)

    def setVal(self, i, j, val):
        self.board[i][j] = val


    def print_board(self):
        count = 0
        for i in range(9):
            print('\n')
            for j in range(9):
                print(self.board[i][j], end = " ")

    def used_in_row(self, row, num):
        for i in range(9):
            if (self.board[row][i] == num):
                return True
        return False

    def used_in_col(self, col, num):
        for i in range(9):
            if (self.board[i][col] == num):
                return True
        return False

    def not_solved(self):
        for i in range(9):
            for j in range(9):
                if(self.board[i][j] == 0):
                    return True

        return False


    def unassigned(self, position):
        for i in range(9):
            for j in range(9):
                if(self.board[i][j] == 0):
                    position[0] = i
                    position[1] = j
                    return True
        return False

    def used_in_box(self,  row, col, num):
        scaled_row = ((row//3) * 3)
        scaled_collum = ((col//3) * 3)
        for i in range(3):
            for j in range(3):
                if (self.board[i + scaled_row][j + scaled_collum] == num):
                    return True
        return False

    def not_used(self, row, col, num):
        return not self.used_in_col(col, num) and not self.used_in_row(row, num) and not self.used_in_box(row, col, num)

    # Takes a partially filled-in grid and attempts to assign values to
    # all unassigned locations in such a way to meet the requirements
    # for Sudoku solution (non-duplication across rows, columns, and boxes)
    def solve_sudoku(self):

        position = [0, 0]

        # If there is no unassigned location, we are done
        if not self.unassigned(position):
            return True

        # Assigning list values to row and col that we got from the above Function
        row = position[0]
        col = position[1]

        # consider digits 1 to 9
        for num in range(1, 10):

            if (self.not_used(row, col, num)):

                # make tentative assignment
                self.board[row][col] = num

                # return, if success, ya!
                if (self.solve_sudoku()):
                    return True, self

                # failure, unmake & try again
                self.board[row][col] = 0

        # this triggers backtracking
        return False, self
