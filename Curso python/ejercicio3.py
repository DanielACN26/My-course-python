numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))
numero3 = int(input("Ingrese el tercer numero entero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El {numero1} es el mas grande")
else:
    if numero2 > numero3:
        print(f"El {numero2} es el numero mas grande")
    else:
        print(f"El {numero3} es el numero mas grande")