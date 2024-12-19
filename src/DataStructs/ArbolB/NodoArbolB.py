class NodoArbolB:
    def __init__(self, hoja: bool = False):
        self.hoja: bool = hoja
        self.claves: list = [] #orden del arbol -1 (m - 1), estos son los valores que se almacenan
        self.hijos: list = [] #Esto si va ha ser el roden del arbol, es decir m