print("Programa que determina si el numero es par o impar")
print("=========================================================\n")
numero = int(input("Ingrese un numero entero: "))

if numero % 2==0:
    print(f"El {numero} es par")
elif numero % 1==0:
    print(f"El {numero} es impar")
else:
    ("El numero que ingreso no es valido")

print("Fin")