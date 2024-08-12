# Utilizo un diccionario para crear la base de datos
base_de_datos = {}

def crear_usuario():
    """
    Crea un nuevo usuario en la base de datos.
    """
    nombre = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    
    # Verifico si el usuario ya está creado
    if nombre in base_de_datos:
        print("El usuario ya está creado.")
    else:
        base_de_datos[nombre] = contraseña
        print(f"Usuario {nombre} creado con éxito.")

def ver_usuarios():
    """
    Muestra todos los usuarios creados en la base de datos.
    """
    if base_de_datos:
        print("Usuarios creados:")
        for usuario, contraseña in base_de_datos.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios creados.")

def login_usuario():
    """
    Realiza el login de un usuario verificando que la contraseña coincida.
    """
    nombre = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    
    if nombre in base_de_datos:
        if base_de_datos[nombre] == contraseña:
            print(f"Hola {nombre}!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

def main():
    """
    Muestra el menú del programa.
    """
    while True:
        print("\nMenu:")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Login")
        print("4. Salir")
        
        opcion = input("Seleccionar una opción: ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Has salido del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecuta el programa
main()
