from .cliente import Cliente
from datetime import datetime, time
import re
from .mesa import Mesa

class Restaurante:
    _restaurantes = []
    _id_con_reservas = []
    _lista_clientes = []

    def __init__(self, nombre, horario_servicio=None):
        self._nombre = nombre
        self._reputacion = 3.8
        self._total_calificaciones = 30
        self._ingresos = 0
        self._horario_servicio = horario_servicio
        self._mesas = []
        self._meseros = []
        self._calificaciones_restaurante = []
        Restaurante._restaurantes.append(self)

    def registrar_visita(self, cliente):
        cliente.incrementar_visitas()

    def determinar_descuentos(self, cliente):
        cliente.incrementar_visitas()
        visitas = cliente.get_visitas_para_descuentos()
        if visitas == 5:
            return 10  # 10% de descuento
        elif visitas == 10:
            return 15  # 15% de descuento
        return 0

    def actualizar_reputacion(self, calificacion):
        suma_acumulada = self._reputacion * self._total_calificaciones
        self._total_calificaciones += 1
        self._reputacion = round((suma_acumulada + calificacion.get_promedio_calificacion()) / self._total_calificaciones, 1)

    def hacer_reserva(self, horario, personas, tipo_mesa):
        mesas_disponibles = [
            mesa for mesa in Mesa._mesas
            if mesa.esta_disponible(horario) and mesa.get_tipo() == tipo_mesa and (mesa.get_capacidad() == personas or mesa.get_capacidad() == personas + 1)
        ]
        return mesas_disponibles

    def validar_fecha_hora(self, fecha, hora):
        """Valida que la fecha tenga dos '/' y la hora tenga un ':'. Muestra una advertencia si son incorrectas."""
    
        # Expresión regular para verificar la fecha en formato dd/mm/yyyy
        patron_fecha = r"^\d{1,2}/\d{1,2}/\d{4}$"
    
        # Expresión regular para verificar la hora en formato hh:mm
        patron_hora = r"^\d{1,2}:\d{2}$"

        # Verificar si la fecha tiene dos '/' y cumple con el formato esperado
        fecha_valida = bool(re.match(patron_fecha, fecha))

        # Verificar si la hora tiene un ':' y cumple con el formato esperado
        hora_valida = bool(re.match(patron_hora, hora))

        return fecha_valida and hora_valida

    def convertir_fecha_hora(self, fecha, tiempo):
        dia, mes, año = map(int, fecha.split("/"))
        hora, minutos = map(int, tiempo.split(":"))
        return datetime(año, mes, dia, hora, minutos)

    def agregar_mesa(self, mesa):
        self._mesas.append(mesa)

    def agregar_mesero(self, mesero):
        self._meseros.append(mesero)

    @staticmethod
    def crear_pedido(restaurante):
        CreacionPedido.pedir_id(restaurante)

    def add_id_con_reserva(self, id_reserva):
        Restaurante._id_con_reservas.append(id_reserva)

    def remove_id_con_reserva(self, id_reserva):
        if id_reserva in Restaurante._id_con_reservas:
            Restaurante._id_con_reservas.remove(id_reserva)

    def validar_cliente(self,id, restaurante):
        for cliente in restaurante.get_lista_clientes():
            if cliente.get_identificacion() == id:
                return True
        return False

    @staticmethod
    def buscar_id(id_reserva):
        return any(cliente.get_identificacion() == id_reserva for cliente in Cliente.get_clientes())

    @staticmethod
    def get_id_con_reservas():
        return Restaurante._id_con_reservas

    def get_nombre(self):
        return self._nombre

    def set_mesas(self, mesas):
        self._mesas = mesas

    def set_meseros(self, meseros):
        self._meseros = meseros

    def get_mesas(self):
        return self._mesas

    def get_meseros(self):
        return self._meseros

    def get_reputacion(self):
        return self._reputacion

    def get_calificaciones_restaurante(self):
        return self._calificaciones_restaurante

    @staticmethod
    def get_lista_clientes():
        return Restaurante._lista_clientes

    def set_reputacion(self, reputacion):
        self._reputacion = reputacion

    @staticmethod
    def get_restaurantes():
        return Restaurante._restaurantes

    def agregar_cliente(self, cliente):
        Restaurante._lista_clientes.append(cliente)


    @staticmethod
    def retornar_cliente(id_cliente):
        for cliente in Restaurante._lista_clientes:
            if cliente.get_identificacion() == id_cliente:
                return cliente
        return None

    def obtener_o_crear_cliente(self, nombre, id_cliente):
        cliente_existente = self.indicar_cliente(id_cliente)
        if cliente_existente:
            print(f"Cliente encontrado: {cliente_existente.get_nombre()}")
            return cliente_existente
        else:
            nuevo_cliente = Cliente(nombre, id_cliente, self)
            print(f"Cliente creado: {nuevo_cliente.get_nombre()}")
            return nuevo_cliente

    def indicar_cliente(self, id_cliente):
        for cliente in Restaurante._lista_clientes:
            if cliente.get_identificacion() == id_cliente:
                return cliente
        return None

    def obtener_tipo_mesa(self, reserva):
        return reserva.get_mesa().get_tipo() == "deluxe"
