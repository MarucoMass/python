# Para cada estudiante de una escuela, es necesario evaluar su desempeño académico y determinar si cumple con los estándares de rendimiento establecidos por la institución. Un estudiante con un promedio de calificaciones igual o superior a 7 cumple con los estándares propuestos por la escuela.

# Se conoce la cantidad de estudiantes a evaluar, los cuales son 60. De cada estudiante se conoce: nombre, número de identificación estudiantil y calificaciones obtenidas.

# Mostrar un menú principal con las siguientes opciones:

# Registrar Estudiantes:
# Se cargan todos los estudiantes de una vez. Para cada estudiante, se ingresan los siguientes datos: nombre, número de identificación estudiantil y calificaciones obtenidas en diferentes materias. Se debe validar que el número de identificación estudiantil tenga una longitud de 6 caracteres.
# Agregar Calificación:
# Se ingresa el número de identificación estudiantil del estudiante y se lo busca. En caso de que el número de identificación estudiantil no sea encontrado, se muestra un mensaje aclaratorio. Si el estudiante es encontrado, se solicita ingresar una nueva calificación para agregar a la lista de calificaciones del estudiante.
# Mostrar Resumen:
# Se muestra un resumen que lista a los estudiantes evaluados, ordenados de mayor a menor por promedio de calificaciones. El resumen incluye el nombre del estudiante, su número de identificación estudiantil, sus calificaciones obtenidas y su promedio de calificaciones. Se indica también si el estudiante cumple o no con los estándares de rendimiento de la escuela.
# Salir.
# Consideraciones:

# Cada estudiante registrado es un diccionario que se agrega a la lista de estudiantes.
# Codificar la función validar_promedio_calificaciones(calificaciones: list) -> bool en un módulo aparte.

estudiantes = []

def cargar():
    for i in range(1):
        nombre = input("Ingrese el nombre: \n")

        identificacion_est = input("Ingrese su identificación: \n")

        while len(identificacion_est) != 6:
            identificacion_est = input("Máximo 6 carácteres. Ingrese su identificación\n")

        calificaciones = []

        while True:
            calificacion = int(input("Ingrese la calificación: \n"))
            calificaciones.append(calificacion)

            agregar = input("Agrega otra?: \n S \n N \n")
            if agregar.upper() == "N":
                break

        estudiante = {
            "nombre": nombre,
            "identificacion": identificacion_est,
            "calificaciones": calificaciones
        }

        estudiantes.append(estudiante)

def agregar():
    identificacion_est = input("Ingrese su identificación: \n")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion_est:
            encontrado = True
            calificaciones = int(input("Calificaciones: \n"))
            estudiante["calificaciones"].append(calificaciones)
            break
    
    if not encontrado:
        print("No hay estudiante con esa identificación")


def validar_promedio_calificaciones(calificaciones: list) -> bool:
    if sum(calificaciones) / len(calificaciones) < 7:
        return False
    return True

def mostrar():
    estudiantes_ordenados = list(sorted(estudiantes, key=lambda x: sum(x["calificaciones"]) / len(x["calificaciones"]), reverse=True))

    for estudiante in estudiantes_ordenados:
        notas = " - ".join(str(nota) for nota in estudiante["calificaciones"])
        print(f"Nombre: {estudiante["nombre"]}")
        print(f"Nro de identificación: {estudiante["identificacion"]}")
        print(f"Calificaciones: {notas}")
        print(f"Promedio: {sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])}")
        print("Aprobó\n" if validar_promedio_calificaciones(estudiante["calificaciones"]) else "No aprobó\n")


while True:
    prompt = "1- Registrar estudiantes\n"
    prompt += "2- Agregar calificación\n"
    prompt += "3- Mostrar resúmen\n"
    prompt += "4- Salir"

    opt = int(input("Elija una opción\n" + prompt + "\n"))

    if opt == 1:
        cargar()
    elif opt == 2:
        agregar()
    elif opt == 3:
        mostrar()
    elif opt == 4:
        print("Chau")
        break
    else:
        print("Opción incorrecta")
