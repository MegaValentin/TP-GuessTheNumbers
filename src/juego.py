import random
from datetime import datetime

def horaDeLaPartida():
    
    hora = datetime.now() 
    horaactual=datetime.strftime(hora,'%d/%m/%Y %H:%M:%S')
    print(horaactual)

def nombreUsuario():
    nombre = ""
    nombre = input("ingrese un nombre de usuario: ")
    print(f'Hola {nombre}. ¡Bienvenido a Guess The Number!')

def randomDe5Numeros(valorMaximo):
    
    """Genera una lista de 5 elementos aleatorios.
    Estos 5 elementos seran los que el usuario debera adivinar"""

    numerosAAdivinar = []
    rango=0
    cantidadDeElemen = 5
    
    while rango < cantidadDeElemen:

        numerosRandom = (random.randint(0, valorMaximo))
        
        if numerosRandom not in numerosAAdivinar:
            numerosAAdivinar.append(numerosRandom)
            rango+=1
    
    return numerosAAdivinar

def numerosIngresadosPorElUsuario():
    
    """Pide al usuario que ingrese los valores que queria en un rango de 0 
    a 10 desde la posicion 1 a la posicion 5"""

    numerosIngresados = []
    rango = 0
    cantidadDeElemen = 5
    
    while rango < cantidadDeElemen:

        numerosDelUsuario = int(input("ingrese un numero entre 0 al 10 : "))

        
        if numerosDelUsuario < 11:
            if numerosDelUsuario not in numerosIngresados:
                numerosIngresados.append(numerosDelUsuario)
                rango +=1
            else:
                print("No es valido ingresar numeros iguales")
            
        else:
            print("Debes colocar una cifra en el rango solicitado")
        
    
    return numerosIngresados

def compararAmbasListas(cantidadDeIntentos):

    """Compara ambas listas(lista random generada y lista armada por el ususario) en una cantidad de intentos"""

    verde = []
    amarillo = []
    numerosAAdivinar = []
    #listaRandom = [1, 2, 3, 4, 5]
    listaRandom = randomDe5Numeros(10)
    jugadas = 0
    intentos = cantidadDeIntentos 
    nombre=nombreUsuario()

    nombre
    horaDeLaPartida()
    """Ocultar los numeros que el usuario debe adivinar"""
    for i in range(len(listaRandom)):
        numerosAAdivinar.append('*')
    print(numerosAAdivinar)

    #verde = Posicion y numero correcto
    #amarillo = Numero correcto pero no la posicion
    #ningunColor = Posicion y numero incorrecto
         
    listaUsuario = numerosIngresadosPorElUsuario()
    
    while (True):
        print("---------------------------------------------")
        print(f'Jugada {jugadas + 1}. Te quedan {intentos - (jugadas + 1)} intentos')
        
        for nu in range(len(listaUsuario)):
            for nr in range(len(listaRandom)):

                if nu == nr :

                    if listaUsuario[nu] == listaRandom[nr]:
                        verde.append(listaUsuario[nu])

                else:
                    if listaUsuario[nu] == listaRandom[nr]:
                        amarillo.append(listaUsuario[nu])

        if len(verde) == 5:
            print("Has ganado")
            return horaDeLaPartida()
              
        else:    
            jugadas += 1 
            
            print(f'Numeros ingresados---> {listaUsuario}')       
            print(f'Verde---> {verde}')
            print(f'Amarillo---> {amarillo}')
            print('Con los datos obtenidos ingrese nuevamente 5 numeros')
            print("---------------------------------------------")

        if jugadas >= intentos:
            print("Has perdido :(")
            print(f'Numeros ingresados---> {listaUsuario}')       
            print(f'Los numeros a adivinar eran---> {listaRandom} ')
            return horaDeLaPartida()
        
        verde.clear()
        amarillo.clear()
        listaUsuario.clear()
        listaUsuario = numerosIngresadosPorElUsuario()

compararAmbasListas(5)