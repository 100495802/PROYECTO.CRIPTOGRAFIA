
import os
import base64

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Key():
    def __init__(self, password):
        # Convertimos la contraseña a bytes
        self.password = password.encode('utf-8')
        # Generamos el salt (número de 16 bytes aleatorio)
        self.salt = os.urandom(16)

    def derivate_key(self):
        """Genera una clave a partir de la contraseña"""
        kdf = Scrypt(salt=self.salt, length=32, n=2 ** 14, r=8, p=1)
        # Derivamos la clave usando la contraseña en formato bytes
        key = kdf.derive(self.password)
        return self.salt, key

    def authenticate(self, user: dict):
        """Verifica la contraseña del usuario"""
        salt_json = user["salt"]
        key_json = user["key"]
        # Convertimos el salt y la clave desde base64 si son cadenas
        if isinstance(salt_json, str):
            salt = base64.b64decode(salt_json)
        else:
            salt = salt_json
        if isinstance(key_json, str):
            key = base64.b64decode(key_json)
        else:
            key = key_json
        # Preparamos el KDF con el salt almacenado
        kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1)
        # Verificamos la contraseña, que debe estar en bytes
        try:
            # Verificamos si la clave derivada coincide
            kdf.verify(self.password, key)
            return True
        except Exception as e:
            return False