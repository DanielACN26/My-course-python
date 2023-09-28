print("Sistema para calcular el promedio de un alumno")
nombre = (input("Ingrese su nombre: "))
matematicas = float(input(nombre + ", Ingrese su calificacion en matematicas: "))
quimica = float(input(nombre + ", Ingrese su calificacion en quimic: "))
biologia = float(input(nombre + ", Ingrese su calificacio en biologia: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >= 5:
    print(f"{nombre}. Felicidades aprobo, su promedio es de: {round(promedio,2)}") #El round funciona para controlar la cantidad de decimales.
else:
    print(f"{nombre}. No aprobo, su promedio es de: {promedio}")

print("Fin")