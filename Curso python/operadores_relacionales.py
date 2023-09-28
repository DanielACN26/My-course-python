print("Introduce dos numero a comparar \n")

numero_uno = int(input("Ingrese el primer numero:"))
numero_dos = int(input("Ingrese el segundo numero:"))

print("\n Los numero a comparar son", numero_uno, "y" ,numero_dos, "\n")

if numero_uno == numero_dos:
    print("Son iguales")
elif numero_uno != numero_dos:
    print("Son diferentes")
else:
    print("Los numeros que ingreso no son validos")

if numero_uno > numero_dos:
    print("El primer numero es mayor")
elif numero_uno < numero_dos:
    print("El segundo numero es mayor")
else:
    print("Son iguales")

if numero_uno >= numero_dos:
    print("El primer numero es mayor o igual")
elif numero_uno <= numero_dos:
    print("El segundo numero es mayor o igual")

print("Fin.")