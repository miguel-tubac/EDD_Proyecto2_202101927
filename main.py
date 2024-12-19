from src.classes.Persona import Persona

def main() -> None:
    nuevaPersona = Persona("Miguel", 25)
    #print(f"Nombre:  {nuevaPersona.get_nombre()}")
    #print(f"Edad: {nuevaPersona.get_edad()}")
    print(nuevaPersona)# Aca no me imprimira la direccion de memoria sino que el metodo __str__ de la clase persona

if __name__ == '__main__':
    main()
