from src.DataStructs.ListaCircularDoble.Nodo import Nodo
from src.classes.Cliente import Cliente

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
            if actual.Cliente.dpi == dpi:
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
    


    def ordenar_por_dpi(self):
        if self.esta_vacia():
            print("La lista está vacía, no se puede ordenar.")
            return

        actual = self.primero
        cambiado = True

        while cambiado:
            cambiado = False
            actual = self.primero

            while True:
                siguiente = actual.siguiente
                if siguiente == self.primero:  # Hemos dado la vuelta completa
                    break

                if int(actual.Cliente.dpi) > int(siguiente.Cliente.dpi):
                    # Intercambiar los nodos
                    actual.Cliente, siguiente.Cliente = siguiente.Cliente, actual.Cliente
                    cambiado = True

                actual = siguiente

        print("La lista ha sido ordenada por DPI en orden ascendente.")




    def mostrar(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        actual = self.primero
        while True:
            cliente = actual.Cliente
            print(f"DPI: {cliente.dpi}, Nombres: {cliente.nombres}, Apellidos: {cliente.apellidos}, Género: {cliente.genero}, Teléfono: {cliente.telefono}, Dirección: {cliente.direccion}")
            actual = actual.siguiente
            if actual == self.primero:
                break

    
    def mostrar_nombres(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        nombres = []
        actual = self.primero
        while True:
            cliente = actual.Cliente
            nombres.append(f"{cliente.nombres} {cliente.apellidos}")
            #print(f"DPI: {cliente.dpi}, Nombres: {cliente.nombres}, Apellidos: {cliente.apellidos}, Género: {cliente.genero}, Teléfono: {cliente.telefono}, Dirección: {cliente.direccion}")
            actual = actual.siguiente
            if actual == self.primero:
                break

        return nombres



    def buscar(self, dpi:str) -> Cliente:
        if self.esta_vacia():
            print("La lista está vacía.")
            return None

        actual = self.primero
        while True:
            cliente = actual.Cliente
            if cliente.dpi == dpi:
                return cliente
            actual = actual.siguiente
            if actual == self.primero:
                break
        
        print(f"El cliente con el numero de DPI: {dpi} no se encontro en el sistema.")
        return None


    def generar_imagen(self) -> str:
        if self.esta_vacia():
            print("La lista está vacía, no se puede generar la imagen.")
            return ""

        dot:str = "digraph G {\n"

        actual = self.primero
        while True:
            cliente = actual.Cliente
            nodo_id = f"{cliente.dpi}"
            dot += f"    {nodo_id} [label=\"DPI: {cliente.dpi}\\n{cliente.nombres} {cliente.apellidos} \\nGenero: {cliente.genero}\\nTelefono: {cliente.telefono}\\nDireccion: {cliente.direccion}\"];\n"

            if actual.siguiente:
                siguiente_id = f"{actual.siguiente.Cliente.dpi}"
                dot += f"    {nodo_id} -> {siguiente_id};\n"

            if actual.anterior:
                anterior_id = f"{actual.anterior.Cliente.dpi}"
                dot += f"    {nodo_id} -> {anterior_id} [constraint=false];\n"

            actual = actual.siguiente
            if actual == self.primero:
                break

        dot += "}"
        return dot
