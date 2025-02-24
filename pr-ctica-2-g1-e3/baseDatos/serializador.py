import pickle 
import os
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


class Serializador:
    @staticmethod
    def serializar(lista, nombre):
        try:
            # Crear la carpeta si no existe
            ruta_carpeta = os.path.join(os.getcwd(), "baseDatos", "temp")
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)  # Crea la carpeta

            # Ruta completa del archivo
            ruta_archivo = os.path.join(ruta_carpeta, f"{nombre}.txt")

            # Guardar la lista en el archivo
            with open(ruta_archivo, 'wb') as file:
                pickle.dump(lista, file)
        except FileNotFoundError as e:
            print(f"El archivo no se encontró: {e}")
        except IOError as e:
            print(f"Error al serializar el objeto: {e}")


    @staticmethod
    def serializarListas():
        Serializador.serializar(Almacen.get_almacen(), "almacenes")
        Serializador.serializar(Calificacion.get_calificaciones(), "calificaciones")
        Serializador.serializar(Cliente.get_clientes(), "clientes")
        Serializador.serializar(Domiciliario.get_lista_domiciliarios(), "domiciliarios")
        Serializador.serializar(Domicilio.get_domicilios(), "domicilios")
        Serializador.serializar(Factura.get_facturas(), "facturas")
        Serializador.serializar(Mesa.get_mesas(), "mesas")
        Serializador.serializar(Mesero.get_meseros(), "meseros")
        Serializador.serializar(Persona.get_personas(), "personas")
        Serializador.serializar(Pedido.get_pedidos(), "pedidos")
        Serializador.serializar(PedidoItem.get_pedido_items(), "pedidoItems")
        Serializador.serializar(Reserva.get_reservas(), "reservas")
        Serializador.serializar(Restaurante.get_restaurantes(), "restaurante")
        Serializador.serializar(Restaurante.get_id_con_reservas(), "idConReservas")
        
    
