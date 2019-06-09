from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/solved', methods=['GET', 'POST'])
def solved():
    val = ''
    if request.method == 'POST':
        val = request.form['A1']

    for x in request.form:
        if not request.form[x]:
            print('-')
        else:
            print(request.form[x])
    return render_template('form.html', data=val)



if __name__ == '__main__':
 app.run(debug=True)
