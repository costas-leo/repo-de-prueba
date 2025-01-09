from flask import Flask
from flask_mysqldb import MySQL
from .configuracion import Config  # Importar la configuración

mysqlPPp = MySQL()  # Crear una instancia de MySQL

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = Config.MYSQL_HOST
    app.config['MYSQL_USER'] = Config.MYSQL_USER
    app.config['MYSQL_DB'] = Config.MYSQL_DB

    # Inicializar MySQL
    mysqlPPp.init_app(app)

    return app