from .models import Jugador

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