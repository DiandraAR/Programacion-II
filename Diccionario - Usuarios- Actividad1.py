# Crear el diccionario de usuarios y roles
usuarios = {
    "paul": "secretario",
    "alexa": "desarrollador",
    "danny": "analista",
    "antonella": "auxiliar"
}

# Pedir al usuario que escriba un nombre
nombre = input("Ingresa el nombre del usuario que deseas buscar: ").lower()

# Buscar el usuario en el diccionario
if nombre in usuarios:
    print(f"El rol de {nombre} es: {usuarios[nombre]}")
else:
    print("Usuario no encontrado.")