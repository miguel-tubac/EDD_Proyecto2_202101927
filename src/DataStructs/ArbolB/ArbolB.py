from src.DataStructs.ArbolB.NodoArbolB import NodoArbolB

class ArbolB:
    def __init__(self, orden:int):
        self.root: NodoArbolB = NodoArbolB(True)
        self.orden:int = orden


    
    def insertar_clave(self, valor:int):
        root: NodoArbolB = self.root

        if len(root.claves) == self.orden -1:
            # aca va la separacion de la hoja
            nodo:NodoArbolB = NodoArbolB()#al no pasarle los parametros se indica que no es una hoja
            self.root = nodo
            nodo.hijos.insert(0, root)
            self.dividir_hijo(nodo, 0)
            self.insertar_valor_no_completo(nodo, valor)
        else:
            # aca se inserta el valor
            self.insertar_valor_no_completo(root, valor)
            

    def insertar_valor_no_completo(self, raiz:NodoArbolB, valor:int):
        contador: int = len(raiz.claves) - 1

        if(raiz.hoja):
            raiz.claves.append(None)

            while contador >= 0 and valor < raiz.claves[contador]:
                raiz.claves[contador + 1] = raiz.claves[contador] # aca desplazo el valor hacia la derecha porque es menor
                contador -= 1
            raiz.claves[contador + 1] = valor
        else:
            while contador >= 0 and valor < raiz.claves[contador]:
                contador -= 1

            contador +=1
            if len(raiz.hijos[contador].claves) == self.orden -1:
                #separar nodos
                self.dividir_hijo(raiz, contador)
                if valor > raiz.claves[contador]:
                    contador += 1

            
            self.insertar_valor_no_completo(raiz.hijos[contador], valor)

        
    def dividir_hijo(self, raiz:NodoArbolB, posicion:int):
        posicion_media: int = int((self.orden -1)/2)
        hijo:NodoArbolB = raiz.hijos[posicion]
        nodo:NodoArbolB = NodoArbolB(hijo.hoja)

        raiz.hijos.insert(posicion + 1, nodo)

        raiz.claves.insert(posicion, hijo.claves[posicion_media])
        nodo.claves = hijo.claves[posicion_media +1: posicion_media*2 +1]
        hijo.claves = hijo.claves[0:posicion_media]

        if not hijo.hoja:
            nodo.hijos = hijo.hijos[posicion_media + 1:posicion_media * 2 +1]
            hijo.hijos = hijo.hijos[0:posicion_media]


    # funcion para mostrar los la informacion de un objeto
    def imprimir_usuario(self) -> str:
        dot:str = "diagrap G { \n"
        return self.imprimir(self.root)
        dot += "\n}"

        return dot

    def imprimir(self, nodo:NodoArbolB, id:int = 0) -> str:
        raiz:NodoArbolB = nodo

        arbol:str = f"n{id}[label=\""
        contador:int = 0
        for item in raiz.claves:
            if contador == len(raiz.claves) - 1:
                arbol += f"<f{contador}>{item}"
                break
            arbol += f"<f{contador}>{item}|"
            contador += 1

        arbol += "\"];\n\t"
        contador:int = 0
        id_padre = id
        for item in raiz.hijos:
            arbol += f'n{id_padre}:f{contador} -> n{id +1};'
            id += 1
            arbol += self.imprimir(item, id)

            contador += 1


        return arbol




    # este es metodo que imprime si paso un objeto para imprmirlo
    def __str__(self):
        return f"{self.root}"