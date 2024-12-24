import os
from src.classes.Persona import Persona
from src.DataStructs.ArbolB.ArbolB import ArbolB

def main() -> None:
    nuevaPersona = Persona("Miguel", 25)
    #print(f"Nombre:  {nuevaPersona.get_nombre()}")
    #print(f"Edad: {nuevaPersona.get_edad()}")
    print(nuevaPersona)# Aca no me imprimira la direccion de memoria sino que el metodo __str__ de la clase persona

    nuevoArbol: ArbolB = ArbolB(5)#Este es el valor de orden
    nuevoArbol.insertar_valor(5)
    nuevoArbol.insertar_valor(6)
    nuevoArbol.insertar_valor(4)
    nuevoArbol.insertar_valor(2)
    nuevoArbol.insertar_valor(7)
    nuevoArbol.insertar_valor(9)
    nuevoArbol.insertar_valor(10)
    nuevoArbol.insertar_valor(3)
    nuevoArbol.insertar_valor(1)
    nuevoArbol.insertar_valor(12)
    nuevoArbol.insertar_valor(0)

    nuevoArbol.insertar_valor(-1)
    nuevoArbol.insertar_valor(13)
    nuevoArbol.insertar_valor(20)
    nuevoArbol.insertar_valor(23)

    print(nuevoArbol.imprimir_usuario())

    #os.system("dot -Tpng Reportes/arbol_b.dot -o Reportes/arbol_b.png")

if __name__ == '__main__':
    main()
