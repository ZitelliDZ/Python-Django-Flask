from flask import Flask, render_template, url_for, jsonify, request
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from dotenv import dotenv_values
from flask import session

app = Flask(__name__)


config = dotenv_values(".env")
app.secret_key = config.get('SECRET_KEY')

@app.route("/")
def hello_world():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'You are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('hello_world'))

    return render_template('login.html')
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('hello_world'))

@app.route("/saludar/<nombre>", methods=['GET'])
def saludar(nombre):
    #return f"<p>Saludar {nombre.upper()}</p>"
    return render_template('mostrar.html',mostrar = nombre.upper())
@app.route("/edad/<int:edad>")
def mostrar_edad(edad):
    return f"<p>Saludar {edad + 1 }</p>"

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('saludar',nombre='Diego'))
@app.route('/salir')
def salir():
    return abort(404)


@app.route('/api/mostrar/<nombre>')
def mostrar_json(nombre):
    valores = {'nombre':nombre, 'method_http': request.method}
    return valores
    # return jsonify(valores)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return (render_template('error404.html',error=error),404)