'''

El usuario introduce un valor (1- Piedra|2- Papel|3-Tijera), si no es correcto se volverá a pedir de nuevo hasta que se correcta.

La “maquina” generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Al
finalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o
empatado.

'''
#Importamos la biblioteca random
import random
opcion = ""
opciones_validas = [1, 2, 3]  
opcion_maquina = random.randint(1, 3) #random.radint(1,3) la maquina genera un numero aleatorio entre el 1 y 3.

puntos_usuario= 0
puntos_maquina = 0
#Dentro del bucle le pedimos al usuario repetidamente que ingrese una opcion y que la maquina genere un numero aleatoriamente repetidamente
while puntos_usuario != 3 and puntos_maquina != 3:

    opcion = int(input("1- Piedra | 2- Papel | 3-Tijera: "))
    opcion_maquina = random.randint(1, 3)

#Condiciones if y elif para comparar el numero del usuario y el numero de la maquina. Depende de cual salga; ganas, pierdes o empatas
    if opcion == 1 and opcion_maquina == 2:

        print(f"El jugador ha elegido piedra")
        print (f"La máquina ha elegido papel")
        print ("Has perdido !! :(")
        puntos_maquina = puntos_maquina +1  #Cada vez que pierdes se añade +1 a las victorias de la maquina

    elif opcion == 1 and opcion_maquina == 3:   

        print(f"El jugador ha elegido piedra")
        print (f"La máquina ha elegido tijera")
        print ("Has ganado !! :)")
        puntos_usuario = puntos_usuario +1  #Cada vez que ganas se añade +1 a tus victorias

    elif opcion == 1 and opcion_maquina == 1:

        print(f"El jugador ha elegido piedra")
        print (f"La máquina ha elegido piedra")
        print ("Habeis empatado :/")

    elif opcion == 2 and opcion_maquina == 2:

        print(f"El jugador ha elegido papel")
        print (f"La máquina ha elegido papel")
        print ("Habeis empatado :/")

    elif opcion == 2 and opcion_maquina == 3:

        print(f"El jugador ha elegido papel")
        print (f"La máquina ha elegido tijera")
        print ("Has perdido !! :(")
        puntos_maquina = puntos_maquina +1

    elif opcion == 2 and opcion_maquina == 1:

        print(f"El jugador ha elegido papel")
        print (f"La máquina ha elegido piedra")
        print ("Has ganado !! :)")
        puntos_usuario = puntos_usuario +1

    elif opcion == 3 and opcion_maquina == 2:

        print(f"El jugador ha elegido tijera")
        print (f"La máquina ha elegido papel")
        print ("Has ganado !! :)")
        puntos_usuario = puntos_usuario +1

    elif opcion == 3 and opcion_maquina == 3:

        print(f"El jugador ha elegido tijera")
        print (f"La máquina ha elegido tijera")
        print ("Habeis empatado :/")

    elif opcion == 3 and opcion_maquina == 1:

        print(f"El jugador ha elegido tijera")
        print (f"La máquina ha elegido papel")
        print ("Has perdido !! :(")
        puntos_maquina = puntos_maquina +1

        #Si la opcion que mete el usuario no esta dentro de las opciones validas (1, 2, 3) te da un error
    elif opcion != opciones_validas:
        print("ERROR, la opción no es válida")
    
if puntos_usuario == 3:
    print("Ganador del juego !!")  #Si llegas a 3 victorias ganas el juego y se cierra el programa
        

if puntos_maquina == 3:
    print("Perdiste el juego, adiós")  #Lo mismo pasa con la maquina, si llega a 3 gana y se acaba
        

