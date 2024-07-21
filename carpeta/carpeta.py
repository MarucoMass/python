from archivo import Archivo

class Carpeta:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__archivos = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def archivos(self):
        return self.__archivos
    
    @property
    def tamano_mb(self):
        return sum(list(x.peso_kb for x in self.archivos))

    @property
    def cantidad_archivos(self):
        return len(self.archivos)

    def nuevo_archivo(self, archivo: Archivo):
        self.__archivos.append(archivo)

    def eliminar_archivo(self, archivo: Archivo):
        self.__archivos.remove(archivo)


    def copiar_carpeta(self):
        nueva_carpeta = Carpeta(f"{self.__nombre}_copia")
        for archivo in self.__archivos:
            nueva_carpeta.nuevo_archivo(archivo.copiar_archivo())
        return nueva_carpeta

    def __str__(self):
        return (f'Carpeta(nombre={self.nombre}, tamano_mb={self.tamano_mb}, '
                f'cantidad_archivos={self.cantidad_archivos})')
