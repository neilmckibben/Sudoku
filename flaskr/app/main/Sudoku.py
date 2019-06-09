import numpy
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

        self.board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]
        """self.board.append([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


        self.cols = self.digits
        self.squares = self.cross(self.rows, self.cols)


        self.unit_list = ([self.cross(self.rows, c) for c in self.cols] +
                    [self.cross(r, self.cols) for r in self.rows] +
                    [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unit_list if s in u])
                     for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s]))
                     for s in self.squares)
        """

    def cross(A, B):
        "Cross product of elements in A and elements in B."
        return [a + b for a in A for b in B]


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
            print(self.board[row][i])
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
                print(self.board[i + scaled_row][j + scaled_collum])
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
mmmm
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




def main():
    print("Hello World!")
    test = Sudoku()
    test.print_board()
    if(test.solve_sudoku()):
            test.print_board()
    else:
        print("rip")


if __name__== "__main__":
  main()
