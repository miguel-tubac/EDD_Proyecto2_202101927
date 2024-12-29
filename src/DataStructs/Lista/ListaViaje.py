from src.DataStructs.Lista.NodoViaje import NodoViaje
from src.classes.Viaje import Viaje


class ListaViaje:

    def __init__(self):
        self.inicio:NodoViaje = None


    def agregar(self, valor:Viaje):
        aux: NodoViaje = self.inicio
        if aux == None:
            aux = NodoViaje(valor)
            self.inicio = aux
            return

        while aux.sig != None:
            aux = aux.sig

        aux.sig = NodoViaje(valor)
        


    def buscar(self, id:int) -> Viaje:
        aux: NodoViaje = self.inicio
        if aux == None:
            print("La lista esta vacia")
            return None

        while aux != None:
            if aux.valor.id == id:#comparamos si existe el valor y si si lo retornamos
                return aux.valor
            aux = aux.sig
        
        return None

