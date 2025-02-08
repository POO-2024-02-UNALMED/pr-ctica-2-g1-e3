from .factura import Factura
from datetime import datetime

class Reserva:
    _reservas = []
    _contador = 0
    _PRECIO = 30000

    def __init__(self, mesa, fecha_hora=None, numero_personas=None, fecha_de_generacion=None, cliente=None, mesero=None):
        self._mesa = mesa
        self._fecha_hora = fecha_hora
        self._numero_personas = numero_personas
        self._fecha_de_generacion = fecha_de_generacion
        self._cliente = cliente
        self._mesero = mesero
        self._precio_total = self._PRECIO
        self._recargo_por_fecha = False
        self._factura = Factura()
        Reserva._contador += 1
        self._id = Reserva._contador
        if fecha_hora and fecha_de_generacion:
            self.calcular_recargo()
        Reserva._reservas.append(self)

    def calcular_recargo(self):
        años_diferencia = self._fecha_hora.year - self._fecha_de_generacion.year
        meses_diferencia = (años_diferencia * 12) + (self._fecha_hora.month - self._fecha_de_generacion.month)

        if meses_diferencia > 1:
            self._precio_total += 50000
            self._recargo_por_fecha = True

    def eliminar_reserva(self):
        if Reserva._reservas:
            Reserva._reservas.pop()

    def sumar_precio(self, precio):
        self._precio_total += precio

    # Getters y Setters
    def get_mesa(self):
        return self._mesa

    def set_mesa(self, mesa):
        self._mesa = mesa

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_fecha_hora(self):
        return self._fecha_hora

    def get_mesero(self):
        return self._mesero

    def set_mesero(self, mesero):
        self._mesero = mesero

    def get_factura(self):
        return self._factura

    def get_precio_total(self):
        return self._precio_total

    @staticmethod
    def get_reservas():
        return Reserva._reservas

    def get_id(self):
        return self._id

    def get_recargo_por_fecha(self):
        return self._recargo_por_fecha

    def set_recargo_por_fecha(self, recargo_por_fecha):
        self._recargo_por_fecha = recargo_por_fecha