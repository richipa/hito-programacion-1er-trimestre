'''

CUESTION 3: Simular el funcionamiento de una cuenta bancaria (2.5 puntos): al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto. 

Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos.

'''
#Inicializamos variables a 0 y definimos
saldo_inicial = 0

opcion_1 = ""
opcion_2 = ""
opcion_3 = ""
opcion_4 = ""
opcion_5 = ""

opciones_validas = [1, 2, 3, 4, 5]  #Solo son validas las opciones del menu, del 1 al 5

numero_ingresos = 0

numero_retiradas = 0

#Solicitamos el saldo inicial al usuario, si no es mayor que cero y no es un numero, le vuelve a pedir que lo introduzca (Permite decimales)
while True:
    saldo_inicial = float(input("Introduce tu saldo inicial: "))

    if saldo_inicial <= 0:
            print ("Porfavor, introducelo de nuevo")
        
    else:
        break

#Mostramos al usuario el menu del cajero

print ("Bienvenido a tu cuenta: ")

print ("1- Ingresar dinero ")

print ("2- Retirar dinero ")

print ("3- Mostrar saldo ")

print ("4- Mostrar estadisticas ")

print ("5- Salir ")


#Bucle while para que el usuario pueda realizar sus operaciones, despues de cada operacion, se vuelve a mostrar el menu para que el usuario pueda hacer otra operacion si lo desea.
while True:

    seleccion = int(input("Selecciona una opcion: "))

    if seleccion in opciones_validas:  #Esto quiere decir que "Si la seleccion del usuario esta entre las opciones del menu, sigue con el programa, si no, "opcion no valida, mete otra"
        
        if seleccion == 1:
            ingreso = int(input("Seleccione la cantidad a ingresar: "))
            if ingreso <= 0:  #No puede ingresar 0 euros o menos
                print("ERROR, la cantidad debe ser mayor que cero")
                ingreso = int(input("Seleccione la cantidad a ingresar: "))
                print (f"Tu saldo ahora es de {saldo_inicial}")
            else:
                saldo_inicial = saldo_inicial + ingreso
                numero_ingresos = numero_ingresos +1   #Cada vez que se realiza un ingreso VALIDO, se añade +1 al contador de ingresos y se almacena en "numero_ingresos"
                print (f"Tu saldo ahora es de {saldo_inicial}")
                

            print("____________________________\n")  #Se vuelve a mostrar el menu

            print ("1- Ingresar dinero ")

            print ("2- Retirar dinero ")

            print ("3- Mostrar saldo ")

            print ("4- Mostrar estadisticas ")

            print ("5- Salir ")
            print("____________________________")

        elif seleccion == 2:
            retirada = int(input("Seleccione la cantidad a retirar: "))
            if retirada > saldo_inicial:
                print("ERROR")  #No puede retirar dinero si se queda en numeros rojos al retirarlo
                retirada = int(input("Seleccione una cantidad válida a retirar: "))
                print (f"Tu saldo ahora es de {saldo_inicial}")

            else:
                saldo_inicial = saldo_inicial - retirada
                numero_retiradas = numero_retiradas +1  #Cada vez que se realiza una retirada VALIDA, se añade +1 al contador de retiradas y se almacena en "numero_retiradas"
                print (f"Tu saldo ahora es de {saldo_inicial}")

            print("____________________________\n")  #Se vuelve a mostrar el menu
            
            print ("1- Ingresar dinero ")

            print ("2- Retirar dinero ")

            print ("3- Mostrar saldo ")

            print ("4- Mostrar estadisticas ")

            print ("5- Salir ")
            print("____________________________")

        elif seleccion == 3:
            print(f"Tu saldo actual es de {saldo_inicial}")  #Simplemente nos muestra nuestro saldo actual, hayamos ingresado, retirado o no

            print("____________________________\n")  #Se vuelve a mostrar el menu
            
            print ("1- Ingresar dinero ")

            print ("2- Retirar dinero ")

            print ("3- Mostrar saldo ")

            print ("4- Mostrar estadisticas ")

            print ("5- Salir ")
            print("____________________________")
        
        elif seleccion == 4:

            print("Estadísticas de tu cuenta:")  #La opcion 4 muestra el total de ingresos y retiradas realizados, que hemos comentado antes

            print(f"Total de ingresos realizados: {numero_ingresos}")
        
            print(f"Total de retiradas realizadas: {numero_retiradas}")
            

            print("____________________________\n")  #Se vuelve a mostrar el menu
            
            print ("1- Ingresar dinero ")

            print ("2- Retirar dinero ")

            print ("3- Mostrar saldo ")

            print ("4- Mostrar estadisticas ")

            print ("5- Salir ")
            print("____________________________")

        elif seleccion == 5:
            print("Hasta pronto, Ricardo")  #Mensaje de despedida del cajero
            break

    else:
        print("Opcion no válida")  #Como decia antes, si el usuario elige un numero fuera del rango (1, 5), le da un error
