# Este programa cifra y descifra un mensaje usando el módulo Fernet de la librería cryptography.
# Utiliza cifrado simétrico (AES) con una clave secreta generada automáticamente.
# El usuario escribe un mensaje, que se convierte en bytes, se cifra y
# luego se descifra para mostrar el texto original.

from cryptography.fernet import Fernet

# 1. Generar la clave
clave = Fernet.generate_key()
fernet = Fernet(clave)

# 2. Pedir mensaje al usuario
mensaje_usuario = input("Escribe un mensaje para cifrar: ")

# 3. Convertir mensaje a bytes
mensaje_bytes = mensaje_usuario.encode()

# 4. Cifrar el mensaje
mensaje_cifrado = fernet.encrypt(mensaje_bytes)
print("Mensaje cifrado:", mensaje_cifrado)

# 5. Descifrar el mensaje
mensaje_descifrado = fernet.decrypt(mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado.decode())
