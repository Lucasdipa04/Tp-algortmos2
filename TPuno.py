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
    calle = ""
    numero = 0
    color = ""

    def __init__(self, nombre, calle, numero, color):
        self.nombre = nombre
        self.calle = calle
        self.numero = numero
        self.color = color

locales = []


while user == "admin@shopping.com" and pasw == "12345" and salida == 0:
    print("Bienvenido de vuelta administrador\n\n Menú de opciones:")
    print("1. Crear local")
    print("2. Colnsultar locales")
    print("0. Salir del sistema")
    option = int(input("Que desea hacer?\n\n"))


    if option == 1:
        if len(locales) < 5:
            nombre = input("Ingrese el nombre del nuevo local: ")
            calle = input("Ingrese la calle del local: ")
            numero = int(input("Ingrese el número de la calle: "))
            color = input("Ingrese el color del local: ")

            local_nuevo = local(nombre, calle, numero, color)
            locales.append(local_nuevo)
            print("el local se ha creado exitosamente")
        else:
            print("Se ha alcanzado el número maximo de locales (5)")

  
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
            print("Ha seleccionado el local: {}\nCalle: {}\nNúmero: {}\nColor: {}".format(local_seleccionado.nombre, local_seleccionado.calle, local_seleccionado.numero, local_seleccionado.color))
    
    elif option == 0:
        print("Gracias por utilizar nuestro sistema")
        salida = 1

    else:
        option != 1 or 2 or 0
        print("esa opcion no existe")
        continue