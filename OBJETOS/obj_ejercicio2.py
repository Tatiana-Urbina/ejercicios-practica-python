class Auto:
    color = ""
    modelo = ""
    llantas = ""
    puertas = ""
    velocidad = ""
    marcha = None

    """
    Creando métodos 
    Sintaxis:
    def nombre_Metodo(self):
    acciones
    """

    def mostrarDatos(self):
        print("Color: ", self.color)
        print("Modelo: ", self.modelo)
        print("Llantas: ", self.llantas)
        print("Puertas: ", self.puertas)
        print("Velocidad: ", self.velocidad)


gol = Auto()
gol.color = "Negro"

gol.mostrarDatos()