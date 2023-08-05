from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'chavesecreta'

def init_db():
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
  conn.commit()
  conn.close()
init_db()

# Pego o id e faço a busca no banco
def username_by_id(user_id):   
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute('select username from users where id = (?)', (user_id,))
  
  # fetchone(): retorna uma tupla, então eu pego o primeiro elemento
  result = cursor.fetchone()
  
  conn.commit()
  conn.close()
  
  # if result: retorna o primeiro elemento da tupla, se não retorna None
  if result:
    return result[0]
  else:
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
  # Por algum motivo ele traz apenas o id, então criei uma função pra fazer a busca no banco
  user_id = session.get('username')
  username = username_by_id(user_id)
  return render_template('pages/index.html', username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('insert into users (username, password) values (?,?)', (username, password))
    conn.commit()
    conn.close()
    
    flash('Usuário cadastrado com sucesso!', 'success')
    return redirect(url_for('login'))
  else:
    flash('Usuário ou senha inválidos.', 'error')
    return render_template('pages/register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
  
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('select * from users where username = ? and password = ?', (username, password))
    
    # fetchone(): retorna uma tupla, então eu pego o primeiro elemento
    user = cursor.fetchone()
    conn.close()
  
    if user:
      # se user existir, a primeira posição do resultado da consulta é armazenada na sessão com a chave 'username' 
      session['username'] = user[0]
      flash('Login realizado com sucesso!', 'success')
      return redirect(url_for('index'))
    else:
      flash('Usuário ou senha inválidos.', 'error')
  return render_template('pages/login.html')
  
@app.route('/logout')
def logout():
  # pop: remove a chave 'username' da sessão
  session.pop('username', None)
  return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(debug=True)
    
  