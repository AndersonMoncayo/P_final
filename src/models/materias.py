
from src.config.db import DB

class MateriasModelo():

    def insertar_materia(self, nombre, semestre):

        cursor = DB.cursor()

        cursor.execute('INSERT INTO materias(nombre, semestre) VALUES(?,?)',(nombre, semestre,))
        cursor.close()

    def traer_materias(self):
        cursor = DB.cursor()
        
        cursor.execute('SELECT * FROM materias')
        materias = cursor.fetchall()
        return materias

    def traer_materia(self,id):
        cursor = DB.cursor()
        
        cursor.execute('SELECT * FROM materias WHERE id = ?',(id,))
        materia = cursor.fetchone()
        return materia

    def traer_usuarios_materia(self, id_materia):
        cursor = DB.cursor()

        cursor.execute('SELECT usuarios.id, usuarios.semestre, usuarios.identificacion, usuarios.nombre, usuarios.apellido, usuarios.email, usuarios.telefono FROM materias_usuarios AS m_s INNER JOIN materias ON m_s.id_materia = materias.id INNER JOIN usuarios ON m_s.id_usuario = usuarios.id WHERE materias.id = ?',(id_materia,))

        usuarios = cursor.fetchall()

        return usuarios


    def eliminar_materia_usuario(self, id_usuario, id_materia):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM materias_usuarios WHERE id_usuario = ? and id_materia = ?',(id_usuario,id_materia,))
        cursor.close()





