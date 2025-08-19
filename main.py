
usuarios = {}

def registrar_usuario():
    print("\n--- Registro de usuario ---")
    nombre = input("Ingrese un nombre de usuario: ")
    if nombre in usuarios:
        print("Ese nombre de usuario ya existe.")
        return
    contraseña = input("Ingrese una contraseña: ")
    usuarios[nombre] = contraseña
    print(f"Usuario '{nombre}' registrado correctamente.")

def mostrar_usuarios():
    print("\n--- Lista de usuarios registrados ---")
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"- {usuario}")

def login():
    print("\n--- Login ---")
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre in usuarios and usuarios[nombre] == contraseña:
        print(f"Bienvenido {nombre}, has iniciado sesión correctamente.")
    else:
        print("Usuario o contraseña incorrectos.")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()