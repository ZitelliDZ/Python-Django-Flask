from app import db


class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    email = db.Column(db.String(20))
    edad = db.Column(db.Integer)

    def __str__(self):
        return f'Persona: {self.id}, {self.nombre + ' ' + self.apellido}, {self.email}, Edad: {self.edad}'