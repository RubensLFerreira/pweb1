from flask import Blueprint, render_template

sobre = Blueprint('sobre', __name__)

@sobre.route('/sobre')
def sobres():
    return render_template('sobre.html')