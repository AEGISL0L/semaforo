from app import app
from models import db, Semaforo

with app.app_context():
    db.create_all()

    # Crear semáforos iniciales
    semaforo1 = Semaforo(nombre='Semáforo 1', estado='rojo')
    semaforo2 = Semaforo(nombre='Semáforo 2', estado='verde')
    semaforo3 = Semaforo(nombre='Semáforo 3', estado='amarillo')

    # Agregar a la sesión y confirmar
    db.session.add_all([semaforo1, semaforo2, semaforo3])
    db.session.commit()
