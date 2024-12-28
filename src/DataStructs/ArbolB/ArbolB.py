import math
from src.DataStructs.ArbolB.NodoArbolB import NodoArbolB
from src.classes.Vehiculo import Vehiculo

class ArbolB:
    def __init__(self, orden:int):
        self.raiz: NodoArbolB = NodoArbolB(True)
        self.orden:int = orden

    
    def insertar_valor(self, valor:Vehiculo):
        raiz: NodoArbolB = self.raiz

        self.insertar_valor_no_completo(raiz, valor)
        if len(raiz.claves) > self.orden - 1:
            nodo: NodoArbolB = NodoArbolB()
            self.raiz  = nodo
            nodo.hijos.insert(0, raiz)
            self.dividir_pagina(nodo, 0)


    def insertar_valor_no_completo(self, raiz:NodoArbolB, valor:Vehiculo):
        posicion: int = len(raiz.claves) -1 #Esto nos sirve para saber donde se incerta la nueva clave
        if (raiz.hoja):
            raiz.claves.append(None)
            while posicion>= 0 and valor.get_placa()< raiz.claves[posicion].get_placa():
                raiz.claves[posicion+1] = raiz.claves[posicion]
                posicion -= 1

            raiz.claves[posicion +1] = valor
        else:
            while posicion >= 0 and valor.get_placa() < raiz.claves[posicion].get_placa():
                posicion -= 1

            posicion += 1
            self.insertar_valor_no_completo(raiz.hijos[posicion], valor) #esta es la llamada recursiva
            if len(raiz.hijos[posicion].claves) > self.orden - 1:
                self.dividir_pagina(raiz, posicion)


        
    def dividir_pagina(self, raiz:NodoArbolB, posicion:int):
        posicion_media: int = int((self.orden -1)/2)

        hijo: NodoArbolB = raiz.hijos[posicion]
        nodo: NodoArbolB = NodoArbolB(hijo.hoja)

        raiz.hijos.insert(posicion + 1, nodo)

        #primero se dividen las claves de la raiz
        raiz.claves.insert(posicion, hijo.claves[posicion_media])
        nodo.claves = hijo.claves[posicion_media + 1:posicion_media*2 +1]
        hijo.claves = hijo.claves[0:posicion_media]
        
        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1:posicion_media*2 + 2]
            hijo.hijos = hijo.hijos[0:posicion_media +1]



    def buscar(self, placa: str) -> Vehiculo:
        """
        Busca un vehículo en el árbol B basado en la placa.
        :param placa: Placa del vehículo a buscar.
        :return: El objeto Vehículo si se encuentra, de lo contrario None.
        """
        return self._buscar_en_nodo(self.raiz, placa)

    def _buscar_en_nodo(self, nodo: NodoArbolB, placa: str) -> Vehiculo:
        """
        Función recursiva para buscar en un nodo del árbol B.
        :param nodo: Nodo actual donde buscar.
        :param placa: Placa del vehículo a buscar.
        :return: El objeto Vehículo si se encuentra, de lo contrario None.
        """
        # Buscar la posición dentro del nodo actual
        i = 0
        while i < len(nodo.claves) and placa > nodo.claves[i].get_placa():
            i += 1

        # Si la clave actual coincide con la placa, devuelve el vehículo
        if i < len(nodo.claves) and placa == nodo.claves[i].get_placa():
            return nodo.claves[i]

        # Si el nodo es hoja, el vehículo no está en el árbol
        if nodo.hoja:
            return None

        # Si no es hoja, buscar en el hijo correspondiente
        return self._buscar_en_nodo(nodo.hijos[i], placa)




    
    def imprimir_usuario(self) ->str:
        dot: str = 'digraph G {\n\t';
        dot += "fontcolor=white;\n\tnodesep=0.5;\n\tsplines=false\n\t";
        dot += 'node [shape=record width=1.2 style=filled fillcolor="#313638"';
        dot += "fontcolor=white color=transparent]; \n\t";
        dot += 'edge [fontcolor=white color="#0070C9"];\n\t';

        dot += self.imprimir(self.raiz)

        dot += "\n}"

        return dot



    # funcion para mostrar los la informacion de un objeto
    def imprimir(self, nodo: NodoArbolB, id: list[int] = [0]) -> str:
        raiz:NodoArbolB = nodo

        arbol = f'n{id[0]} [label="'
        contador: int = 0;
        for item in raiz.claves:
            if (contador == len(raiz.claves) - 1):
                arbol += f"<f{contador}>|{item.get_placa()}|<f{contador + 1}>"
                break

            arbol += f"<f{contador}>|{item.get_placa()} |"

            contador += 1

        arbol += "\"];\n\t"

        contador: int = 0
        id_padre = id[0]
        for item in raiz.hijos:
            #if contador == len(raiz.hijos) -1:
                    #arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
                #else:
            
            arbol += f'n{id_padre}:f{contador} -> n{id[0] + 1};\n\t'
            id[0] += 1
            arbol += self.imprimir(item, id)

            contador += 1

        return arbol
    



    # este es metodo que imprime si paso un objeto para imprmirlo
    def __str__(self):
        return f"{self.raiz}"
    





    def eliminar(self, placa: str) -> bool:
        """
        Elimina un vehículo del árbol B basado en la placa.
        :param placa: Placa del vehículo a eliminar.
        :return: True si se eliminó, False si no se encontró.
        """
        if not self.raiz.claves:
            return False  # El árbol está vacío
        
        eliminado = self._eliminar_en_nodo(self.raiz, placa)

        # Si la raíz queda vacía y no es hoja, ajustar el árbol
        if not self.raiz.claves and not self.raiz.hoja:
            self.raiz = self.raiz.hijos[0]
        
        return eliminado

    def _eliminar_en_nodo(self, nodo: NodoArbolB, placa: str) -> bool:
        """
        Función recursiva para eliminar en un nodo del árbol B.
        :param nodo: Nodo actual donde realizar la eliminación.
        :param placa: Placa del vehículo a eliminar.
        :return: True si se eliminó, False si no se encontró.
        """
        i = 0
        # Encontrar la posición del valor o el hijo correspondiente
        while i < len(nodo.claves) and placa > nodo.claves[i].get_placa():
            i += 1

        # Caso 1: La clave está en el nodo actual
        if i < len(nodo.claves) and placa == nodo.claves[i].get_placa():
            # Caso 1a: El nodo es hoja
            if nodo.hoja:
                del nodo.claves[i]  # Eliminar la clave
                return True
            # Caso 1b: El nodo no es hoja
            else:
                # Obtener el predecesor o sucesor y reemplazar
                if len(nodo.hijos[i].claves) >= math.ceil(self.orden / 2):
                    predecesor = self._obtener_predecesor(nodo, i)
                    nodo.claves[i] = predecesor
                    return self._eliminar_en_nodo(nodo.hijos[i], predecesor.get_placa())
                elif len(nodo.hijos[i + 1].claves) >= math.ceil(self.orden / 2):
                    sucesor = self._obtener_sucesor(nodo, i)
                    nodo.claves[i] = sucesor
                    return self._eliminar_en_nodo(nodo.hijos[i + 1], sucesor.get_placa())
                else:
                    # Fusionar hijos y eliminar
                    self._fusionar_hijos(nodo, i)
                    return self._eliminar_en_nodo(nodo.hijos[i], placa)

        # Caso 2: La clave no está en el nodo actual
        elif not nodo.hoja:
            # Asegurarse de que el hijo tenga suficientes claves antes de continuar
            if len(nodo.hijos[i].claves) < math.ceil(self.orden / 2):
                self._rellenar_hijo(nodo, i)

            return self._eliminar_en_nodo(nodo.hijos[i], placa)

        # Si no se encuentra en el nodo y es hoja
        return False

    def _obtener_predecesor(self, nodo: NodoArbolB, indice: int) -> Vehiculo:
        """
        Obtiene el predecesor de una clave en el árbol.
        """
        actual = nodo.hijos[indice]
        while not actual.hoja:
            actual = actual.hijos[-1]
        return actual.claves[-1]

    def _obtener_sucesor(self, nodo: NodoArbolB, indice: int) -> Vehiculo:
        """
        Obtiene el sucesor de una clave en el árbol.
        """
        actual = nodo.hijos[indice + 1]
        while not actual.hoja:
            actual = actual.hijos[0]
        return actual.claves[0]

    def _fusionar_hijos(self, nodo: NodoArbolB, indice: int):
        """
        Fusiona dos hijos y la clave del nodo padre en un solo nodo.
        """
        hijo_izq = nodo.hijos[indice]
        hijo_der = nodo.hijos[indice + 1]
        clave_media = nodo.claves[indice]

        # Fusionar clave media y claves de hijo derecho en hijo izquierdo
        hijo_izq.claves.append(clave_media)
        hijo_izq.claves.extend(hijo_der.claves)
        if not hijo_izq.hoja:
            hijo_izq.hijos.extend(hijo_der.hijos)

        # Actualizar el nodo padre
        del nodo.claves[indice]
        del nodo.hijos[indice + 1]

    def _rellenar_hijo(self, nodo: NodoArbolB, indice: int):
        """
        Rellena un hijo si tiene menos claves que el mínimo permitido.
        """
        if indice > 0 and len(nodo.hijos[indice - 1].claves) >= math.ceil(self.orden / 2):
            self._tomar_del_anterior(nodo, indice)
        elif indice < len(nodo.hijos) - 1 and len(nodo.hijos[indice + 1].claves) >= math.ceil(self.orden / 2):
            self._tomar_del_siguiente(nodo, indice)
        else:
            if indice < len(nodo.hijos) - 1:
                self._fusionar_hijos(nodo, indice)
            else:
                self._fusionar_hijos(nodo, indice - 1)

    def _tomar_del_anterior(self, nodo: NodoArbolB, indice: int):
        """
        Toma una clave del hijo anterior para rellenar el hijo actual.
        """
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice - 1]

        # Mover una clave del nodo al hijo
        hijo.claves.insert(0, nodo.claves[indice - 1])
        if not hijo.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())
        nodo.claves[indice - 1] = hermano.claves.pop()

    def _tomar_del_siguiente(self, nodo: NodoArbolB, indice: int):
        """
        Toma una clave del hijo siguiente para rellenar el hijo actual.
        """
        hijo = nodo.hijos[indice]
        hermano = nodo.hijos[indice + 1]

        # Mover una clave del nodo al hijo
        hijo.claves.append(nodo.claves[indice])
        if not hijo.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))
        nodo.claves[indice] = hermano.claves.pop(0)
