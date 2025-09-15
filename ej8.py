NOT1=int(input("Ingrese la primera calificación: "))
NOT2=int(input("Ingrese la segunda calificación: "))
NOT3=int(input("Ingrese la tercera calificación: "))

sum = NOT1 + NOT2 + NOT3 
promedio = sum / 3 
print("Calificaciones:", NOT1, NOT2, NOT3)
print("Promedio:", promedio)
if promedio >= 7:
    print("¡Excelente!")
elif promedio >= 5:
    print("Pasaste, pero puedes mejorar.")
else:
    print("Reprobaste, mejor suerte la próxima vez.")   