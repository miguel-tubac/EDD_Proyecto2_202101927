from NodoArbolB import NodoArbolB

class ArbolB:
    def __init__(self, orden:int):
        self.root: NodoArbolB = NodoArbolB(True)
        self.orden:int = orden


    
    def insertar_clave(self, valor:int):
        root: NodoArbolB = self.root

        if len(root.claves) == self.orden -1:
            # aca va la separacion de la hoja
            pass
        else:
            # aca se inserta el valor
            self.insertar_valor(root, valor)
            

    def insertar_valor(self, raiz:NodoArbolB, valor:int):
        contador: int = len(raiz.claves) - 1

        if(raiz.hoja):
            raiz.claves.append(None)

            while contador >= 0 and valor < raiz.claves[contador]:
                raiz.claves[contador + 1] = raiz.claves[contador] # aca desplazo el valor hacia la derecha porque es menor
                contador -= 1
            raiz.claves[contador + 1] = valor
        else:
            while contador >= 0 and valor < raiz.claves[contador]
                contador -= 1
            if len(raiz.hijos[contador].claves) == self.orden -1:
                #separar nodos
                pass

            
            self.insertar_valor(raiz.hijos[contador], valor)
            
