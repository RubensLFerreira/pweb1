from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/alteracao')
def alteracao():
    return render_template('alteracao.html')

if __name__ == '__main__':
    app.run(debug=True)