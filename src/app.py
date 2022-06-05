from crypt import methods
from urllib import request
from flask import Flask, render_template

app=Flask(__name__)
#primer ruta
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user' , methods=['POST'])
def usuario():
    nombre = request.form['nombre']
    return render_template('usuario.html', nombre=nombre)

    