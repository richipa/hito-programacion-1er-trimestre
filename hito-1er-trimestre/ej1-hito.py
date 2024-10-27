'''

Mostrar figuras por pantalla (2,5 puntos): a través de un menú solicitaremos al usuario qué tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no es correcta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta.

▪ Si ha seleccionada un cuadrado, pediremos su lado y mostraremos la figura, su área y perímetro

▪ Si ha seleccionado un rectángulo, pediremos base y altura y mostraremos la figura, su área y perímetro.


'''
#Definimos variables
opcion = ""
opciones_validas = [1, 2, 3]

#Mostramos el menu al usuario

print("MENU")

print("1 - Cuadrado")

print("2 - Rectángulo")

print("3 - Salir")

#Bucle while que muestre el menú de opciones hasta que el usuario elija "3" y salga del programa
while True:
    opcion = int (input("Dime una opcion: " ))

    if opcion == 1:
        
        lado = int(input("Dime el lado del cuadrado: "))

        print ("*" *lado)  #Hacemos "*" por el lado, asi depende del numero que introduzca el usuario, saldran "x" asteriscos
        print ("*" *lado)

        area = lado * lado  

        print (f"Su area es de {area} ")

        perimetro = lado * 4  

        print (f"Su perimetro es de {perimetro}")

        #Después de cada “resultado” le volvemos a mostrar el menú al usuario para que si quiere, haga otra operación hasta que el decida salir

        print ("_____________________________")

        print("MENU")

        print("1 - Cuadrado")

        print("2 - Rectángulo")

        print("3 - Salir")


    elif opcion == 2:

        base = int(input("Dame la base del rectangulo: "))

        altura = int(input("Dame la altura del rectangulo: "))

        print ("*" *base)  #Lo mismo que con el cuadrado pero en vez de "lado por" es "base y altura por"
        print ("*" *altura)

        area = base * altura

        print (f"Su area es {area}")

        perimetro = base * 2 + altura * 2

        print (f"Su perimetro es {perimetro}")


        print ("_____________________________")

        print("MENU")

        print("1 - Cuadrado")

        print("2 - Rectángulo")

        print("3 - Salir")
        

    elif opcion == 3:
        
        print ("Hasta la próxima")
        break

    else:
        print ("Opcion incorrecta")  #Si el usuario decide elegir otra opcion que no este dentro del menu, ERROR y de nuevo le muestra menu

        print ("_____________________________")

        print("MENU")

        print("1 - Cuadrado")

        print("2 - Rectángulo")

        print("3 - Salir")
