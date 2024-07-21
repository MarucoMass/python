from clienteFrecuente import ClienteFrecuente
from cliente import Cliente

cliente_frecuente = ClienteFrecuente(178, "mariomass23@gmail.com")

cliente1 = Cliente("Mario", "Mass", cliente_frecuente)

cliente_frecuente.add_puntos(1000)

cliente1.nueva_compra(2400)


print(cliente1)