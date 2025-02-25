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
from gestorAplicacion.menu import Menu, MenuCortesias
from field_frame import FieldFrame
from datetime import datetime, time,timedelta
from baseDatos.serializador import Serializador
from baseDatos.deserializador import Deserializador
from uiMain.Utilidad import Utilidad
from excepciones import *


import re
from tkinter import ttk
import tkinter as tk
from field_frame import FieldFrame
from tkinter import messagebox

ultimo_cliente_reserva = None 
# Lista global para almacenar los datos de los clientes
clientes_globales = []
Deserializador.deserializarListas()

#creación de instancias para prueba!!!
restPrueba = Restaurante("Aura Gourmet")
clienteParaPrueba1=Cliente(nombre="mariano herrera", identificacion=2004)
clienteParaPrueba2=Cliente(nombre="maria perez", identificacion=1990)

fechaPrueba1 = "23/04/2025"
horaReservaPrueba1 = "15:00"
fechaReservaPrueba1 = restPrueba.convertir_fecha_hora(fecha=fechaPrueba1, tiempo=horaReservaPrueba1)
#print(fechaReservaPrueba1)


                

fechaPrueba2 = "27/09/2025"
horaReservaPrueba2 = "17:00"
fechaReservaPrueba2 = restPrueba.convertir_fecha_hora(fecha=fechaPrueba2, tiempo=horaReservaPrueba2)
#print(fechaReservaPrueba2)

mesaPrueba1=Mesa(numero='6', capacidad='2', tipo="deluxe", restaurante=restPrueba)
mesaPrueba2=Mesa(numero='4', capacidad='4', tipo="basic", restaurante=restPrueba)

reservaPrueba1=Reserva(mesaPrueba1, fechaReservaPrueba1,mesaPrueba1.get_capacidad(), datetime.today().date())
reservaPrueba2=Reserva(mesaPrueba2, fechaReservaPrueba2,mesaPrueba2.get_capacidad(), datetime.today().date())

#asignación mutua 
clienteParaPrueba1.set_reserva(reservaPrueba1)
clienteParaPrueba2.set_reserva(reservaPrueba2)
reservaPrueba2.set_cliente(clienteParaPrueba2)
reservaPrueba2.set_cliente(clienteParaPrueba2)

# Verificar que el cliente se ha añadido a la lista de clientes del restaurante
print("Clientes lista de clientes del restaurante:", [c.get_nombre() for c in restPrueba._lista_clientes])

# Verificar que el cliente se ha añadido a la lista estática de clientes
#print("Todos los clientes desde clientes:", [c.get_nombre() for c in Cliente._clientes])
#fin de instancias para prueba!!!

#Ubica la ventana en el centro de la pantalla
def centrarVentana(ventana, ancho, alto):
    # Obtiene las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    # Calcula las coordenadas para centrar la ventana
    x = (ancho_pantalla - ancho) // 2
    y = (alto_pantalla - alto) // 2

    # Establece la geometría de la ventana
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#Muestra la ventana de dialogo acerca de
def acercaDe():
    messagebox.showinfo('Acerca de', 'Restaurante que prepara comida para comer <3')

#Muestra la ventana de dialogo que explica de forma básica el sistema
def mensajeAplicacion():
    messagebox.showinfo('Acerca de Aura Gourmet System','Puedes navegar por las distintas funciones que te ofrece nuestro sistema para brindarte la posibilidad de realizar: Reservas, pedidos, domicilios, calificaciones y gestionar recompesas.')
    
def descripcionDelSistema():
    labelP3.config(text="Este es un sistema que te ayudara a gestionar \n" 
                   + "Reservas, pedidos, domicilios, calificaciones y recompesas.")

#Cierra la ventana principal y serializa
def salir():
    Serializador.serializarListas()
    ventana.quit()

#Oculta ventana y muestra ventana2
def ventanaUsuario():
    ventana.withdraw()
    ventana2.deiconify()
    ventana2.state('zoomed')


#devuelve de la ventana2 a la ventana  
def salirMenuInicio():
    ventanaUsuarioDefault()
    labelP3.config(text="Bienvenidos(as) al sistema de gestión \n para usuarios de Aura Gourmet.")
    ventana2.withdraw()
    ventana.deiconify()
    ventana.state('zoomed')

#Cambia el texto del labelP3 para describir el programa
def descripcionSistema():
    labelP3.config(text="Bienvenidos(as) al sistema de gestión\npara usuarios de Aura Gourmet."
                   + "\n\nEste sistema se encarga de proporcionar al cliente\nuna herramienta para realizar:"
                   + "\nReservas, domicilios, gestionar pedidos,\nrecompensas y calificaciones.", justify="left", font=("Segoe UI", 13, "bold"))

#Para Obtener la ruta actual de donde están las imagenes #agregado
current_dir = os.path.dirname(os.path.abspath(__file__)) #agregado
image_dir = os.path.join(current_dir, os.path.join(current_dir, "imagenes")) #agregado

#Ventana inicio
ventana = tk.Tk()
ventana.title("Aura Gourmet System")
centrarVentana(ventana, 650, 650)
ventana.iconbitmap(os.path.join(image_dir, "logoRes.ico")) #modificado
#ventana.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico') #original
ventana.config(bg='#1E1E1E')
ventana.state('zoomed')

# Cargar imágenes
imagenes = [
    # Creación de objetos PhotoImage con las rutas completas
    tk.PhotoImage(file=os.path.join(image_dir, "restaurante1.png")), #modificado
    tk.PhotoImage(file=os.path.join(image_dir, "restaurante2.png")), #modificado
    tk.PhotoImage(file=os.path.join(image_dir, "restaurante3.png")), #modificado
    tk.PhotoImage(file=os.path.join(image_dir, "restaurante4.png")), #modificado
   # tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante1.png"), 
   # tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante2.png"),
   # tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante3.png"),
   #tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante4.png"),
]
indice_imagen = 0  # Índice para alternar entre las imágenes

#Descripciones de los desarrolladores
descripciones = [
    "Nombre: Mateo Pérez\nCédula: 1000761827\nCarrera: Ingeniería de Sistemas e informática\nNacimiento: 18/06/2003",
    "Nombre: Kevin Rubiano\nCédula: 1035417435\nCarrera: Ciencias de la computación\nNacimiento: 19/07/2005",
    "Nombre: Andrés Chica\nCédula: 1041351362\nCarrera: Ingeniería de sistemas e informática\nNacimiento: 24/04/2007",
    "Nombre: María de los ángeles\nCédula: 1104936416\nCarrera: Ciencia de la computación\nNacimiento: 24/11/2004",
    "Nombre: Diana Jacanamejoy\nCédula: 1004232264\nCarrera: Ingenieria Fisica\nNacimiento: 01/01/2000",
]
indice_descripcion = 0  # Índice para alternar entre las descripciones

#PROVISIONAL DE PRUEBA PARA P6
fotos_p6 = [
    [tk.PhotoImage(file=os.path.join(image_dir, "mateo1.png")), tk.PhotoImage(file=os.path.join(image_dir, "mateo2.png")), tk.PhotoImage(file=os.path.join(image_dir, "mateo3.png")), tk.PhotoImage(file=os.path.join(image_dir, "mateo4.png"))],
    [tk.PhotoImage(file=os.path.join(image_dir, "kevin1.png")), tk.PhotoImage(file=os.path.join(image_dir, "kevin2.png")), tk.PhotoImage(file=os.path.join(image_dir, "kevin3.png")), tk.PhotoImage(file=os.path.join(image_dir, "kevin4.png"))],
    [tk.PhotoImage(file=os.path.join(image_dir, "andres1.png")), tk.PhotoImage(file=os.path.join(image_dir, "andres2.png")), tk.PhotoImage(file=os.path.join(image_dir, "andres3.png")), tk.PhotoImage(file=os.path.join(image_dir, "andres4.png"))],
    [tk.PhotoImage(file=os.path.join(image_dir, "maria1.png")), tk.PhotoImage(file=os.path.join(image_dir, "maria2.png")), tk.PhotoImage(file=os.path.join(image_dir, "maria3.png")), tk.PhotoImage(file=os.path.join(image_dir, "maria4.png"))],
    [tk.PhotoImage(file=os.path.join(image_dir, "diana1.png")), tk.PhotoImage(file=os.path.join(image_dir, "diana2.png")), tk.PhotoImage(file=os.path.join(image_dir, "diana3.png")), tk.PhotoImage(file=os.path.join(image_dir, "diana4.png"))], 
]
indice_foto = 0  # Índice para alternar entre colores

def EventoP4(evento):
    global indice_imagen
    nueva_imagen = imagenes[indice_imagen]
    imagen_label.config(image=nueva_imagen)
    indice_imagen = (indice_imagen + 1) % len(imagenes)

# Evento para cambiar la descripción en labelP5 y fotos en p6
def EventoP5(evento):
    global indice_descripcion, indice_foto

    # Cambia la descripción de labelP5
    labelP5.config(text=descripciones[indice_descripcion])
    indice_descripcion = (indice_descripcion + 1) % len(descripciones)

    # Cambia las imágenes de las secciones de labelP6
    imagenes_actuales = fotos_p6[indice_foto]
    for i in range(4):
        secciones_p6[i].config(image=imagenes_actuales[i])
        secciones_p6[i].image = imagenes_actuales[i]

    indice_foto = (indice_foto + 1) % len(fotos_p6)




    

#Creacion de los frames
frameP1 = tk.Frame(ventana,bg="#2D2D2D", relief="solid", bd= 4)
frameP2 = tk.Frame(ventana,bg="#2D2D2D", relief="solid", bd= 4)
frameP3 = tk.Frame(frameP1,bg="white", relief="solid", bd= 4)
frameP4 = tk.Frame(frameP1,bg="#1C2B2D", relief="solid", bd= 4)
frameP5 = tk.Frame(frameP2,bg="#1C2B2D", relief="solid", bd= 4)
frameP6 = tk.Frame(frameP2,bg="#1C2B2D", relief="solid", bd= 4)

#Creacion de los labels
labelP3 = tk.Label(frameP3,bg="#1C2B2D",fg="white",text="Bienvenidos(as) al sistema de gestión\npara usuarios de Aura Gourmet."
                   + "\n\nEste sistema se encarga de proporcionar al cliente\nuna herramienta para realizar:"
                   + "\nReservas, domicilios, gestionar pedidos,\nrecompensas y calificaciones.", justify="left", font=("Segoe UI", 15, "bold"))

# Contenedor principal
labelP4 = tk.Frame(frameP4, bg="#1C2B2D")
labelP4.pack(fill="both", expand=True)

# Sección superior para la imagen
P4Superior = tk.Frame(labelP4, bg="#1C2B2D")
P4Superior.grid(row=0, column=0, sticky="nsew")

# Label para mostrar la imagen
imagen_label = tk.Label(P4Superior, image=imagenes[0], bg="#1C2B2D")
imagen_label.pack(expand=True, fill="both")

# Asignar evento para cambiar imagen cuando el cursor entre
P4Superior.bind("<Enter>", EventoP4)

# Sección inferior con botón
P4Boton = tk.Frame(labelP4, bg="white")
P4Boton.grid(row=1, column=0, sticky="nsew")

boton = tk.Button(P4Boton, text="Ingresar", bg='#2C2F33', fg='white', relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command= ventanaUsuario)
boton.pack(expand=True, fill="both", padx=5, pady=5)

# Configurar distribución de filas y columnas
labelP4.grid_rowconfigure(0, weight=3)
labelP4.grid_rowconfigure(1, weight=1)
labelP4.grid_columnconfigure(0, weight=1)


labelP5 = tk.Label(frameP5,bg="#1C2B2D",fg="white",text="Hojas de vida (Click para cambiar)", justify="left", font=("Segoe UI", 15, "bold"))



# Contenedor de las secciones de p6
labelP6 = tk.Frame(frameP6, bg="#1C2B2D")  # Contenedor de las secciones
secciones_p6 = [
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
]

# Distribuir las 4 secciones en una cuadrícula 2x2
secciones_p6[0].grid(row=0, column=0, sticky="nsew")
secciones_p6[1].grid(row=0, column=1, sticky="nsew")
secciones_p6[2].grid(row=1, column=0, sticky="nsew")
secciones_p6[3].grid(row=1, column=1, sticky="nsew")

# Expande cada celda en la cuadrícula
for i in range(2):
    labelP6.grid_rowconfigure(i, weight=1)
    labelP6.grid_columnconfigure(i, weight=1)


#Menu inicio
menuInicio = tk.Menu(ventana)
subMenuInicio = tk.Menu(menuInicio, tearoff=0, activebackground='#1C2B2D')
subMenuInicio.add_cascade(label = 'Descripcion del sistema', command= descripcionDelSistema)
subMenuInicio.add_separator()
subMenuInicio.add_cascade(label = 'Salir', command=salir)
menuInicio.add_cascade(label='Inicio', menu= subMenuInicio)
ventana.config(menu= menuInicio)

#Ventana Usuario
ventana2 = tk.Tk()
ventana2.title("Aura Gourmet System")
ventana2.iconbitmap(os.path.join(image_dir, "logoRes.ico")) #modificado
#ventana.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico') #original
centrarVentana(ventana2, 650, 650)
ventana2.config(bg='#1E1E1E')
ventana2.withdraw()


#Frames ventana Usuario
#Frame que contiene a los demás
framev1 = tk.Frame(ventana2, bg='#2D2D2D', relief="solid", bd= 4)
framev1.pack(expand=True, fill="both", padx=10, pady=10)
#Frame que contiene "Nombre del proceso o consulta"
framev2 = tk.Frame(framev1, bg='#1C2B2D', relief="solid", bd= 4)
framev2.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.2)
#Frame que contiene "Descripción del proceso o la consulta"
framev3 = tk.Frame(framev1, bg='#1C2B2D', relief="solid", bd= 4)
framev3.place(relx=0.01,rely=0.22,relwidth=0.98,relheight=0.2)
#Frame que contiene al fieldFrame
framev4 = tk.Frame(framev1, bg='#1C2B2D', relief="solid", bd= 4)
framev4.place(relx=0.01,rely=0.43,relwidth=0.98,relheight=0.56)
framev4.grid_propagate(False)
framev4.grid_rowconfigure(0, weight=1)
framev4.grid_columnconfigure(0, weight=1)
#Labels ventana Usuario
labelv1 = tk.Label(framev2, text='Funcionalidades', fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
labelv1.pack(expand=True, fill="both")
labelv2 = tk.Label(framev3, text='Descripciones', fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
labelv2.pack(expand=True, fill="both")
labelv3 = FieldFrame(framev4,tipo = 3, tituloCriterios='Información\n\n\nPara acceder a las funcionalidades dirijase a la pestaña Procesos y consultas.\nPosteriormente seleccione la funcionalidad que desea acceder.')
labelv3.grid(row= 0, column=0 ,columnspan=2, pady=15, sticky='new')


def ventanaUsuarioDefault():
    global labelv3
    labelv3.destroy()

    for widget in framev4.winfo_children():
        widget.destroy()

    labelv1.config(text='Funcionalidades')
    labelv2.config(text='Descripciones')
    labelv3 = FieldFrame(framev4, tipo= 3, tituloCriterios='Información\n\n\nPara acceder a las funcionalidades dirijase a la pestaña Procesos y consultas.\nPosteriormente seleccione la funcionalidad que desea acceder.')
    labelv3.grid(row= 0, column=0 ,columnspan=2, pady=15, sticky='new')
    
#Funcionalidad1

def funcionalidad1(restaurante):
    
    nombre = ""
    identificacion = None
    personas = 0
    tipoMesa = ""
    fecha = None
    horaReserva = None
    fechaReserva = None
    cliente = None

    labelv1.config(text="Realizar Reserva")
    labelv2.config(text="Desde este menú puedes realizar una reserva en nuestro restaurante, ingrese los datos que se le solicitan a continuación")    

    def salirFuncionalidad():
        salir()

    def resumenReserva(framev4,nombre,identificacion,personas,tipoMesa,fechaReserva,reserva,decoracion="Normal",horaAdicional="No",alergias="No"):
        # Crear el resumen como un texto
        for widget in framev4.winfo_children():
            widget.destroy()

        for widget in framev3.winfo_children():
            if isinstance(widget, tk.Label):  # Verifica si el widget es de tipo Label
                widget.config(text="A continuación podrá ver el resumen de su reserva")  # Cambia el texto del Label
            else:
                widget.destroy()
                labelv2 = tk.Label(framev3,text="A continuación podrá ver el resumen de su reserva",fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
                labelv2.pack(expand=True, fill="both")
        

        resumen = (
            f"Nombre: {nombre}\n"
            f"Identificación: {identificacion}\n"
            f"Número de personas: {personas}\n"
            f"Tipo de Mesa: {tipoMesa}\n"
            f"Fecha de Reserva: {fechaReserva}\n"
            f"Número de reserva: {reserva.get_id()}\n"
            f"Decoración: {decoracion}\n"
            f"Hora Adicional: {horaAdicional}\n"
            f"Alergias: {alergias}"
        )
        
        # Crear un label en el framev4 para mostrar el resumen
        frameResumen = FieldFrame(framev4, tituloCriterios=resumen, comandoContinuar=salirFuncionalidad)
        frameResumen.grid(sticky = "new")

    def eleccion_mesa(frame):
        global fechaReserva
        global personas
        global identificacion
        global nombre
        global tipoMesa

        try:
            numeroMesaEscogida = int(frame.obtener_datos()[0])
            print("Numero mesa escogida:")
            print(numeroMesaEscogida)
            mesaEscogida = None

            for i in Mesa._mesas:
                if i.get_numero() == numeroMesaEscogida:
                    mesaEscogida = i
                    print(mesaEscogida.get_numero())
                    break

            fechaActual = datetime.today().date()
            reserva = Reserva(mesaEscogida,fechaReserva,personas,fechaActual)
            meseroAsignado = mesaEscogida.reservar(reserva)
            #asignación de clases
            cliente = restaurante.obtener_o_crear_cliente(nombre,identificacion)
            cliente.set_reserva(reserva)
            reserva.set_cliente(cliente)
            reserva.get_factura().set_cliente(cliente)
            
            if tipoMesa == "deluxe":
                def info_deluxe(frame):
                    try:
                        infoDeluxe = frame.obtener_datos()
                        frame.destroy()
                        #Actualización datos Deluxe
                        if infoDeluxe[1] == "Seleccione una opción" or infoDeluxe[0] == "Seleccione una opción":
                            raise BoxVacio("Decoración o Añadir Tiempo")
                        
                        if infoDeluxe[1] != "Seleccione una opción" and infoDeluxe[0] != "Seleccione una opción":
                            mesaEscogida.set_decoracion(infoDeluxe[0])
                            horaAdicional = infoDeluxe[1]
                            if horaAdicional == "Sí":
                                print(type(fechaReserva))
                                sumarHora = fechaReserva + timedelta(hours=1)
                                print(fechaReserva)
                                print(sumarHora)
                                validacion = mesaEscogida.esta_disponible(sumarHora)
                                if validacion == True:
                                    print("Hora añadida con éxito")
                                    recargoReserva = 30000
                                    reserva.sumar_precio(recargoReserva)
                                if validacion == False:
                                    print("No se pudo agregar la hora adicional")
                            ingredientes = Menu.obtener_todos_los_ingredientes()
                            ingredientesAlergias = []
                            
                            for i in ingredientes:
                                if(not Menu.ingrediente_esta_duplicado(i,ingredientes)):
                                    ingredientesAlergias.append(i)
                            labelv2.destroy()
                            
                            scrollbar = tk.Scrollbar(framev3, orient="vertical")
                            listbox = tk.Listbox(framev3,bg="black",fg="white",font=("Segoe UI", 15, "bold"),justify="center",yscrollcommand=scrollbar.set)
                            scrollbar.config(command=listbox.yview)
                            scrollbar.pack(side="right", fill="y")  
                            listbox.pack(pady=10, fill="y", expand=True)
                            for ingrediente in ingredientesAlergias:
                                listbox.insert(tk.END, ingrediente)
                            listbox.config(state="disabled")
                            def final(frame):
                                alergias = frame.obtener_datos()
                                frame.destroy()
                                listbox.destroy()
                                scrollbar.destroy()
                                if alergias is not None:
                                    labelAlergias = tk.Label(framev3,text="A continuacion podrá ver los platos que no contienen los alimentos restringidos",fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
                                    labelAlergias.pack(expand=True, fill="both")
                                    formatoAlergias = [ingrediente.strip() for ingrediente in alergias[0].split(",")]
                                    for i in formatoAlergias:
                                        print(i)
                                    platosSinAlergias = []
                                    listaPlatos = tk.Listbox(framev4,bg="black",fg="white",font=("Segoe UI", 15, "bold"),justify="center")
                                    for plato in Menu:
                                        if not Menu.plato_contiene_alergia(plato,formatoAlergias):
                                            platosSinAlergias.append(plato)
                                            listaPlatos.insert(tk.END, plato.get_nombre())
                                    botonFinal = tk.Button(framev4,text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=lambda: resumenReserva(framev4,nombre,identificacion,personas,tipoMesa,fechaReserva,reserva,infoDeluxe[0],horaAdicional,alergias))
                                    botonFinal.pack(side="right",anchor="n",padx=20,pady=125)
                                    listaPlatos.config(state="disabled")
                                    listaPlatos.pack(pady=10, fill="y", expand=True)
                                    
                            frameAlergias = FieldFrame(framev4,"Alergias",["Ingrese los nombres de las alergias que posse, si no tiene, deje la casilla vacía"],comandoContinuar=lambda: final(frameAlergias))
                            frameAlergias.grid(sticky = "new")
                    except(ValueError):
                        BoxVacio("Decoración o Añadir Tiempo")
                frame.destroy()
                fieldFrameDeluxe = FieldFrame(framev4,"Personalizacion de la reserva",["Decoración de la mesa","¿Desea agregar 1 hora de permanencia en el restaurante?"],valores=[["Elegante","Rústico","Moderno"],["Sí","No"]],tipo=1,comandoContinuar=lambda: info_deluxe(fieldFrameDeluxe))
                fieldFrameDeluxe.grid(sticky="new")
            else:
                Restaurante._id_con_reservas.append(identificacion) #agregado
                # Serializador.serializarListas() #agregado
                resumenReserva(framev4, nombre, identificacion,personas,tipoMesa,fechaReserva,reserva)
                # print(Restaurante._id_con_reservas) para probar
        except(ValueError):
            BoxVacio("Mesa")
        

    def obtenerDatosCliente(informacion1,fieldFrame2):
        global nombre
        global identificacion 
        global personas
        global tipoMesa
        global fecha
        global horaReserva
        global fechaReserva
        global clientes_globales

        mesasDisponibles = []

        try:
            informacion2 = fieldFrame2.obtener_datos()
            nombre = informacion1[0]
            identificacion = int(informacion1[1])
            personas = int(informacion2[0])
            tipoMesa = informacion2[1]
            fecha = informacion2[2]
            horaReserva = informacion2[3]

            cliente = {
                "nombre": nombre,
                "identificacion": identificacion,
                "personas": personas,
                "tipoMesa": tipoMesa,
                "fecha": fecha,
                "horaReserva": horaReserva
            }
            clientes_globales.append(cliente) #agrgear a la lista de clientes 

            print("Fecha correcta")
            if not restaurante.validar_fecha(fecha):
                raise FechaInvalida(fecha)
            if not restaurante.validar_hora(horaReserva):
                raise HoraInvalida(horaReserva)
            if tipoMesa not in ["basic","deluxe"]:
                raise ExcepcionTipoMesa(tipoMesa)
            if restaurante.validar_fecha(fecha) and restaurante.validar_hora(horaReserva)and tipoMesa in ["basic","deluxe"]:
                fechaReserva = restaurante.convertir_fecha_hora(fecha,horaReserva)
                mesasDisponibles = restaurante.hacer_reserva(fechaReserva,personas,tipoMesa)
                fieldFrame2.destroy()
                fieldFrame2 = FieldFrame(framev4,"Datos de la Reserva",["Personas","Tipo de Mesa(basic o deluxe)","Fecha","Hora"],"Informacion",comandoContinuar=lambda: obtenerDatosCliente(informacion1,fieldFrame2))
                fieldFrame2.grid(sticky="new")

                mesaCorrecta = False
                mesas=[]
                for i in mesasDisponibles:
                    print(i.get_numero())
                    numeroMesa = i.get_numero()
                    mesas.append(numeroMesa)

                fieldFrame2.destroy()
                frameMesas = FieldFrame(framev4,"Mesas disponibles",["Mesa"],"Numero de mesa",valores=[mesas],tipo=1,comandoContinuar=lambda: eleccion_mesa(frameMesas))
                frameMesas.grid(sticky="new")
                print("Vamos bien")
        except (ValueError):
            IdEntryNoNumerico("#Personas")

    def segundo_fieldFrame(fieldFrame1):
        informacion1 = fieldFrame1.obtener_datos()
        try:
            if not informacion1[0]:
                print("Entry vacío")
                raise EntryVacio("Nombre")
            if not informacion1[1]:
                raise EntryVacio("Identificacion")
            identificacion = int(informacion1[1])
            if informacion1[0] and informacion1[1]:
                fieldFrame1.destroy()
                fieldFrame2 = FieldFrame(framev4,"Datos de la Reserva",["Personas","Tipo de Mesa(basic o deluxe)","Fecha","Hora"],"Informacion",comandoContinuar=lambda: obtenerDatosCliente(informacion1,fieldFrame2))
                fieldFrame2.grid(sticky="new")
        except(EntryVacio):
            pass
        except(ValueError):
            IdEntryNoNumerico(informacion1[1])

    labelv3.destroy()
    fieldFrame1 = FieldFrame(framev4,"Datos del Cliente",["Nombre","Numero de identificacion"],"Información",comandoContinuar=lambda:segundo_fieldFrame(fieldFrame1))
    fieldFrame1.grid(sticky="new")
#FinFuncionalidad1


#Funcionalidad4
def funcionalidad4(restaurante):
    # Configuración inicial de los labels
    labelv1.config(text="Gestión de Recompensas")
    labelv2.config(text="Ingrese el número de identificación del cliente para usar sus puntos")

    # Función para mostrar la información del cliente
    def mostrar_informacion_cliente(cliente):
        """Muestra la información del cliente en framev4."""
        # Limpiar framev4 antes de mostrar el resumen
        for widget in framev4.winfo_children():
            widget.destroy()

        # Crear el resumen del cliente
        resumen = (
            f"Nombre: {cliente.get_nombre()}\n"
            f"Identificación: {cliente.get_identificacion()}\n"
        )

        # Verificar si el cliente tiene una reserva
        if cliente.get_reserva():
            reserva = cliente.get_reserva()
            # Asignar un valor arbitrario al costo total de consumo
            costo_total_consumo = 300000  # Valor arbitrario
            resumen += (
                f"Tipo: Reserva\n"
                f"Personas: {reserva._numero_personas}\n"
                f"Tipo de Mesa: {reserva.get_mesa().get_tipo()}\n"
                f"Fecha: {reserva.get_fecha_hora().strftime('%Y-%m-%d %H:%M')}\n"
                f"Costo Total de Consumo: ${costo_total_consumo}\n"
            )
        # Verificar si el cliente tiene un domicilio
        else:
            domicilio_encontrado = None
            for domicilio in Domicilio.get_domicilios():
                if domicilio.get_cliente().get_identificacion() == cliente.get_identificacion():
                    domicilio_encontrado = domicilio
                    break

            if domicilio_encontrado:
                resumen += (
                    f"Tipo: Domicilio\n"
                    f"Domicilio Prioritario: {'Sí' if domicilio_encontrado.is_domicilio_prioritario() else 'No'}\n"
                    f"Dirección: {domicilio_encontrado.get_direccion()}\n"
                    f"Costo de Envío: {domicilio_encontrado.get_costo()}\n"
                    f"Domiciliario: {domicilio_encontrado.get_domiciliario().get_nombre()}\n"
                )
            else:
                resumen += "El cliente no tiene reservas ni domicilios registrados.\n"

        # Crear un label en el framev4 para mostrar el resumen
        label_resumen = tk.Label(framev4, text=resumen, fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
        label_resumen.pack(padx=20, pady=20, fill="both", expand=True)

        # Si el cliente tiene una reserva, mostrar botones para gestionar puntos
        if cliente.get_reserva():
            # Botón para ver los puntos acumulados
            boton_ver_puntos = tk.Button(
                framev4,
                text="Ver Puntos",
                command=lambda: ver_puntos(cliente, costo_total_consumo)
            )
            boton_ver_puntos.pack(pady=10)

            # Botón para usar los puntos
            boton_usar_puntos = tk.Button(
                framev4,
                text="Usar Puntos",
                command=lambda: usar_puntos(cliente)
            )
            boton_usar_puntos.pack(pady=10)

    # Función para calcular y mostrar los puntos acumulados
    def ver_puntos(cliente, costo_total_consumo):
        """Calcula y muestra los puntos acumulados por el cliente."""
        # Calcular puntos (1 punto por cada $1000 de consumo)
        puntos = costo_total_consumo // 1000
        messagebox.showinfo("Puntos Acumulados", f"El cliente {cliente.get_nombre()} tiene {puntos} puntos acumulados.")

    # Función para usar los puntos
    def usar_puntos(cliente):
        """Muestra las opciones para usar los puntos."""
        # Limpiar framev4 antes de mostrar el menú
        for widget in framev4.winfo_children():
            widget.destroy()

        # Crear un nuevo frame para las opciones de uso de puntos
        frame_opciones = tk.Frame(framev4, bg="#1C2B2D")
        frame_opciones.pack(pady=10)

        # Opciones para usar los puntos
        opciones = ["Servicios Exclusivos", "Reserva", "Producto"]
        seleccion = tk.StringVar(frame_opciones)
        seleccion.set(opciones[0])  # Valor por defecto

        # Crear un menú desplegable para seleccionar la opción
        menu_opciones = tk.OptionMenu(frame_opciones, seleccion, *opciones)
        menu_opciones.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        menu_opciones.pack(pady=10)

        # Botón para confirmar la selección
        boton_confirmar = tk.Button(
            frame_opciones,
            text="Confirmar",
            command=lambda: confirmar_uso_puntos(cliente, seleccion.get())
        )
        boton_confirmar.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        boton_confirmar.pack(pady=10)

    # Función para confirmar el uso de los puntos
    def confirmar_uso_puntos(cliente, opcion):
        """Confirma el uso de los puntos según la opción seleccionada."""
        if opcion == "Producto":
            mostrar_menu_productos(cliente)
        elif opcion == "Reserva":
            mostrar_mensaje_reserva(cliente)
        elif opcion == "Servicios Exclusivos":
            mostrar_mesas_deluxe(cliente)
        else:
            messagebox.showinfo("Uso de Puntos", f"El cliente {cliente.get_nombre()} ha decidido usar sus puntos para: {opcion}")

    # Función para mostrar el menú de productos
    def mostrar_menu_productos(cliente):
        """Muestra el menú de productos disponibles."""
        # Limpiar framev4 antes de mostrar el menú
        for widget in framev4.winfo_children():
            widget.destroy()

        # Crear un label para el título del menú
        label_titulo = tk.Label(framev4, text="Menú de Productos", fg="white", bg="#1C2B2D", font=("Segoe UI", 20, "bold"))
        label_titulo.pack(pady=10)

        # Variable para almacenar la selección del producto
        producto_seleccionado = tk.StringVar(framev4)
        producto_seleccionado.set("Seleccione un producto")  # Valor por defecto

        # Crear un menú desplegable para seleccionar el producto
        menu_productos = tk.OptionMenu(framev4, producto_seleccionado, *[plato.get_nombre() for plato in Menu])
        menu_productos.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        menu_productos.pack(pady=10)

        # Botón para confirmar la selección del producto
        boton_confirmar_producto = tk.Button(
            framev4,
            text="Confirmar Producto",
            command=lambda: canjear_producto(cliente, producto_seleccionado.get())
        )
        boton_confirmar_producto.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        boton_confirmar_producto.pack(pady=10)

        # Botón para volver al menú anterior
        boton_volver = tk.Button(
            framev4,
            text="Volver",
            command=lambda: mostrar_informacion_cliente(cliente)
        )
        boton_volver.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        boton_volver.pack(pady=10)

    # Función para canjear un producto
    def canjear_producto(cliente, producto):
        """Muestra un mensaje de confirmación de canje."""
        messagebox.showinfo("Canje Exitoso", f"Producto '{producto}' canjeado con éxito.")

    # Función para mostrar el mensaje de reserva
    def mostrar_mensaje_reserva(cliente):
        """Muestra un mensaje para realizar la reserva con descuento."""
        messagebox.showinfo("Reserva", "Realice su reserva. Se le hará su descuento.")

    # Función para mostrar las mesas deluxe disponibles
    def mostrar_mesas_deluxe(cliente):
        """Muestra las mesas deluxe disponibles."""
        # Limpiar framev4 antes de mostrar las mesas
        for widget in framev4.winfo_children():
            widget.destroy()

        # Crear un label para el título de las mesas
        label_titulo = tk.Label(framev4, text="Mesas Deluxe Disponibles", fg="white", bg="#1C2B2D", font=("Segoe UI", 20, "bold"))
        label_titulo.pack(pady=10)

        # Lista de mesas deluxe
        mesas_deluxe = [
            "Mesa 2 | Capacidad: 4 | Puntos requeridos: 200",
            "Mesa 5 | Capacidad: 6 | Puntos requeridos: 300",
            "Mesa 6 | Capacidad: 2 | Puntos requeridos: 200",
            "Mesa 9 | Capacidad: 4 | Puntos requeridos: 200",
            "Mesa 10 | Capacidad: 2 | Puntos requeridos: 200"
        ]

        # Variable para almacenar la selección de la mesa
        mesa_seleccionada = tk.StringVar(framev4)
        mesa_seleccionada.set("Seleccione una mesa")  # Valor por defecto

        # Crear un menú desplegable para seleccionar la mesa
        menu_mesas = tk.OptionMenu(framev4, mesa_seleccionada, *mesas_deluxe)
        menu_mesas.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        menu_mesas.pack(pady=10)

        # Botón para confirmar la selección de la mesa
        boton_confirmar_mesa = tk.Button(
            framev4,
            text="Confirmar Mesa",
            command=lambda: canjear_mesa(cliente, mesa_seleccionada.get())
        )
        boton_confirmar_mesa.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        boton_confirmar_mesa.pack(pady=10)

        # Botón para volver al menú anterior
        boton_volver = tk.Button(
            framev4,
            text="Volver",
            command=lambda: mostrar_informacion_cliente(cliente)
        )
        boton_volver.config(font=("Segoe UI", 12), bg="#2C3E50", fg="white")
        boton_volver.pack(pady=10)

    # Función para canjear una mesa
    def canjear_mesa(cliente, mesa):
        """Muestra un mensaje de confirmación de canje de mesa."""
        messagebox.showinfo("Canje Exitoso", f"Mesa '{mesa}' canjeada con éxito. Puntos canjeados con éxito.")

    # Función para buscar el cliente por identificación
    def buscar_cliente_por_identificacion(identificacion):
        """Busca al cliente en la lista global."""
        print(f"Buscando cliente con identificación: {identificacion}")  # Depuración

        try:
            identificacion = int(identificacion)  # Convertir la identificación a número
        except ValueError:
            messagebox.showerror("Error", "La identificación debe ser un número.")
            return

        # Buscar el cliente en la lista de clientes del restaurante
        cliente_encontrado = None
        for cliente in Cliente.get_clientes():
            if cliente.get_identificacion() == identificacion:
                cliente_encontrado = cliente
                break

        # Si no se encuentra en la lista del restaurante, buscar en la lista global
        if not cliente_encontrado:
            print("Buscando en la lista global...")  # Depuración
            for cliente in clientes_globales:
                if cliente["identificacion"] == identificacion:
                    # Crear un objeto Cliente con los datos de la lista global
                    cliente_encontrado = Cliente(cliente["nombre"], cliente["identificacion"])
                    break

        if cliente_encontrado:
            print(f"Cliente encontrado: {cliente_encontrado.get_nombre()}")  # Depuración
            mostrar_informacion_cliente(cliente_encontrado)
        else:
            print("Cliente no encontrado.")  # Depuración
            messagebox.showerror("Error", "Cliente no encontrado.")

    # Crear el FieldFrame para solicitar la identificación
    fieldFrame1 = FieldFrame(
        framev4,
        "Datos del Cliente",
        ["Número de identificación"],
        "Información",
        comandoContinuar=lambda: buscar_cliente_por_identificacion(fieldFrame1.obtener_datos()[0])
    )
    fieldFrame1.grid(sticky="new")

    

# Funcionalidad5

def funcionalidad5():
    Mesero.organizar_meseros_por_calificacion()
    calidadComida = 0
    calidadMesero = 0
    tiempoEspera = 0
    comentario = ''
    restaurante = Restaurante.get_restaurantes()[0]
    idCliente = ''

    # Crear nuevos Labels
    labelv1.config(text='Sistema de calificación de servicio')
    labelv2.config(text='Indique Sí o No dado el caso')

    def apartadoEx():
        global comentario
        global restaurante
        global labelv3
        global idCliente
        global calidadComida 
        global calidadMesero 
        global tiempoEspera
        global reputacionActualMesero
        global posicionActualPrioridadMesero
        global posicionNuevaPrioridadMesero
        global calificacionActualDomiciliario
        global reputacionActualRestaurante


        
        cliente = Cliente.indicarCliente(idCliente)
        if cliente.tipo_cliente(): #Valida si es consumo local
            def estadoMesero(cliente):
                if Mesero.posicion_prioridad_mesero(cliente.get_reserva().get_mesero()) == -1:
                    return f'El mesero {cliente.get_reserva().get_mesero().get_nombre()}, ha sido despedido'
                else:
                    return f'El mesero {cliente.get_reserva().get_mesero().get_nombre()}, sigue activo'


            labelv3.destroy()
            labelv3 = FieldFrame(framev4, tipo=3, tituloCriterios=(" ANTES DE SU CALIFICACIÓN       DESPUÉS DE SU CALIFICACIÓN\n"
            "Restaurante:          {:.1f}                             {:.1f}\n"
            "Mesero:               {:.1f}                             {:.1f}\n"
            "Prioridad Mesero:     {}                               {}\n\n"
            "{}"
            ).format(
                reputacionActualRestaurante, restaurante.get_reputacion(),
                reputacionActualMesero, cliente.get_reserva().get_mesero().get_prom_calificaciones(),
                posicionActualPrioridadMesero, posicionNuevaPrioridadMesero,
                estadoMesero(cliente)
            )

            )

            btnf6 = tk.Button(labelv3, text="Finalizar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=ventanaUsuarioDefault)
            btnf6.grid(row=16, column=0, pady=15, columnspan=2)

            labelv3.grid(sticky='new')
        else:
            labelv3.destroy()
            labelv3 = FieldFrame(framev4, tipo=3, tituloCriterios=(" ANTES DE SU CALIFICACIÓN       DESPUÉS DE SU CALIFICACIÓN\n"
            "Restaurante:          {:.1f}                             {:.1f}\n"
            "Domiciliario:               {:.1f}                             {:.1f}\n"
            
            ).format(
                reputacionActualRestaurante, restaurante.get_reputacion(),
                calificacionActualDomiciliario, Domicilio.indicar_domicilio(idCliente).get_domiciliario().get_prom_calificaciones()
                
               
            )

            )
            btnf6 = tk.Button(labelv3, text="Finalizar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=ventanaUsuarioDefault)
            btnf6.grid(row=16, column=0, pady=15, columnspan=2)

            labelv3.grid(sticky='new')


    def preguntaApartadoEx():
        global comentario
        global restaurante
        global labelv3
        global idCliente
        global calidadComida 
        global calidadMesero 
        global tiempoEspera
        global reputacionActualMesero
        global posicionActualPrioridadMesero
        global posicionNuevaPrioridadMesero
        global calificacionActualDomiciliario
        global reputacionActualRestaurante

        cliente = Cliente.indicarCliente(idCliente)
       

        

        if cliente.tipo_cliente(): #Valida si es consumo local
            if (cliente.get_reserva().get_mesa().tipo_mesa()): #valida si es mesa deluxe
                labelv2.config(text=f'¡Hola {cliente.get_nombre()}, Bienvenido al apartado exclusivo para clientes premium,\npor los beneficios de haber estado en una de nuestras mesas deluxe.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 2, tituloCriterios="Se le proporciona la posibilidad de visualizar el impacto de su calificación.\n¿Desea verlo?", comandoCancelar = ventanaUsuarioDefault, comandoContinuar= apartadoEx)
                labelv3.grid(sticky='new')
            else:
                labelv2.config(text='Oprime Finalizar para concluir el proceso.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 3, tituloCriterios='Consulta con nuestro equipo sobre como acceder a una mesa deluxe,\nen tu próxima visita y obtener un apartado exclusivo')
                btnf7 = tk.Button(labelv3, text="Finalizar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=ventanaUsuarioDefault)
                btnf7.grid(row=16, column=0, pady=15, columnspan=2)
                labelv3.grid(sticky='new')
        else:
            if Domicilio.indicar_domicilio(idCliente)._domicilio_prioritario == True: #Valida si el domicilio es prioritario
                labelv2.config(text=f'¡Hola {cliente.get_nombre()}, Bienvenido al apartado exclusvo para clientes premium,\npor el beneficio de que su pedido es prioritario.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 2, tituloCriterios="Se le proporciona la posibilidad de visualizar el impacto de su calificación.\n¿Desea verlo?", comandoCancelar = ventanaUsuarioDefault, comandoContinuar= apartadoEx)
                labelv3.grid(sticky='new')
            else:
                labelv2.config(text='Oprime Finalizar para concluir el proceso.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 3, tituloCriterios='Consulta con nuestro equipo sobre como acceder a un apartado exclusivo si tu proximo pedido es prioritario.')
                btnf7 = tk.Button(labelv3, text="Finalizar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=ventanaUsuarioDefault)
                btnf7.grid(row=16, column=0, pady=15, columnspan=2)
                labelv3.grid(sticky='new')

    def calificar(comentario):
        #global comentario
        global restaurante
        global labelv3
        global idCliente
        global calidadComida 
        global calidadMesero 
        global tiempoEspera
        global reputacionActualMesero
        global posicionActualPrioridadMesero
        global posicionNuevaPrioridadMesero
        global reputacionActualRestaurante

        
        
        if comentario != 'No':
            if labelv3.obtener_datos()[0] == '':
                raise EntryVacio('Comentario')


        
        

        if labelv3.obtener_datos() == []:
            comentario = ''
        else:
            comentario = labelv3.obtener_datos()[0]

        cliente = Cliente.indicarCliente(idCliente)

        reputacionActualRestaurante = restaurante.get_reputacion()
        
        if Cliente.indicarCliente(idCliente).tipo_cliente():# Valida si es consumo local
            labelv3.destroy()
            #Datos antes de la calificación por consumo local
            reputacionActualMesero = cliente.get_reserva().get_mesero().get_prom_calificaciones()
            posicionActualPrioridadMesero = Mesero.posicion_prioridad_mesero(cliente.get_reserva().get_mesero())

            #Se hace la calificacion
            calificacion = cliente.calificar(pedido = cliente.get_reserva().get_mesa().get_pedido(), calidad_comida= calidadComida,  calidad_mesero = calidadMesero, comentario = comentario, tiempo_espera = tiempoEspera)

            #Se encarga de actualizar la reputacion del restaurante por el tiempo de espera
            cliente.get_reserva().get_mesa().get_pedido().tiempo_espera_restaurante(calificacion)
            
            #Se aplica determinado descuento si el promCalificacion es mejor que 3 
            cliente.get_reserva().get_mesa().get_pedido().get_factura().aplicar_descuento(calificacion)

            #Se actualiza la reputacion del restaurante
            restaurante.actualizar_reputacion(calificacion=calificacion)

            labelv2.config(text='A continuación se le proporciona un resumen de la factura de su consumo.\nMuchas gracias por escogernos,\nesperamos verlo pronto.')

            labelv3= FieldFrame(framev4, tipo=3, tituloCriterios=cliente.get_reserva().get_mesa().get_pedido().get_factura())
            labelv3.grid(sticky='new')
            btnf5 = tk.Button(labelv3, text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=preguntaApartadoEx)
            btnf5.grid(row=16, column=0, pady=15, columnspan=2)

            #Se encarga de revisar las 3 ultimas calificaciones de cada mesero, y si alguno tieien las 3 ultimas calificaciones por debajo o igual a 2, será despedido(eliminado de la lista de los meseros del restaurante)
            Mesero.revision_meseros()

            posicionNuevaPrioridadMesero = Mesero.posicion_prioridad_mesero(cliente.get_reserva().get_mesero())

            Mesero.organizar_meseros_por_calificacion()
        else:#Entra para domicilio

            global calificacionActualDomiciliario


            #dato antes de la calificacion
            calificacionActualDomiciliario = Domicilio.indicar_domicilio(idCliente).get_domiciliario().get_prom_calificaciones()

            #se hace la calificacion
            calificacion = cliente.calificar_domicilio(domicilio = Domicilio.indicar_domicilio(idCliente), calidad_comida= calidadComida, tiempo_espera = tiempoEspera, comentario = comentario)

            #Se encarga de actualizar la reputación del restaurante por el tiempo de espera
            if tiempoEspera < 3: 
                restaurante.set_reputacion(restaurante.get_reputacion()-0.1)

            #Se actualiza la reputación del restaurante
            restaurante.actualizar_reputacion(calificacion)

            labelv2.config(text='A continuación se le proporciona un resumen de la factura de su consumo.\nMuchas gracias por escogernos,\nesperamos verlo pronto.')
            labelv3.destroy()
            labelv3= FieldFrame(framev4, tipo=3, tituloCriterios="\n=====================================" + "\n" +
                    "         FACTURA DE CONSUMO AURA GOURMET         " + "\n" +
                    "Restaurante: " + restaurante.get_nombre() + "\n" +
                    "Cliente: " + cliente.get_nombre() + "\n" +
                    "Domiciliario encargado: " + Domicilio.indicar_domicilio(idCliente).get_domiciliario().get_nombre() + "\n" +
                    "-------------------------------------" + "\n" +
                    str(Utilidad.aplicar_descuento(calificacion, Domicilio.indicar_domicilio(idCliente).get_costo())) + "\n" +
                    "Calificación del servicio: " + str(calificacion.get_promedio_calificacion()) + "\n" +
                    "\n=====================================" + "\n" +
                    "Gracias por visitarnos. ¡Esperamos verlo pronto!" + "\n" +
                    "=====================================")
            labelv3.grid(sticky='new')
            btnf5 = tk.Button(labelv3, text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=preguntaApartadoEx)
            btnf5.grid(row=16, column=0, pady=15, columnspan=2)
    
    def dejarComentario():
        global labelv3
        global idCliente

        nombreCliente = Cliente.indicarCliente(idCliente).get_nombre()
        labelv3.destroy()
        labelv2.config(text='Le agradecemos que haya elegido dejarnos su comentario.\nPorfavor escribanos su percepción respecto al servicio.')
        labelv3 = FieldFrame(framev4, tipo= 0, tituloCriterios='Dato solicitado', criterios=['Deje su comentario:', 'Nombre:\n(Nombre de la persona\ncomo se registrará en el sistema)'], valores = [None, nombreCliente], tituloValores='Ingrese el dato solicitado', comandoContinuar = lambda: calificar(comentario= None))
        labelv3.grid(sticky='new')

    def preguntaDejarComentario():
        global labelv3
        global calidadComida 
        global calidadMesero 
        global tiempoEspera
        global idCliente

        try:
            calidadComida = int(labelv3.obtener_datos()[0])
        except:
            raise BoxVacio('calidad comida')
        
        try:
            calidadComida = int(labelv3.obtener_datos()[1])
        except:
            raise BoxVacio('calidad mesero')
        
        if len(labelv3.obtener_datos()) == 3:
            try:
                calidadComida = int(labelv3.obtener_datos()[2])
            except:
                raise BoxVacio('tiempo espera')

        if Cliente.indicarCliente(idCliente).tipo_cliente():
            calidadComida = int(labelv3.obtener_datos()[0])
            calidadMesero = int(labelv3.obtener_datos()[1])
            tiempoEspera = int(labelv3.obtener_datos()[2])
        else:
            calidadComida = int(labelv3.obtener_datos()[0])
            tiempoEspera = int(labelv3.obtener_datos()[1])


        

        labelv3.destroy()
        labelv2.config(text='Para finalizar la encuesta responda la ultima pregunta')
        labelv3 = FieldFrame(framev4, tipo=2, tituloCriterios="Por ultimo, ¿desea dejar un comentario?",comandoCancelar= lambda: calificar(comentario='No'), comandoContinuar= dejarComentario)
        labelv3.grid(sticky='new')

    def continuarInteraccion1():
        global labelv3
        if labelv3.obtener_datos()[0] == '':
            raise EntryVacio('Identificación')
        
        

        try:
            int(labelv3.obtener_datos()[0])
            global idCliente
            idCliente = int(labelv3.obtener_datos()[0])
            if Cliente.validarCliente(int(labelv3.obtener_datos()[0])) == False:
                raise IdNoEncontrado(labelv3.obtener_datos()[0])


            if  Cliente.validarCliente(int(labelv3.obtener_datos()[0])):  #Valida que el id sea de un cliente
                if Cliente.indicarCliente(int(labelv3.obtener_datos()[0])).tipo_cliente():# Valida si es consumo local
                    labelv2.config(text=f'Bienvendo {Cliente.indicarCliente(idCliente).get_nombre()}, has entrado en el sistema de calificación para clientes con consumo en el local.\nPara realizar la calificación porfavor conteste la siguiente encuesta.')
                    labelv3.destroy()
                    labelv3 = FieldFrame(framev4, tipo = 1, tituloCriterios='Apartado de la encuesta', criterios=['Para puntuar la calidad de la comida:', 'Para puntuar la calidad del mesero:', 'Para puntuar el tiempo de espera:'], tituloValores='Seleccione su calificación', valores=[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]], comandoContinuar=preguntaDejarComentario)
                    labelv3.grid(sticky='new')
                else: #Entra en consumo a domicilio
                    labelv2.config(text=f'Bienvenido {Cliente.indicarCliente(idCliente).get_nombre()}, has entrado en el sistema de calificación para clientes con consumo a domicilio.\nPara realizar la calificación porfavor conteste la siguiente encuesta.')
                    labelv3.destroy()
                    labelv3 = FieldFrame(framev4, tipo = 1, tituloCriterios='Apartado de la encuesta', criterios=['Para puntuar la calidad de la comida:', 'Para puntuar la calidad del mesero:'], tituloValores='Seleccione su calificación', valores=[[1,2,3,4,5], [1,2,3,4,5]], comandoContinuar=preguntaDejarComentario)
                    labelv3.grid(sticky='new')

        except:
            raise IdEntryNoNumerico(labelv3.obtener_datos()[0])


        
        

    def continuarInteraccion():
        global labelv3
        labelv3.destroy()
        labelv2.config(text='Para acceder al sistema de califaciones porfavor siga las intruciones y llene los datos')
        labelv3 = FieldFrame(framev4, tipo= 0, tituloCriterios='Dato solicitado', criterios=['Número de identificación (CC/CE):'],tituloValores='Ingrese el dato solicitado', comandoContinuar=continuarInteraccion1)
        labelv3.grid(sticky='new')
        
    
    global labelv3
    labelv3.destroy()
    labelv3 = FieldFrame(framev4, tipo=2, tituloCriterios="¿Desea realizar una calificación?", comandoCancelar = ventanaUsuarioDefault, comandoContinuar=continuarInteraccion)
    labelv3.grid(sticky='new')
#FinFuncionalidad5


#Funcionalidad2
def funcionalidad2(restaurante):
    labelv1.config(text="Realizar Domicilio")
    labelv2.config(text="Desde este menú puedes realizar un domicilio en nuestro restaurante, ingrese los datos que se le solicitan a continuación") 

    alimentos_seleccionados = []  # Lista de alimentos seleccionados

    def limpiar_frame():
        """ Elimina todos los widgets en framev4 """
        for widget in framev4.winfo_children():
            widget.destroy()

    def mostrarResumen(nombre, identificacion, direccion, domicilio_prioritario):
        global alimentos_seleccionados  # Asegurar acceso a la lista global
        limpiar_frame()
        resumen = (
            f"Resumen del Domicilio\n"
            f"Nombre: {nombre}\n"
            f"Identificación: {identificacion}\n"
            f"Domicilio Prioritario: {domicilio_prioritario}\n"
            f"Direccion: {direccion}\n"
            "Platos pedidos:\n"
        )
        total_precio = 0
        if alimentos_seleccionados:
            for alimento, cantidad in alimentos_seleccionados:
                for plato in Menu:
                    if plato.get_nombre() == alimento:
                        precio_plato = plato.get_precio() * int(cantidad)
                        total_precio += precio_plato
                        resumen += f"  - {alimento}: {cantidad} unidades ({precio_plato} COP)\n"
                        break
        else:
            resumen += "No se seleccionaron platos.\n"
    
        resumen += f"\n**Precio Total: {total_precio} COP**"
    
        # Mostrar resumen en framev4
        label_resumen = tk.Label(framev4, text=resumen, fg="white", bg="#1C2B2D", 
                                 font=("Segoe UI", 14), justify="left", anchor="w")
        label_resumen.pack(padx=20, pady=20, fill="both", expand=True)
    
        btn_ir_pago = tk.Button(framev4, text="Proceder al Pago", bg='#2C2F33', fg='white', 
                        relief="solid", bd=3, font=("Segoe UI", 15, "bold"),
                        command=lambda: mostrarPantallaPago(nombre, identificacion, domicilio_prioritario, direccion, total_precio))
        btn_ir_pago.pack(pady=10)

    def mostrarPantallaPago(nombre, identificacion, direccion, domicilio_prioritario, total_precio):
        """ Muestra la pantalla de pago en framev4 """
        global framev4
        limpiar_frame()
    
        tk.Label(framev4, text="Ingrese la cantidad con la que va a pagar:", 
                 fg="white", bg="#1C2B2D", font=("Segoe UI", 14)).pack(pady=10)
    
        field_frame = ttk.Frame(framev4)
        field_frame.pack(pady=10)
    
        entrada_pago = ttk.Entry(field_frame, width=10, font=("Segoe UI", 14))
        entrada_pago.pack(side="left", padx=5)
        entrada_pago.focus_set()
    
        def mostrarPantallaFinal(monto, cambio):
            """ Muestra el resumen final con los datos del pago y pedido """
            limpiar_frame()
    
            resumen = (
                f"Resumen de su pedido\n"
                f"Nombre: {nombre}\n"
                f"Identificación: {identificacion}\n"
                f"Domicilio Prioritario: {domicilio_prioritario}\n"
                f"Direccion: {direccion}\n"
                "Platos pedidos:\n"
            )
    
            if alimentos_seleccionados:
                for alimento, cantidad in alimentos_seleccionados:
                    for plato in Menu:
                        if plato.get_nombre() == alimento:
                            precio_plato = plato.get_precio() * int(cantidad)
                            resumen += f"  - {alimento}: {cantidad} unidades ({precio_plato} COP)\n"
                            break
            else:
                resumen += "No se seleccionaron platos.\n"
    
            resumen += f"\nTotal a pagar: {total_precio} COP"
            resumen += f"\nMonto ingresado: {monto} COP"
            resumen += f"\nCambio devuelto: {cambio} COP"
    
            # Mostrar resumen en pantalla
            label_resumen = tk.Label(framev4, text=resumen, fg="white", bg="#1C2B2D", 
                                     font=("Segoe UI", 14), justify="left", anchor="w")
            label_resumen.pack(padx=20, pady=20, fill="both", expand=True)
    
            # Botón para finalizar
            btn_finalizar = tk.Button(framev4, text="Finalizar", bg='#2C2F33', fg='white', 
                                      relief="solid", bd=3, font=("Segoe UI", 15, "bold"),
                                      command=lambda: limpiar_frame())
            btn_finalizar.pack(pady=10)
    
        def procesarPago():
            valor_ingresado = entrada_pago.get().strip()
            print(f"DEBUG - Contenido de entrada_pago: '{valor_ingresado}'")  # Para depuración
    
            if not valor_ingresado:
                print("ERROR - No se ingresó ningún valor.")
                tk.Label(framev4, text="Ingrese un monto válido.", fg="red", bg="#1C2B2D", font=("Segoe UI", 12)).pack(pady=5)
                return
    
            try:
                monto = int(valor_ingresado)
                print(f"DEBUG - Monto ingresado: {monto}, Total a pagar: {total_precio}")
    
                if monto < total_precio:
                    tk.Label(framev4, text="Monto insuficiente, intente de nuevo.", 
                             fg="red", bg="#1C2B2D", font=("Segoe UI", 12)).pack(pady=5)
                else:
                    cambio = monto - total_precio
                    mostrarPantallaFinal(monto, cambio)
            except ValueError:
                print(f"ERROR - Entrada inválida: '{valor_ingresado}'")  # Depuración
                tk.Label(framev4, text="Ingrese un monto válido.", fg="red", bg="#1C2B2D", font=("Segoe UI", 12)).pack(pady=5)
    
        btn_pagar = tk.Button(framev4, text="Pagar", bg='#2C2F33', fg='white', font=("Segoe UI", 14), command=procesarPago)
        btn_pagar.pack(pady=10)
    
        btn_regresar = tk.Button(framev4, text="Volver al Resumen", bg='#1C2B2D', fg='white', 
                                 relief="solid", bd=3, font=("Segoe UI", 12), 
                                 command=lambda: mostrarResumen(nombre, identificacion, domicilio_prioritario, direccion))
        btn_regresar.pack(pady=10)

    def obtenerDatosCliente(informacion1):
        """ Obtiene los datos del cliente y muestra el resumen """
        nombre = informacion1[0] if len(informacion1) > 0 else "No ingresado"
        try:
            identificacion = int(informacion1[1]) if len(informacion1) > 1 else "No ingresado"
        except ValueError:
            identificacion = "Valor inválido"
        domicilio_prioritario = informacion1[2] if len(informacion1) > 2 else "No ingresado"
        direccion = informacion1[3] if len(informacion1) > 3 else "No ingresado"
        mostrarResumen(nombre, identificacion, domicilio_prioritario, direccion)
    
    def segundo_fieldFrame(fieldFrame1):
        """ Frame para la selección de alimentos """
        informacion1 = fieldFrame1.obtener_datos()
        limpiar_frame()  # Limpia el frame antes de mostrar el nuevo contenido
    
        global alimentos_seleccionados
        alimentos_seleccionados = []  
    
        # Configurar framev4 para centrar el contenido
        framev4.grid_columnconfigure(0, weight=1)
        framev4.grid_rowconfigure(0, weight=1)
    
        # Crear el frame principal dentro de framev4
        frame_alimentos = tk.Frame(framev4, bg="#1C2B2D")
        frame_alimentos.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    
        # Centramos el contenido dentro de frame_alimentos
        frame_alimentos.grid_columnconfigure(0, weight=1)
        frame_alimentos.grid_columnconfigure(1, weight=1)
        frame_alimentos.grid_columnconfigure(2, weight=1)
    
        tk.Label(frame_alimentos, text="Seleccione su pedido", fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
    
        # Listbox para mostrar los alimentos
        listbox_alimentos = tk.Listbox(frame_alimentos, height=len(Menu), font=("Segoe UI", 12))
        for plato in Menu:
            listbox_alimentos.insert(tk.END, plato.get_nombre())
    
        listbox_alimentos.grid(row=1, column=0, padx=10, pady=10, sticky="n")
    
        # Entrada para la cantidad
        tk.Label(frame_alimentos, text="Cantidad:", fg="white", bg="#1C2B2D").grid(row=1, column=1, padx=10, sticky="e")
        cantidad_var = tk.StringVar(value="1")
        entrada_cantidad = tk.Entry(frame_alimentos, textvariable=cantidad_var, width=5)
        entrada_cantidad.grid(row=1, column=2, padx=10, sticky="w")
    
        # Frame para mostrar la lista de alimentos agregados
        frame_lista = tk.Frame(frame_alimentos, bg="#1C2B2D")
        frame_lista.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
        # Centramos la lista de alimentos agregados
        frame_lista.grid_columnconfigure(0, weight=1)
    
        # Función para agregar alimento
        def agregarAlimento():
            try:
                seleccion = listbox_alimentos.curselection()[0]  # Obtener el índice seleccionado
                alimento = listbox_alimentos.get(seleccion).strip()
            except IndexError:
                print("Ningún alimento seleccionado")  # Debugging
                return  # No hacer nada si no se seleccionó nada
    
            cantidad = cantidad_var.get().strip()
    
            if not cantidad.isdigit() or int(cantidad) <= 0:
                print("Selección inválida")  # Debugging print
                return  # No hacer nada si la cantidad no es válida
    
            # Agregar a la lista global
            alimentos_seleccionados.append((alimento, cantidad))
            print(f"Lista actualizada: {alimentos_seleccionados}")  # Debugging print
    
            # Limpiar y actualizar la lista visualmente
            for widget in frame_lista.winfo_children():
                widget.destroy()
    
            for item, qty in alimentos_seleccionados:
                tk.Label(frame_lista, text=f"{item} - {qty} unidades", fg="white", bg="#1C2B2D", font=("Segoe UI", 12)).pack(anchor="center")
    
        # Botón para agregar otro alimento
        btn_agregar = tk.Button(frame_alimentos, text="Agregar alimento", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=agregarAlimento)
        btn_agregar.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        # Botón para continuar
        btn_continuar = tk.Button(frame_alimentos, text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=lambda: [frame_alimentos.destroy(), obtenerDatosCliente(informacion1)])
        btn_continuar.grid(row=2, column=2, padx=10, pady=10, columnspan=3)

    def seleccionar_domiciliario(es_prioritario):
        """ Selecciona un domiciliario según la prioridad del cliente """
        if not Domiciliario._lista_domiciliarios:
            Domiciliario.inicializar_domiciliarios()  # Asegurar que hay domiciliarios disponibles
    
        if es_prioritario:
            # Prioridad alta: Mejor calificación promedio
            domiciliario = max(Domiciliario._lista_domiciliarios, key=lambda d: d.get_prom_calificaciones())
        else:
            # Prioridad baja: Peor calificación promedio
            domiciliario = min(Domiciliario._lista_domiciliarios, key=lambda d: d.get_prom_calificaciones())
    
        return domiciliario

    def validar_datos_cliente(fieldFrame, precio_total):
        """ Valida los datos ingresados y crea un objeto Domicilio con el domiciliario adecuado. """
        try:
            datos = fieldFrame.obtener_datos()
            nombre, identificacion, domicilio_prioritario, direccion = datos
    
            # Validar Nombre (Solo letras y espacios)
            if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre.strip()):
                raise ValueError("El nombre solo debe contener letras y espacios.")
    
            # Validar Identificación (Número entero entre 8 y 12 dígitos)
            if not identificacion.isdigit() or not (8 <= len(identificacion) <= 12):
                raise ValueError("La identificación debe tener entre 8 y 12 dígitos.")
    
            # Validar Domicilio Prioritario ("si" o "no")
            domicilio_prioritario = domicilio_prioritario.strip().lower()
            if domicilio_prioritario not in ["si", "no"]:
                raise ValueError("Domicilio prioritario debe ser 'si' o 'no'.")
            es_prioritario = domicilio_prioritario == "si"
    
            # Validar Dirección (Formato: "Calle/Carrera/Cll/Cr [Número] # [Número]")
            patron_direccion = r"^(Calle|Carrera|Cll|Cr) \d+ # \d+$"
            if not re.match(patron_direccion, direccion.strip(), re.IGNORECASE):
                raise ValueError("La dirección debe tener el formato: 'Calle/Carrera/Cll/Cr [Número] # [Número]'.")
    
            # 5Seleccionar un domiciliario según la prioridad
            domiciliario_asignado = seleccionar_domiciliario(es_prioritario)
    
            # Crear y guardar el objeto Domicilio con el domiciliario asignado
            clientee = Cliente(nombre = nombre, identificacion= int(identificacion))
            nuevo_domicilio = Domicilio(
                cliente=clientee,
                direccion=direccion,
                domicilio_prioritario=es_prioritario,
                costo_envio=precio_total,
                domiciliario=domiciliario_asignado
            )
            
            print(f"Nuevo domicilio guardado: {nuevo_domicilio}")
            print(f"Domiciliario asignado: {domiciliario_asignado.get_nombre()} (Calificación: {domiciliario_asignado.get_prom_calificaciones()})")
    
            messagebox.showinfo("Éxito", f"Datos guardados correctamente.\nDomiciliario asignado: {domiciliario_asignado.get_nombre()}")
    
            # Limpiar los campos del FieldFrame
            fieldFrame.limpiar_entradas()
    
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))
            nuevo_domicilio = Domicilio(cliente=nombre, direccion=direccion, domicilio_prioritario=es_prioritario)
            nuevo_cliente = Cliente(nombre=nombre, identificacion=identificacion)
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))

        print(f"Nuevo domicilio guardado: {nuevo_domicilio}")
        segundo_fieldFrame(fieldFrame)
    
    precio_total = 0

    fieldFrame1 = FieldFrame(
        framev4,
        "Datos del Cliente",
        ["Nombre", "Número de identificación", "¿Domicilio prioritario? (si/no)", "Direccion"],
        "Información",
        comandoContinuar=lambda: validar_datos_cliente(fieldFrame1, precio_total)
    )
    
    fieldFrame1.grid(sticky="new")

               
#Funcionalidad3
def funcionalidad3():
    global reservaAsociada, ofrecerCortesia, platoCortesiaSeleccionado, clienteAsociado
    clienteAsociado = None
    platoCortesiaSeleccionado = None
    reservaAsociada = None
    ofrecerCortesia = False
    
    labelv1.config(text= "Realizar el pedido de mi reserva")
    labelv2.config(text= "Desde esta ventana podrá seleccionar los platos y las"
                    " cantidades que desee ordenar para su\nmesa, por favor ingrese todos los"
                    " datos que se le solicitan a continuación")
    #print("Esta es la lista de reservas: ", Restaurante.get_id_con_reservas()) #para probar
    #print("Esta es la lista de clientes: ", Restaurante.get_lista_clientes()) #para probar
    #print("Todos los clientes:", [c.get_nombre() for c in Cliente._clientes]) #para probar

    def limpiar_frame(): 
        for widget in framev4.winfo_children():
            widget.destroy()

    def ofrecerCortesiaDeluxe():
        limpiar_frame()
        listaDeCortesias =[]
        for platoCortesia in MenuCortesias:
            listaDeCortesias.append(platoCortesia.get_nombre().upper())
        print("platos de cortesia disponibles:", listaDeCortesias) #solo para verificar

        def guardarCortesia():
            global platoCortesiaSeleccionado, clienteAsociado
            platoCortesiaSeleccionado = labelv3._datos[0].get()
            #asignar el atributo plato de cortesia de pedido
            clienteAsociado.get_pedido().set_plato_cortesia(platoCortesiaSeleccionado)
            #print("platoo: ",clienteAsociado.get_pedido().get_plato_cortesia())
            if platoCortesiaSeleccionado.strip() == 'Seleccione una opción':
               raise BoxVacio('plato de cortesia')
            
            frameParaMostrarResumen()  # Llamar a FrameParaMostrarResumen después de guardar la selección

        labelv3 = FieldFrame(framev4, tipo=1, tituloCriterios="¡Su reserva con mesa tipo deluxe" 
                             " incluye un plato de cortesia!", 
                 criterios=["plato de cortesia"], tituloValores='seleccione una opción', 
                 valores=[listaDeCortesias], comandoContinuar=guardarCortesia, textoBoton="Guardar selección"
                 )
        labelv3.grid(sticky='new')

    def buscarReserva(frame):
            global reservaAsociada, ofrecerCortesia, clienteAsociado
            try:
               datos = frame.obtener_datos()
               if not datos[0].strip():  #Verificar si la entrada está vacía
                  raise EntryVacio("Identificación")
        
               id = int(datos[0])  #Intentar convertir la entrada a un número entero
            except ValueError:     #Manejar la entrada no numérica
                    raise IdEntryNoNumerico(datos[0])
    
            reservaEncontrada = Restaurante.buscar_en_lista_reservas(id)
           #print(reservaEncontrada)

            if reservaEncontrada: #si el usuario tiene reserva
               clienteConReserva = Restaurante.retornar_cliente(id) #retorna el objeto cliente asociado al id ingresado
               #print("cliente con reserva: ", clienteConReserva) #para probar
               reservaAsociada = clienteConReserva.get_reserva() #para obtener la reserva asociada a ese cliente
               ofrecerCortesia = restaurante.obtener_tipo_mesa(reservaAsociada) #saber si la mesa asociada a la reserva es deluxe, devuelve true o false
               #print("ofrecerCortesia es: ", ofrecerCortesia)
               descuento=Restaurante.determinar_descuentos(clienteConReserva)
               clienteConReserva.set_descuento_por_visitas(descuento) #le asigne el atributo al cliente
               clienteAsociado = clienteConReserva

               #crear un objeto pedido al que se le asigna el cliente como titular y aignarle el pedido al cliente
               pedidoAsociado = Pedido(clienteAsociado, reservaAsociada.get_factura(), restaurante)
               clienteAsociado.set_pedido(pedidoAsociado)
               #asignarle el pedido a la mesa asociada a la reserva
               mesaAsociada = clienteAsociado.get_reserva().get_mesa()
               mesaAsociada.set_pedido(pedidoAsociado)
               #print("pedido creado: ", pedidoAsociado)
               #print("pedido de la mesa: ", mesaAsociada.get_pedido())

               limpiar_frame()
               labelv2.config(text= clienteConReserva.saludar(), fg='red') #llama al metodo saludar que le indica al usuario su # de visita al restaurante y su descuento
               
               #Para mostrar botón "Continuar con la creación de mi pedido"
               global botonContinuarConPedido

               def alDarClick(): #Para destruir el botón después de oprimirlo
                   botonContinuarConPedido.destroy()  
                   FieldFrameParaCrearPedido()  #Llamar a FieldFrameParaCrearPedido

               #creacion del boton
               botonContinuarConPedido = tk.Button(framev4, text="Continuar con la creación de mi pedido", bg='#2C2F33', fg='white', relief="solid", bd=3, font=("Segoe UI", 13, "bold"), command=alDarClick, padx=20, pady=20, cursor='hand2')
               botonContinuarConPedido.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            else:
                raise IdNoEncontrado(id) #cuando la id ingresada no tenga reserva
            
            #Para mostrar el resumen del pedido cuando se seleccione el boton "finalizar pedido"

    import tkinter as tk

    def mostrarResumenPedido():
        limpiar_frame()
        global pedidosResumen, clienteAsociado, framev4, ofrecerCortesia, platoCortesiaSeleccionado, reservaAsociada
        resumen_pedido = pedidosResumen

        # Crear una nueva ventana donde mostrar el resumen del pedido
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Resumen del Pedido")
        nueva_ventana.geometry("700x700")  

        # Crear un widget Frame para contener el resumen
        frameResumen = tk.Frame(nueva_ventana, bg='#1C2B2D')
        frameResumen.pack(fill='both', expand=True)

        # Usar un Text widget para mostrar el resumen del pedido
        resumen_texto = tk.Text(frameResumen, wrap='word', bg='#1C2B2D', fg='white', font=("Helvetica", 12), borderwidth=0, padx=10, pady=10)
        resumen_texto.pack(fill='both', expand=True)

        resumenTexto = "\nResumen del Pedido:\n"
        resumenTexto += "------------------------------------------------------------\n"
        resumenTexto += "{:<20} {:<20} {:25} {:<25}\n".format("Producto", "Cantidad", "Precio Unitario", "Precio Total")
        resumenTexto += "------------------------------------------------------------\n"

        costoTotal = 0.0
        for plato, cantidad in resumen_pedido:
            for menu in Menu:
                if menu.get_nombre().upper() == plato.upper():
                    precioUnitario = menu.get_precio()
                    precioTotal = float(precioUnitario) * int(cantidad)
                    costoTotal += float(precioTotal)

                    precio_unitario_format = "{:,.2f}".format(precioUnitario).replace(',', '.')
                    precio_total_format = "{:,.2f}".format(precioTotal).replace(',', '.')

                    resumenTexto += "{:<20} {:<20} {:<25} {:<25}\n".format(
                        menu.get_nombre(), cantidad, precio_unitario_format, precio_total_format)

        resumenTexto += "------------------------------------------------------------\n"
        resumenTexto += "{:<40} {:<15}\n".format("Subtotal", "{:,.2f}".format(costoTotal).replace(',', '.'))
        if ofrecerCortesia:
            resumenTexto += "------------------------------------------------------------\n"
            resumenTexto += "PLATO DE CORTESIA: " + platoCortesiaSeleccionado + "\n"
        if clienteAsociado.get_descuento_por_visitas() != 0:
            descuento = costoTotal * (clienteAsociado.get_descuento_por_visitas() / 100)
            resumenTexto += "------------------------------------------------------------\n"
            resumenTexto += "INFORMACION DE LOS DESCUENTOS POR FIDELIDAD:\n"
            resumenTexto += "Descuento por numero de visitas: {}%\n".format(clienteAsociado.get_descuento_por_visitas())
            resumenTexto += "Valor del descuento: {:,.2f}\n".format(descuento).replace(',', '.')
            costoTotal -= descuento
            resumenTexto += "Total de los platos: {:,.2f}\n".format(costoTotal).replace(',', '.')

        resumenTexto += "------------------------------------------------------------\n"
        resumenTexto += "COBROS ASOCIADOS A LA RESERVA:\n"
        cobrosPorReserva = 0
        if ofrecerCortesia:
            resumenTexto += "Reserva con mesa tipo deluxe: {:,.2f}\n".format(30000).replace(',', '.')
            cobrosPorReserva += 30000
        if reservaAsociada.get_recargo_por_fecha():
            resumenTexto += "Reserva creada con más de un mes de anticipación: {:,.2f}\n".format(50000).replace(',', '.')
            cobrosPorReserva += 50000

        if cobrosPorReserva == 0:
            resumenTexto += "No aplica\n"
        else:
            resumenTexto += "{:<25} {:<10} {:<15}\n".format("Total cobros de reserva", "", "{:,.2f}".format(cobrosPorReserva).replace(',', '.'))

        resumenTexto += "------------------------------------------------------------\n"
        #resumenTexto += "{:<25} {:<10} {:<15} {:<15}\n".format("", "", "Total", "{:,.2f}".format(costoTotal + cobrosPorReserva).replace(',', '.'))
        resumenTexto += "{:<40} {:<15}\n".format("Total", "{:,.2f}".format(costoTotal + cobrosPorReserva).replace(',', '.'))

        #asignarle el valor a la factura 
        facturaAsociada = clienteAsociado.get_reserva().get_mesa().get_pedido().get_factura()
        facturaAsociada.set_total_factura(costoTotal + cobrosPorReserva)
        #print("total de la factura: ",clienteAsociado.get_pedido().get_factura().get_total_factura())

        # Insertar el texto en el Text widget
        resumen_texto.insert(tk.END, resumenTexto)
        resumen_texto.configure(state='disabled')  # Deshabilitado para evitar ediciones

        # Alinear el texto a la izquierda
        resumen_texto.tag_configure("left", justify='left')
        resumen_texto.tag_add("left", "1.0", "end")


    def frameParaMostrarResumen():
        limpiar_frame()
        global framev4

        def mostrarResumen():
            mostrarResumenPedido()
            frameParaMostrarResumen()

        def salirDeLaVentana():
            limpiar_frame()
            salir()

        #configura los botones Ver Resumen y Salir
        labelv3 = FieldFrame(
        framev4,
        tipo=4,
        tituloCriterios=f"¡Gracias {clienteAsociado.get_nombre()}, Su pedido ha sido creado con éxito!",
        criterios=["Ver Resumen", "       Salir       "],
        valores=[mostrarResumen, salirDeLaVentana]
        )
        labelv3.grid(sticky='new')


    global pedidosResumen 
    pedidosResumen = [] 
    def finalizarPedido():
            global ofrecerCortesia
            if ofrecerCortesia == True:
               ofrecerCortesiaDeluxe()
            else:
                frameParaMostrarResumen()

    def FieldFrameParaCrearPedido():
        limpiar_frame()
        global labelv3, pedidosResumen 
        almacen = Almacen()

        listaDePlatos = []
        unidadesDisponibles = []
        almacen = Almacen._almacen[0]  # Obtiene el almacen de la lista de la clase Almacen
        #almacen.mostrar_inventario() 
        for plato in Menu:
           hayIngredientes = almacen.verificar_disponibilidad(plato)
           if hayIngredientes:
            listaDePlatos.append(plato.get_nombre().upper()) #mostrar solo los platos disponibles

            # Calcular unidades disponibles para el plato
            ingredients = plato.get_ingredientes()
            cantidades_disponibles = []
            for ingrediente in ingredients:
                cantidad = almacen._cantidades[almacen._nombres.index(ingrediente)]
                cantidades_disponibles.append(cantidad)
            unidades_plato = min(cantidades_disponibles)  #El mínimo de los ingredientes disponibles determina cuántas veces se puede preparar el plato
            unidadesDisponibles.append(unidades_plato)
            
        #print("platosDisponibles:", listaDePlatos) #para verificar
        #mostrar = [f"{plato} (Unidades: {unidades})" for plato, unidades in zip(listaDePlatos, unidadesDisponibles)]
        #print(mostrar) #para verificar

        #actualizar el combobox que muestra las unidades disponibles del dependiendo del plato seleccionado
        def actualizar_unidades_disponibles(field_frame, platoSeleccionado, listaDePlatos, unidadesDisponibles):
            if platoSeleccionado in listaDePlatos:
               indice_plato = listaDePlatos.index(platoSeleccionado)
               unidades_disponibles = list(range(1, unidadesDisponibles[indice_plato] + 1))
               field_frame._datos[1]['values'] = unidades_disponibles
               field_frame._datos[1].set('Seleccione unidades')
               field_frame._datos[1]['state'] = 'readonly'  #Para habilitar el combobox de unidades

               
        def agregarPlatoAlResumen():
            global labelv3
            nombrePlato = labelv3._datos[0].get()
            unidades = labelv3._datos[1].get()

            #Manejar excepiones si no se selecciona una opción
            if nombrePlato.strip() == 'Seleccione una opción': 
               raise BoxVacio('plato')
            if unidades.strip() == 'Seleccione unidades' or unidades.strip() == 'Seleccione una opción':
                raise BoxVacio('unidades a pedir')

            # Buscar el objeto Menu correspondiente al nombre del plato
            plato = None
            for item in Menu:
                if item.get_nombre().upper() == nombrePlato.upper():
                    plato = item
                    break

            if plato and unidades:
                #Para actualizar el inventario (restar de los ingredientes las cantidades pedidas)
                almacen.actualizar_inventario(plato, unidades)

            if nombrePlato and unidades:
               mensajeResumen = f"{unidades} unidades de {nombrePlato} añadidas con éxito!"
               pedidosResumen.append((nombrePlato, unidades)) #para mostrar el posterior resumen del pedido
        
               limpiar_frame()

               #Mostrar el ultimo plato añadido, la pregunta "¿Qué desea hacer ahora? 
               #y los botones "Continuar Pidiendo" y "Finalizar Pedido"
               labelv3 = FieldFrame(
               framev4, 
               tipo=4, 
               tituloCriterios=(f"{mensajeResumen}\n¿Qué desea hacer ahora?"), 
               criterios=["Continuar Pidiendo", "Finalizar Pedido"], 
               valores=[FieldFrameParaCrearPedido, finalizarPedido]
               )
               labelv3.grid(sticky='new')

       #seleccionar los platos y cantidades
        labelv3 = FieldFrame(framev4, tipo=1, tituloCriterios="A continuación seleccione el nombre\n del plato y la cantidad de unidades que desea pedir", 
                 criterios=["plato", "unidades a pedir"], tituloValores='Platos y unidades disponibles', 
                 valores=[listaDePlatos, []], comandoContinuar=agregarPlatoAlResumen, textoBoton="Agregar plato")
        labelv3.grid(sticky='new')
 
       #Deshabilitar el combobox de unidades para que no se pueda usar hasta que se seleccione un plato
        labelv3._datos[1]['state'] = 'disabled'

        #Bind evento de selección para actualizar las unidades que se muestran en el combobox de unidades
        labelv3._datos[0].bind("<<ComboboxSelected>>", lambda event:  actualizar_unidades_disponibles(labelv3, event.widget.get(), listaDePlatos, unidadesDisponibles))

    #por aqui empieza el flujo de la funcionalidad
    global labelv3
    if labelv3:  # Verifica si labelv3 ya existe
        labelv3.destroy()  #Destruye el FieldFrame anterior
    
    limpiar_frame() 

    fieldFrameParaIdentificacion = FieldFrame(framev4, tipo = 0, tituloCriterios="Confirmación de existencia de reserva", tituloValores='CC/CE', criterios=["Ingrese el número de Identificación asociado a su reserva"], comandoContinuar=lambda: buscarReserva(fieldFrameParaIdentificacion), textoBoton="Verificar")
    fieldFrameParaIdentificacion.grid(sticky="new")

#FinFuncionalidad3








#Funcion que elimina los widgets dentro de los frames ingresados, para poder ingresar nuevos
def limpiar_ventana_usuario(framev2, framev3, framev4):
    for widget in framev4.winfo_children():
        widget.destroy()

    for widget in framev3.winfo_children():
        widget.destroy()

    for widget in framev2.winfo_children():
        widget.destroy()


#Creación objetos
restaurante = Restaurante("Aura Gourmet")

#Menu ventana usuario
menuUsuario = tk.Menu(ventana2)
subMenuUsuario1 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario1.add_cascade(label = 'Aplicación', command=mensajeAplicacion)
subMenuUsuario1.add_separator()
subMenuUsuario1.add_cascade(label = 'Salir', command=salirMenuInicio)
menuUsuario.add_cascade(label='Archivo', menu=subMenuUsuario1)
subMenuUsuario2 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario2.add_cascade(label = 'Realizar una reserva',command = lambda:funcionalidad1(restaurante))
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Realizar un domicilio', command = lambda:funcionalidad2(restaurante))
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Realizar el pedido de mi reserva', command=funcionalidad3)
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Gestionar recompensas',command = lambda:funcionalidad4(restaurante))
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Calificar el servicio', command= funcionalidad5)
menuUsuario.add_cascade(label = 'Procesos y Consultas', menu=subMenuUsuario2)
subMenuUsuario3 = tk.Menu(menuUsuario, tearoff=0, activebackground='#1C2B2D')
subMenuUsuario3.add_cascade(label = 'Acerca de', command=acercaDe)
menuUsuario.add_cascade(label = 'Ayuda', menu=subMenuUsuario3)
ventana2.config(menu= menuUsuario)

#Posicionamiento de los frames
frameP1.place(relx=0.02,rely=0.1,relwidth=0.47,relheight=0.85)
frameP2.place(relx=0.51,rely=0.1,relwidth=0.47,relheight=0.85)
frameP3.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP4.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)
frameP5.place(relx=0.02,rely=0.01,relwidth=0.96,relheight=0.35)
frameP6.place(relx=0.02,rely=0.37,relwidth=0.96,relheight=0.62)

labelP3.pack(expand=True,fill='both')
labelP4.pack(side='top', fill='x')
labelP5.pack(expand=True, fill='both')
labelP6.pack(expand=True, fill='both')

# Asignar los eventos evento
P4Superior.bind("<Enter>", EventoP4)
labelP5.bind("<Button-1>", EventoP5)





ventana.mainloop()      
