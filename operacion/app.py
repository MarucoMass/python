from datetime import date
from tipo_operacion import TipoOperacion
from activo import Activo
from operacion import Operacion

# Crear un tipo de operación
tipo_operacion = TipoOperacion("Compra")

# Crear un activo
activo = Activo("Acción A", "A", 0.5)

# Crear una operación
operacion = Operacion(
    date.today(),
    100,
    10.0,
    tipo_operacion,
    activo
)

# Mostrar la operación
print(operacion)