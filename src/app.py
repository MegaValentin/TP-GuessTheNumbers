
from urllib import request
from flask import Flask, render_template

app=Flask(__name__)
#ruta a la plantilla principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user' , methods=['POST'])
def usuario():
    #datos del usuario para comenzar el juego
    nombre = request.form['nombre']
    email = request.form['email']
    return render_template('usuario.html', nombre=nombre, email=email)

if __name__=='__main__':
    app.run(port=3000, debug=True)