from flask import Blueprint, render_template

alteracao = Blueprint('alteracao', __name__)

@alteracao.route('/alteracao')
def alteracoes():
    return render_template('alteracao.html')