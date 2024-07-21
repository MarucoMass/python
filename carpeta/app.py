from archivo import Archivo
from carpeta import Carpeta

archivo1 = Archivo("documento1", 500)
archivo2 = Archivo("imagen1", 1500)

# Crear una carpeta y agregar los archivos
carpeta = Carpeta("mi_carpeta")
carpeta.nuevo_archivo(archivo1)
carpeta.nuevo_archivo(archivo2)

# Mostrar la carpeta y sus archivos
print(carpeta)

# Eliminar un archivo
carpeta.eliminar_archivo(archivo1)
print(carpeta)

# Copiar la carpeta
copia_carpeta = carpeta.copiar_carpeta()
print(copia_carpeta)