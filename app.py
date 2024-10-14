from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic_lights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models import Semaforo

@app.route('/')
def index():
    semaforos = Semaforo.query.all()
    return render_template('index.html', semaforos=semaforos)

@app.route('/semaforo/<int:id>')
def semaforo_detail(id):
    semaforo = Semaforo.query.get_or_404(id)
    return render_template('semaforo_detail.html', semaforo=semaforo)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    light = Semaforo.query.get_or_404(id)
    if request.method == 'POST':
        light.estado = request.form['estado']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', light=light)

if __name__ == '__main__':
    app.run(debug=True)
