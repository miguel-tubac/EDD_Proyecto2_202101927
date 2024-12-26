class Cliente:

    def __init__(self, dpi:str, nombres:str, apellidos:str, genero:str, telefono:int, direccion:str):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.genero = genero
        self.telefono = telefono
        self.direccion = direccion


    # Getters
    def get_dpi(self):
        return self.dpi

    def get_nombres(self):
        return self.nombres

    def get_apellidos(self):
        return self.apellidos

    def get_genero(self):
        return self.genero

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    # Setters
    def set_dpi(self, dpi: str):
        self.dpi = dpi

    def set_nombres(self, nombres: str):
        self.nombres = nombres

    def set_apellidos(self, apellidos: str):
        self.apellidos = apellidos

    def set_genero(self, genero: str):
        self.genero = genero

    def set_telefono(self, telefono: int):
        self.telefono = telefono

    def set_direccion(self, direccion: str):
        self.direccion = direccion

    