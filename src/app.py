from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from domain.User import User 
import random
from datetime import datetime
from info.basedata import db



app=Flask(__name__)
app.secret_key = 'secret_key'
SQLAlchemy(app)
#ruta a la plantilla principal
@app.route('/')
def index():
    return render_template('index.html')

def esValido(palabra):
    return palabra.strip() != ""

@app.route('/user' , methods=['GET', 'POST'])
# @app.route('/user' , methods=['GET', 'POST'])
# def usuario():
#     if request.method == 'POST':
#         #datos del usuario para comenzar el juego
#         usuario = request.form.get('usuario')

#         user = User(usuario)
#         error = None
#         if not usuario:
#             error= "Se requiere un nombre de usuario"
        
#         user_name = User.query.filter_by(usuario=usuario).first()

#         if user_name == None:
#             db.session.add(user)
#             db.session.commit()
#         else:
#             error = f'El usuario {usuario} ya esta registrado'
#         flash (error)

#         global intentos
#         intentos = 5
#         cont = 0
        
#     return render_template('user.html', usuario=usuario)
def usuario():
    if request.method == 'POST':
        #datos del usuario para comenzar el juego
        usuario = request.form['usuario']
       
        global intentos
        intentos = 5
        
        usuarioValido = esValido(usuario)
        if usuarioValido:
            user = User.query.filter_by(usuario=usuario)
        else:
            return render_template('index.html')

        if user is None:
            user = User(usuario)
            session["usuario"] = usuario
            return redirect(url_for('user'))

    return render_template('user.html', usuario=usuario)

def listaRandom():
        
    numerosAleatorios= []
    rango=0
    
    while rango < 5:

        numerosRandom = (random.randint(0, 10))
        
        if numerosRandom not in numerosAleatorios:
            numerosAleatorios.append(numerosRandom)
            rango+=1
    
    return numerosAleatorios

def horaDeLaPartida():
        
        hora = datetime.now() 
        horaactual=datetime.strftime(hora)
        print(horaactual)

@app.route('/game', methods=['GET','POST'])
def game(): 
    if request.method == 'GET':

        return render_template('user.html')

    elif request.method == 'POST':
        
        jugadasTotales = []
        verde = []
        amarillo = []
        cont = 0
        intentosDelJugador= intentos
        print(intentos)

        numero1= request.form['1']
        numero2= request.form['2']
        numero3= request.form['3']
        numero4= request.form['4']
        numero5= request.form['5']

        numerosRandom = [1,2,3,4,5]
        
        #numerosRandom = listaRandom()
        
        print(numerosRandom)
        numerosDelUsuario = [int(numero1), int(numero2), int(numero3), int(numero4), int(numero5)]
        jugadasTotales.append(numerosDelUsuario)
        while (cont <= intentosDelJugador ):
            
            
            for nu in range(len(numerosDelUsuario)):
                for nr in range(len(numerosRandom)):

                    if nu == nr :

                        if numerosDelUsuario[nu] == numerosRandom[nr]:
                            verde.append(numerosDelUsuario[nu])

                    elif numerosDelUsuario[nu] == numerosRandom[nr]:
                        amarillo.append(numerosDelUsuario[nu])

            cont += 1
            print(cont)

            if len(verde) == 5:
                tiempo = horaDeLaPartida()
                return render_template('ganaste.html', tiempo=tiempo, jugadasTotales=jugadasTotales)
            
            
            if len(jugadasTotales) == 5:

                return render_template('perdiste.html', jugadasTotales=jugadasTotales)

            # elif intentos == 5:
            #     return render_template('perdiste.html',jugadasTotales=jugadasTotales )
            else:
                    
                return render_template('user.html', jugadasTotales=jugadasTotales , verde=verde, amarillo=amarillo,cont = cont)

            
    return redirect(url_for('user'))       
        
        