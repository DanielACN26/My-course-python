print("=====================================")
print('"CONVERTIDOR"')
print("=====================================")

print("Menu.\n")
print("Presiona 1 para convertir un numero a palabra")
print("Presiona 2 para convertir en palabra un numero. \n")

opcion_seleccionada = int(input("Ingrese la opcion que desea: "))

print()

if opcion_seleccionada == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_uno = int(input("Ingrese el numero que desea convertir: "))

    if opcion_uno == 1:
        print(f'El numero {opcion_uno} se escribe "1"')
    elif opcion_uno == 2:
        print(f'El numero {opcion_uno} se escribe "dos"')
    else:
        print("El numero que ingreso esta fuera de rango")

elif opcion_seleccionada == 2:
    print("\n Conversor de palabra a numero. \n")

    opcion_dos = (input("Ingrese la palabra que desea convertir: "))
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print(f' La palabra {opcion_dos} es "1"')
    elif opcion_dos == "dos":
        print(f'La palabra {opcion_dos} es "2"')
    else:
        print("La palabra igresada no esta registrada")

else:
    print("La opcion seleccionada no existe")

print("Fin.")