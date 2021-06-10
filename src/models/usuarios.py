from src.config.db import DB

class UsuariosModelo():

    def insertar_usuario(self, semestre, identificacion, nombre, apellido, email, telefono):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO usuarios(semestre,identificacion, nombre, apellido, email, telefono) VALUES(?,?,?,?,?,?)',(semestre, identificacion, nombre, apellido, email, telefono,))

        cursor.close()

    def traer_usuarios(self):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM usuarios')

        usuarios = cursor.fetchall()

        return usuarios

    def traer_usuario(self, id_usuario):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE id = ?',(id_usuario,))

        usuario = cursor.fetchone()

        return usuario

    def insertar_usuario_materia(self, id_usuario, id_materia):
        cursor = DB.cursor()

        cursor.execute('INSERT INTO materias_usuarios(id_usuario, id_materia) VALUES(?,?)',(id_usuario,id_materia,))

        cursor.close()

    def editar_usuario(self, id_usuario,semestre, identificacion, nombre, apellido, email, telefono):
        cursor = DB.cursor()

        cursor.execute('UPDATE usuarios SET semestre=?, identificacion=?, nombre=?, apellido=?, email=?, telefono=? WHERE id=?',(semestre, identificacion, nombre, apellido, email, telefono,id_usuario,))
        cursor.close()

    def eliminar_usuario(self, id_usuario):

        cursor = DB.cursor()
        cursor.execute('DELETE FROM usuarios WHERE id = ?',(id_usuario,))
        cursor.close()

    




