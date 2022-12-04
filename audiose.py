from flask import Flask, redirect, render_template, url_for, request, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
import datetime
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user, login_required
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl

audioseApp = Flask(__name__)
db = MySQL(audioseApp)
login_manager_app = LoginManager(audioseApp)
 
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@audioseApp.route('/')
def index():
    return render_template('index.html')

@audioseApp.route('/micarrito')
def micarrito():   
    return  render_template('micarrito.html')

@audioseApp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']
        passwordCifrada = generate_password_hash(password)
        telefono = request.form['telefono']
        edad = request.form['edad']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        cp = request.form['cp']
        colonia = request.form['colonia']
        calle = request.form['calle']
        fechanac = request.form['fechanac']

        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, apellidos, correo, password, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(nombre, apellidos, correo, passwordCifrada, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac))
        db.connection.commit()
        usuario = User(0, nombre, apellidos, correo, password, passwordCifrada, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac)
        usuarioAut = ModelUser.login(db, usuario)
        login_user(usuarioAut)        
        html = render_template('plantillac.html')
        sender = 'audioseapp@gmail.com'
        password = 'ewcwioojetsfuakl'
        receiver = correo
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = '!Bienvenido a AudioSE¡'
        message.attach(MIMEText(html, 'html'))
        pdfname = 'Chayanne.pdf'
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender, password)       
        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        return redirect(url_for('producto'))
    else:
        return render_template('register.html')
    
@audioseApp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = User(0, None, None, request.form['correo'], request.form['password'], None, None, None, None, None, None, None, None, None, None)
        usuarioAut = ModelUser.login(db, usuario)
        if usuarioAut is not None:
            if usuarioAut.password:
                login_user(usuarioAut)
                if usuarioAut.perfil == 'A':
                    return redirect(url_for('sUsuario'))
                else:
                    return redirect(url_for('producto'))
            else:
                flash('Contraseña Incorrecta')
                return redirect(request.url)
        else:
            flash('Usuario No Encontrado')
            return redirect(request.url)
    else:
        return render_template('index.html')

@audioseApp.route('/logout')
def logout():
    logout_user()
    return render_template('index.html') 

@audioseApp.route('/sUsuario', methods=['GET', 'POST'])
def sUsuario():
    selUsuario = db.connection.cursor()
    selUsuario.execute("SELECT * FROM usuario")
    u = selUsuario.fetchall()
    return render_template('admin.html',usuario = u)

@audioseApp.route('/dUsuario/<string:id>', methods=['GET','POST'])
def dUsuario(id):
    if request.method == 'GET':
        delUsuario = db.connection.cursor()
        delUsuario.execute("DELETE FROM usuario WHERE id = %s",(id,))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('sUsuario'))
    else: 
        return redirect(request.url)

@audioseApp.route('/iUsuario', methods=['GET', 'POST'])
def iUsuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']
        passwordCifrada = generate_password_hash(password)
        telefono = request.form['telefono']
        edad = request.form['edad']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        cp = request.form['cp']
        colonia = request.form['colonia']
        calle = request.form['calle']
        fechanac = datetime.datetime.now()
        perfil = request.form['perfil']

        regUsuario = db.connection.cursor()
        regUsuario.execute("INSERT INTO usuario (nombre, apellidos, correo, password, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac, perfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(nombre, apellidos, correo, passwordCifrada, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac, perfil))
        db.connection.commit()
        flash('Has creado una cuenta exitosamente')
        return redirect(url_for('sUsuario'))
    else:
        return redirect(request.url)

@audioseApp.route('/uUsuario/<string:id>', methods=['GET', 'POST'])
def uUsuario(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        telefono = request.form['telefono']
        edad = request.form['edad']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        cp = request.form['cp']
        colonia = request.form['colonia']
        calle = request.form['calle']
        fechanac = request.form['fechanac']
        # fechanac = datetime.datetime.now()
        perfil = request.form['perfil']

        upUsuario = db.connection.cursor()
        upUsuario.execute("UPDATE usuario SET nombre = %s, apellidos = %s, correo = %s, telefono = %s, edad = %s, pais = %s, estado = %s, municipio = %s, cp = %s, colonia = %s, calle = %s, fechanac = %s, perfil = %s WHERE id = %s", (nombre, apellidos, correo, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac, perfil, id,))
        db.connection.commit()
        flash('Usuario actualizado')
        return redirect(url_for('sUsuario'))
    else:
        return redirect(request.url)

@audioseApp.route('/dUsuarios/<string:id>', methods=['GET','POST'])
def dUsuarios(id):
    if request.method == 'GET':
        delUsuario = db.connection.cursor()
        delUsuario.execute("DELETE FROM usuario WHERE id = %s",(id,))
        db.connection.commit()
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('producto'))
    else: 
        return redirect(request.url)

@audioseApp.route('/uUsuarios/<string:id>', methods=['GET', 'POST'])
def uUsuarios(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        telefono = request.form['telefono']
        edad = request.form['edad']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        cp = request.form['cp']
        colonia = request.form['colonia']
        calle = request.form['calle']
        fechanac = request.form['fechanac']
        # fechanac = datetime.datetime.now()
        perfil = request.form['perfil']

        upUsuario = db.connection.cursor()
        upUsuario.execute("UPDATE usuario SET nombre = %s, apellidos = %s, correo = %s, telefono = %s, edad = %s, pais = %s, estado = %s, municipio = %s, cp = %s, colonia = %s, calle = %s, fechanac = %s, perfil = %s WHERE id = %s", (nombre, apellidos, correo, telefono, edad, pais, estado, municipio, cp, colonia, calle, fechanac, perfil, id,))
        db.connection.commit()
        flash('Usuario actualizado')
        return redirect(url_for('producto'))
    else:
        return redirect(request.url)

@audioseApp.route('/cClave/<string:id>', methods = ['GET', 'POST'])
def cClave(id):
    if request.method == 'POST':
        usuario = User(id,None,None,None,request.form['clave'],None,None,None,None,None,None,None,None,None,None)
        usuarioAut = ModelUser.clave(db, usuario)
        if usuarioAut is not None:
            if usuarioAut.password:
                cClave = request.form['claves']
                passwordCifrada = generate_password_hash(cClave)
                cClave = db.connection.cursor()
                cClave.execute("UPDATE usuario SET password = %s WHERE id = %s",(passwordCifrada,id,))
                db.connection.commit()
                flash('Contraseña cambiada')
                return redirect(url_for('sUsuario'))
            else:
                flash('Contraseña Incorrecta')
                return redirect(url_for('sUsuario'))
        else:
            flash('id no disponible')
    else:
        return redirect(request.url)

@audioseApp.route('/cClaves/<string:id>', methods = ['GET', 'POST'])
def cClaves(id):
    if request.method == 'POST':
        usuario = User(id,None,None,None,request.form['clave'],None,None,None,None,None,None,None,None,None,None)
        usuarioAut = ModelUser.clave(db, usuario)
        if usuarioAut is not None:
            if usuarioAut.password:
                cClave = request.form['claves']
                passwordCifrada = generate_password_hash(cClave)
                cClave = db.connection.cursor()
                cClave.execute("UPDATE usuario SET password = %s WHERE id = %s",(passwordCifrada,id,))
                db.connection.commit()
                flash('Contraseña cambiada')
                return redirect(url_for('producto'))
            else:
                flash('Contraseña Incorrecta')
                return redirect(url_for('producto'))
        else:
            flash('id no disponible')
    else:
        return redirect(request.url)

@audioseApp.route('/producto', methods=['GET', 'POST'])
def producto():
    sProducto = db.connection.cursor()
    sProducto.execute("SELECT * FROM productos")
    p = sProducto.fetchall()
    return render_template('user.html',productos = p)

@audioseApp.route('/sProducto', methods=['GET', 'POST'])
def sProducto():
    sProducto = db.connection.cursor()
    sProducto.execute("SELECT * FROM productos")
    p = sProducto.fetchall()
    return render_template('sproducto.html',productos = p)

@audioseApp.route('/dProducto/<string:id>', methods=['GET','POST'])
def dProducto(id):
    if request.method == 'GET':
        delProducto = db.connection.cursor()
        delProducto.execute("DELETE FROM productos WHERE id = %s",(id,))
        db.connection.commit()
        flash('Producto eliminado exitosamente')
        return redirect(url_for('sProducto'))
    else: 
        return redirect(request.url)

@audioseApp.route('/iProducto', methods=['GET', 'POST'])
def iProducto():
    if request.method == 'POST':
        precio = request.form['precio']
        descipcion = request.form['descripcion']
        metodoenvio = request.form['metodoenvio']
        imagen = request.form['imagen']
    
        iProducto = db.connection.cursor()
        iProducto.execute("INSERT INTO productos (precio, descripcion, metodoenvio, imagen) VALUES (%s, %s, %s, %s)",(precio, descipcion, metodoenvio, imagen,))
        db.connection.commit()
        flash('Producto agregado exitosamente')
        return redirect(url_for('sProducto'))
    else:
        return redirect(request.url)

@audioseApp.route('/uProducto/<string:id>', methods=['GET', 'POST'])
def uProducto(id):
    if request.method == 'POST':
        precio = request.form['precio']
        descipcion = request.form['descripcion']
        metodoenvio = request.form['metodoenvio']
        imagen = request.form['imagen']
        uProducto = db.connection.cursor()
        uProducto.execute("UPDATE productos SET precio = %s, descripcion = %s, metodoenvio = %s, imagen = %s WHERE id = %s", (precio, descipcion, metodoenvio, imagen, id,))
        db.connection.commit()
        flash('Producto actualizado exitosamente')
        return redirect(url_for('sProducto'))
    else:
        return redirect(request.url)

if __name__ == '__main__':
    audioseApp.config.from_object(config['development'])
    audioseApp.run(port=3000)