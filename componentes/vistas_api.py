from flask import jsonify
from flask import render_template
from flask import request

from app import app
from componentes.modelos import Persona

@app.route("/api-subs/subs", methods=['POST'])
def crear_():
    
    if request.method == 'POST':
        datos = request.json["datos"]
    
        subs_nuevo = Persona(  
                 datos['nombre'],
                 datos['apellido'],
                 datos['correo'],
                 datos['whatsapp']
             )
        subs_nuevo = subs_nuevo.guardar_db()
        print(request.json)
        respuesta = {'mensaje': subs_nuevo}
    else: 
        respuesta = {'mensaje': 'no se recibieron datos.'}

    return jsonify(respuesta)

@app.route('/api-subs/subs' , methods=["GET"]) # 127.0.0.1:5000/api-subs/subs
def obtener_subs():
    datos = Persona.obtener()
    datos = [vars(d) for d in datos]
    return jsonify(datos)


# estaba en el endpoint de arriba
'''
try:
    cursor = conexion.cursor(dictionary=True)
except Exception as e:
    print(e)
    print('reconexión')
    conexion.connect()
    cursor = conexion.cursor(dictionary=True)
        
    cursor.execute('SELECT * FROM persona;')
'''

@app.route('/api-subs/subs', methods=['PUT'])
def modificar_subs(id):
    datos = request.json["datos"]
    if Persona.modificar(id, datos):
        return jsonify({'mensaje': 'Suscripción modificada exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Error al modificar la Suscripción'}), 404

@app.route('/api-subs/subs/<int:id>', methods=['DELETE'])
def eliminar_subs(id):
    
    suscripcion = Persona(id)  
    if suscripcion:
        Persona.eliminar(suscripcion)  
        return jsonify({"message": "Suscripción eliminada exitosamente"}), 200
    else:
        return jsonify({"message": "Suscripción no encontrada"}), 404
    
# @app.route('/api-subs/subs', methods=['DELETE'])
# def eliminar_():
    
#     if request.method == 'DELETE':
#         datos = request.json["datos"]
#         subs = subs.obtener('correo', datos)
        
#         eliminar_subs = Persona.eliminar(Persona.id)
       
        
#         if eliminar_subs:
#             respuesta = {'mensaje': eliminar_subs}
#         else:
#             respuesta = {'mensaje': 'Algo salió mal!'}
    
#     else:
#         respuesta = {'mensaje': 'no se recibieron datos.'}
        
#     return jsonify(respuesta)


    
 