empleados = []


def registarEmpleados():
    # Itero por cada empleado
    for i in range(2):

        nombre = input("Ingrese el nombre de empleado: ")
        while True:
            legajo = input("Ingrese su numero de legajo: ")
            if len(legajo) != 5:
                print("El legajo debe de tener 5 caracteres")
            else:
                break
        antiguedad = int(input("Ingrese su antiguedad(En meses): "))
        dic = {
            "Nombre": nombre,
            "legajo": legajo,
            "antiguedad": antiguedad,
            "cursosRealizados": [],
        }
        empleados.append(dic)


def agregarCursos():

    legajoPersona = input("Ingrese su numero de legajo: ")
    bandera = False
    for dicEmpleado in empleados:
        if dicEmpleado["legajo"] == legajoPersona:
            bandera = True
            optEmpleado: str = " "
            while optEmpleado != "N":
                cursosNuevos = input("Ingrese el curso que haya realizado: ")
                dicEmpleado["cursosRealizados"].append(cursosNuevos)
                optEmpleado = input(
                    "Si quiere ingresar más cursos presione S, sino N: "
                ).upper()

    if not bandera:
        print("Ese numero de legajo no existe")



print("1 - Registrar empleados")
print("2 - Agregar nuevo curso")
print("3 - Mostrar resumen")
print("4 - Salir")
opt = input("Ingrese una opcion del menu: ")
while opt != 4:
    if opt == "1":
        registarEmpleados()
    elif opt == "2":
        agregarCursos()
        print(empleados)
    elif opt == "3":
        listaOrdenada = list(
            sorted(empleados, key=lambda x: len(x["cursosRealizados"]), reverse=True)
        )
        print(listaOrdenada)
    elif opt == "4":

        break

    print("1 - Registrar empleados")
    print("2 - Agregar nuevo curso")
    print("3 - Mostrar resumen")
    print("4 - Salir")
    opt = input("Ingrese una opcion del menu: ")
print("Gracias por utilizar nuestro sistema.")