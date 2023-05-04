#Declaro las variables necesarias para el algoritmo de inicio de sesión
nombreUsuario = ""
claveUsuario = ""
intentos = 0

print("Bienvenido\n\n")

#aca hasta que no ingrese "admin@shopping.com" no podra seguir y si se equivoca 3 veces el programa finalizara
while nombreUsuario != "admin@shopping.com" and intentos < 3:

    nombreUsuario = input("\ningresa correo\n\n")

    if nombreUsuario != "admin@shopping.com":
        intentos += 1
    if intentos == 3:
        print("Ha superado el limite de intentos posibles.")

#aca hasta que no ingrese "12345" no podra seguir y si se equivoca 3 veces el programa finalizara
#(se arrastran los errores que haya tenido si no ingreso bien el correo)
while claveUsuario != "12345" and intentos < 3:

    claveUsuario = input("\ningresa contraseña\n\n")

    if claveUsuario != "12345":
        intentos += 1
    if intentos == 3:
        print("Ha superado el limite de intentos posibles.")

#Cree la calse local con sus atributos y utilizamos el método "init" para luego poder asignarles otros valores
class local:
    nombreLocal = ""
    ubicacionLocal = ""
    rubroLocal = ""

    def __init__(self, nombreLocal, ubicacionLocal, rubroLocal):
        self.nombreLocal = nombreLocal
        self.ubicacionLocal = ubicacionLocal
        self.rubroLocal = rubroLocal

#Cree una lista para los locales y un diccionario para cuando tenga que saber cual es el rubro mayor
locales = []                #lista
rubros_validos = {          #diccionario
    "indumentaria": 0,
    "perfumería": 0,
    "gastronomía": 0
}
#mientras se cumplan las condiciones estipuladas el sistema seguida funcionando y al declarar una variable con 0 si luego la cambio
#se dejaran de cumplir todas las variables y asi podremos finalizar el programa
salida = 0
while nombreUsuario == "admin@shopping.com" and claveUsuario == "12345" and salida == 0:
    print("\nMenú de opciones:")
    print("1. Gestión de locales")
    print("2. Crear cuentas de dueños de locales")
    print("3. Aprobar / Denegar solicituda de descuento")
    print("4. Gestión de novedades")
    print("5. Reporte de utilización de descuentos")
    print("0. Salir del sistema")
    option = int(input("Que desea hacer?\n\n"))


    #le pregunte al usuario que opcion elegia y si ingresa "1" le saldra otro menú con más opciones
    if option == 1:
        secondOption = ""
        while secondOption != "d":
            print("a) Crear locales")
            print("b) Modificar local")
            print("c) Eliminar local")
            print("d) volver")

            secondOption = input("Que desea hacer?\n\n")

            #le pregunte al usuario que opcion elegia y si ingresa "a" y la cantidad de locales creados es menor a 10 le pedire
            #que ingrese los valores de los atributos del local que quiere crear
            if secondOption == "a":
            
                if len(locales) < 10:
                    nombreLocal = input("\nIngrese el nombre del nuevo local: ")
                    ubicacionLocal = input("Ingresa la ubicación del local: ")
                    rubroLocal = input("A que rubro pertenece el local? (indumentaria, perfumería o gastronomía. Recuerde usar los acentos.)")

                    #verifico que el rubro ingresado sea alguno de los que estan dentro del diccionario creado anteriormente
                    if rubroLocal not in rubros_validos:
                        print("El rubro que ingresaste no es valido")
                        continue
                    
                    #añado el local creado a la lista de locales y sumo 1 al rubro al que pertenece el local creado
                    local_nuevo = local(nombreLocal, ubicacionLocal, rubroLocal)
                    locales.append(local_nuevo)
                    rubros_validos[rubroLocal] += 1

                    #obtengo el valor del rubro con más cantidad de locales y lo muestro
                    rubro_max = max(rubros_validos, key=rubros_validos.get)
                    cant_max = rubros_validos[rubro_max]
                    print("Rubro con más locales: {} con {} locales".format(rubro_max, cant_max))
                    
                    #obtengo el valor del rubro con menos cantidad de locales y lo muestro
                    rubro_min = min(rubros_validos, key=rubros_validos.get)
                    cant_min = rubros_validos[rubro_min]
                    print("Rubro con menos locales: {} con {} locales".format(rubro_min, cant_min))
                
                    print("\nEl local se ha creado exitosamente\n")

                else:
                    print("Se ha alcanzado el número maximo de locales (10)")
            
            elif secondOption == "b" or secondOption == "c":
                print("\nEn construcción...")
           
    elif option == 0:
        print("\nGracias por utilizar nuestro sistema")
        salida = 1

    elif option == 2 or 3 or 4 or 5:
        print("\nEn construcción...")

    else:
        option != 0 or 1 or 2 or 3 or 4 or 5
        print("\nEsa opcion no existe")
        continue