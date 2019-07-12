from flask import Flask

# Inicializacion de la app
app = Flask(__name__, instance_relative_config=True)

# Cargar Vistas 
from app import views

# Cargar archivo de configuracion
app.config.from_object('config')