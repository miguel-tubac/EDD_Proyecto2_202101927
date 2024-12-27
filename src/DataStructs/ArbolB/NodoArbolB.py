from src.classes.Vehiculo import Vehiculo
class NodoArbolB:
    def __init__(self, hoja: bool = False):
        self.hoja: bool = hoja
        #self.claves: list[int] = [] #orden del arbol -1 (m - 1), estos son los valores que se almacenan
        self.claves: list[Vehiculo] = [] #esto es lo que debo de desarrollar 
        self.hijos: list[NodoArbolB] = [] #Esto si va ha ser el roden del arbol, es decir m


    def __str__(self):
        return f"Hoja: {self.hoja} - Claves: {self.claves} - Hijos {self.hijos}"