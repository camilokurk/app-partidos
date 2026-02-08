# Gestor de Rotaciones de Baloncesto

> ⚠️ **Proyecto en desarrollo activo** - Esta aplicación está en construcción y todo está sujeto a mejoras y cambios.

Aplicación web para gestionar las rotaciones de jugadores durante partidos de baloncesto, diseñada para equipos de categorías base.

## 📋 Descripción

Aplicación Flask que ayuda a llevar el control de las rotaciones durante los partidos, buscando que todos los jugadores reciban tiempo de juego de forma equilibrada. 

**Estado actual:** La lógica de rotaciones está en proceso de desarrollo y mejora continua.

## ✨ Funcionalidades Actuales

- **Gestión de Equipo**
  - Agregar y eliminar jugadores
  - Asignar números de camiseta
  - Ver plantilla completa

- **Inicio de Partido**
  - Seleccionar jugadores convocados
  - Elegir titulares
  - Mínimo 7 jugadores para iniciar

- **Sistema de Rotaciones** (en desarrollo)
  - Cálculo básico de cambios por cuarto
  - Seguimiento de cuartos jugados por jugador
  - Vista de jugadores en pista y banquillo

- **Historial**
  - Guardar rotaciones por cuarto

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: SQLite con SQLAlchemy ORM
- **Frontend**: HTML5, CSS3
- **Estilos**: Google Fonts (Roboto Condensed, SN Pro)

## 📦 Requisitos

- Python 3.7+
- pip

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install flask sqlalchemy
```

4. **Crear directorio de datos**
```bash
mkdir data
```

5. **Ejecutar la aplicación**
```bash
python main.py
```

6. **Acceder a la aplicación**
```
http://localhost:5000
```

## 📖 Uso Básico

1. **Configurar Equipo**: Agrega jugadores con nombre y número
2. **Iniciar Partido**: Selecciona convocados (mínimo 7) y titulares
3. **Gestionar Cuartos**: Visualiza jugadores en pista y banquillo con sus cuartos jugados

La aplicación se abrirá en `http://localhost:5000`

## 📁 Estructura del Proyecto

```
.
├── main.py                      # Aplicación Flask principal
├── data/
│   └── *.db                     # Base de datos SQLite (auto-generada)
│
├── src/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py            # Modelos de base de datos
│   │   └── db_manager.py        # Gestor de BD
│   └── logic/
│       ├── __init__.py
│       ├── rotaciones.py        # Lógica de rotaciones (en desarrollo)
│       └── estadisticas.py      # (pendiente de implementar)
│
├── templates/
│   ├── equipo.html              # Gestión del equipo
│   ├── partido.html             # Selección de convocados
│   ├── cuartos.html             # Vista de cuartos
│   └── config.html              # (pendiente de implementar)
│
├── static/
│   └── css/
│       └── style.css            # Estilos
│
└── .gitignore
```

## 🎯 Lógica de Rotaciones (en desarrollo)

**Estado actual:** Implementación básica en proceso de mejora.

Funcionamiento actual:
- **Primer cuarto**: Juegan los titulares
- **Cuartos siguientes**: Los del banquillo salen a pista, priorizando a los que menos han jugado

Esta lógica está siendo revisada y mejorada constantemente.

## ⚠️ Limitaciones Conocidas

Funcionalidades aún por completar o mejorar:
- Navegación del menú inferior (enlaces por corregir)
- Botón "Siguiente cuarto" (pendiente de conectar)
- Página de configuración (vacía)
- Sistema de estadísticas (no implementado)
- Algoritmo de rotaciones (necesita optimización)

## 🎨 Interfaz

Diseño responsive optimizado para móvil:
- Tema oscuro
- Navegación inferior fija
- Fuentes de Google Fonts

## 🔧 Próximas Mejoras

Este proyecto está en desarrollo continuo. Algunas áreas en las que se está trabajando:

- Mejorar el algoritmo de rotaciones
- Completar la sección de configuración
- Optimizar la interfaz de usuario
- Implementar funcionalidades adicionales

## 📝 Notas de Desarrollo

- La base de datos se crea automáticamente en `data/`
- Algunos archivos están preparados para futuras funcionalidades
- El proyecto se ejecuta en modo debug

---

*Proyecto en construcción - Todo está abierto a cambios y mejoras* 🏀

