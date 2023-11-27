from dotenv import dotenv_values
from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from db_connect import db
from forms import PersonaForm
from models import Persona


app = Flask(__name__)


config = dotenv_values(".env")

# config flask-Migrate
migrate = Migrate()
migrate.init_app(app,db)

# config flask-Migrate
app.config['SECRET_KEY']= config.get('SECRET_KEY')

user_db = config.get('USER_DB')
pass_db = config.get('PASS_DB')
host_db = config.get('HOST_DB')
port_db = config.get('PORT_DB')
name_db = config.get('NAME_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user_db}:{pass_db}@{host_db}:{port_db}/{name_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)




@app.route('/')
@app.route('/index')
def index():
    #personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_personas = Persona.query.count()
    app.logger.debug(f'Listado de Personas: {personas}')
    app.logger.debug(f'Total: {total_personas}')
    return render_template('index.html',personas=personas,total=total_personas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    #persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver Persona: {persona}')
    return render_template('ver_detalle.html',persona=persona)

@app.route('/agregar',methods=['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar: {persona}')
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('agregar.html',forma=personaForm)

@app.route('/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a editar: {persona}')
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('editar.html',forma=personaForm)
@app.route('/eliminar/<int:id>',methods=['GET','POST'])
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminar: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))
