
from flask import request, jsonify

from src import app

from src.models.materias import MateriasModelo
from src.models.usuarios import UsuariosModelo
from src.models.sesiones import SesionesModelo

@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    usuariosModelo = UsuariosModelo()
    
    semestre = request.json['semestre']
    identificacion = request.json['identificacion']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    telefono = request.json['telefono']

    usuariosModelo.insertar_usuario(semestre, identificacion, nombre, apellido, email, telefono)

    return jsonify({
        'semestre': semestre,
        'identificacion': identificacion,
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono
    })




@app.route('/usuarios', methods=['GET'])
def usuarios_registrardos():
    usuariosModelo = UsuariosModelo()
   
    lista = []
    usuarios = usuariosModelo.traer_usuarios()
    for u in usuarios:
        lista.append({
            'id':u[0],
            'semestre':u[1],
            'identificacion':u[2],
            'nombre':u[3],
            'apellido': u[4],
            'email':u[5],
            'telefono':u[6]
        })
    
    return jsonify(lista)

@app.route('/usuarios/<id_usuario>', methods=['PUT','DELETE'])
def editar_eliminar_usuario(id_usuario):
    usuariosModelo = UsuariosModelo()
  
    if request.method == 'DELETE':

        usuariosModelo.eliminar_usuario(id_usuario)
    

        return jsonify({
            'mensaje':'Eliminado'
        })
        

    semestre = request.json['semestre']
    identificacion = request.json['identificacion']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    telefono = request.json['telefono']

    usuariosModelo.editar_usuario(id_usuario,semestre, identificacion, nombre, apellido, email, telefono)

    return jsonify({
        'semestre':semestre,
        'identificacion':identificacion,
        'nombre':nombre,
        'apellido': apellido,
        'email':email,
        'telefono':telefono
    })

    



@app.route('/usuarios/<id_usuario>/materias/<id_materia>', methods=['POST','DELETE'])
def registrar_eliminar_usuario_materia(id_usuario, id_materia):

    usuariosModelo = UsuariosModelo()
    materiasModelo = MateriasModelo()
    sesionesModelo = SesionesModelo()

    if request.method == 'DELETE':
        

        materiasModelo.eliminar_materia_usuario(id_usuario,id_materia)
        sesiones = sesionesModelo.traer_sesiones_materia(id_materia)
        for s in sesiones:
            sesionesModelo.eliminar_usuario_sesiones(id_usuario, s[0])

        return jsonify({
            'mensaje':'Eliminado'
        })

    usuariosModelo.insertar_usuario_materia(id_usuario, id_materia)

    sesiones = sesionesModelo.traer_sesiones_materia(id_materia)
    
    for s in sesiones:
        sesionesModelo.insertar_usuario_sesiones(id_usuario,s[0])

    usuario = usuariosModelo.traer_usuario(id_usuario)
    return jsonify({
        'id': usuario[0],
        'semestre': usuario[1],
        'identificacion': usuario[2],
        'nombre': usuario[3],
        'apellido': usuario[4],
        'email': usuario[5],
        'telefono': usuario[6],
        'materia': materiasModelo.traer_materia(id_materia)[1]
    })



