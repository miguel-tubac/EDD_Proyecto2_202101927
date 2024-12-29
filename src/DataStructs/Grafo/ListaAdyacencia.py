from src.DataStructs.Lista.Lista import Lista
from src.classes.Vertice import Vertice
from src.DataStructs.Lista.Nodo import Nodo
from src.classes.Ruta import Ruta
from src.DataStructs.Cola.Cola import Cola

class ListaAdyacencia:

    def __init__(self):
        self.vertices:Lista[Vertice] = Lista()
        self.ruta_corta:Lista[Vertice] = Lista() # Aca se almacenara la ruta mas corta

    def insertar(self, ruta:Ruta):
        origen:Vertice = Vertice(ruta.origen)
        destino:Vertice = Vertice(ruta.destino, ruta.tiempo)

        resultado: Nodo[Vertice] = self.vertices.buscar(origen)

        if resultado != None:#si el valor ya existe
            resultado.valor.vecinos.insertar_final(destino)
        else:
            resultado = self.vertices.insertar_final(origen)

            resultado.valor.vecinos.insertar_final(destino)


    
    def obtener_rutaCorta(self, origen:str, destino:str):
        colaRuta:Cola = Cola()
        nodo_origen: Nodo[Vertice] = self.vertices.buscar(Vertice(origen))
        colaRuta.encolar(nodo_origen.valor)
        self.obtener_rutaCorta_Recursiva(Vertice(destino), colaRuta)






    def obtener_rutaCorta_Recursiva(self, destino:Vertice, colaRuta:Cola):
        nodoOrigen:Nodo[Vertice] = colaRuta.desencolar()

        if nodoOrigen == None:
            print("La ciaudad origen no Existe")
            return
        
        nodoOrigen = self.vertices.buscar(nodoOrigen.valor)
        
        #Validar que se ingresen solo los nodos de la ruta correcta
        self.ruta_corta.insertar_final(nodoOrigen)
        nodoOrigen.valor.visitado = True

        # aca es donde ya se encontro el destino
        if nodoOrigen.valor.valor == destino.valor:
            return
        
        cabezaVecinos: Nodo[Vertice] = nodoOrigen.valor.vecinos.cabeza
        while cabezaVecinos != None:
            nodo_veciono:Nodo[Vertice] = self.vertices.buscar(cabezaVecinos.valor)

            if not nodo_veciono.valor.visitado:
                nodo_veciono.valor.get_peso_acumulado(cabezaVecinos.valor.peso)
                colaRuta.encolar(nodo_veciono.valor)

            cabezaVecinos = cabezaVecinos.sig

        self.ordenar_acendente(colaRuta)

        self.obtener_rutaCorta_Recursiva(destino, colaRuta)



    
    def ordenar_acendente(self, cola:Cola):
        inicio: Nodo = cola.cabeza
        aux: Vertice

        while inicio != None:
            inicio_sig = inicio.sig
            while(inicio_sig != None):
                if(inicio.valor.get_peso_acumulado() > inicio_sig.valor.get_peso_acumulado ()):
                    aux = inicio_sig.valor
                    inicio_sig.valor = inicio.valor
                    inicio.valor = aux.valor

                inicio_sig = inicio_sig.sig

            inicio = inicio.sig        





    def obtener_lista_origenes(self) -> list:
        lista_origenes = []
        aux: Nodo[Vertice] = self.vertices.cabeza

        while aux is not None:
            lista_origenes.append(aux.valor.valor)  # Se obtiene el dato del vertice origen
            aux = aux.sig

        return lista_origenes




    def imprimir(self)->str:
        dot = 'digraph G {\n\tedge [arrowhead=none fontcolor=black color="#ff5400"];\n\t'
        dot += 'node [shape=circle fixedsize=shape width=0.5 fontsize=7 style=filled fillcolor="#313638" fontcolor=white '
        dot += 'color=transparent];\n\t'

        aux: Nodo[Vertice] = self.vertices.cabeza

        while aux != None:
            if aux != None:
                dot += str(aux.valor)
            aux = aux.sig

        dot += "}"

        return dot