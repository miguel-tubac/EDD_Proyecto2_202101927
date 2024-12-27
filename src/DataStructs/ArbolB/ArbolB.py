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