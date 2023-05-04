user = None
pasw = None
salida = 0
intent = 0
while user != "admin@shopping.com" and intent < 3:

    user = input("ingresa correo\n\n")

    if user != "admin@shopping.com":
        intent += 1
    if intent == 3:
        print("andate flaco")


while pasw != "12345" and intent < 3:

    pasw = input("ingresa contraseña\n\n")

    if pasw != "12345":
        intent += 1
    if intent == 3:
        print("andate flacovich")


class local:
    nombre = ""
    ubicacion = ""
    rubro = ""

    def __init__(self, nombre, ubicacion, rubro):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.rubro = rubro

locales = []
rubros_validos = {
    "indumentaria": 0,
    "perfumería": 0,
    "gastronomía": 0
}



while user == "admin@shopping.com" and pasw == "12345" and salida == 0:
    print("Menú de opciones:")
    print("1. Gestión de locales")
    print("2. Crear cuentas de dueños de locales")
    print("3. Aprobar / Denegar solicituda de descuento")
    print("4. Gestión de novedades")
    print("5. Reporte de utilización de descuentos")
    print("0. Salir del sistema")
    option = int(input("Que desea hacer?\n\n"))


    if option == 1:

        print("1. Crear locales")
        print("")
        
        if len(locales) < 10:
            nombre = input("\nIngrese el nombre del nuevo local: ")
            ubicacion = input("Ingresa la ubicación del local: ")
            rubro = input("A que rubro pertenece el local? (indumentaria, perfumería o gastronomía. Recuerde usar los acentos.)")
            
            if rubro not in rubros_validos:
                print("El rubro que ingresaste no es valido")
                continue

            local_nuevo = local(nombre, ubicacion, rubro)
            locales.append(local_nuevo)
            rubros_validos[rubro] += 1

            rubro_max = max(rubros_validos, key=rubros_validos.get)
            cant_max = rubros_validos[rubro_max]
            print("Rubro con más locales: {} con {} locales".format(rubro_max, cant_max))

            rubro_min = min(rubros_validos, key=rubros_validos.get)
            cant_min = rubros_validos[rubro_min]
            print("Rubro con menos locales: {} con {} locales".format(rubro_min, cant_min))
            
            print("\nEl local se ha creado exitosamente\n")

        else:
            print("Se ha alcanzado el número maximo de locales (10)")

  
    elif option == 2:
        print("Se han creado {} locales:".format(len(locales)))
        for i, local in enumerate(locales):
            print("{}. {}".format(i+1, local.nombre))

        num_local = int(input("Ingrese el numero del local que quiere consultar: "))
        if num_local == 0:
            continue
        elif num_local > len(locales):
            print("El número ingresado no es valido")
        else:
            local_seleccionado = locales[num_local - 1]
            print("Ha seleccionado el local: {}\nUbicación: {}\nRubro: {}".format(local_seleccionado.nombre, local_seleccionado.ubicacion, local_seleccionado.rubro))
            
            vuelta = input("Presiona Enter para continuar")
    
    
    elif option == 3 or 4 or 5:
        print("En construcción...")
        continue
    
    
    elif option == 0:
        print("Gracias por utilizar nuestro sistema")
        salida = 1

    else:
        option != 0 or 1 or 2 or 3 or 4 or 5
        print("esa opcion no existe")
        continue