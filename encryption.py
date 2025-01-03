#encryption.py

from cryptography.fernet import Fernet

def load_secret_key():
    """Carga la clave secreta desde un archivo."""
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            return f.read()
    else:
        print("No se encontró la clave secreta. Generando una nueva clave.")
        return None

def save_secret_key(secret_key):
    """Guarda la clave secreta en el archivo."""
    with open(key_file, 'wb') as f:
        f.write(secret_key)
