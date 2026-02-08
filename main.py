from flask import Flask, render_template
from flask import request, redirect
from src.database.db_manager import DatabaseManager
from src.logic.rotaciones import calcular_cambios

app = Flask(__name__)
db = DatabaseManager()

@app.route('/')
def index():
    return redirect ('/equipo')

@app.route('/equipo')
def equipo():
    jugadores = db.listar_jugadores()
    return render_template('equipo.html', jugadores=jugadores)

@app.route('/partido')
def partido():
    return render_template('partido.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form["nombre"]
    numero = request.form["numero"]
    db.agregar_jugador(nombre, numero)
    return redirect ('/equipo')

@app.route('/quitar', methods=['POST'])
def quitar():
    numero = request.form["numero"]
    db.quitar_jugador(numero)
    return redirect ('/equipo')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

