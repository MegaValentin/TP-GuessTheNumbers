from flask import Flask, render_template, request, session
from domain.User import User 
from juego import juego #archivo - clase


app=Flask(__name__)
#ruta a la plantilla principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user' , methods=['POST'])
def usuario():
    #datos del usuario para comenzar el juego
    usuario =( request.form['usuario'])
    
    return render_template('user.html', usuario=usuario)

@app.route('/game', methods=['GET','POST'])
def game(): 
    if request.method == "GET":

        return render_template('user.html')

    elif request.method == "POST":
        
        verde = []
        amarillo = []

        numero1= request.form['1']
        numero2= request.form['2']
        numero3= request.form['3']
        numero4= request.form['4']
        numero5= request.form['5']

        numerosDelUsuario = [int(numero1), int(numero2), int(numero3), int(numero4), int(numero5)]
        numerosRandom = [1,2,3,4,5]
        #numerosRandom = juego.randomDe5Numeros(5)
        
        while (True):
            for nu in range(len(numerosDelUsuario)):
                for nr in range(len(numerosRandom)):

                 if nu == nr :

                        if numerosDelUsuario[nu] == numerosRandom[nr]:
                            verde.append(numerosDelUsuario[nu])

                else:
                    if numerosDelUsuario[nu] == numerosRandom[nr]:
                        amarillo.append(numerosDelUsuario[nu])

            if len(verde) == 5:
                return render_template("ganaste.html")
        
    return render_template('user.html')       
        
        