from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  cpf = db.Column(db.String(11))
  nascimento = db.Column(db.String(11))
  email = db.Column(db.String(100))
  telefone = db.Column(db.String(20))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['telefone']
    nascimento = request.form['nascimento']

    cliente = Cliente(
      nome=nome,
      email=email,
      telefone=telefone,
      cpf=cpf,
      nascimento=nascimento
    )

    db.session.add(cliente)
    db.session.commit()

    return redirect(url_for('clientes'))
  else:
    return render_template('cadastro.html')

@app.route('/clientes')
def clientes():
  clientes = Cliente.query.all()
  return render_template('clientes.html', clientes=clientes)

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/alteracao')
def alteracao():
  return render_template('alteracao.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)