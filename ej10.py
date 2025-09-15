contraseña=str(input("Ingrese la contraseña: "))
contrasñaminima=8
print("La contraseña tiene", len(contraseña), "caracteres")
if len(contraseña) >= contrasñaminima:
    print("Contraseña válida")
else:  
    print("Contraseña inválida, debe tener al menos", contrasñaminima, "caracteres")    