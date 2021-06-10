from flask import request, jsonify

from src import app

from src.models.materias import MateriasModelo


@app.route('/materias', methods=['POST'])
def registrar_materia():
    materiasModelo = MateriasModelo()

    nombre = request.json['nombre']
    semestre = request.json['semestre']

    materiasModelo.insertar_materia(nombre, semestre)

    return jsonify({
        'nombre': nombre,
        'semestre': semestre
    })


@app.route('/materias')
def materias_registradas():
    materiasModelo = MateriasModelo()
    lista = []
    materias = materiasModelo.traer_materias()
    
    for m in materias:
        lista.append({
            'id': m[0],
            'nombre': m[1],
            'semestre': m[2]
        })

    return jsonify(lista)


@app.route('/materias/<id_materia>/usuarios', methods=['GET'])
def usuarios_registrados_materia(id_materia):

    materiasModelo = MateriasModelo()
    lista = []
    usuarios = materiasModelo.traer_usuarios_materia(id_materia)
    for u in usuarios:
        lista.append({
            'id': u[0],
            'semestre': u[1],
            'identificacion': u[2],
            'nombre': u[3],
            'apellido': u[4],
            'email': u[5],
            'telefono': u[6],
            'materia': materiasModelo.traer_materia(id_materia)[1]
        }) 

    return jsonify(lista)






