from src.DataStructs.Lista.NodoViaje import NodoViaje
from src.classes.Viaje import Viaje


class ListaViaje:

    def __init__(self):
        self.inicio:NodoViaje = None


    def agregar(self, valor:Viaje):
        aux: NodoViaje = self.inicio
        if aux == None:
            aux = NodoViaje(valor)
            self.inicio = aux
            return

        while aux.sig != None:
            aux = aux.sig

        aux.sig = NodoViaje(valor)
        


    def buscar(self, id:int) -> Viaje:
        aux: NodoViaje = self.inicio
        if aux == None:
            print("La lista esta vacia")
            return None

        while aux != None:
            if aux.valor.id == id:#comparamos si existe el valor y si si lo retornamos
                return aux.valor
            aux = aux.sig
        
        return None
    



    def obtener_viajesMas_largos(self)->list:
        aux: NodoViaje = self.inicio
        if aux is None:
            print("La lista está vacía")
            return []

        viajes: list[Viaje] = []

        # Recorremos la lista y almacenamos los viajes
        while aux is not None:
            viaje: Viaje = aux.valor
            # Verificar si el camino no está vacío
            if viaje.camino.cabeza is not None:
                viajes.append(viaje)
            aux = aux.sig

        # Ordenar los viajes por el peso acumulado de mayor a menor
        viajes.sort(key=lambda v: v.EnViaje_Obtener_pesoAcumulado(), reverse=True)

        # Retornar los 5 primeros o menos si no hay suficientes viajes
        return viajes[:5]
    

    def obtener_viajesMas_caros(self)->list:
        aux: NodoViaje = self.inicio
        if aux is None:
            print("La lista está vacía")
            return []

        viajes: list[Viaje] = []

        # Recorremos la lista y almacenamos los viajes
        while aux is not None:
            viaje: Viaje = aux.valor
            # Verificar si el camino no está vacío
            if viaje.camino.cabeza is not None:
                viajes.append(viaje)
            aux = aux.sig

        # Ordenar los viajes por el peso acumulado de mayor a menor
        viajes.sort(key=lambda v: v.objener_precio_viaje(), reverse=True)

        # Retornar los 5 primeros o menos si no hay suficientes viajes
        return viajes[:5]
    


    def obtener_clientes_Mas_Viajes(self)->list:
        aux: NodoViaje = self.inicio
        if aux is None:
            print("La lista está vacía")
            return []

        viajes: list[Viaje] = []

        # Recorremos la lista y almacenamos los viajes
        while aux is not None:
            viaje: Viaje = aux.valor
            # Verificar si el camino no está vacío
            if viaje.camino.cabeza is not None:
                viajes.append(viaje)
            aux = aux.sig

        # Ordenar los viajes por el peso acumulado de mayor a menor
        viajes.sort(key=lambda v: v.cliente.get_cantidad_viajes(), reverse=True)

        # Retornar los 5 primeros o menos si no hay suficientes viajes
        return viajes[:5]




    def obtener_vehiculos_Mas_Viajes(self)->list:
        aux: NodoViaje = self.inicio
        if aux is None:
            print("La lista está vacía")
            return []

        viajes: list[Viaje] = []

        # Recorremos la lista y almacenamos los viajes
        while aux is not None:
            viaje: Viaje = aux.valor
            # Verificar si el camino no está vacío
            if viaje.camino.cabeza is not None:
                viajes.append(viaje)
            aux = aux.sig

        # Ordenar los viajes por el peso acumulado de mayor a menor
        viajes.sort(key=lambda v: v.vehiculo.get_cantidad_viajes(), reverse=True)

        # Retornar los 5 primeros o menos si no hay suficientes viajes
        return viajes[:5]




    

    def generar_codigo_dot(self) -> str:
        aux: NodoViaje = self.inicio
        if aux is None:
            print("La lista está vacía")
            return None

        dot: str = "digraph ListaEnlazada {\n"
        dot += "    rankdir=LR;\n"  # Representar de izquierda a derecha
        dot += "    node [shape=record];\n"

        nodo_index = 0  
        conexiones = ""  

        # Generar nodos y conexiones
        while aux is not None:
            # Crear el nodo con la información del viaje
            viaje: Viaje = aux.valor
            dot += f"    node{nodo_index} [label=\"ID: {viaje.id}\\nCliente: {viaje.cliente.get_nombres()} {viaje.cliente.get_apellidos()}\\nVehiculo: {viaje.vehiculo.get_placa()}\"];\n"
            
            # Crear conexión si hay un siguiente nodo
            if aux.sig is not None:
                conexiones += f"    node{nodo_index} -> node{nodo_index + 1};\n"
            
            aux = aux.sig
            nodo_index += 1

        dot += conexiones  # Añadir todas las conexiones
        dot += "}\n"
        return dot

