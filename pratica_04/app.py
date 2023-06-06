from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Criando o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)


class Tarefa(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  status = db.Column(db.Boolean, default=False)


# Rota inicial
@app.route('/')
def index():
  return render_template('index.html')


# Roda de cadastro
@app.route('/adicionar-tarefa', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nome = request.form['nome']

    tarefa = Tarefa(
        nome=nome,
    )

    db.session.add(tarefa)
    db.session.commit()

    return redirect(url_for('tarefas'))
  else:
    return render_template('cadastro.html')


# Rota de tarefas
@app.route('/lista-tarefas-pendentes')
def tarefas():
  tarefas = Tarefa.query.filter(Tarefa.status == False).all()
  return render_template('tarefas.html', tarefas=tarefas)


@app.route('/lista-tarefas-concluidas')
def concluidas():
  tarefas = Tarefa.query.filter(Tarefa.status == True).all()
  return render_template('concluidas.html', tarefas=tarefas)


# Alterar ou excluir cliente
@app.route('/concluidas/<int:id>')
def concluidasId(id):
  tarefa = Tarefa.query.get(id)
  if tarefa:
    tarefa.status = True
    db.session.commit()
    return redirect(url_for('tarefas'))


# Excluir o cliente
@app.route('/alteracao/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
  tarefa = Tarefa.query.get(id)
  if tarefa:
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('concluidas'))


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)
