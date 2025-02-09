import pickle 
import os
from gestorAplicacion.reserva import Reserva
from gestorAplicacion.almacen import Almacen
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

class Deserializador():
    @staticmethod
    def deserializar(lista, nombre):
        try:
            ruta_archivo = os.path.join(os.getcwd(), "baseDatos", "temp", f"{nombre}.txt")

            # Verifica si el archivo existe
            if not os.path.exists(ruta_archivo):
                print(f"Error: El archivo {ruta_archivo} no existe.")
                return

            with open(ruta_archivo, 'rb') as file:
                lista.extend(pickle.load(file))

        except FileNotFoundError as e:
            print(f"Archivo no encontrado: {e}")
        except IOError as e:
            print(f"Error de IO: {e}")
        except pickle.UnpicklingError as e:
            print(f"Error deserializando objeto: {e}")

    @staticmethod
    def deserializarListas():
        Deserializador.deserializar(Almacen.get_almacen(), "almacenes")
        Deserializador.deserializar(Calificacion.get_calificaciones(), "calificaciones")
        Deserializador.deserializar(Cliente.get_clientes(), "clientes")
        Deserializador.deserializar(Domiciliario.get_lista_domiciliarios(), "domiciliarios")
        Deserializador.deserializar(Domicilio.get_domicilios(), "domicilios")
        Deserializador.deserializar(Factura.get_facturas(), "facturas")
        Deserializador.deserializar(Mesa.get_mesas(), "mesas")
        Deserializador.deserializar(Mesero.get_meseros(), "meseros")
        Deserializador.deserializar(Persona.get_personas(), "personas")
        Deserializador.deserializar(Pedido.get_pedidos(), "pedidos")
        Deserializador.deserializar(PedidoItem.get_pedido_items(), "pedidoItems")
        Deserializador.deserializar(Reserva.get_reservas(), "reservas")
        Deserializador.deserializar(Restaurante.get_restaurantes(), "restaurante")