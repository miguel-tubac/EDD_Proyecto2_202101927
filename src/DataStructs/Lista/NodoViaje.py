from src.classes.Viaje import Viaje

class NodoViaje:

    def __init__(self, valor:Viaje):
        self.valor:Viaje = valor
        self.sig:NodoViaje = None