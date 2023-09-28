print("Bienvenido, vamos a convertir numero en letras")

numero = int(input("Ingrese un numero del 1 al 5:"))

if numero == 1:
     print(f'El numero {numero}  se escribe "uno"')
elif numero == 2:
     print(f'El numero {numero} se escribe "dos"')
elif numero == 3:
     print(f'El numero {numero} se escribe "tres"')
elif numero == 4:
     print(f'El numero {numero} se escribe "cuatro"')
elif numero == 5:
     print(f'El numero {numero} se escribe "cinco"')
else:
    print(f"Numero invalido, vuelva a intentarlo")

print("Fin.")