#main.py

import os
import sys
from pysafevault import SafeVault, DATA_FILE
from cryptography.fernet import Fernet

def display_menu():
    print("\n=== PySafeVault ===")
    print("1. Guardar nueva contraseña")
    print("2. Consultar contraseñas")
    print("3. Eliminar servicio")
    print("4. Salir")

def delete_service(secret_key):
    """Elimina un servicio completo del almacén de contraseñas."""
    vault = SafeVault(secret_key)
    services = vault.list_services()  # Obtener todos los servicios disponibles

    if not services:
        print("No hay servicios almacenados.")
        return

    print("Servicios disponibles:")
    for idx, service in enumerate(services, start=1):
        print(f"{idx}. {service}")

    service_idx = int(input("Selecciona el servicio que deseas eliminar: ")) - 1
    if 0 <= service_idx < len(services):
        service = services[service_idx]
        if vault.delete_service(service):
            print(f"Servicio '{service}' y todas sus credenciales han sido eliminados exitosamente.")
        else:
            print(f"No se pudo eliminar el servicio '{service}'.")
    else:
        print("Opción inválida.")

def main():
    # Cargar o generar la clave secreta
    vault = SafeVault()

    while True:
        display_menu()
        choice = input("Elige una opción (1-4): ")

        if choice == '1':
            service = input("Introduce el nombre del servicio (ej. Gmail): ")
            username = input("Introduce el nombre de usuario: ")
            password = input("Introduce la contraseña: ")
            vault.add_credential(service, username, password)
            print(f"Contraseña para {username} en {service} guardada exitosamente.")
        elif choice == '2':
            consult_password(vault.secret_key)
        elif choice == '3':
            delete_service(vault.secret_key)  # Llamada a la nueva función de eliminar servicio
        elif choice == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
