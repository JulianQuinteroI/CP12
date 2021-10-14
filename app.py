from flask import Flask, render_template, request
import formulario
import os
import db


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = os.urandom(24)


@app.route('/')
def main():
    formulario1 = formulario.formularioWTF()
    return render_template('index.html', formulario1=formulario1)


@app.route('/recibido', methods=['POST'])
def recibido():
    nombre = request.form.get('nombre')
    correo = request.form.get("correo")
    """print(request.form)"""
    return login(nombre, correo)


def login(nombre, correo):
    connect_db = db.get_db()
    cursor = connect_db.cursor()
    consulta = "select * from usuario where nombre ='{}' and correo ='{}'".format(
        nombre, correo)
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return str(resultado)
