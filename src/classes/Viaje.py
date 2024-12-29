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

        return ruta