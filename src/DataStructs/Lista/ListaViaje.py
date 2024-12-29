from src.DataStructs.Lista.NodoViaje import NodoViaje
from src.classes.Viaje import Viaje


class ListaViaje:

    def __init__(self):
        self.inicio: NodoViaje = None

    def esta_vacia(self) -> bool:
        return self.inicio is None


    def agregar(self, valor:Viaje):
        """Agrega un nuevo elemento al final de la lista."""
        nuevo_nodo = NodoViaje(valor)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.sig is not None:
                actual = actual.sig
            actual.sig = nuevo_nodo


    def buscar(self, id:str) -> Viaje:
        """Busca un valor en la lista. Retorna el objeto Viaje"""
        if self.esta_vacia:
            print("La lista esta vacia")
            return None
        
        actual = self.inicio
        while actual is not None:
            if actual.valor.id == id:
                print(f"este es el id: {actual.valor.id}")
                return actual.valor
            actual = actual.sig
        return None

