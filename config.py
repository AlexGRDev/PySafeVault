# config.py

import os
import sys

# Obtener el directorio del proyecto actual
base_dir = os.path.dirname(os.path.abspath(__file__))

# Crear el directorio si no existe
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Ruta donde se almacenará la clave secreta y la base de datos en la carpeta del proyecto
DATA_FILE = "vault.db"
SECRET_KEY_FILE = "secret.key"

print(f"Clave secreta almacenada en: {SECRET_KEY_FILE}")  # Usar SECRET_KEY_FILE aquí
print(f"Base de datos almacenada en: {DATA_FILE}")
