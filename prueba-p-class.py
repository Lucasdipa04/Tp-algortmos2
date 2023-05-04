class Local:
    calle = ""
    numero = 0
    color = ""


def __init__(self, calle, numero, color):
    self.calle = calle
    self.numero = numero
    self.color = color

new_local = input("crear local? (y/n)")

if new_local == "s":
    calle = input("ingrese la calle\n\n")
    numero = int(input("ingrese el numero\n\n"))
    color = input("ingrese el color\n\n")

    print("el local se creo exitosamente")

else: 
    print("no se creo jaja")