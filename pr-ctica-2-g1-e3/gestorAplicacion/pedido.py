from typing import List, Tuple

class Pedido:
    _pedidos = []  # Lista estática para almacenar todos los pedidos

    def __init__(self, cliente, factura=None, restaurante=None):
        self._titular = cliente
        self._factura = factura if factura else cliente.get_reserva().get_factura()
        self._restaurante = restaurante
        self._pedido_lista_tuplas: List[Tuple[str, int]] = []
        self._calificacion = None
        self._prom_calificacion = 0.0
        self._plato_cortesia = "No aplica"
        self._descuento = 0
        self._valor_sin_descuento = 0
        self._valor_con_descuento = 0

        Pedido._pedidos.append(self)

        if factura is None:  # Si no se pasó una factura, se obtiene de la reserva del cliente
            cliente.get_reserva().get_mesa().set_pedido(self)

    def agregar_al_pedido(self, nombre_plato: str, cantidad: int):
        self._pedido_lista_tuplas.append((nombre_plato, cantidad))

    def calcular_valor_del_pedido(self, lista_de_tuplas: List[Tuple[str, int]], menu):
        subtotal = 0
        for plato, cantidad in lista_de_tuplas:
            for item in menu:
                if item.name.lower() == plato.lower():
                    subtotal += item.get_precio() * cantidad
                    break
        self._valor_sin_descuento = subtotal

    def realizar_descuentos(self, total: int, descuento: int):
        if descuento != 0:
            descuento_aplicado = (total * descuento) // 100
            nuevo_valor_pedido = total - descuento_aplicado
            self._descuento = descuento_aplicado
            self._valor_con_descuento = nuevo_valor_pedido
        else:
            self._descuento = 0
            self._valor_con_descuento = total
        self._factura.sumar_valor(self._valor_con_descuento)

    def tiempo_espera_restaurante(self, calificacion):
        tiempo_espera = calificacion.get_tiempo_espera()
        if tiempo_espera < 3:
            self._restaurante.set_reputacion(self._restaurante.get_reputacion() - 0.1)

    @staticmethod
    def get_pedidos():
        return Pedido._pedidos

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def get_calificacion(self):
        return self._calificacion

    def set_calificacion(self, calificacion):
        self._calificacion = calificacion

    def get_prom_calificacion(self):
        return self._prom_calificacion

    def get_factura(self):
        return self._factura

    def set_factura(self, factura):
        self._factura = factura

    def promediar_calificacion(self, calificacion):
        self._prom_calificacion = calificacion._calcular_prom_calificacion()

    def get_pedido_lista_tuplas(self):
        return self._pedido_lista_tuplas

    def set_pedido_lista_tuplas(self, pedido_lista_tuplas):
        self._pedido_lista_tuplas = pedido_lista_tuplas

    def get_plato_cortesia(self):
        return self._plato_cortesia

    def set_plato_cortesia(self, plato_cortesia):
        self._plato_cortesia = plato_cortesia

    def get_descuento(self):
        return self._descuento

    def set_descuento(self, descuento):
        self._descuento = descuento

    def get_valor_sin_descuento(self):
        return self._valor_sin_descuento

    def set_valor_sin_descuento(self, valor_sin_descuento):
        self._valor_sin_descuento = valor_sin_descuento

    def get_valor_con_descuento(self):
        return self._valor_con_descuento

    def set_valor_con_descuento(self, valor_con_descuento):
        self._valor_con_descuento = valor_con_descuento

    def get_restaurante(self):
        return self._restaurante

    def set_restaurante(self, restaurante):
        self._restaurante = restaurante
