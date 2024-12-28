from src.DataStructs.Lista.Lista import Lista
from src.DataStructs.Lista.Nodo import Nodo

class Cola(Lista):#Esta es una clase heredada, por lo que cola hereda de lista

    def __init__(self):
        super().__init__()

    def encolar(self, valor):
        Lista.insertar_final(self, valor)
        


    def desencolar(self)->Nodo:
        return Lista.eliminar_alFrente(self)
    


    