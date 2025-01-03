# PySafeVault

**PySafeVault** es un gestor de contraseñas sencillo y seguro desarrollado en Python. Este proyecto utiliza la librería `cryptography` para cifrar y proteger tus credenciales, asegurando que solo tú tengas acceso a ellas.

## Características
- **Guardar contraseñas:** Almacena credenciales de forma encriptada.
- **Consultar contraseñas:** Recupera contraseñas de forma segura.
- **Eliminar contraseñas:** Borra entradas que ya no necesites.

## Requisitos
- Python 3.8 o superior.
- Paquete `cryptography` para cifrado de datos.

Instala el paquete con el siguiente comando:

```bash
   pip install cryptography
```
## Instalación

1. Clona este repositorio:

```bash
   git clone https://github.com/username/PySafeVault.git
   cd PySafeVault
```
2. Instala las dependencias:
_Asegúrate de tener pip instalado y luego instala las dependencias necesarias:_

```bash
   pip install -r requirements.txt
```

3. Genera la clave secreta:
_Si es la primera vez que ejecutas la aplicación, se generará una clave secreta automáticamente al ejecutar el siguiente comando:_

```bash
   python main.py
```
_Esto creará un archivo secret.key que se utilizará para cifrar y descifrar las contraseñas._

## Uso

_Una vez que hayas instalado todas las dependencias y generado la clave secreta, puedes ejecutar el programa con el siguiente comando:_

```bash
   python main.py
```
_Esto iniciará el menú de la aplicación, desde donde podrás:_
1. **Guardar contraseñas:** Introduce el nombre de la cuenta y la contraseña, y la aplicación las cifrará y almacenará en el archivo secret.key.
2. **Consultar contraseñas:** Introduce el nombre de la cuenta y la aplicación recuper ará la contraseña cifrada y la mostrará en pantalla.
3. **Eliminar contraseñas:** Introduce el nombre de la cuenta y la aplicación eliminará la entrada correspondiente del archivo secret.key.
4. **Salir:** Cierra la aplicación.

## Archivos importantes
- **secret.key:**  Contiene la clave secreta utilizada para cifrar y descifrar las contraseñas.
- **vault.db:**  Base de datos donde se almacenan las contraseñas cifradas.

## Contribuciones
_Si deseas contribuir a PySafeVault, sigue estos pasos:_

1. Haz un fork del repositorio.
2. Crea una rama nueva 
```bash 
   git checkout -b feature-nueva 
```
3. Realiza tus cambios y confirma 
```bash 
   git commit -am 'Agregada nueva característica' 
```
4. Haz un push a la rama 
```bash
   git push origin feature-nueva 
```
5. Abre un pull request.

