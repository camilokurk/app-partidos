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
    jugadores = db.listar_jugadores()
    return render_template('partido.html', jugadores=jugadores)

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

@app.route('/seleccionar_convocados', methods=['POST'])
def seleccionar_convocados():
    convocados = request.form.getlist('convocado')
    titulares = request.form.getlist('titular')

    convocados = [int(x) for x in convocados]
    titulares = [int(x) for x in titulares]
    
    en_pista = titulares.copy()

    cuartos_jugados = {jugador: 0 for jugador in convocados}
    
    banquillo = []
    for jugador in convocados:
        if jugador not in en_pista:
            banquillo.append(jugador)
    
    descansan = []
    salen_a_pista = []

    if len(convocados) >= 7:
        calcular_cambios(convocados, en_pista, banquillo, descansan, salen_a_pista)
        
        for jugador in salen_a_pista:
            cuartos_jugados[jugador] +=1
        en_pista = salen_a_pista.copy()

        banquillo = []
        for jugador in convocados:
            if jugador not in en_pista:
                banquillo.append(jugador)

        descansan = []
        salen_a_pista = []

        db.guardar_partido_activo(convocados, en_pista, 1, cuartos_jugados)

        return redirect('/partido/cuartos')
    else:
        return redirect('/seleccionar_convocados')

@app.route('/partido/cuartos')
def cuartos():
    partido = db.obtener_partido_activo()
    jugadores = db.listar_jugadores()

    convocados = partido['convocados']
    en_pista = partido['en_pista']

    banquillo = []
    for jugador in convocados:
        if jugador not in en_pista:
            banquillo.append(jugador)

    return render_template('cuartos.html', partido=partido, jugadores=jugadores, banquillo = banquillo)

@app.route('/siguente_cuarto', methods=['POST'])
def siguiente_cuarto():
    partido = db.obtener_partido_activo()

    convocados = partido['convocados']
    en_pista = partido['en_pista']
    cuarto_actual = partido['cuarto_actual']
    cuartos_jugados = partido['cuartos_jugados']

    banquillo = []
    for jugador in convocados:
        if jugador not in en_pista:
            banquillo.append(jugador)

    db.guardar_historial_cuarto(numero_cuarto=cuarto_actual, 
                                en_pista=en_pista, 
                                banquillo=banquillo)
    
    descansan = []
    salen_a_pista = []
    
    calcular_cambios(convocados, en_pista, banquillo, descansan, salen_a_pista)
    
    for jugador in salen_a_pista:
        cuartos_jugados[jugador] +=1
    en_pista = salen_a_pista.copy()

    banquillo = []
    for jugador in convocados:
        if jugador not in en_pista:
            banquillo.append(jugador)


    db.guardar_partido_activo(convocados, en_pista, cuarto_actual + 1, cuartos_jugados)

    return redirect('/partido/cuartos')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

