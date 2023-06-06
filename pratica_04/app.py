from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Criando o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))

# Rota inicial
@app.route('/')
def index():
  return render_template('index.html')

# Roda de cadastro
@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nome = request.form['nome']

    cliente = Cliente(
      nome=nome,
    )

    db.session.add(cliente)
    db.session.commit()

    return redirect(url_for('clientes'))
  else:
    return render_template('cadastro.html')

# Rota de clientes
@app.route('/lista-tarefas')
def clientes():
  clientes = Cliente.query.all()
  return render_template('clientes.html', clientes=clientes)

# SObre o cliente
@app.route('/sobre/<int:id>')
def sobre(id):
  cliente = Cliente.query.get(id)
  return render_template('sobre.html', cliente=cliente)

# Alterar ou excluir cliente
@app.route('/concluidas/<int:id>')
def alteracao(id):
  cliente = Cliente.query.get(id)
  return render_template('concluidas.html', cliente=cliente)

# Editar cliente
@app.route('/alteracao/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('clientes'))
    else:
        return render_template('editar.html', cliente=cliente)

# Excluir o cliente
@app.route('/alteracao/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
  cliente = Cliente.query.get(id)
  if cliente:
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes'))
  else:
    return render_template('clientes.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)