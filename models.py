from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Semaforo(db.Model):
    __tablename__ = 'semaforo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(10), nullable=False)  # 'rojo', 'amarillo', 'verde'

    def __repr__(self):
        return f'<Semaforo {self.nombre}>'
