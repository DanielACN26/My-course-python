#Ejmplo para break
print("While con la sentencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print(f"Valor actual de la variable {contador}")

print("Fin del programa, la sentencia break se ha ejecutado")


#Ejemplo para continue

print("While con la sentencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print(f"Valor actual de la variable {contador}")