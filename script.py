
from register_authenticate import Register_Authenticate

class Script():
    def __init__(self):
        self.user_manager = Register_Authenticate()

    def menu(self):
        """Imprime por pantalla un menú que se ejecuta hasta el fin del programa"""
        # Desplegamos el menú de opciones
        print("\n--- Menú ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        # Preguntamos por la opción a ejecutar
        opcion = input("\nSelecciona una opción (1/2/3): ")
        # Guardamos la opción
        return opcion

    def action(self, opcion):
        """Dependiendo de la acción a ejecutar, mostraremos ciertos mensajes y ejecutaremos
        los respectivos métodos de registro y/o autenticado"""
        # Registro de usuario
        if opcion == "1":
            username = input("Ingresa un nombre de usuario: ")
            password = input("Ingresa una contraseña: ")
            self.user_manager.registrar_usuario(username, password)
        # Autenticado de usuario registrado (inicio de sesión)
        elif opcion == "2":
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña: ")
            if self.user_manager.autenticar_usuario(username, password):
                print(f"¡Bienvenido {username}!")
                return True
            else:
                print("Acceso denegado.")
        # Salir del bucle
        elif opcion == "3":
            print("Saliendo...")
            # Indicamos que queremos salir
            return True
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    def run(self):
        """Ejecuta el menú en un bucle hasta que el usuario decida salir"""
        while True:
            # Ejecutamos el menú en un bucle infinito
            opcion = self.menu()
            # Si la acción fue salir, rompemos el bucle y finalizamos el programa
            if self.action(opcion):
                break