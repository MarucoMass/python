# Ejercicio 2: Evaluación de Clientes en una Tienda

# Para cada cliente de una tienda, es necesario evaluar su historial de compras y determinar si cumple con ciertos criterios de fidelidad establecidos por el negocio. Un cliente con al menos 5 compras realizadas en los últimos 3 meses cumple con los estándares propuestos por la tienda.

# Se desconoce la cantidad de clientes a evaluar. De cada cliente se conoce: nombre, número de cliente y detalle de compras realizadas.

# Mostrar un menú principal con las siguientes opciones:

# Registrar Cliente:
# Se registra a un cliente con los siguientes datos: nombre y número de cliente. Se debe validar que el número de cliente no esté duplicado en la lista de clientes registrados.
# Agregar Compra:
# Se ingresa el número de cliente y se lo busca. En caso de que el número de cliente no sea encontrado, se muestra un mensaje aclaratorio. Si el cliente es encontrado, se solicita ingresar los detalles de una nueva compra para agregar a su historial de compras.
# Mostrar Resumen:
# Se muestra un resumen que lista a los clientes evaluados, ordenados de mayor a menor por cantidad de compras realizadas en los últimos 3 meses. El resumen incluye el nombre del cliente, su número de cliente, sus detalles de compras y la cantidad de compras realizadas en los últimos 3 meses. Se indica también si el cliente cumple o no con los estándares de fidelidad de la tienda.
# Salir.
# Consideraciones:

# Cada cliente registrado es un diccionario que se agrega a la lista de clientes.
# Codificar la función validar_fidelidad(cliente: dict) -> bool en un módulo aparte.

from funcion_preparcial4 import validar_fidelidad

clientes = []

def registrar_cliente():
    nombre = input("Ingrese su nombre: ")

    numero_cliente = input("Numero de cliente: ")

    while any(x["num_cliente"] == numero_cliente for x in clientes):
        numero_cliente = input("Numero de cliente repetido. Ingrese otro: ")
        
    cliente = {
        "nombre": nombre,
        "num_cliente": numero_cliente,
        "compras": []
    }
    clientes.append(cliente)


def agregar_compra():
    numero_cliente = input("Numero de cliente: ")
    encontrado = False
    for cliente in clientes:
        if cliente["num_cliente"] == numero_cliente:
            encontrado = True
            compras = input("Ingrese la compra: ")
            cliente["compras"].append(compras)
    
    if not encontrado:
        print("No se encontró a nadie")

def mostrar_resumen():
    clientes_ordenados = sorted(clientes, key=lambda x: len(x["compras"]), reverse=True)
    for cliente in clientes_ordenados:
        compras = ", ".join(cliente["compras"])
        print(f"Nombre: {cliente["nombre"]}")
        print(f"Numero cliente: {cliente["num_cliente"]}")
        print(f"Compras: {compras}")
        print(f"Cantidad de compras: {len(cliente["compras"])}")
        print(f"El cliente es fiel" if validar_fidelidad(cliente['compras']) else "No es fiel el cliente")

while True:
    prompt = "1- Registrar cliente\n"
    prompt += "2- Agregar compra\n"
    prompt += "3- Mostrar resumen\n"
    prompt += "4- Salir\n"

    opt = int(input("Ingrese una opción\n" + prompt))

    if opt == 1:
        registrar_cliente()
    elif opt == 2:
        agregar_compra()
    elif opt == 3:
        mostrar_resumen()
    elif opt == 4:
        print("Chau\n")
        break
    else:
        print("Opción inválida\n")
