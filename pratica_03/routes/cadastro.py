from flask import Blueprint, render_template

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastro')
def cadastros():
    return render_template('cadastro.html')