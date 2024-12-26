from src.DataStructs.ListaCircularDoble.Nodo import Nodo

class CircularDoble:
    def __init__(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def agregar(self, cliente):
        nuevo_nodo = Nodo(cliente)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            ultimo = self.primero.anterior
            nuevo_nodo.siguiente = self.primero
            nuevo_nodo.anterior = ultimo
            self.primero.anterior = nuevo_nodo
            ultimo.siguiente = nuevo_nodo

    def eliminar(self, dpi):
        if self.esta_vacia():
            return False

        actual = self.primero
        while True:
            if actual.cliente.dpi == dpi:
                if actual.siguiente == actual:  # Solo un elemento en la lista
                    self.primero = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    if actual == self.primero:
                        self.primero = actual.siguiente
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def mostrar(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        actual = self.primero
        while True:
            cliente = actual.cliente
            print(f"DPI: {cliente.dpi}, Nombres: {cliente.nombres}, Apellidos: {cliente.apellidos}, Género: {cliente.genero}, Teléfono: {cliente.telefono}, Dirección: {cliente.direccion}")
            actual = actual.siguiente
            if actual == self.primero:
                break