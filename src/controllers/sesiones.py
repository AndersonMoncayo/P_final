
from flask import request, jsonify

from src import app

from src.models.materias import MateriasModelo
from src.models.usuarios import UsuariosModelo
from src.models.sesiones import SesionesModelo

@app.route('/sesiones/<id_sesion>/usuarios', methods=['GET','POST'])
def usuarios_sesiones(id_sesion):
    sesionesModelo = SesionesModelo()
    lista = []
    usuarios = sesionesModelo.traer_usuarios_sesion(id_sesion)

    for u in usuarios:
        if u[7]==None:
            asistencia  = 'http://127.0.0.1:5000/sesiones/'+str(u[8])+'/usuarios'
        else:
            if u[7]==1:
                asistencia = 'si asistio'
            else:
                asistencia = 'no asistio'

        lista.append({
            'id':u[0],
            'semestre':u[1],
            'identificacion':u[2],
            'nombre':u[3],
            'apellido': u[4],
            'email':u[5],
            'telefono':u[6],
            'asistencia': asistencia
        })
    
    return jsonify(lista)


@app.route('/sesiones/<id_sesion_estudiante>/usuarios', methods=['PUT'])
def confirmar_asistencia(id_sesion_estudiante):

    sesionesModelo = SesionesModelo()
    verificacion = request.json['verificacion']
    sesionesModelo.confirmar_asistencia(verificacion,id_sesion_estudiante)
    
    return jsonify(message='Verificado')



@app.route('/sesiones/<id_materia>', methods=['GET','POST'])
def sesiones(id_materia):
    sesionesModelo = SesionesModelo()
    materiasModelo = MateriasModelo()
    usuariosModelo = UsuariosModelo()

    if request.method == 'GET':
        lista = []
        sesiones = sesionesModelo.traer_sesiones_materia(id_materia)
        for s in sesiones:
            lista.append({
                'id': s[0],
                'materia': materiasModelo.traer_materia(id_materia)[1],
                'nombre':s[2],
                'fecha': str(s[3]),
                'inicia': str(s[4]),
                'termina': str(s[5])
            })
        
        return jsonify(lista)


    #idMateria = request.json['idMateria']
    nombre = request.json['nombre']
    fecha = request.json['fecha']
    inicia = request.json['inicia']
    termina = request.json['termina']
    sesionesModelo.insertar_session(id_materia,nombre,fecha,inicia,termina)
    
    usuarios = materiasModelo.traer_usuarios_materia(id_materia)
    sesion  = sesionesModelo.traer_sesion(id_materia,nombre,fecha,inicia,termina)
    print(sesion)
    for u in usuarios:
        sesionesModelo.insertar_usuario_sesiones(u[0],sesion[0])


    print(id_materia,nombre,fecha,inicia,termina)
    return jsonify({
        'materia': materiasModelo.traer_materia(id_materia)[1],
        'nombre': nombre,
        'fecha': fecha,
        'inicia': inicia,
        'termina': termina
    })




