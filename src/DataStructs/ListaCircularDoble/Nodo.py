from src.classes.Cliente import Cliente

class Nodo:
    def __init__(self, Cliente:Cliente):
        self.Cliente = Cliente
        self.siguiente = None
        self.anterior = None