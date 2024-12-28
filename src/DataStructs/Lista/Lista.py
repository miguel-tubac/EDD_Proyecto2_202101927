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


    def insertar_frente(self, valor) -> Nodo:
        nuevo_nodo: Nodo = Nodo(valor)

        if self.cabeza == None:
            self.cabeza = nuevo_nodo

            return self.cabeza

        nuevo_nodo.sig = self.cabeza
        self.cabeza = nuevo_nodo
        return self.cabeza




    def buscar(self, valor) -> Nodo:
        aux: Nodo = self.cabeza
        if aux == None:
            return None

        while aux != None:
            if aux.valor.valor == valor.valor:#comparamos si existe el valor y si si lo retornamos
                return aux
            aux = aux.sig
        
        return None
    


    def eliminar_alFrente(self)->Nodo:
        cabeza:Nodo = self.cabeza

        if cabeza != None:
            self.cabeza = cabeza.sig
            return cabeza
        
        return None

