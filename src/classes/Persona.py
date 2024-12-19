class Persona:
    #este es el metodo constructor
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre # esto es para colocar las variables privadas "__"
        self.__edad = edad

    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_edad(self)-> int:
        return self.__edad
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} \nEdad: {self.__edad}"