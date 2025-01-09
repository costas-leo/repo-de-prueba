from configuracion import Config

mysqlPPp = MySQL()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = Config.MYSQL_HOST
    app.config['MYSQL_USER'] = Config.MYSQL_USER
    app.config['MYSQL_DB'] = Config.MYSQL_DB

    # Inicializar MySQL
    mysqlPPp.init_app(app)

    return app