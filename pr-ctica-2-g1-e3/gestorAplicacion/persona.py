class Persona:
    _personas = []  # Lista estática para almacenar personas

    def __init__(self, nombre: str = None, identificacion: int = None):
        self._nombre = nombre
        self._identificacion = identificacion
        Persona._personas.append(self)

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_identificacion(self):
        return self._identificacion

    def set_identificacion(self, identificacion: int):
        self._identificacion = identificacion

    @staticmethod
    def get_personas():
        return Persona._personas

    def saludar(self):
        print(f"hola {self.get_nombre}! :)")