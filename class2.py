class Local:
    # Atributos de la clase
    calle = ""
    numero = 0
    color = ""
    nombre = ""

    # Constructor de la clase
    def __init__(self, calle, numero, color, nombre):
        self.calle = calle
        self.numero = numero
        self.color = color
        self.nombre = nombre

# Lista para almacenar los objetos Local
locales = []

# Ciclo while para repetir el programa hasta que el usuario decida salir
while True:
    # Mostrar el menú de opciones
    print("Menú de opciones:")
    print("1. Crear un nuevo local")
    print("2. Consultar locales")
    print("3. Salir del programa")
    opcion = int(input("Ingrese su opción: "))

    # Opción 1: Crear un nuevo local
    if opcion == 1:
        # Verificar si se han creado menos de 5 locales
        if len(locales) < 5:
            calle = input("Ingrese la calle del local: ")
            numero = int(input("Ingrese el número del local: "))
            color = input("Ingrese el color del local: ")
            nombre = input("ingrese el nombre del local: ")
            # Crear una nueva instancia de la clase Local con los datos ingresados
            local_nuevo = Local(calle, numero, color, nombre)
            locales.append(local_nuevo)
            print("El local se ha creado exitosamente.")
        else:
            print("No se pueden crear más locales. Ya se han creado 5.")

    # Opción 2: Consultar locales
    elif opcion == 2:
        # Mostrar la cantidad de locales creados
        print("Se han creado {} locales:".format(len(locales)))
        for i, local in enumerate(locales):
            print("{}. {}".format(i+1, local.nombre))
        # Preguntar al usuario qué local desea consultar
        num_local = int(input("Ingrese el número del local que desea consultar (o 0 para volver al menú principal): "))
        # Mostrar los atributos del local seleccionado
        if num_local == 0:
            continue
        elif num_local > len(locales):
            print("El número de local ingresado no es válido.")
        else:
            local_seleccionado = locales[num_local - 1]
            print("Usted esta viendo los datos del local: {}\nCalle: {}\nNúmero: {}\nColor: {}".format(local_seleccionado.nombre, local_seleccionado.calle, local_seleccionado.numero, local_seleccionado.color))
            # Preguntar al usuario si desea volver al menú principal
            volver_menu = input("Presione enter para volver al menú principal.")
            
    # Opción 3: Salir del programa
    elif opcion == 3:
        print("Gracias por utilizar el programa.")
        break

    # Opción inválida
    else:
        print("Opción inválida. Intente nuevamente.")
