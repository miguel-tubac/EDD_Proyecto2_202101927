class Vehiculo:
    def __init__(self, placa:str, marca:str, modelo:int, precio:float):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad_viajes = 0

    def incrementar_cantidad_viajes(self):
        self.cantidad_viajes += 1

    # Getters
    def get_placa(self) -> str:
        return self.placa

    def get_marca(self) -> str:
        return self.marca

    def get_modelo(self) -> int:
        return self.modelo

    def get_precio(self) -> float:
        return self.precio
    
    def get_cantidad_viajes(self)->int:
        return self.cantidad_viajes

    # Setters
    def set_placa(self, placa: str) -> None:
        self.placa = placa

    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def set_modelo(self, modelo: int) -> None:
        self.modelo = modelo

    def set_precio(self, precio: float) -> None:
        self.precio = precio