
import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Key():
    def __init__(self, password):
        self.password = password
        self.salt = os.urandom(16)
    def encode_password(self):
        """Cifra la contraseña"""
        missing_padding = len(self.password) % 4
        if missing_padding:
            self.password += "=" * (4 - missing_padding)
        return base64.b64decode(self.password)
    def derivate_key(self):
        """A partir de la contraseña cifrada, generamos la clave"""
        encoded_password = self.encode_password()
        kdf = Scrypt(salt=self.salt, length=32, n=2 ** 14, r=8, p=1)
        key = kdf.derive(encoded_password)
        return self.salt, key

    def authenticate(self, user:dict):
        salt_json = user["salt"]
        key_json = user["key"]
        # Convierte a bytes si son cadenas
        if isinstance(salt_json, str):
            salt = salt_json.encode()  # Convertimos el salt a bytes
        else:
            salt = salt_json  # Si ya es bytes, lo dejamos tal cual
        if isinstance(key_json, str):
            key = key_json.encode()  # Convertimos la clave a bytes
        else:
            key = key_json  # Si ya es bytes, lo dejamos tal cual
        kdf = Scrypt(salt=salt, length=32, n=2 ** 14, r=8, p=1)
        # Asegúrate de que la contraseña derivada esté en formato bytes
        derived_password = self.encode_password()
        if isinstance(derived_password, str):
            derived_password = derived_password.encode()
        # Verificación de la clave
        try:
            kdf.verify(derived_password, key)
            return True
        except Exception as e:
            return False