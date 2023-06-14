from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)

class Pet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String())
  peso = db.Column(db.Float())
  raca = db.Column(db.String())
  porte = db.Column(db.String())
  sexo = db.Column(db.String())
  dono = db.Column(db.String())

def __repr__(self):
        return '<Pet %r>' % self.nome

@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/lista', methods=['GET', 'POST'])
def lista():
  pets = Pet.query.all();
  return render_template('lista.html', pets=pets)
  

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
  if request.method == 'POST':
    nome = request.form['nome']
    peso = request.form['peso']
    raca = request.form['raca']
    porte = request.form['porte']
    sexo = request.form['sexo']
    dono = request.form['dono']
    
    
    pet = Pet(
      nome = nome,
      peso = peso,
      raca = raca,
      porte = porte,
      sexo = sexo,
      dono = dono,
    )
    
    db.session.add(pet)
    db.session.commit()
    
    return redirect(url_for('lista'))
  else:
    return render_template('cadastrar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
  pet = Pet.query.get(id)
  if request.method == 'POST':
    pet.nome = request.form['nome']
    pet.peso = request.form['peso']
    pet.raca = request.form['raca']
    pet.porte = request.form['porte']
    pet.sexo = request.form['sexo']
    pet.dono = request.form['dono']
    db.session.commit()
    return redirect(url_for('lista'))
  else:
    return render_template('editar.html', pet=pet)

@app.route('/deletar/<int:id>')
def deletar(id):
  pet = Pet.query.get(id)
  if pet:
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('lista'))
  else: 
    return render_template('index')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)