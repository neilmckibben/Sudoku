from flask import Flask, render_template, request
from Sudoku import Sudoku

intValues = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
            'I': 8 }



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/solved', methods=['GET', 'POST'])
def solved():
    board = Sudoku()
    if request.method == 'POST':
        for x in request.form:
            (i, j) = x
            j = int(j)
            if request.form[x]:
                board.setVal(intValues[i], (j-1), request.form[x])
        board.print_board()
    if(board.solve_sudoku()):
            board.print_board()
    values = board.toMap()
    return render_template('solved.html', values=values)



if __name__ == '__main__':
 app.run(debug=True)
