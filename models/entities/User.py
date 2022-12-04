from werkzeug.security import check_password_hash
from flask_login import UserMixin
class User(UserMixin):
    def __init__(self, id, nombre, apellidos, correo, password, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac, perfil ) -> None:
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.edad = edad
        self.pais = pais
        self.estado = estado
        self.municipio = municipio
        self.cp = cp
        self.colonia = colonia
        self.calle = calle
        self.fechanac = fechanac
        self.perfil = perfil

    @classmethod
    def validar_clave(self, passwordCifrada, password):
        return check_password_hash(passwordCifrada, password)
