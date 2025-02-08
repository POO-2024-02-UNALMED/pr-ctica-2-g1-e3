class Factura:
    _facturas = []

    def __init__(self, descuento=0, restaurante=None, cliente=None, total_factura=0.0, propina=0.0):
        self._descuento = descuento
        self._calificacion = None
        self._mesero = None
        self._restaurante = restaurante
        self._cliente = cliente
        self._total_factura = total_factura
        self._propina = propina
        Factura._facturas.append(self)

    def __str__(self):
        return f"""
        =====================================
                FACTURA DE CONSUMO AURA GOURMET         
        Restaurante: {self._restaurante.get_nombre() if self._restaurante else "N/A"}
        Cliente: {self._cliente.get_nombre() if self._cliente else "N/A"}
        Mesero encargado: {self._cliente.get_reserva().get_mesero() if self._cliente and self._cliente.get_reserva() else "N/A"}
        -------------------------------------
        Total: {self._total_factura}
        Descuento aplicado: {self.aplicar_descuento(self._calificacion)}
        Calificación del servicio: {self._calificacion.get_promedio_calificacion() if self._calificacion else "N/A"}/5
        =====================================
        Gracias por visitarnos. ¡Esperamos verlo pronto!
        =====================================
        """

    def get_total_factura(self):
        return self._total_factura

    def set_calificacion(self, calificacion):
        self._calificacion = calificacion

    @staticmethod
    def get_facturas():
        return Factura._facturas

    def sumar_valor(self, precio):
        self._total_factura += precio

    def asociar_calificacion(self, calificacion):
        self._calificacion = calificacion

    def aplicar_descuento(self, calificacion):
        if calificacion:
            promedio = calificacion.get_promedio_calificacion()

            if promedio <= 2:
                self._descuento = 10  # 10% de descuento
                self._total_factura -= (self._total_factura * self._descuento) / 100
                return "10% de descuento"
            elif promedio <= 3:
                self._descuento = 5  # 5% de descuento
                self._total_factura -= (self._total_factura * self._descuento) / 100
                return "5% de descuento"
            else:
                self._descuento = 0  # sin descuento
                self._total_factura -= (self._total_factura * self._descuento) / 100
                return "Sin descuento"
        return "N/A"

    def prioridad_meseros(self, restaurante):
        if restaurante:
            restaurante.get_meseros().sort(key=lambda mesero: mesero.get_prom_calificaciones(), reverse=True)

    def set_cliente(self, cliente):
        self._cliente = cliente
