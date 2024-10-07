
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
        kdf = Scrypt(salt=salt_json, length=32, n=2 ** 14, r=8, p=1)
        kdf.verify(self.encoded_password(), key_json)