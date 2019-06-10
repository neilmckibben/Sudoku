import numpy
from flask import Flask, render_template, request
intValues = { 0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
            8: 'I' }
stringValues = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
            'I': 8 }


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

    def solve(self, request):
        for x in request.form:
            (i, j) = x
            j = int(j)
            print(x)
            if request.form[x]:
                self.setVal(stringValues[i], (j-1), request.form[x])

        return self.toMap()


    def toMap(self):
        data = dict()
        for i in range(9):
            for j in range(9):
                val =  intValues[i] + str(j+1)
                data[val] = self.board[i][j]
        return data

    def setVal(self, i, j, val):
        print(i, j, val)
        self.board[i][j] = val


    def horizontal_check(self, i,j):
        return self.master_number - set(self.board[i])

    def vertical_check(self, i,j):
        ret_set = []
        for x in range(9):
            ret_set.append(self.board[x][j])
        return self.master_number - set(ret_set)

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if (j) % 3 == 0 and 0 < j < 8:
                    print("|", end=' ')
                print(val, end=' ')
            print()
            if (i - 2) % 3 == 0 and i < 8:
                print("_____________________", end='')
                print()
            print()
        print()
        print("||||||||||||||||||||||")

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

            # if looks promising
            if (self.not_used(row, col, num)):

                # make tentative assignment
                self.board[row][col] = num

                # return, if success, ya!
                if (self.solve_sudoku()):
                    return True

                # failure, unmake & try again
                self.board[row][col] = 0

        # this triggers backtracking
        return False
