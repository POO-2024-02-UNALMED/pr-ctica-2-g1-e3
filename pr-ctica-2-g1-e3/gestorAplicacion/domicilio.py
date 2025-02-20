class Domicilio:
    _domicilios = []

    def __init__(self, cliente = None, pedido_domicilio= None, direccion= None, domicilio_prioritario = False, costo_envio= None, domiciliario= None):
        self._cliente = cliente
        self._pedido_domicilio = pedido_domicilio
        self._direccion = direccion
        self._domicilio_prioritario = domicilio_prioritario
        self._costo_envio = costo_envio
        self._domiciliario = domiciliario
        self._calificacion = None
        self._prom_calificacion = 0.0
        Domicilio._domicilios.append(self)

    def promediar_calificacion(self, calificacion):
        self._prom_calificacion = calificacion._calcular_prom_calificacion()

    @staticmethod
    def indicar_domicilio(id_cliente):
        for domicilio in Domicilio._domicilios:
            if domicilio._cliente.get_identificacion() == id_cliente:
                return domicilio
        return None

    @staticmethod
    def indicar_cliente(id_cliente):
        for domicilio in Domicilio._domicilios:
            if domicilio._cliente.get_identificacion() == id_cliente:
                return domicilio._cliente
        return None

    # Getters y Setters
    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente):
        self._cliente = cliente

    def get_pedido_domicilio(self):
        return self._pedido_domicilio

    def set_pedido_domicilio(self, pedido_domicilio):
        self._pedido_domicilio = pedido_domicilio

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def is_domicilio_prioritario(self):
        return self._domicilio_prioritario

    def set_domicilio_prioritario(self, domicilio_prioritario):
        self._domicilio_prioritario = domicilio_prioritario

    def get_costo(self):
        return self._costo_envio

    def set_costo(self, costo_envio):
        self._costo_envio = costo_envio

    @staticmethod
    def get_domicilios():
        return Domicilio._domicilios

    def get_calificacion(self):
        return self._calificacion

    def set_calificacion(self, calificacion):
        self._calificacion = calificacion

    def get_prom_calificacion(self):
        return self._prom_calificacion

    def set_prom_calificacion(self, prom_calificacion):
        self._prom_calificacion = prom_calificacion

    def get_domiciliario(self):
        return self._domiciliario

    def set_domiciliario(self, domiciliario):
        self._domiciliario = domiciliario
