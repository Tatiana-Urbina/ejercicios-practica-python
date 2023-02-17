#creando la clase
"""Sintaxis:
class nombre_Clase:
    acciones"""
class auto:
    pass

#creando objetos de la clase o instancias
"""Sintaxis:
variable= nombre_de_la_Clase"""

cochecito = auto()


#Asignar atributos
"""
Nombre_objeto.nombre_atributo= valor
"""
cochecito.color = "rojo"
cochecito.modelo = "SEG"
cochecito.puertas = 4
cochecito.ruedas = 4

print("Color: ", cochecito.color)
print("Puertas: ", cochecito.puertas)
print("Modelo: ", cochecito.modelo)
print("Ruedas: ", cochecito.ruedas)
