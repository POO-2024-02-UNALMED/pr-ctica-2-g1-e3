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
from gestorAplicacion.menu import Menu
from field_frame import FieldFrame
from datetime import datetime, time,timedelta
from baseDatos.serializador import Serializador
from baseDatos.deserializador import Deserializador
from uiMain.Utilidad import Utilidad


import tkinter as tk
from field_frame import FieldFrame
from tkinter import messagebox


Deserializador.deserializarListas()




 
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
    messagebox.showinfo('Acerca de', 'Matías es un niño rata')

#Muestra la ventana de dialogo que explica de forma básica el sistema
def mensajeAplicacion():
    messagebox.showinfo('Acerca de Aura Gourmet System','Puedes navegar por las distintas funciones que te ofrece nuestro sistema para brindarte la posibilidad de realizar: Reservas, pedidos, domicilios, calificaciones y gestionar recompesas.')

#Cierra la ventana principal y serializa
def salir():
    #Serializador.serializarListas()
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
                   + "\nReservas, domicilios, gestionar pedidos,\nrecompensas y calificaciones.", justify="left", font=("Segoe UI", 15, "bold"))
    
#Ventana inicio
ventana = tk.Tk()
ventana.title("Aura Gourmet System")
centrarVentana(ventana, 650, 650)
ventana.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico')
ventana.config(bg='#1E1E1E')
ventana.state('zoomed')


# Cargar imágenes
imagenes = [
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante1.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante2.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante3.png"),
    tk.PhotoImage(file="pr-ctica-2-g1-e3/imagenes/restaurante4.png"),
]
indice_imagen = 0  # Índice para alternar entre las imágenes

#Descripciones de los desarrolladores
descripciones = [
    "Nombre: Mateo Pérez\nCédula: 1000761827\nCarrera: Ingeniería de Sistemas\nNacimiento: 18/06/2003",
    "Nombre: Kevin Rubiano\nCédula: 1035417435\nCarrera: Ciencias de la computación\nNacimiento: 19/07/2005",
    "Nombre: Andrés Chica\nCédula: 1041351362\nCarrera: Ingeniería de sistemas e informática\nNacimiento: 24/04/2007",
    "Nombre: NOMBRE3\nCédula: CEDULA3\nCarrera: CARRERA3\nNacimiento: FECHANACIMIENTO3",
    "Nombre: NOMBRE4\nCédula: CEDULA4\nCarrera: CARRERA4\nNacimiento: FECHANACIMIENTO4",
]
indice_descripcion = 0  # Índice para alternar entre las descripciones

#PROVISIONAL DE PRUEBA PARA P6
colores_p6 = [
    ["red", "blue", "green", "yellow"],
    ["purple", "orange", "gray", "pink"],
    ["brown", "cyan", "white", "black"],
    ["#D4AF37", "#2F4F4F", "black", "white"],
    ["#D4AF37", "red", "orange", "yellow"],
]
indice_color = 0  # Índice para alternar entre colores

# Evento que modifica las 4 imagenes en el rectangulo inferior izquierdo
def EventoP4(evento):
    global indice_imagen
    nueva_imagen = imagenes[indice_imagen]
    labelP4.config(image=nueva_imagen)
    indice_imagen = (indice_imagen + 1) % len(imagenes)  # Alternar entre las 

# Evento para cambiar la descripción en labelP5 Y PROVISIONAL PARA P6
def EventoP5(evento):
    global indice_descripcion, indice_color

    # Cambia la descripción de labelP5
    labelP5.config(text=descripciones[indice_descripcion])
    indice_descripcion = (indice_descripcion + 1) % len(descripciones)

    # Cambia los colores de las secciones de labelP6
    colores_actuales = colores_p6[indice_color]
    for i in range(4):
        secciones_p6[i].config(bg=colores_actuales[i])
    
    indice_color = (indice_color + 1) % len(colores_p6)



    

#Creacion de los frames
frameP1 = tk.Frame(ventana,bg="#2D2D2D", relief="solid", bd= 4)
frameP2 = tk.Frame(ventana,bg="#2D2D2D", relief="solid", bd= 4)
frameP3 = tk.Frame(frameP1,bg="white", relief="solid", bd= 4)
frameP4 = tk.Frame(frameP1,bg="#1C2B2D", relief="solid", bd= 4)
frameP5 = tk.Frame(frameP2,bg="#1C2B2D", relief="solid", bd= 4)
frameP6 = tk.Frame(frameP2,bg="#1C2B2D", relief="solid", bd= 4)

#Creacion de los labels
labelP3 = tk.Label(frameP3,bg="#1C2B2D",fg="white",text="Bienvenidos(as) al sistema de gestión \n para usuarios de Aura Gourmet.", font=("Segoe UI", 15, "bold"))
labelP4 = tk.Label(frameP4, bg="#1C2B2D", fg="white", text="hola", image=imagenes[0])
labelP5 = tk.Label(frameP5,bg="#1C2B2D",fg="white",text="Hojas de vida (Click para cambiar)", justify="left", font=("Segoe UI", 15, "bold"))

#PROVISIONAL PARA P6
labelP6 = tk.Frame(frameP6, bg="#1C2B2D")  # Contenedor de las secciones
secciones_p6 = [
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
    tk.Label(labelP6, bg="#1C2B2D", width=20, height=5),
]

# Creación de los botones
buttonP4 = tk.Button(frameP4,text="Acceder al sistema",width=20,height=3,bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 20, "bold"), command=ventanaUsuario)
buttonP4.pack(expand=True, fill="both", padx=10, pady=100)

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
subMenuInicio.add_cascade(label = 'Descripción del sistema', command= descripcionSistema)
subMenuInicio.add_separator()
subMenuInicio.add_cascade(label = 'Salir', command=salir)
menuInicio.add_cascade(label='Inicio', menu= subMenuInicio)
ventana.config(menu= menuInicio)

#Ventana Usuario
ventana2 = tk.Tk()
ventana2.title("Aura Gourmet System")
ventana2.iconbitmap('pr-ctica-2-g1-e3/imagenes/logoRes.ico')
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

    labelv1.config(text='Funcionalidades')
    labelv2.config(text='Descripciones')
    labelv3 = FieldFrame(framev4, tipo= 3, tituloCriterios='Información\n\n\nPara acceder a las funcionalidades dirijase a la pestaña Procesos y consultas.\nPosteriormente seleccione la funcionalidad que desea acceder.')
    labelv3.grid(row= 0, column=0 ,columnspan=2, pady=15, sticky='new')
    
#Funcionalidad1

def funcionalidad1(restaurante):
    
    labelv1.config(text="Realizar Reserva")
    labelv2.config(text="Desde este menú puedes realizar una reserva en nuestro restaurante, ingrese los datos que se le solicitan a continuación")    

    def resumenReserva(framev4,nombre,identificacion,personas,tipoMesa,fechaReserva,decoracion="Normal",horaAdicional="No",alergias="No"):
        # Crear el resumen como un texto
        for widget in framev4.winfo_children():
            widget.destroy()

        for widget in framev3.winfo_children():
            widget.destroy()

        labelResumen = tk.Label(framev3,text="A continuación podrá ver el resumen de su reserva",fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
        labelResumen.pack(expand=True, fill="both")

        resumen = (
            f"Nombre: {nombre}\n"
            f"Identificación: {identificacion}\n"
            f"Número de personas: {personas}\n"
            f"Tipo de Mesa: {tipoMesa}\n"
            f"Fecha de Reserva: {fechaReserva}\n"
            f"Decoración: {decoracion}\n"
            f"Hora Adicional: {horaAdicional}\n"
            f"Alergias: {alergias}"
        )
        
        # Crear un label en el framev4 para mostrar el resumen
        label_resumen = tk.Label(framev4, text=resumen, fg="white", bg="#1C2B2D", font=("Segoe UI", 15, "bold"))
        label_resumen.pack(padx=20, pady=20, fill="both", expand=True)

    def obtenerDatosCliente(informacion1,fieldFrame2):
        informacion2 = fieldFrame2.obtener_datos()
        nombre = informacion1[0]
        identificacion = int(informacion1[1])
        personas = int(informacion2[0])
        tipoMesa = informacion2[1]
        fecha = informacion2[2]
        horaReserva = informacion2[3]

        fechaCorrecta = False
        mesasDisponibles = []

        print("Hola")
        while(not fechaCorrecta):
            if restaurante.validar_fecha_hora(fecha,horaReserva)==True:
                print("Fecha correcta")
                fechaReserva = restaurante.convertir_fecha_hora(fecha,horaReserva)
                mesasDisponibles = restaurante.hacer_reserva(fechaReserva,personas,tipoMesa)
                fechaCorrecta = True
            else:
                funcionalidad1(restaurante)

        mesaCorrecta = False
        mesas=[]
        for i in mesasDisponibles:
            print(i.get_numero())
            numeroMesa = i.get_numero()
            mesas.append(numeroMesa)

        def eleccion_mesa(frame):
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
            cliente = restaurante.obtener_o_crear_cliente(nombre,identificacion)
            reserva.set_cliente(cliente)
            reserva.get_factura().set_cliente(Cliente)

            if tipoMesa == "deluxe":
                def info_deluxe(frame):
                    infoDeluxe = frame.obtener_datos()
                    frame.destroy()

                    #Actualización datos Deluxe
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

                            botonFinal = tk.Button(framev4,text="Continuar", bg='#2C2F33', fg='white' ,relief="solid", bd=3, font=("Segoe UI", 15, "bold"), command=lambda: resumenReserva(framev4,nombre,identificacion,personas,tipoMesa,fechaReserva,infoDeluxe[0],horaAdicional,alergias))
                            botonFinal.pack(side="right",anchor="n",padx=20,pady=125)
                            listaPlatos.config(state="disabled")
                            listaPlatos.pack(pady=10, fill="y", expand=True)
                            
                    frameAlergias = FieldFrame(framev4,"Alergias",["Ingrese los nombres de las alergias que posse, si no tiene, deje la casilla vacía"],comandoContinuar=lambda: final(frameAlergias))
                    frameAlergias.grid(sticky = "new")

                frameMesas.destroy()
                fieldFrameDeluxe = FieldFrame(framev4,"Personalizacion de la reserva",["Decoración de la mesa","¿Desea agregar 1 hora de permanencia en el restaurante?"],valores=[["Elegante","Rústico","Moderno"],["Sí","No"]],tipo=1,comandoContinuar=lambda: info_deluxe(fieldFrameDeluxe))
                fieldFrameDeluxe.grid(sticky="new")

        fieldFrame2.destroy()
        frameMesas = FieldFrame(framev4,"Mesas disponibles",["Mesa"],"Numero de mesa",valores=[mesas],tipo=1,comandoContinuar=lambda: eleccion_mesa(frameMesas))
        frameMesas.grid(sticky="new")
        print("Vamos bien")

    def segundo_fieldFrame(fieldFrame1):
        informacion1 = fieldFrame1.obtener_datos()
        fieldFrame1.destroy()
        fieldFrame2 = FieldFrame(framev4,"Datos de la Reserva",["Personas","Tipo de Mesa","Fecha","Hora"],"Informacion",comandoContinuar=lambda: obtenerDatosCliente(informacion1,fieldFrame2))
        fieldFrame2.grid(sticky="new")

    labelv3.destroy()
    fieldFrame1 = FieldFrame(framev4,"Datos del Cliente",["Nombre","Numero de identificacion"],"Información",comandoContinuar=lambda:segundo_fieldFrame(fieldFrame1))
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
    
    def calificar():
        global comentario
        global restaurante
        global labelv3
        global idCliente
        global calidadComida 
        global calidadMesero 
        global tiempoEspera

        


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
        else:#Entra para domicilio


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
    
    def dejarComentario():
        global labelv3
        labelv3.destroy()
        labelv2.config(text='Le agradecemos que haya elegido dejarnos su comentario.\nPorfavor escribanos su percepción respecto al servicio.')
        labelv3 = FieldFrame(framev4, tipo= 0, tituloCriterios='Dato solicitado', criterios=['Deje su comentario:'], tituloValores='Ingrese el dato solicitado', comandoContinuar=calificar)
        labelv3.grid(sticky='new')

    def preguntaDejarComentario():
        global labelv3
        global calidadComida 
        global calidadMesero 
        global tiempoEspera
        global idCliente

        if Cliente.indicarCliente(idCliente).tipo_cliente():
            calidadComida = int(labelv3.obtener_datos()[0])
            calidadMesero = int(labelv3.obtener_datos()[1])
            tiempoEspera = int(labelv3.obtener_datos()[2])
        else:
            calidadComida = int(labelv3.obtener_datos()[0])
            tiempoEspera = int(labelv3.obtener_datos()[1])


        

        labelv3.destroy()
        labelv2.config(text='Para finalizar la encuesta responda la ultima pregunta')
        labelv3 = FieldFrame(framev4, tipo=2, tituloCriterios="Por ultimo, ¿desea dejar un comentario?",comandoCancelar=calificar, comandoContinuar=dejarComentario)
        labelv3.grid(sticky='new')

    def continuarInteraccion1():
        global labelv3
        global idCliente
        idCliente = int(labelv3.obtener_datos()[0])

        if  Cliente.validarCliente(int(labelv3.obtener_datos()[0])):  #Valida que el id sea de un cliente
            if Cliente.indicarCliente(int(labelv3.obtener_datos()[0])).tipo_cliente():# Valida si es consumo local
                labelv2.config(text='Usted ha entrado en el sistema de calificación para clientes con consumo en el local.\nPara realizar la calificación porfavor conteste la siguiente encuesta.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 1, tituloCriterios='Apartado de la encuesta', criterios=['Para puntuar la calidad de la comida:', 'Para puntuar la calidad del mesero:', 'Para puntuar el tiempo de espera:'], tituloValores='Seleccione su calificación', valores=[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]], comandoContinuar=preguntaDejarComentario)
                labelv3.grid(sticky='new')
            else: #Entra en consumo a domicilio
                labelv2.config(text='Usted ha entrado en el sistema de calificación para clientes con consumo a domicilio.\nPara realizar la calificación porfavor conteste la siguiente encuesta.')
                labelv3.destroy()
                labelv3 = FieldFrame(framev4, tipo = 1, tituloCriterios='Apartado de la encuesta', criterios=['Para puntuar la calidad de la comida:', 'Para puntuar la calidad del mesero:'], tituloValores='Seleccione su calificación', valores=[[1,2,3,4,5], [1,2,3,4,5]], comandoContinuar=preguntaDejarComentario)
                labelv3.grid(sticky='new')

    def continuarInteraccion():
        global labelv3
        labelv3.destroy()
        labelv2.config(text='Para acceder al sistema de califaciones porfavor siga las intruciones y llene los datos')
        labelv3 = FieldFrame(framev4, tipo= 0, tituloCriterios='Dato solicitado', criterios=['Número de identificación (CC/CE):'], tituloValores='Ingrese el dato solicitado', comandoContinuar=continuarInteraccion1)
        labelv3.grid(sticky='new')
        
       
    
    global labelv3
    labelv3.destroy()
    labelv3 = FieldFrame(framev4, tipo=2, tituloCriterios="¿Desea realizar una calificación?", comandoCancelar = ventanaUsuarioDefault, comandoContinuar=continuarInteraccion)
    labelv3.grid(sticky='new')

    


   

    

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
subMenuUsuario2.add_cascade(label = 'Realizar un domicilio')
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Realizar el pedido de mi reserva')
subMenuUsuario2.add_separator()
subMenuUsuario2.add_cascade(label = 'Gestionar recompensas')
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

buttonP4.pack(side='bottom',expand = True)

# Asignar los eventos evento
labelP4.bind("<Enter>", EventoP4)
labelP5.bind("<Button-1>", EventoP5)





ventana.mainloop()      
