from src.DataStructs.Lista.Lista import Lista

class Vertice:

    def __init__(self, valor: str, peso:int = 0, padre = None):
        self.valor:str = valor
        self.vecinos:Lista[Vertice] = Lista() #Esta es al linkedist
        self.peso:int = peso
        self.peso_acumulado:int = 0
        self.visitado:bool = False
        self.padre:Vertice = padre

    def get_peso_acumulado(self, peso)->int:
        self.peso_acumulado += peso
        return self.peso_acumulado
    

    def agregar_vecino(self, valor:str, peso:int):
        vecino:Vertice = Vertice(valor, peso)
        vecino.set_peso_acumulado(peso)

        self.vecinos.insertar_final(vecino)

    
    def set_peso_acumulado(self, peso:int):
        self.peso_acumulado += peso


    def __str__(self) -> str:
        aux = self.vecinos.cabeza
        dot: str = ""
        while aux != None:
            dot += f'edge [label={aux.valor.peso} fontsize=5]; \n\t{self.valor} -> {aux.valor.valor}; \n\t'
            aux = aux.sig

        return dot