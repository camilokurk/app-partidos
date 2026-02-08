from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    nombre = Column(String, nullable=True)
    min_tot = Column(Integer, default=0)

class RegistroTiempo(Base):
    __tablename__ = 'registro_tiempo'
    id = Column(Integer, primary_key=True)
    jugador_id = Column(Integer)
    min_entrada = Column(Integer)
    min_salida = Column(Integer, nullable=True)
    
class PartidoActivo(Base):
    __tablename__ = 'partido'
    id = Column(Integer, primary_key=True)
    convocados = Column(String, nullable=False)
    en_pista = Column(String, nullable=False)
    cuarto_actual = Column(Integer, nullable=False, default=1)
    cuartos_jugados = Column(String, nullable=False, default=0)

class HistorialCuartos(Base):
    __tablename__ = 'historial_cuartos'
    id = Column(Integer, primary_key=True)
    numero_cuarto = Column(Integer)
    en_pista = Column(String)
    banquillo = Column(String)