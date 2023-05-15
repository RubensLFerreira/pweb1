from flask import Blueprint, render_template

clientes = Blueprint('clientes', __name__)

@clientes.route('/clientes')
def cliente():
    return render_template('clientes.html')