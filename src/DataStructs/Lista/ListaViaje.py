from src.DataStructs.Lista.NodoViaje import NodoViaje



class ListaViaje:

    def __init__(self):
        self.inicio: NodoViaje = None

    def esta_vacia(self) -> bool:
        return self.inicio is None


    def agregar(self, valor):
        """Agrega un nuevo elemento al final de la lista."""
        nuevo_nodo = NodoViaje(valor)
        if self.esta_vacia():
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.sig is not None:
                actual = actual.sig
            actual.sig = nuevo_nodo

    
    def eliminar(self, valor) -> bool:
        """Elimina un nodo con el valor dado. Retorna True si lo elimina, False si no lo encuentra."""
        if self.esta_vacia():
            return False

        # Si el nodo a eliminar es el primero
        if self.inicio.valor == valor:
            self.inicio = self.inicio.sig
            return True

        # Buscar el nodo a eliminar
        actual = self.inicio
        while actual.sig is not None:
            if actual.sig.valor == valor:
                actual.sig = actual.sig.sig
                return True
            actual = actual.sig
        return False



    def buscar(self, valor) -> bool:
        """Busca un valor en la lista. Retorna True si lo encuentra, False si no."""
        actual = self.inicio
        while actual is not None:
            if actual.valor == valor:
                return True
            actual = actual.sig
        return False


    def mostrar(self):
        """Imprime los valores de la lista."""
        actual = self.inicio
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.sig
        print("None")
