from functionsPreParcial2 import validar_numero_documento

medicos = []

def registrar_medico():
    dni = input("Ingrese el dni\n")

    while validar_numero_documento(medicos, dni):
        print("Ya hay un médico con ese dni\n")
        dni = input("Ingrese el dni")

    if not validar_numero_documento(medicos, dni):
        nombre = input("Ingrese el nombre\n")

        medico = {
            "dni": dni,
            "nombre": nombre,
            "titulos": []
        }

        medicos.append(medico)


def agregar_titulo():
    dni = input("Ingrese el dni\n")
    bandera = False

    for medico in medicos:
        if medico["dni"] == dni:
            titulo_realizados = input("Ingrese el titulo\n")
            medico["titulos"].append(titulo_realizados)
            bandera = True
            break

    if not bandera:
        print("No se encontró a nadie con ese dni")



def mostrar():
    medicos_ordenados = list(sorted(medicos, key=lambda x: len(x["titulos"]), reverse=True))
    for indice, medico in enumerate(medicos_ordenados):
        titulos = ", ".join(medico["titulos"])
        print(indice + 1)
        print(f"{medico['nombre']} - {medico['dni']}\nTitulos: {titulos} \nCantidad de titulos: {len(medico['titulos'])}")


while True:
    prompt = "\n1- Registrar al médico"
    prompt += "\n2- Agregar titulo reconocido"
    prompt += "\n3- Mostrar resumen"
    prompt += "\n4- Salir"

    opt = int(input("Elija una opción:" + prompt + "\n"))

    if opt == 1:
        print("Registrar")
        registrar_medico()
    elif opt == 2:
        print("Agregar")
        agregar_titulo()
    elif opt == 3:
        print("Mostrar")
        mostrar()
    elif opt == 4:
        print("Chau")
        break
    else:
        print("Invalid option")