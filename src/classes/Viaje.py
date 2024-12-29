from src.classes.Cliente import Cliente
from src.classes.Vehiculo import Vehiculo
from src.DataStructs.Lista.Lista import Lista
from src.DataStructs.Grafo.ListaAdyacencia import ListaAdyacencia
from src.DataStructs.Lista.Nodo import Nodo
from src.classes.Vertice import Vertice

class Viaje:
    
    def __init__(self, id:int, origen:str, destino:str, fecha:str, cliente:Cliente, vehiculo:Vehiculo, camino:Lista):
        self.origen:str = origen
        self.destino:str = destino
        self.fecha:str = fecha
        self.cliente:Cliente = cliente
        self.vehiculo:Vehiculo = vehiculo
        self.id:int = id
        self.camino:Lista = camino

    # def get_ruta(self, grafo:ListaAdyacencia):
        # self.camino = grafo.obtener_ruta(self.origen, self.destino)

    '''
    def mostrar_rutas(self)->str:
        ruta:str = ""
        aux:Nodo[Vertice] = self.camino.cabeza

        while aux != None:
            if aux.valor.peso_acumulado == 0:
                ruta += f"{aux.valor.valor}({aux.valor.peso_acumulado}) -> "
            else:
                ruta += f"{aux.valor.valor}({peso} + {aux.valor.peso} = {aux.valor.peso_acumulado}) -> "

            peso:int = aux.valor.peso_acumulado
            aux = aux.sig

        return ruta'''
    

    def mostrar_rutas(self) -> str:
        """
        Genera el código DOT para representar la lista enlazada simple
        correspondiente al camino del viaje.
        """
        dot_code: str = "digraph ListaEnlazada {\n"
        dot_code += "    rankdir=LR;\n"  # Representar de izquierda a derecha
        dot_code += "    node [shape=record];\n"

        aux: Nodo[Vertice] = self.camino.cabeza
        nodo_index = 0  # Para nombrar los nodos de manera única

        # Generar nodos
        while aux is not None:
            if aux.valor.peso_acumulado == 0:
                dot_code += f"    node{nodo_index} [label=\"Lugar: {aux.valor.valor}\\nTiempo: {aux.valor.peso_acumulado}\"];\n"
            else:
                dot_code += f"    node{nodo_index} [label=\"Lugar: {aux.valor.valor}\\nTiempo: {peso} + {aux.valor.peso} = {aux.valor.peso_acumulado}\"];\n"
            nodo_index += 1
            peso:int = aux.valor.peso_acumulado
            aux = aux.sig

        # Generar conexiones
        aux = self.camino.cabeza
        nodo_index = 0
        while aux is not None and aux.sig is not None:
            dot_code += f"    node{nodo_index} -> node{nodo_index + 1};\n"
            nodo_index += 1
            aux = aux.sig

        dot_code += "}\n"
        return dot_code
