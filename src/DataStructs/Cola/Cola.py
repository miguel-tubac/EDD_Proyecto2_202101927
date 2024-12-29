from src.DataStructs.Lista.Nodo import Nodo
from src.classes.Vertice import Vertice

class Cola():#Esta es una clase heredada, por lo que cola hereda de lista

    def __init__(self):
        self.cabeza = None

    def encolar(self, valor):
        nuevo_nodo:Nodo = Nodo(valor)

        if self.esta_vacio():
            self.cabeza = nuevo_nodo
            return
        
        aux:Nodo = self.cabeza
        while aux.sig != None:
            aux = aux.sig

        aux.sig = nuevo_nodo


    def desencolar(self)->Nodo:
        if self.esta_vacio():
            print("La cola esta vacia, no se puede desencolar")
            return
        
        aux:Nodo = self.cabeza
        self.cabeza = aux.sig
        return aux
    

    def ordenar(self):
        '''Esto es lo que hace que la cola se comporte como una cola de prioridad:
            Esto debido a que los valores mas pequeños pasen al frente y los mas grandes atras
        '''
        if self.esta_vacio:
            print("La cola esta vacia, para poder ordenar")
            return
        
        actual:Nodo[Vertice] = self.cabeza
        while actual != None:
            siguiete:Nodo[Vertice] = actual.sig

            while siguiete != None:
                if actual.valor.peso_acumulado > siguiete.valor.peso_acumulado:
                    aux:Vertice = siguiete.valor
                    siguiete.valor = actual.valor
                    actual.valor = aux
                
                siguiete = siguiete.sig
            
            actual = actual.sig

    def buscar_enCola(self, valor)->Nodo:
        aux:Nodo[Vertice] = self.cabeza
        
        while aux != None:
            if aux.valor.valor == valor:
                return aux
            aux = aux.sig

        return None




    def esta_vacio(self)->bool:
        return self.cabeza == None
    