'''
2. Validación de acceso:
Solicita usuario, contraseña y rol (admin, editor, visitante). Verifica si las credenciales
son válidas y muestra los permisos disponibles según el rol. Usa múltiples condicionales
y lógica anidada.
'''

usuarios={
    'admin':{'contraseña':'admin123','rol':'admin'},
    'editor':{'contraseña':'editor123','rol':'editor'},
    'visitante':{'contraseña':'visitante123','rol':'visitante'}
}
usuario= input("Por favor, ingresa el usuario: ")
contraseña= input("Por favor, ingresa la contraseña: ")

if usuario in usuarios and  contraseña==usuarios[usuario]['contraseña']:
    rol= usuarios[usuario]['rol']
    print(f"Acceso concedido- Rol: {rol.upper()}")

    if rol=="admin":
        print("Permisos") 
        print("Permisos de Admin")
    elif rol=="editor":
        print("Permisos")
        print("Permisos de Editor")
    else:
        print("Permisos")
        print("Permisos de Visitante")
else:
    print("Acceso denegado")         
    
