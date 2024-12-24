from src.DataStructs.Lista.Nodo import Nodo
#from src.classes.Vertice import Vertice

class Lista:

    def __init__(self):
        self.cabeza: Nodo = None


    def insertar_final(self, valor) -> Nodo:
        aux: Nodo = self.cabeza

        if aux == None:
            aux = Nodo(valor)
            self.cabeza = aux
            return self.cabeza

        while aux.sig != None:
            aux = aux.sig

        aux.sig = Nodo(valor)
        return aux.sig



    def buscar(self, valor) -> Nodo:
        aux: Nodo = self.cabeza

        if aux == None:
            return None

        while aux != None:
            if aux.valor.valor == valor.valor:#comparamos si existe el valor y si si lo retornamos
                return aux
            aux = aux.sig
        
        return None

