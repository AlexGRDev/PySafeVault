#__init__.py

import os
import json
from cryptography.fernet import Fernet
import base64

class SafeVault:
    def __init__(self, secret_key=None):
        if secret_key is None:
            if os.path.exists('secret.key'):
                with open('secret.key', 'rb') as f:
                    self.secret_key = f.read()
            else:
                self.secret_key = Fernet.generate_key()
                with open('secret.key', 'wb') as f:
                    f.write(self.secret_key)
                print(f"Clave secreta generada y almacenada en: secret.key")
        else:
            self.secret_key = secret_key

        self.data = self.load_data()  # Asumiendo que data es un diccionario

    def load_data(self):
        try:
            with open(DATA_FILE, 'rb') as f:
                encrypted_data = f.read()
                if encrypted_data:
                    cipher = Fernet(self.secret_key)
                    decrypted_data = cipher.decrypt(encrypted_data)
                    return pickle.loads(decrypted_data)
        except (FileNotFoundError, EOFError):
            return {}

    def save_data(self):
        with open(DATA_FILE, 'wb') as f:
            cipher = Fernet(self.secret_key)
            encrypted_data = cipher.encrypt(pickle.dumps(self.data))
            f.write(encrypted_data)

    def list_services(self):
        return list(self.data.keys())

    def add_credential(self, service, username, password):
        if service not in self.data:
            self.data[service] = {}
        self.data[service][username] = password
        self.save_data()
        return True

    def view_service_credentials(self, service):
        if service in self.data:
            for username, password in self.data[service].items():
                print(f"Usuario: {username} | Contraseña: {password}")
        else:
            print(f"No se encontraron credenciales para el servicio '{service}'.")

    def delete_credential(self, service, username):
        if service in self.data and username in self.data[service]:
            del self.data[service][username]
            self.save_data()
            return True
        return False

    def delete_service(self, service):
        """Elimina un servicio completo y todas sus credenciales."""
        if service in self.data:
            del self.data[service]
            self.save_data()
            return True
        return False
