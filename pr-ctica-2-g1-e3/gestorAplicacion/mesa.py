from .mesero import Mesero
from datetime import datetime, timedelta

class Mesa:
    _mesas = []
    
    def __init__(self, numero, capacidad, tipo, restaurante):
        self._numero = numero
        self._capacidad = capacidad
        self._tipo = tipo
        self._mesero = None
        self._decoracion = "normal" if tipo == "basic" else None
        self._pedido = None
        self._reservas = []
        
        Mesa._mesas.append(self)
        restaurante.agregar_mesa(self)

    def esta_disponible(self, horario: datetime) -> bool:
        for reserva in self._reservas:
            inicio_reserva = reserva.get_fecha_hora()
            fin_reserva = inicio_reserva + timedelta(hours=1)
            if inicio_reserva <= horario <= fin_reserva:
                return False
        return True

    def reservar(self, reserva):
        Mesero.organizar_meseros_por_calificacion()
        for mesero in Mesero.get_meseros():
            if mesero.disponibilidad(reserva.get_fecha_hora()):
                self._mesero = mesero
                reserva.set_mesero(mesero)
                self._reservas.append(reserva)
                mesero.agregar_fecha(reserva.get_fecha_hora())
                return True
        return False

    def tipo_mesa(self) -> bool:
        return self._tipo == "deluxe"

    def eliminar_reserva(self):
        if self._reservas:
            self._reservas.pop()

    def get_numero(self):
        return self._numero

    def get_capacidad(self):
        return self._capacidad

    def get_tipo(self):
        return self._tipo

    def set_mesero(self, mesero):
        self._mesero = mesero

    def get_mesero(self):
        return self._mesero

    def get_pedido(self):
        return self._pedido

    def set_pedido(self, pedido):
        self._pedido = pedido

    def set_decoracion(self, decoracion):
        self._decoracion = decoracion

    def get_decoracion(self):
        return self._decoracion

    @classmethod
    def get_mesas(cls):
        return cls._mesas