nombre = input("Ingrese su nombre: ")
print(nombre + ", Vamos a promediar tus notas")
nota_mate = int(input((nombre +", Cual es tu calificacion en Matematicas?: ")))
nota_quim = int(input((nombre +", Cual es tu calificacion en Quimica?: ")))
nota_bio = int(input((nombre +", Cual es tu calificacion en Biologia?: ")))

promedio = (nota_mate + nota_quim + nota_bio) / 3
promedio = int(promedio)

if promedio >= 5:
    print('Felicidades' + nombre + ' "Aprobaste" con un promedio de:', promedio)

print("Fin")