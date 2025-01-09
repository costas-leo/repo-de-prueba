from app import create_app
from app.routes import routes

# Crear la aplicación Flask
app = create_app()

# Registrar las rutas
app.register_blueprint(routes)

if __name__ == "__main__":
    print("Iniciando la aplicación Flask en http://127.0.0.1:5000/")
    app.run(debug=True)
