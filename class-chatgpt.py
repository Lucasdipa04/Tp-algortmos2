class Local:
    # Atributos de la clase
    calle = ""
    numero = 0
    color = ""

    # Constructor de la clase
    def __init__(self, calle, numero, color):
        self.calle = calle
        self.numero = numero
        self.color = color

# Preguntar al usuario si desea crear un local
crear_local = input("¿Desea crear un nuevo local? (s/n)")

# Si el usuario responde "s", pedir los datos para crear el local
if crear_local == "s":
    calle = input("Ingrese la calle del local: ")
    numero = int(input("Ingrese el número del local: "))
    color = input("Ingrese el color del local: ")
    
    # Crear una nueva instancia de la clase Local con los datos ingresados
    local_1 = Local(calle, numero, color)
    print("El local se ha creado exitosamente.")
else:
    print("No se ha creado ningún local.")
