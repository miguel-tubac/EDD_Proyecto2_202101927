from src.DataStructs.Lista.Lista import Lista
from src.classes.Vertice import Vertice
from src.DataStructs.Lista.Nodo import Nodo
from src.classes.Ruta import Ruta
from src.DataStructs.Cola.Cola import Cola
from copy import copy

class ListaAdyacencia:

    def __init__(self):
        self.vertices:Lista[Vertice] = Lista()

    def insertar(self, ruta:Ruta):
        origen:Vertice = Vertice(ruta.origen)
        destino:Vertice = Vertice(ruta.destino, ruta.tiempo)

        resultado: Nodo[Vertice] = self.vertices.buscar(origen)

        if resultado != None:#si el valor ya existe
            resultado.valor.vecinos.insertar_final(destino)
        else:
            resultado = self.vertices.insertar_final(origen)

            resultado.valor.vecinos.insertar_final(destino)



    def obtener_ruta(self, origen:str, destino:str)->Lista:
        ruta:Lista[Vertice] = Lista()
        nodos_visitados:Cola = Cola()
        nodos:Cola = Cola()

        # Aca se busca el vertice al que pertenece el origen y se realiza una copia del mismo
        original:Vertice = copy(self.vertices.buscar(origen))
        if original == None:
            print(f"No existe la ciudad origen: {origen}")
            return
        
        nodos.encolar(original)

    
    def get_ruta_corta(self, destino:str, nodos_visitados:Cola, nodos:Cola)->Vertice:
        



    def imprimir(self)->str:
        dot = 'digraph G {\n\tedge [arrowhead=none fontcolor=black color="#ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white '
        dot += 'color=transparent];\n\t'

        aux: Nodo[Vertice] = self.vertices.cabeza

        while aux != None:
            if aux != None:
                dot += str(aux.valor)
            aux = aux.sig

        dot += "}"

        return dot