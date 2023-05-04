variable1 = ""
variable2 = ""


listalol = []

class lista:
    color = ""
    numero = 0

    def __init__(self, color, numero):
        self.color = color
        self.numero = numero


print("hola pelotudo")
color = input("declarame el color cabeza")
numero = input("delcarame el numero")

variable1 = input("que va primero?")
variable2 = input("que va segundo?")

if variable1 == "color":
    variable1 = color
else: variable1 == "numero"
variable1 = numero

if variable2 == "color":
    variable2 = color
else: variable2 == "numero"
variable2 = numero

print(variable1, variable2)
