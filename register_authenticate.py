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
        return {'nombre_usuario':username, 'salt':str(salt), 'key':str(key)}

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

    """def autenticar_usuario(self, username, password):
    user = self.get_user_by_username(username)  # Asumimos que recupera el usuario por nombre
    if user is None:
        return False

    # Ahora intentamos autenticar usando la clase Key
    key = Key(password)  # Pasamos la contraseña ingresada
    if key.authenticate(user):
        return True
    return False"""