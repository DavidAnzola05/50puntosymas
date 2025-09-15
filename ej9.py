numerochose=7
numeroescogido=int(input("Adivina el número que estoy pensando del 1 al 10: "))
if numeroescogido == numerochose:
    print("¡Felicidades! ¡Has adivinado el número!")
elif numeroescogido < numerochose:
    print("El número es mayor. Intenta de nuevo.")
else:
    print("El número es menor. Intenta de nuevo.")