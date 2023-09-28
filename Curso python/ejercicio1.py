print("Bienvenido al programa de Rappi")
print("========================================")
nombre = input("Ingrese su nombre: ")
print("Acontinuacion ingrese su departamento\n")
print('Departamento de atencion al cliente "Clave 1"')
print('Departamento de logistica "Clave 2"')
print('Gerencia "Clave 3"')

clave = input("Ingrese su clave: ")
clave = clave.lower()

antiguedad = int(input("Ingrese el tiempo que lleva en la empresa: "))

if clave == "clave 1":
    print("Bienvenido al departamento de atencion al cliente\n")
    print("===============================")
    if antiguedad >=1 and antiguedad <=2:
        print(f"{nombre}, tiene 6 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print(f"{nombre}, tiene 14 dias de vacaciones")
    elif antiguedad >=7:
        print(f"{nombre}, tiene 20 dias de vacaciones")
    else:
        print(f"{nombre}, no tiene vacaciones")

elif clave == "clave 2":
    print("\nBienvenido al departamento de logistica\n")
    print("===============================")
    if antiguedad >=1 and antiguedad <=2 :
        print(f"{nombre}, tiene 7 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print(f"{nombre}, tiene 15 dias de vacaciones")
    elif antiguedad >=7:
        print(f"{nombre}, tiene 22 dias de vacaciones")
    else:
        print(f"{nombre}, no tiene vacaciones")

elif clave == "clave 3":
    print("\nBienvenido al departamento de gerencia")
    print("===============================")
    if antiguedad >=1 and antiguedad <=2:
        print(f"{nombre}, tiene 10 dias de vacaciones")
    elif antiguedad >=2 and antiguedad <=6:
        print(f"{nombre}, tiene 20 dias de vacaciones")
    elif antiguedad >=7:
        print(f"{nombre}, tiene 30 dias de vacaciones")
    else:
        print(f"{nombre}, no tiene vacaciones")
else:
    print("Esta clave de departamento no existe, Por favor vuelve a intenarlo")