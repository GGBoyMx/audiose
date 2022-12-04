from models.entities.User import User

class ModelUser:
    @classmethod
    def login(self,db,usuario):
        try:
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE correo = %s",(usuario.correo,))
            u = selUsuario.fetchone()
            if u is not None:
                return User(u[0],u[1],u[2],u[3],User.validar_clave(u[4],usuario.password),u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14]) 
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db , id):
        try:
            selUsuario = db.connection.cursor()
            selUsuario.execute("SELECT * FROM usuario WHERE id = %s",(id,))
            u = selUsuario.fetchone()
            if u is not None:
                return User(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8],u[9],u[10],u[11],u[12],u[13],u[14])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def clave(self,db,usuario):
        try:
            SelUsuario = db.connection.cursor()
            SelUsuario.execute("SELECT * FROM usuario WHERE id = %s", (usuario.id,))
            u = SelUsuario.fetchone()
            if u is not None:
                return User(u[0],u[1],u[2],u[3],User.validar_clave(u[4],usuario.password),u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14]) 
                # return User(u[0],u[1],u[2],u[3],u[4],u[5],User.validar_clave(u[6],usuario.password),u[7],u[8],u[9],u[10],u[11],u[12],u[13],u[14])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)