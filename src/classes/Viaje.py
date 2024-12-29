from src.classes.Cliente import Cliente
from src.classes.Vehiculo import Vehiculo
from src.DataStructs.Lista.Lista import Lista

class Viaje:
    
    def __init__(self, id:int, origen:str, destino:str, fecha:str, cliente:Cliente, vehiculo:Vehiculo, camino:Lista):
        self.origen:str = origen
        self.destino:str = destino
        self.fecha:str = fecha
        self.cliente:Cliente = cliente
        self.vehiculo:Vehiculo = vehiculo
        self.id:int = id
        self.camino:Lista = camino
