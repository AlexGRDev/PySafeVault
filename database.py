# database.py

import json
import os
from pysafevault import *

# Definir el archivo de datos de la base de datos
DATA_FILE = os.path.expanduser("~\\AppData\\Roaming\\PySafeVault\\vault.db")

def load_data(self):
    """Carga los datos desde el archivo de base de datos (vault.db)."""
    if os.path.exists(self.vault_file):
        with open(self.vault_file, 'r') as file:
            content = file.read().strip()  # Leer el contenido y eliminar espacios en blanco
            if content:  # Si el archivo no está vacío
                return json.loads(content)
            else:
                print("El archivo está vacío, retornando un diccionario vacío.")
                return {}  # Retorna un diccionario vacío si el archivo está vacío
    else:
        print("No se encontró el archivo de datos, retornando un diccionario vacío.")
        return {}  # Retorna un diccionario vacío si el archivo no existe

def save_data(data):
    """Guarda las credenciales en el archivo de datos en formato JSON."""
    print("Guardando datos en el archivo...")
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
