from src.classes.Cliente import Cliente

class Nodo:
    def __init__(self, Cliente):
        self.Cliente = Cliente
        self.siguiente = None
        self.anterior = None