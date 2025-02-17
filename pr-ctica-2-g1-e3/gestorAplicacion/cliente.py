from .persona import Persona
from .calificacion import Calificacion


class Cliente(Persona):
    _clientes = []
    
    def __init__(self, nombre=None, identificacion=None, restaurante=None, reserva=None):
        super().__init__(nombre, identificacion)
        self._reserva = reserva
        self._restaurante = restaurante
        self._visitas = 0
        self._visitas_para_descuentos = 0
        self._descuento_por_visitas = 0
        restaurante._lista_clientes.append(self)
        Cliente._clientes.append(self)
    


    def set_reserva(self, reserva):
        self._reserva = reserva
    
    def get_reserva(self):
        return self._reserva
    
    def set_visitas(self, visitas):
        self._visitas = visitas
    
    def get_visitas(self):
        return self._visitas
    
    def get_visitas_para_descuentos(self):
        return self._visitas_para_descuentos
    
    def set_visitas_para_descuentos(self, visitas_para_descuentos):
        self._visitas_para_descuentos = visitas_para_descuentos
    
    def get_descuento_por_visitas(self):
        return self._descuento_por_visitas
    
    def set_descuento_por_visitas(self, descuento_por_visitas):
        self._descuento_por_visitas = descuento_por_visitas
    
    def incrementar_visitas(self):
        self._visitas += 1
        self._visitas_para_descuentos += 1
        if self._visitas_para_descuentos == 11:
            self._visitas_para_descuentos = 1
    
    def __str__(self):
        return f"Cliente [reserva={self._reserva}, restaurante={self._restaurante}, visitas={self._visitas}, nombre={self._nombre}, id={self._identificacion}]"
    
    def calificar(self, pedido, calidad_comida, calidad_mesero, tiempo_espera, comentario):
        nueva_calificacion = Calificacion(self, pedido= pedido, calidad_comida= calidad_comida, calidad_mesero= calidad_mesero, tiempo_espera= tiempo_espera, comentario= comentario)
        pedido.set_calificacion(nueva_calificacion)
        pedido.promediar_calificacion(nueva_calificacion)
        self._restaurante.get_calificaciones_restaurante().append(nueva_calificacion.get_promedio_calificacion())
        self._reserva.get_mesero().get_calificaciones().append(calidad_mesero)
        self._reserva.get_mesero().actualizar_desempeno_mesero(nueva_calificacion)
        self._reserva.get_mesa().get_pedido().get_factura().set_calificacion(nueva_calificacion)
        return nueva_calificacion
    
    def calificar_domicilio(self, domicilio, calidad_comida, tiempo_espera, comentario):
        nueva_calificacion = Calificacion(self, domicilio,calidad_comida= calidad_comida, tiempo_espera= tiempo_espera, comentario= comentario)
        domicilio.set_calificacion(nueva_calificacion)
        domicilio.promediar_calificacion(nueva_calificacion)
        self._restaurante.get_calificaciones_restaurante().append(nueva_calificacion.get_promedio_calificacion())
        domicilio.get_domiciliario().get_calificaciones().append(tiempo_espera)
        domicilio.get_domiciliario().actualizar_desempeno_domiciliario(nueva_calificacion)
        return nueva_calificacion
    
    @staticmethod
    def validarCliente(ident):
        for cliente in Cliente.get_clientes():
            if cliente.get_identificacion() == ident:
                return True
        return False
    
    @staticmethod
    def indicarCliente(id):
        for cliente in Cliente.get_clientes():
                if cliente.get_identificacion() == id:
                    return cliente
        return None

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_identificacion(self):
        return self._identificacion
    
    def set_identificacion(self, identificacion):
        self._identificacion = identificacion
    
    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}")
        print(f"Identificación: {self._identificacion}")
    
    def ingresar_datos(self):
        self._nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self._identificacion = int(input("Ingrese su identificación (número): "))
                break
            except ValueError:
                print("Error: La identificación debe ser un número. Intente nuevamente.")
        print("Datos ingresados correctamente.")
    
    @staticmethod
    def get_clientes():
        return Cliente._clientes
    
    def tipo_cliente(self):
        return self._reserva is not None
    
    def get_restaurante(self):
        return self._restaurante
