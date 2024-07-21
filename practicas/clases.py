# El siguiente ejemplo implementa todo lo explicado hasta aquí:
# Se implementa una clase llamada Alumno, que posee un atributo de clase (nro_alumnos) que lleva la cuenta de los objetos instanciados.
# Cada objeto posee un nombre y una nota.  
# Se definen métodos para inicializar sus atributos, imprimir el estado del objeto, procesar su eliminación de la memoria y para mostrar un texto con su estado. El estado es “regular” (nota menor o igual a 4), “bueno” (nota mayor a 4 y menor que 9) o “excelente” (nota mayor que 9).
# En el programa principal se instancian dos objetos de la clase Alumno y se muestran algunas de sus características. Al salir del programa se ve como son eliminados de la memoria.


# class Alumno:
#     nro_alumnos = 0

#     def __init__(self, nombre, nota):
#         self.nombre = nombre
#         self.nota = nota
#         Alumno.nro_alumnos += 1

#     def __str__(self):
#         return f"El nombre: {self.nombre}. Nota: {self.nota}"
    
#     def __del__(self):
#         Alumno.nro_alumnos -= 1
#         print("Alumno dado de baja")
#         print(f"{Alumno.nro_alumnos} es la cantidad restante de alumnos")
    
#     def mostrar_estado(self): # ¿está aprobado?
#         print(f"El estado de {self.nombre} es ",end="" )
#         if self.nota <= 4:
#             print("regular")
#         elif self.nota < 9:
#             print("bueno")
#         else:
#             print("excelente")



# alumno1 = Alumno("Mario", 10)
# alumno2 = Alumno("Jorge", 1)
# print(alumno1)
# print(alumno2)

# alumno1.mostrar_estado()
# alumno2.mostrar_estado()
# input("Pulse enter para salir")

    



    
# from datetime import date

# class Usuario:
#     def __init__(self, user_name, email, password, nombre, apellido):
#         self._user_name = user_name
#         self.estado = True 
#         self.email = email
#         self.password = password
#         self.nombre = nombre
#         self.apellido = apellido
#         self.fecha_alta = date.today()
#         self.fecha_baja = None

