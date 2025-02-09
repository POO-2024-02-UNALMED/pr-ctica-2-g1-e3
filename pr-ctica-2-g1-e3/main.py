from gestorAplicacion.almacen import Almacen
from gestorAplicacion.reserva import Reserva
from gestorAplicacion.calificacion import Calificacion
from gestorAplicacion.cliente import Cliente
from gestorAplicacion.domiciliario import Domiciliario
from gestorAplicacion.factura import Factura
from gestorAplicacion.domicilio import Domicilio
from gestorAplicacion.mesa  import Mesa
from gestorAplicacion.mesero import Mesero
from gestorAplicacion.pedidoItem import PedidoItem
from gestorAplicacion.pedido import Pedido
from gestorAplicacion.persona import Persona
from gestorAplicacion.restaurante import Restaurante
from datetime import datetime, time
from baseDatos.serializador import Serializador
from baseDatos.deserializador import Deserializador

class Main:
    if __name__ == "__main__":
        Deserializador.deserializarListas()
        
        

