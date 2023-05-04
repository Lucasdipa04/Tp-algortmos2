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
    print("1.Gestión de locales")
    print("2.Gestión de novedades")

while True:
    seccion = None
    while seccion not in ["1", "2", "0"]:
        seccion = input("Indique a que sección desea entrar ingresando el número de acción que se encuentra a la izquierda\n\n")

        if seccion == "1":
            option = None
            while option != "0":
                mostrar_opciones()
                option = input("Indique que accion desea realizar ingresando el número de acción que se encuentra a la izquierda\n\n")
                if option == "1":
                    print("prueba 1 realizada")
                elif option == "2":
                    print("prueba 2 realizada")
                elif option == "0":
                    break
        
        elif seccion == "2":
            option = None
            while option != "0":
                mostrar_opciones()
                option = input("Indique que accion desea realizar ingresando el número de acción que se encuentra a la izquierda\n\n")
                if option == "1":
                    print("prueba 3 realizada")
                elif option == "2":
                    print("prueba 4 realizada")
                elif option == "0":
                    break

        elif seccion == "0":
            break
                
                    
                