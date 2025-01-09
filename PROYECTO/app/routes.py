from flask import Blueprint, jsonify, request
from .funciones import obtener_productos, insertar_producto  # Import relativo

routes = Blueprint('routes', __name__)

@routes.route('/productos', methods=['GET'])
def lista_productos():
    productos = obtener_productos()
    return jsonify(productos)

@routes.route('/productos', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')
    insertar_producto(nombre, precio)
    return jsonify({"message": "Producto agregado exitosamente"}), 201
