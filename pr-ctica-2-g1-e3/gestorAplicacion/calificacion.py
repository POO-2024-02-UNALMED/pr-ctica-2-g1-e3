class Calificacion:
    _calificaciones = []

    def __init__(self, cliente, pedido=None, domicilio=None, calidad_comida=0, calidad_mesero=0, tiempo_espera=0, comentario=""):
        self._cliente = cliente
        self._pedido = pedido
        self._domicilio = domicilio
        self._calidad_comida = calidad_comida
        self._calidad_mesero = calidad_mesero
        self._tiempo_espera = tiempo_espera
        self._comentario = comentario
        Calificacion._calificaciones.append(self)
        
        if pedido:
            self._promedio_calificacion = self._calcular_prom_calificacion()
        else:
            self._promedio_calificacion = self._calcular_prom_calificacion_domicilio()
        
        Calificacion._calificaciones.append(self)
    
    def _calcular_prom_calificacion(self):
        return (self._calidad_comida + self._calidad_mesero + self._tiempo_espera) / 3.0

    def _calcular_prom_calificacion_domicilio(self):
        return (self._calidad_comida + self._tiempo_espera) / 2.0

    def get_promedio_calificacion(self):
        return self._promedio_calificacion

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_calidad_mesero(self):
        return self._calidad_mesero

    def set_calidad_mesero(self, calidad_mesero):
        self._calidad_mesero = calidad_mesero

    def get_calidad_comida(self):
        return self._calidad_comida

    def set_calidad_comida(self, calidad_comida):
        self._calidad_comida = calidad_comida

    def get_tiempo_espera(self):
        return self._tiempo_espera

    def set_tiempo_espera(self, tiempo_espera):
        self._tiempo_espera = tiempo_espera

    @staticmethod
    def get_calificaciones():
        return Calificacion._calificaciones
