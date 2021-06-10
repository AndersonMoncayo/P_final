from src.config.db import DB

class SesionesModelo():

    def insertar_session(self, id_materia, nombre, fecha, inicia, termina):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO sesiones(id_materia, nombre, fecha, inicia, termina) VALUES(?,?,?,?,?)',(id_materia, nombre, fecha, inicia, termina,))
        
        cursor.close()

    def traer_sesiones_materia(self, id_materia):
        cursor = DB.cursor()

        cursor.execute('SELECT * FROM sesiones WHERE id_materia = ?',(id_materia,))
        sesiones = cursor.fetchall()

        cursor.close()
        return sesiones

    def traer_usuarios_sesion(self, id_sesion):
        cursor = DB.cursor()

        cursor.execute('SELECT usuarios.id, usuarios.semestre, usuarios.identificacion, usuarios.nombre, usuarios.apellido, usuarios.email, usuarios.telefono, s_u.asistencia, s_u.id FROM sesiones_usuarios AS s_u INNER JOIN usuarios ON s_u.id_usuario = usuarios.id INNER JOIN sesiones ON s_u.id_sesion = sesiones.id WHERE sesiones.id = ?',(id_sesion,))
        usuarios = cursor.fetchall()

        cursor.close()
        
        return usuarios


    def traer_sesion(self,id_materia,nombre,fecha,inicia,termina):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM sesiones WHERE id_materia=? and nombre=? and fecha=? and inicia=? and termina=?',(id_materia,nombre,fecha,inicia,termina,))

        sesion = cursor.fetchone()
        return sesion 


    def insertar_usuario_sesiones(self, id_usuario, id_sesion):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO sesiones_usuarios(id_usuario,id_sesion) VALUES(?,?)',(id_usuario,id_sesion,))

        cursor.close()

    def confirmar_asistencia(self,verificacion, id_sesion_usuario,):
        cursor = DB.cursor()
        cursor.execute('UPDATE sesiones_usuarios SET asistencia = ? WHERE id = ?',(verificacion,id_sesion_usuario,))
        cursor.close()


    def eliminar_usuario_sesiones(self, id_usuario, id_sesion):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM sesiones_usuarios WHERE id_usuario and id_sesion= ?',(id_usuario, id_sesion,))
        cursor.close()

    
