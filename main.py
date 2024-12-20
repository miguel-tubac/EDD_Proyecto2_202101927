from src.classes.Persona import Persona
from src.DataStructs.ArbolB.ArbolB import ArbolB

def main() -> None:
    nuevaPersona = Persona("Miguel", 25)
    #print(f"Nombre:  {nuevaPersona.get_nombre()}")
    #print(f"Edad: {nuevaPersona.get_edad()}")
    print(nuevaPersona)# Aca no me imprimira la direccion de memoria sino que el metodo __str__ de la clase persona

    nuevoArbol: ArbolB = ArbolB(5)#Este es el valor de orden
    nuevoArbol.insertar_clave(5)
    nuevoArbol.insertar_clave(6)
    nuevoArbol.insertar_clave(4)
    nuevoArbol.insertar_clave(2)
    nuevoArbol.insertar_clave(9)
    nuevoArbol.insertar_clave(7)

    print(nuevoArbol.imprimir_usuario())

if __name__ == '__main__':
    main()
