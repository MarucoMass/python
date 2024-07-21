from movimiento import Movimiento
from tipo_movimiento import TipoMovimiento 
from datetime import date, time

tipo_movimiento = TipoMovimiento("hola", 34)

movimiento = Movimiento(
    5,
    150.0,
    tipo_movimiento
)


print(movimiento)
print(movimiento.fecha_liquidacion)
print(movimiento.iva)
print(movimiento.comision)