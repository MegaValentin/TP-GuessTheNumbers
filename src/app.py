from flask import Flask, render_template, request, session
from domain.User import User 
import random
from datetime import datetime



app=Flask(__name__)
#ruta a la plantilla principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user' , methods=['GET', 'POST'])
def usuario():
    #datos del usuario para comenzar el juego
    usuario = request.form['usuario']
    
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

@app.route('/game', methods=['GET','POST'])
def game(): 
    if request.method == 'GET':

        return render_template('user.html')

    elif request.method == 'POST':
        
        jugadasTotales = []
        verde = []
        amarillo = []
        rojo = []

        numero1= request.form['1']
        numero2= request.form['2']
        numero3= request.form['3']
        numero4= request.form['4']
        numero5= request.form['5']

        
        numerosRandom = [1,2,3,4,5]
        #numerosRandom = listaRandom()
        
        
        while (True):
            numerosDelUsuario = [int(numero1), int(numero2), int(numero3), int(numero4), int(numero5)]
            jugadasTotales.append(numerosDelUsuario)
            
            for nu in range(len(numerosDelUsuario)):
                for nr in range(len(numerosRandom)):

                    if nu == nr :

                        if numerosDelUsuario[nu] == numerosRandom[nr]:
                            verde.append(numerosDelUsuario[nu])

                    elif numerosDelUsuario[nu] == numerosRandom[nr]:
                        amarillo.append(numerosDelUsuario[nu])
                    else:
                        if numerosDelUsuario[nu] != numerosRandom[nr]:
                            rojo.append(numerosDelUsuario[nu])

            if len(verde) == 5:
                return render_template("ganaste.html")
        
    return render_template('user.html')       
        
        