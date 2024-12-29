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
        original:Vertice = copy(self.vertices.buscar_texto(origen))
        if original == None:
            print(f"No existe la ciudad origen: {origen}")
            return
        
        nodos.encolar(original)
        resultado:Vertice = self.get_ruta_corta(destino, nodos_visitados, nodos)

        while resultado != None:
            ruta.insertar_frente(resultado)
            resultado = resultado.padre
        
        return ruta



    
    def get_ruta_corta(self, destino:str, nodos_visitados:Cola, nodos:Cola)->Vertice:
        origen:Vertice = nodos.desencolar().valor

        if origen.valor == destino:
            nodos_visitados.encolar(origen)
            return origen
        
        aux:Nodo[Vertice] = origen.vecinos.cabeza
        #Se agregan los vecinos a la cola de nodos
        while aux != None:
            if not self.estaVicitado(nodos_visitados, aux.valor):
                peso:int = aux.valor.peso

                vecino:Vertice = copy(self.vertices.buscar_texto(aux.valor.valor))
                vecino.peso = peso
                vecino.set_peso_acumulado(origen.peso_acumulado + peso)
                vecino.padre = origen

                nodos.encolar(vecino)

            aux = aux.sig
        nodos.ordenar()
        nodos_visitados.encolar(origen)
        return self.get_ruta_corta(destino, nodos_visitados, nodos)






    def estaVicitado(self, nodos_visitados:Cola, valor:Vertice)->bool:
        resultado:Nodo = nodos_visitados.buscar_enCola(valor.valor)
        return resultado != None



    def obtener_lista_origenes(self) -> list:
        lista_origenes = []
        aux: Nodo[Vertice] = self.vertices.cabeza

        while aux is not None:
            lista_origenes.append(aux.valor.valor)  # Se obtiene el dato del vertice origen
            aux = aux.sig

        return lista_origenes



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