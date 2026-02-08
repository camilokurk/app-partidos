import json

from .models import Jugador
from .models import PartidoActivo
from .models import HistorialCuartos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

class DatabaseManager:
    def __init__(self, db_path='data/preminis.db'):
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(self.engine)
        self.session = Session()

    def agregar_jugador(self, nombre, numero):
        if not nombre or not numero:
            print("No se han completado los campos")
            return
        
        jugador_existente = self.session.query(Jugador).filter(Jugador.numero == numero).first()

        if jugador_existente:
            print(f"Error: Ya existe un jugador con el número {numero}")
        else:
            nuevo_jugador = Jugador(nombre=nombre, numero=numero)
            self.session.add(nuevo_jugador)
            self.session.commit()

    def quitar_jugador(self, numero):
        jugador_existente = self.session.query(Jugador).filter(Jugador.numero == numero).first()

        if jugador_existente:
            self.session.delete(jugador_existente)
            self.session.commit()
        else:
            print("El jugador no existe")

    def listar_jugadores(self):
        jugadores = self.session.query(Jugador).all()
        return jugadores
    
    def guardar_partido_activo(self, convocados, en_pista, cuarto_actual, cuartos_jugados):
        partido = self.session.query(PartidoActivo).filter(PartidoActivo.id == 1).first()
        
        convocados_json = json.dumps(convocados)
        en_pista_json = json.dumps(en_pista)
        cuarto_actual_json = json.dumps(cuarto_actual)
        cuartos_jugados_json = json.dumps(cuartos_jugados)

        if partido:
            partido.convocados = convocados_json
            partido.en_pista = en_pista_json
            partido.cuarto_actual = cuarto_actual_json
            partido.cuartos_jugados = cuartos_jugados_json
        else:
            nuevo = PartidoActivo(
                id=1, 
                convocados = convocados_json, 
                en_pista = en_pista_json, 
                cuarto_actual = cuarto_actual_json,
                cuartos_jugados = cuartos_jugados_json)
            self.session.add(nuevo)
        
        self.session.commit()

    def obtener_partido_activo(self):
        partido = self.session.query(PartidoActivo).filter(PartidoActivo.id == 1).first()

        if not partido:
            return None
        
        convocados = json.loads(partido.convocados)
        en_pista = json.loads(partido.en_pista)
        cuarto_actual = partido.cuarto_actual
        cuartos_jugados = json.loads(partido.cuartos_jugados)

        return {
            'convocados': convocados,
            'en_pista': en_pista,
            'cuarto_actual': cuarto_actual,
            'cuartos_jugados': cuartos_jugados
        }
    
    def guardar_historial_cuarto(self, numero_cuarto, en_pista, banquillo):      
        
        en_pista_json = json.dumps(en_pista)
        banquillo_json = json.dumps(banquillo)

        cuarto = HistorialCuartos(
            numero_cuarto = numero_cuarto,
            en_pista = en_pista_json,
            banquillo = banquillo_json
        )
        self.session.add(cuarto)
        self.session.commit()

    def obtener_historial_partido(self):
        cuartos = self.session.query(HistorialCuartos).order_by(HistorialCuartos.numero_cuarto).all()

        historial = []
        for cuarto in cuartos:
            historial.append({
                'numero_cuarto': cuarto.numero_cuarto,
                'en_pista': json.loads(cuarto.en_pista),
                'banquillo': json.loads(cuarto.banquillo)
            })
        
        return historial
    


