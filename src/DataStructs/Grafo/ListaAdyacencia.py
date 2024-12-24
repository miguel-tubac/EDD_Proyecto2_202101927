from src.DataStructs.Lista.Lista import Lista
#from src.classes.Vertice import Vertice
#from src.DataStructs.Lista.Nodo import Nodo

class ListaAdyacencia:

    def __init__(self):
        self.vertices:Lista = Lista()

    def insertar(self, origen, destino):
        resultado = self.vertices.buscar(origen)

        if resultado != None:#si el valor ya existe
            resultado.valor.vecinos.insertar_final(destino)
        else:
            resultado = self.vertices.insertar_final(origen)

            resultado.valor.vecinos.insertar_final(destino)