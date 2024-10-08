import base64
import json
from key import Key

class Register_Authenticate():
    def __init__(self):
        self.filename = "usuarios.json"
        self.inicializar_json()

    def inicializar_json(self):
        """ Crea el archivo JSON con la información de los usuarios registrados. """
        # Comprobamos que el JSON no esté creado
        try:
            with open(self.filename, 'x') as file:
                # Creamos el JSON y le añadimos una lista vacía
                json.dump([], file, indent=4, sort_keys=True)
        # Si el archivo existe, no hacemos nada
        except FileExistsError:
            pass

    def obtener_usuarios_registrados(self):
        """ Actualiza el registro volcando el contenido del JSON """
        with open(self.filename, 'r') as file:
            return json.load(file)

    def guardar_usuarios_registrados(self, lista):
        """Vuelca el contenido pasado por parámetro en el archivo JSON"""
        with open(self.filename, 'w') as file:
            json.dump(lista, file, indent=4, sort_keys=True)

    def crear_usuario(self, username, password):
        """Devuelve un diccionario con el nuevo registro del usuario"""
        key = Key(password)
        salt, key = key.derivate_key()
        key = Key(password)
        salt, key = key.derivate_key()

        # Codificar salt y key en Base64 antes de almacenarlos

        key_base64 = base64.b64encode(key).decode('utf-8')
        salt_base64 = base64.b64encode(salt).decode('utf-8')

        return {'nombre_usuario':username, 'salt':salt_base64, 'key':key_base64}

    def registrar_usuario(self, username, password):
        """Comprueba si el usuario entrante no está registrado, y añade sus datos en el archivo JSON"""
        # Actualizamos el registro de usuarios
        registro = self.obtener_usuarios_registrados()
        # Verificamos si el usuario ya existe
        for user in registro:
            if user['nombre_usuario'] == username:
                return False
        # Creamos el nuevo usuario registrado
        usuario = self.crear_usuario(username, password)
        registro.append(usuario)
        # Guardamos los datos actualizados en el archivo JSON
        self.guardar_usuarios_registrados(registro)
        return True

    def autenticar_usuario(self, username, password):
        """Comprueba si el usuario entrante está registrado, y compara las contraseñas para darle
        acceso"""
        # Actualizamos el registro de usuarios
        registro = self.obtener_usuarios_registrados()
        # Verificamos si el usuario existe
        for user in registro:
            if user['nombre_usuario'] == username:
                key = Key(password)
                return key.authenticate(user)
        return False
