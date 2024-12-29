from src.classes.Cliente import Cliente
from src.classes.Vehiculo import Vehiculo

class Viaje:
    
    def __init__(self, origen:str, destino:str, fecha:str, cliente:Cliente, vehiculo:Vehiculo):
        self.origen:str = origen
        self.destino:str = destino
        self.fecha:str = fecha
        self.cliente:Cliente = cliente
        self.vehiculo:Vehiculo = vehiculo
        self.id = 1
        #self.camino:ListaRutaCorta = camino


    def incrementar_id(self):
        self.id += 1