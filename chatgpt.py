print("Bienvenido")
for intento in range (3):
    user = input("Por favor ingrese su correo\n\n")
    
    if user == "admin@shopping.com":
        verify = 1
        break
        
    else:
        print("El correo ingresado no es valido")   

else:
    print("Has superado el límite de intentos para ingresar")
    exit()

for intento in range (3):
    pasw = input("Por favor ingrese su contraseña\n\n")
    
    if pasw == "12345":
        numero = 1
        print("\nBienvenido de vuelta Administrador")
        break

    else:
        print("La contraseña ingresada es incorrecta")

else:
    print("Has superado el límite de intentos para ingresar")
    exit() 

def mostrar_opciones():
    print("1. Crear")
    print("2. Eliminar")
    print("0. Volver")

def mostrar_secciones():
    print("1.Gestión de locales")
    print("2.Gestión de novedades")


if numero == 1:
    mostrar_secciones()
    seccion = input(
        "Indique a que sección desea entrar ingresando el número de acción que se encuentra a la izquierda\n\n")

seccion = None
while seccion not in ["1", "2"]:
    seccion = input("Ingrese la sección a la que desea ingresar (1 o 2): ")

if seccion == "1":
    opcion = None
    while opcion != "0":
        mostrar_opciones()
        opcion = input("Ingrese la opción que desea seleccionar: ")
        if opcion == "1":
            # Llamar a la función para crear
        elif opcion == "2":
            # Llamar a la función para eliminar
        elif opcion == "0":
            # Salir del bucle y volver a la sección

elif seccion == "2":
    opcion = None
    while opcion != "0":
        mostrar_opciones()
        opcion = input("Ingrese la opción que desea seleccionar: ")
        if opcion == "1":
            # Llamar a la función para crear
        elif opcion == "2":
            # Llamar a la función para eliminar
        elif opcion == "0":
            # Salir del bucle y volver a la sección
