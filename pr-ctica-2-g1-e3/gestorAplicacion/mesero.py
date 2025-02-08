from .persona import Persona
import datetime

class Mesero(Persona):
    _meseros = []

    def __init__(self, identificacion, nombre, prom_calificaciones, total_calificaciones, restaurante):
        super().__init__(nombre, identificacion)
        self._prom_calificaciones = prom_calificaciones
        self._total_calificaciones = total_calificaciones
        self._calificaciones = []
        self._disponibilidad = []
        Mesero._meseros.append(self)
        restaurante.agregar_mesero(self)

    def actualizar_desempeno_mesero(self, calificacion):
        suma_acumulada = self._prom_calificaciones * self._total_calificaciones
        self._total_calificaciones += 1
        self._prom_calificaciones = round((suma_acumulada + calificacion.get_calidad_mesero()) / self._total_calificaciones, 1)

    @staticmethod
    def organizar_meseros_por_calificacion():
        Mesero._meseros.sort(key=lambda mesero: mesero.get_prom_calificaciones(), reverse=True)

    def agregar_fecha(self, fecha):
        self._disponibilidad.append(fecha)

    def disponibilidad(self, fecha):
        for horario in self._disponibilidad:
            inicio_horario = horario
            fin_horario = inicio_horario + datetime.timedelta(hours=1)

            if inicio_horario <= fecha <= fin_horario:
                return False
        return True

    def __str__(self):
        return f"Nombre: {self._nombre}, Calificación: {self._prom_calificaciones}"

    @staticmethod
    def posicion_prioridad_mesero(mesero):
        for i, m in enumerate(Mesero._meseros):
            if m.get_nombre() == mesero.get_nombre():
                return i + 1
        return -1

    @staticmethod
    def revision_meseros():
        for mesero in Mesero._meseros[:]:
            if len(mesero.get_calificaciones()) > 2:
                if mesero.get_calificaciones()[-1] <= 2 and mesero.get_calificaciones()[-2] <= 2 and mesero.get_calificaciones()[-3] <= 2:
                    Mesero._meseros.remove(mesero)

    def get_identificacion(self):
        return self._identificacion

    def get_nombre(self):
        return self._nombre

    def get_prom_calificaciones(self):
        return self._prom_calificaciones

    def get_calificaciones(self):
        return self._calificaciones

    def get_total_calificaciones(self):
        return self._total_calificaciones

    @staticmethod
    def get_meseros():
        return Mesero._meseros

    @staticmethod
    def set_meseros(meseros):
        Mesero._meseros = meseros
